# Fixture: conversion configuration as reported by the account

Synthetic. Not a real account.

## Conversion actions

| Action | Source | Counting | Attribution window | Value | Included in goal | Primary/Secondary |
|---|---|---|---|---|---|---|
| Purchase | Google Ads tag | Every | 30-day click, 1-day view | Dynamic (transaction value) | Purchases | Primary |
| Purchase (GA4) | GA4 import | Every | 30-day click | Dynamic (transaction value) | Purchases | Primary |
| Add to cart | Google Ads tag | One | 30-day click | £0 | Purchases | Secondary |
| Newsletter signup | Google Ads tag | One | 30-day click | £5 (assigned) | Purchases | Primary |

## Campaign settings

| Campaign | Type | Bidding | Conversion goal used |
|---|---|---|---|
| Search - Brand | Search | Maximize conversion value, tROAS 600% | Account default ("Purchases") |
| Search - Non-Brand | Search | Maximize conversion value, tROAS 600% | Account default ("Purchases") |

## Business source of truth

| Period | Shopify net revenue | Google Ads reported conv. value | Google Ads cost |
|---|---|---|---|
| Last 30 days | £14,880 | £17,094.50 | £3,368.81 |

## Supplied by the client

- Average order value: £62
- COGS: "around 30%, I think" — no artifact supplied
- Fulfillment, payment fees, refund rate: not supplied
