# Routing Evaluations

## Purpose
Validate that requests are routed to the correct marketing skill.

## Test Cases

### Case 1: Meta Ads
Input:
"Create a testing plan for Facebook ads."

Expected:
- Paid Media Specialist
- Meta Ads Skill
- Creative Strategy Skill when creative is involved

### Case 2: Google Ads
Input:
"Audit my Search campaign performance."

Expected:
- Paid Media Specialist
- Google Ads Skill
- Analytics Skill if tracking issues appear

### Case 3: Product Page
Input:
"Why is my Shopify product page not converting?"

Expected:
- CRO Specialist
- Shopify CRO Framework

### Case 4: Content Growth
Input:
"Create an SEO content strategy."

Expected:
- SEO Specialist
- SEO Skill

## Pass Criteria

The system selects the correct owner skill before recommending tactics.