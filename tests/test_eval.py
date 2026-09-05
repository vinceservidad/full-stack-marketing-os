"""Offline regression tests: no provider calls, no credentials, no behavior claims."""
import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

REPO = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('evaluation_harness', REPO / 'scripts/eval.py')
evaluation = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = evaluation
SPEC.loader.exec_module(evaluation)


class EvaluationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        subprocess.run(['git', 'init', '-q', str(self.root)], check=True)
        self.output = self.root / 'result.json'
        self.quiet = contextlib.redirect_stdout(io.StringIO())
        self.quiet.__enter__()
        self.addCleanup(self.quiet.__exit__, None, None, None)
        self.no_secrets = mock.patch.dict(os.environ, {}, clear=True)
        self.no_secrets.start()
        self.addCleanup(self.no_secrets.stop)
        # Any accidentally unmocked provider request fails the offline test.
        self.network = mock.patch.object(evaluation.urllib.request, 'build_opener', side_effect=AssertionError('network is forbidden in offline tests'))
        self.network.start()
        self.addCleanup(self.network.stop)

    def parse(self, text, kind):
        path = self.root / 'cases.md'
        path.write_text(text, encoding='utf-8')
        return evaluation.parse_cases('example', path, kind)

    def test_numbered_continuation_and_title_only_scenario(self):
        cases = self.parse('# Cases\n\n1. **First:** Situation\ncontinued. Pass only if criterion\ncontinues.\n2. **Second:** Pass if preserve scope.\n', 'numbered')
        self.assertEqual(cases[0].scenario, 'Situation\ncontinued.')
        self.assertEqual(cases[0].criterion, 'Pass only if criterion\ncontinues.')
        self.assertEqual(cases[1].scenario, 'Second')

    def test_numbered_malformed_case_cannot_disappear(self):
        with self.assertRaisesRegex(evaluation.EvaluationError, 'malformed numbered'):
            self.parse('1. **Valid:** A. Pass if B.\n2. Missing bold title. Pass if C.\n', 'numbered')

    def test_numbered_missing_criterion_fails(self):
        with self.assertRaises(evaluation.EvaluationError):
            self.parse('1. **Valid:** A. Pass if B.\n2. **Incomplete:** No criterion.\n', 'numbered')

    def test_duplicate_case_id_fails(self):
        with self.assertRaisesRegex(evaluation.EvaluationError, 'duplicate case'):
            self.parse('1. **One:** A. Pass if B.\n1. **Two:** C. Pass if D.\n', 'numbered')

    def test_mixed_authoring_shapes_fail_instead_of_early_return(self):
        with self.assertRaises(evaluation.EvaluationError):
            self.parse('1. **One:** A. Pass if B.\n## New case\n**Prompt:** C\n**Pass:** D\n', 'numbered')
        with self.assertRaises(evaluation.EvaluationError):
            self.parse('## One\nPrompt: A\nPass if B.\n1. **Two:** C. Pass if D.\n', 'sections-h2')

    def test_section_multiple_fields_preserve_full_text(self):
        case = self.parse('## 7. Test\n**Prompt:** “Line one\nline two”\n\n**Pass:** First criterion.\nSecond criterion.\n\n**Fail:** Counterexample.\n', 'sections-h2')[0]
        self.assertEqual(case.identifier, '7')
        self.assertEqual(case.scenario, 'Line one\nline two')
        self.assertEqual(case.criterion, 'First criterion.\nSecond criterion.')
        self.assertEqual(case.counter, 'Counterexample.')
        self.assertTrue(case.literal_prompt)

    def test_plain_prompt_and_prose_expected_shapes(self):
        case = self.parse('## Attribution\nPrompt: “A user question.”\n\nPass if boundaries preserved.\n', 'sections-h2')[0]
        self.assertEqual(case.scenario, 'A user question.')
        case = self.parse('## Group\n### 1. Value\nCustomer has no result.\n\nExpected: do not invent value.\n', 'sections-h3')[0]
        self.assertEqual(case.scenario, 'Customer has no result.')
        self.assertIn('do not invent', case.criterion)

    def test_legacy_plain_pass_criterion_preserves_explicit_fail_field(self):
        case = self.parse('## One\nPrompt: \"Assess this.\"\n\nPass if the uncertainty is explicit.\n\nFail: Inventing a value.\n', 'sections-h2')[0]
        self.assertEqual(case.scenario, 'Assess this.')
        self.assertEqual(case.counter, 'Inventing a value.')
        self.assertEqual(case.criterion, 'Pass if the uncertainty is explicit.')

    def test_code_identifier_and_missing_section_criterion(self):
        case = self.parse('## Group\n### CI-01 — Example\n**Input:** A\n**Expected:** B\n', 'sections-h3')[0]
        self.assertEqual(case.identifier, 'CI-01')
        self.assertFalse(case.literal_prompt)
        with self.assertRaises(evaluation.EvaluationError):
            self.parse('## One\nPrompt: A\nPass if B.\n## Two\nMissing criterion.\n', 'sections-h2')

    def test_h2_case_cannot_hide_among_h3_groups(self):
        with self.assertRaises(evaluation.EvaluationError):
            self.parse('## Hidden\n**Prompt:** A\n**Pass:** B\n### 1. Visible\n**Prompt:** C\n**Pass:** D\n', 'sections-h3')

    def test_duplicate_fields_and_criterion_leak_rejected(self):
        with self.assertRaises(evaluation.EvaluationError):
            self.parse('## One\n**Prompt:** A\n**Prompt:** B\n**Pass:** C\n', 'sections-h2')
        with self.assertRaises(evaluation.EvaluationError):
            self.parse('## One\n**Prompt:** A. Pass if leaking answer.\n**Pass:** C\n', 'sections-h2')

    def test_table_escaped_pipe_and_bad_row(self):
        header = '| # | Case | Expected behavior |\n|---:|---|---|\n'
        cases = self.parse(header + '| 1 | A \\| B | C |\n', 'table')
        self.assertEqual(cases[0].scenario, 'A | B')
        with self.assertRaisesRegex(evaluation.EvaluationError, 'malformed case table'):
            self.parse(header + '| 1 | A | B |\n| two | C | D |\n', 'table')

    def test_current_corpus_is_registered_with_explicit_historical_exclusions(self):
        suites, parsed = evaluation.validate_corpus(REPO)
        self.assertEqual(len(suites), 41)
        self.assertEqual(sum(map(len, parsed.values())), 874)
        self.assertEqual(sum(len(s.get('live_exclusions', {})) for s in suites), 9)
        for suite in suites:
            self.assertEqual(suite['case_count'], len(parsed[suite['id']]))
        architecture = next(s for s in suites if s['id'] == 'v1.2-architecture')
        self.assertNotIn('3', architecture['live_exclusions'])
        self.assertIn('historical', architecture['case_notes']['3'])
        self.assertIn('nonexistent analytics or reporting skill', parsed['v1.2-architecture'][2].criterion)

    def test_count_drift_and_unknown_skill_fail(self):
        suites = evaluation.load_suites(REPO)
        suites[0]['case_count'] += 1
        with mock.patch.object(evaluation, 'load_suites', return_value=suites):
            with self.assertRaisesRegex(evaluation.EvaluationError, 'declared count'):
                evaluation.validate_corpus(REPO)
        suites[0]['case_count'] -= 1
        suites[0]['owners'] = ['missing-skill']
        with mock.patch.object(evaluation, 'load_suites', return_value=suites):
            with self.assertRaisesRegex(evaluation.EvaluationError, 'nonexistent'):
                evaluation.validate_corpus(REPO)

    def test_unregistered_file_and_duplicate_suite_fail(self):
        suites = evaluation.load_suites(REPO)
        with mock.patch.object(evaluation, 'load_suites', return_value=suites[:-1]):
            with self.assertRaisesRegex(evaluation.EvaluationError, 'registration mismatch'):
                evaluation.validate_corpus(REPO)
        with mock.patch.object(evaluation, 'load_suites', return_value=suites + [suites[0]]):
            with self.assertRaisesRegex(evaluation.EvaluationError, 'duplicate suite'):
                evaluation.validate_corpus(REPO)

    def test_path_escape_and_symlink_escape_rejected(self):
        target = self.root / 'outside.md'
        target.write_text('private', encoding='utf-8')
        nested = self.root / 'repo'
        nested.mkdir()
        (nested / 'alias.md').symlink_to(target)
        for path in ('../outside.md', 'alias.md'):
            with self.assertRaisesRegex(evaluation.EvaluationError, 'escapes'):
                evaluation.within_repo(nested, path)

    def test_judge_grade_requires_exact_evidence_and_strict_schema(self):
        answer = 'The source is unknown. No budget change is justified.'
        good = {'verdict': 'PASS', 'evidence_quotes': ['The source is unknown.'], 'reasoning': 'Records the uncertainty.'}
        self.assertEqual(evaluation.parse_grade(json.dumps(good), answer)['verdict'], 'PASS')
        for change in ({'evidence_quotes': ['invented quote']}, {'evidence_quotes': []}, {'reasoning': ''}, {'verdict': 'PASS or FAIL'}, {'extra': 'PASS'}):
            with self.subTest(change=change), self.assertRaises(evaluation.EvaluationError):
                evaluation.parse_grade(json.dumps({**good, **change}), answer)
        for raw in ('VERDICT: PASS\nEVIDENCE: unknown', '```json\n' + json.dumps(good) + '\n```', '{"verdict":"FAIL","verdict":"PASS","evidence_quotes":[],"reasoning":"x"}'):
            with self.assertRaises(ValueError):
                evaluation.parse_grade(raw, answer)

    def test_truncated_or_empty_response_is_not_scorable(self):
        for body in ({'stop_reason': 'max_tokens', 'content': [{'type': 'text', 'text': 'Looks good'}]}, {'stop_reason': 'end_turn', 'content': []}, {'stop_reason': 'tool_use', 'content': []}):
            with self.assertRaises(evaluation.EvaluationError):
                evaluation.response_text(body)

    def live_fixture(self, exclusion=False):
        case = evaluation.Case('smoke', '1', 'Example', 'Assess unknown data.', 'Preserve uncertainty.')
        suite = {'id': 'smoke', 'cases': 'case.md', 'owners': ['marketing-router'], 'prompt_template': 'Situation: {scenario}\n\nGive your assessment and state exactly what should happen next.'}
        if exclusion:
            suite['live_exclusions'] = {'1': 'Historical criterion superseded.'}
        (self.root / 'case.md').write_text('supplied case source', encoding='utf-8')
        patches = [mock.patch.object(evaluation, 'validate_corpus', return_value=([suite], {'smoke': [case]})), mock.patch.object(evaluation, 'skill_context', return_value=('governed test context', [{'path': 'core', 'sha256': 'hash', 'text': 'text'}])), mock.patch.object(evaluation, 'repository_state', return_value={'commit': 'abc', 'working_tree_status': ''})]
        for patch in patches:
            patch.start()
            self.addCleanup(patch.stop)
        return suite, case

    @staticmethod
    def api_body(answer):
        return {'id': 'msg_test', 'model': 'mock-model-2026', 'stop_reason': 'end_turn', 'content': [{'type': 'text', 'text': answer}], 'usage': {'input_tokens': 10, 'output_tokens': 10}}

    def run_mock_live(self):
        with mock.patch.dict(os.environ, {'ANTHROPIC_API_KEY': 'offline-test-only'}):
            return evaluation.run_live(self.root, ['smoke'], 'caller-chosen-model', None, 1, False, self.output)

    def test_no_key_is_nonzero_and_makes_no_request_or_artifact(self):
        self.live_fixture()
        with mock.patch.object(evaluation, 'call_api') as api:
            result = evaluation.main(['--repo', str(self.root), '--live', '--suite', 'smoke', '--model', 'caller-model', '--out', str(self.output)])
        self.assertEqual(result, 2)
        api.assert_not_called()
        self.assertFalse(self.output.exists())

    def test_live_requires_model_suite_positive_limit_and_new_output(self):
        self.live_fixture()
        for suites, model, limit in (([], 'x', 1), (['unknown'], 'x', 1), (['smoke'], None, 1), (['smoke'], 'x', 0), (['smoke'], 'x', -1)):
            with self.subTest(suites=suites, model=model, limit=limit), self.assertRaises(evaluation.EvaluationError):
                evaluation.run_live(self.root, suites, model, None, limit, False, self.output)
        self.output.write_text('old evidence', encoding='utf-8')
        with self.assertRaisesRegex(evaluation.EvaluationError, 'overwrite'):
            self.run_mock_live()
        self.assertEqual(self.output.read_text(), 'old evidence')

    def test_mocked_live_pass_retains_raw_answer_grade_context_and_source(self):
        self.live_fixture()
        answer = 'The data is unknown.'
        grade = json.dumps({'verdict': 'PASS', 'evidence_quotes': [answer], 'reasoning': 'Preserves uncertainty.'})
        with mock.patch.object(evaluation, 'call_api', side_effect=[self.api_body(answer), self.api_body(grade)]) as api:
            self.assertEqual(self.run_mock_live(), 0)
        self.assertEqual(api.call_count, 2)
        report = json.loads(self.output.read_text())
        row = report['results'][0]
        self.assertEqual(row['answer'], answer)
        self.assertEqual(row['judge_raw'], grade)
        self.assertEqual(row['responder_api']['model'], 'mock-model-2026')
        self.assertIn('scenario', json.loads(row['judge_prompt']))
        self.assertIn('case_source_sha256', report['contexts']['smoke'])
        self.assertIn('governed test context', report['contexts']['smoke']['system'])
        self.assertNotIn('offline-test-only', self.output.read_text())

    def test_malformed_judge_is_unscored_and_nonzero(self):
        self.live_fixture()
        with mock.patch.object(evaluation, 'call_api', side_effect=[self.api_body('unknown'), self.api_body('VERDICT: PASS')]):
            self.assertEqual(self.run_mock_live(), 1)
        report = json.loads(self.output.read_text())
        self.assertEqual(report['results'][0]['status'], 'UNSCORED')
        self.assertFalse(report['summary']['complete_selected_sample'])
        self.assertIsNone(report['summary']['pass_rate_among_scored'])

    def test_api_error_is_error_not_behavior_failure(self):
        self.live_fixture()
        with mock.patch.object(evaluation, 'call_api', side_effect=TimeoutError('request timed out')):
            self.assertEqual(self.run_mock_live(), 1)
        counts = json.loads(self.output.read_text())['summary']
        self.assertEqual(counts['ERROR'], 1)
        self.assertEqual(counts['FAIL'], 0)
        self.assertIsNone(counts['pass_rate_among_scored'])

    def test_truncated_response_is_preserved_but_not_judged(self):
        self.live_fixture()
        body = self.api_body('partial answer')
        body['stop_reason'] = 'max_tokens'
        with mock.patch.object(evaluation, 'call_api', return_value=body) as api:
            self.assertEqual(self.run_mock_live(), 1)
        api.assert_called_once()
        row = json.loads(self.output.read_text())['results'][0]
        self.assertEqual(row['responder_api'], body)
        self.assertEqual(row['status'], 'ERROR')

    def test_historical_exclusion_is_visible_and_not_a_pass(self):
        self.live_fixture(exclusion=True)
        with mock.patch.object(evaluation, 'call_api') as api:
            self.assertEqual(self.run_mock_live(), 1)
        api.assert_not_called()
        report = json.loads(self.output.read_text())
        self.assertEqual(report['results'][0]['status'], 'EXCLUDED')
        self.assertFalse(report['summary']['complete_selected_sample'])

    def test_mixed_score_denominators_report_errors_separately(self):
        counts = evaluation.summary([{'status': s} for s in ['PASS', 'FAIL', 'ERROR', 'UNSCORED', 'EXCLUDED', 'NOT_SELECTED']])
        self.assertEqual(counts['pass_rate_among_scored'], 0.5)
        self.assertEqual(counts['ERROR'], 1)
        self.assertFalse(counts['complete_selected_sample'])

    def test_context_includes_canonical_contracts_and_optional_nested_references(self):
        for name in evaluation.CORE_CONTEXT:
            (self.root / name).write_text(name, encoding='utf-8')
        skill = self.root / '.agents/skills/example'
        (skill / 'references/nested').mkdir(parents=True)
        (skill / 'SKILL.md').write_text('owning skill', encoding='utf-8')
        (skill / 'references/nested/detail.md').write_text('reference details', encoding='utf-8')
        system, sources = evaluation.skill_context(self.root, ['example'], False)
        self.assertNotIn('reference details', system)
        self.assertTrue(set(evaluation.CORE_CONTEXT) <= {source['path'] for source in sources})
        system, _ = evaluation.skill_context(self.root, ['example'], True)
        self.assertIn('reference details', system)

    def context_fixture(self):
        for name in evaluation.CORE_CONTEXT:
            (self.root / name).write_text(name, encoding='utf-8')
        skill = self.root / '.agents/skills/example'
        (skill / 'references').mkdir(parents=True)
        (skill / 'SKILL.md').write_text('owning skill', encoding='utf-8')
        (self.root / '.gitignore').write_text('work/\nprivate*.md\n', encoding='utf-8')
        (self.root / '.git/info/exclude').write_text('local-only.md\n', encoding='utf-8')
        return skill / 'references'

    def test_context_excludes_ignored_scratch_and_local_excludes_from_text_and_provenance(self):
        references = self.context_fixture()
        (references / 'work').mkdir()
        (references / 'nested').mkdir()
        for relative in ('work/notes.md', 'private-client.md', 'local-only.md'):
            (references / relative).write_text('PRIVATE-CONTENT-DO-NOT-SEND', encoding='utf-8')
        (references / 'nested/public.md').write_text('Public reference', encoding='utf-8')
        system, sources = evaluation.skill_context(self.root, ['example'], True)
        self.assertIn('Public reference', system)
        self.assertNotIn('PRIVATE-CONTENT-DO-NOT-SEND', system)
        provenance = json.dumps(sources)
        self.assertNotIn('PRIVATE-CONTENT-DO-NOT-SEND', provenance)
        for relative in ('work/notes.md', 'private-client.md', 'local-only.md'):
            self.assertNotIn(relative, provenance)
        self.assertIn('nested/public.md', provenance)

    def test_deliberately_tracked_reference_remains_eligible_despite_ignore_pattern(self):
        references = self.context_fixture()
        public = references / 'private-but-reviewed.md'
        public.write_text('Intentionally versioned reference', encoding='utf-8')
        subprocess.run(['git', '-C', str(self.root), 'add', '-f', str(public.relative_to(self.root))], check=True)
        system, sources = evaluation.skill_context(self.root, ['example'], True)
        self.assertIn('Intentionally versioned reference', system)
        self.assertIn(public.relative_to(self.root).as_posix(), {source['path'] for source in sources})

    def test_explicit_ignored_core_source_is_rejected_instead_of_sent(self):
        self.context_fixture()
        with (self.root / '.gitignore').open('a', encoding='utf-8') as ignore:
            ignore.write('AGENTS.md\n')
        with self.assertRaisesRegex(evaluation.EvaluationError, 'ignored or undiscoverable'):
            evaluation.skill_context(self.root, ['example'], True)

    def test_context_rejects_in_repository_symlink_to_ignored_private_content(self):
        references = self.context_fixture()
        (references / 'work').mkdir()
        secret = references / 'work/private.md'
        secret.write_text('PRIVATE-CONTENT-DO-NOT-SEND', encoding='utf-8')
        alias = references / 'public-alias.md'
        alias.symlink_to(secret)
        with self.assertRaisesRegex(evaluation.EvaluationError, 'symlink source'):
            evaluation.skill_context(self.root, ['example'], True)
        alias.unlink()
        (references / 'public-directory').symlink_to(secret.parent, target_is_directory=True)
        with self.assertRaisesRegex(evaluation.EvaluationError, 'symlink source'):
            evaluation.skill_context(self.root, ['example'], True)

    def test_source_archive_fails_closed_without_reading_private_references(self):
        archive = self.root / 'archive'
        archive.mkdir()
        for operation in (
            lambda: evaluation.skill_context(archive, ['example'], True),
            lambda: evaluation.claim_lint(archive),
        ):
            with self.assertRaisesRegex(evaluation.EvaluationError, 'Git checkout root'):
                operation()

    def corpus_fixture(self):
        self.context_fixture()
        (self.root / 'tests/evaluations').mkdir(parents=True)
        (self.root / 'evaluations').mkdir()
        (self.root / 'agents/work').mkdir(parents=True)
        case = self.root / 'evaluations/routing-tests.md'
        case.write_text('## One\nPrompt: Assess this.\nPass if evidence remains uncertain.\n', encoding='utf-8')
        suite = {'id': 'routing', 'cases': 'evaluations/routing-tests.md', 'review_note': 'Fixture only.', 'owners': ['example'], 'case_count': 1, 'prompt_template': '{scenario}', 'format': 'sections-h2'}
        manifest = self.root / 'tests/evaluations/suites.json'
        manifest.write_text(json.dumps({'version': 1, 'suites': [suite]}), encoding='utf-8')
        return manifest, suite

    def test_corpus_skips_ignored_case_and_role_scratch(self):
        self.corpus_fixture()
        (self.root / 'tests/evaluations/private-cases.md').write_text('PRIVATE-CASE-MUST-NOT-BE-PARSED', encoding='utf-8')
        (self.root / 'agents/work/notes.md').write_text('$private-nonexistent-skill PRIVATE-NOTES', encoding='utf-8')
        (self.root / 'evaluations/work').mkdir()
        (self.root / 'evaluations/work/notes.md').write_text('$private-nonexistent-skill PRIVATE-NOTES', encoding='utf-8')
        suites, parsed = evaluation.validate_corpus(self.root)
        self.assertEqual(len(suites), 1)
        self.assertEqual(list(parsed), ['routing'])

    def test_registered_ignored_case_is_rejected_before_parsing(self):
        manifest, suite = self.corpus_fixture()
        private = self.root / 'tests/evaluations/private-cases.md'
        private.write_text('PRIVATE-CASE-MUST-NOT-BE-PARSED', encoding='utf-8')
        suite['cases'] = private.relative_to(self.root).as_posix()
        manifest.write_text(json.dumps({'version': 1, 'suites': [suite]}), encoding='utf-8')
        with mock.patch.object(evaluation, 'parse_cases') as parse:
            with self.assertRaisesRegex(evaluation.EvaluationError, 'ignored or undiscoverable'):
                evaluation.validate_corpus(self.root)
        parse.assert_not_called()

    def test_claim_lint_ignores_scratch_and_does_not_share_negation_across_sentence(self):
        subprocess.run(['git', 'init', '-q', str(self.root)], check=True)
        (self.root / '.gitignore').write_text('work/\n', encoding='utf-8')
        (self.root / 'examples/work').mkdir(parents=True)
        (self.root / 'examples/work/private.md').write_text('guaranteed revenue', encoding='utf-8')
        (self.root / 'examples/public.md').write_text('Do not assume causality. Guaranteed revenue follows.', encoding='utf-8')
        findings = evaluation.claim_lint(self.root)
        self.assertEqual(len(findings), 1)
        self.assertIn('public.md', findings[0])
        (self.root / 'examples/public.md').write_text('Do not promise guaranteed revenue.', encoding='utf-8')
        self.assertEqual(evaluation.claim_lint(self.root), [])

    def test_static_arguments_cannot_accidentally_start_network(self):
        with mock.patch.object(evaluation, 'run_live') as live:
            self.assertEqual(evaluation.main(['--model', 'x']), 2)
        live.assert_not_called()


if __name__ == '__main__':
    unittest.main()
