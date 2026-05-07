# Kotn — Mobile App MVP Proposal

> Note: kotn.com blocked the automated content fetch. Brand
> understanding is drawn from the brand directory, sustainability
> coverage, retail listings, and B Corp / Good On You profiles, and
> should be validated against internal materials.

## 1. Strategy in one paragraph

Erth to Erth stewards a wardrobe. Pineda Covalín is a pocket museum.
Titika Active is a daily companion. **Kotn's app should be a thread
between the customer and the people who made what she wears** — the
Soliman family farm in Fayoum, the women's sewing collective in the
Nile Delta, the school built with last quarter's profits. Kotn's
product is essential clothing in 100% Egyptian cotton; the brand's
moat is that every step from cotton boll to hanger is traceable, and
every purchase funds a measurable social outcome. Most of that story
is lost in a checkout flow. The app surfaces it — calmly, honestly,
without guilt-tripping — and turns the buyer of a t-shirt into the
ally of a community.

## 2. The six product pillars

### 1. The Origin — every piece carries its provenance
Each Kotn piece scannable to its full traceability ledger. This is the
brand's actual product, alongside the cotton.

- Farm cooperative · harvest season · GPS region (privacy-blurred)
- Mill, dye-house, sewing collective, finishing facility
- Energy and water footprint (cited and audited)
- Education impact: this piece contributed X to the Fayoum schools
- A 90-second audio guide voiced by a maker, in their language, with subtitles

### 2. The Wardrobe — register every piece you own
Closet is the bedrock of long-life design. Buy less, wear more.

- Register every piece (auto-fill from order history; scan-to-add for older)
- Wear log per piece (helps the customer feel the cost-per-wear story)
- Outfit grid — pair with what you already own
- Care guide tied to fabric — cotton-specific, climate-aware

### 3. The Atelier — make it last
Repair, care, and slow-fashion craft. The opposite of disposable.

- Care videos for cotton, knits, wovens, denim
- Order a mending kit (button + thread + brief)
- Photo-based repair triage (Phase 2 — vision AI)
- Drop-off at any flagship store · or mail-in service
- "10 wears until it's softer" — celebrate the patina

### 4. The Field — the impact you make, made visible
The strongest social-mission story in the category. This pillar makes
it concrete and personal — without saccharine guilt.

- "Your purchases funded 47 days of school for kids in Fayoum"
- Aggregated traceability across your closet — farms, mills, makers
- Letters and dispatches from the Nile Delta (with maker consent)
- Annual transparency report — auditable, citation-linked
- Cotton-to-classroom dashboard — schools funded, farmers supported

### 5. The Shop — calm, considered, multi-region
Kotn's customer doesn't want noise. The shop reflects that.

- Multi-currency (CAD, USD, GBP, EUR), multi-language (EN / FR)
- Drops & restock alerts on saved items
- Style quiz that powers home recommendations
- Store-event push (block parties, mending workshops)

### 6. The Studio — internal-facing web admin portal
The brand's internal twin. Catalog and orders stay in Shopify; The
Studio owns everything new the app introduces.

- Origin / provenance editor — farm, mill, maker, citation links
- Impact ledger admin — school funding, education days, transparency report builder
- Repair queue (Phase 2)
- Drop & store-event scheduler
- Concierge inbox — provenance questions, repair, store appointments
- Multilingual translation workflow — EN-first, AI drafts FR/AR/etc., editors approve
- Phase 1 analytics — wear count, traceability scan rate, education-impact narrative reach

Built in the same brand palette so the team that uses it daily isn't
working in an off-brand admin tool.

## 3. Suggested screens (Phase 1)

> Visual wireframes:
> - **Mobile app** — open `mockups.html` for the Phase 1 phone screens
> - **The Studio (web admin portal)** — open `studio-mockups.html` for
>   the four core admin views: dashboard, origin / provenance editor,
>   impact ledger, concierge inbox.

1. Onboarding — language, region, fit profile, what matters to you
2. Home — your impact, today's piece, drop hero
3. The Origin — scan / open from order, full passport
4. The Wardrobe — registered pieces, wear log
5. Product detail — origin pills, "ask the atelier" CTA
6. The Atelier — care, repair, mending kit
7. The Field — impact dashboard, dispatch from the Delta
8. The Shop — collections, drops, store events
9. Profile — sizes, language, privacy, "what we know about you"

## 4. Phase 1 feature set (months 0–4)

**Foundation**
- Apple / Google / email sign-in
- Multilingual onboarding (EN / FR at launch; AR, GB, EU expandable)
- Multi-currency, multi-region storefront (CA / US / UK / EU)
- Profile: sizes, fit notes, motivations, region, opt-ins

**The Origin**
- Scan QR / NFC tag or open from order history
- Farm, mill, dye-house, sewing collective, finishing facility
- Energy + water citations (audited, sourced)
- Education-day attribution per piece
- 90-sec audio guide in the maker's language

**The Wardrobe**
- Register every piece (order auto-fill; scan-to-add)
- Wear log + cost-per-wear visible
- Outfit grid — pair with what you own

**The Atelier**
- Care guides per fabric
- Order a mending kit
- Book a repair drop-off at any flagship
- "Make it last" video library

**The Field**
- Personal impact summary — schools funded, education days
- Aggregated wardrobe traceability map
- Dispatches from the Delta (curator-approved, opt-in maker stories)
- Annual transparency report exportable as PDF

**The Shop**
- Multi-currency, multi-region
- Drop hero + restock alerts
- Style quiz → home feed
- Store-event push (region-aware)

**Rewards**
- "Threads" — points for registering pieces, posting reviews, store visits
- Mending kits redeemable via points
- Refer-a-friend (give-and-get a credit)

**AI · Tier 1**
- Origin summary AI — Claude drafts the per-piece passport story; editors approve
- Atelier care + repair chat (Sonnet) — multilingual
- Fit assistant chat — past-order context
- Visual search — see a look, find the piece
- Multilingual brand-voice translation (Haiku + brand glossary)
- Wardrobe-gap analyser — "you're missing a true-white tee"

**The Studio (web admin portal)**
- Origin / provenance editor with citation manager
- Impact ledger admin — school funding, transparency-report builder
- Drop & store-event scheduler
- Concierge inbox
- Multilingual translation workflow
- Phase 1 analytics

## 5. Phase 2 — Depth (months 5–9)

- ⬆ **AR provenance overlay** — point camera at item, see origin (farm region) overlaid on the piece (triggers Enterprise upgrade for native modules)
- **Photo-based repair triage** — vision AI classifies wear/damage, returns DIY guide or atelier quote
- **In-store events at scale** — mending workshops, cotton-tasting, supplier visits livestreamed
- **Heritage / archive** — past-season pieces re-released with full provenance
- **Wholesale / corporate gifting portal** (triggers Enterprise upgrade for SSO + audit logging)
- **Maker-direct video Q&A** — quarterly live sessions from the Nile Delta, EN + AR + FR
- **Returns triage** — fit-related vs damage-related routing, reduces handling cost

## 6. Phase 3 — Cultural authority (months 10+)

- Editorial / journal — long-form on slow fashion, supply chain, education
- Annual VOICES film series — short docs from the field
- ⬆ Demand-sensing AI — drives planting plans with Egyptian growers
- ⬆ Multilingual content scaling AI — EN-first, AI drafts FR/AR/ES/IT for editor review
- Counterfeit-listing detection — Amazon, eBay, Asian marketplaces
- VIP signal detection — concierge welcomes high-value supporters before they self-identify
- School-impact narrative generation — auto-builds annual letter to customers from real ledger data

## 7. Data we'd collect (with consent)

| Category               | Examples                                                | Use                                          |
| ---------------------- | ------------------------------------------------------- | -------------------------------------------- |
| Identity & contact     | email, name, address                                    | orders, shipping                             |
| Fit profile            | sizes, fit notes (body shape opt-in)                    | reduce returns, recommend size               |
| Language & region      | UI language, country, currency                          | multi-region storefront                      |
| Wardrobe               | registered pieces, wear count, repair history           | cost-per-wear story, recommendations         |
| Care preferences       | fabric care, repair vs replace                          | personalisation                              |
| Motivation tags        | sustainability / craft / minimalism / supply-chain      | content & product targeting                  |
| Engagement             | views, wishlists, push response                         | personalisation                              |
| Channel of origin      | online / store / referral                               | attribution                                  |
| Impact narrative consent | opt-in to receive maker stories, school dispatches    | The Field content                            |

**Won't collect**: precise GPS, contacts, social-graph imports,
third-party ad-tracking IDs, weight / BMI, anything that compromises
maker privacy.

## 8. What to deliberately NOT build

- AI-generated provenance stories — every claim must be real and sourced; existential brand risk if AI invents
- Greenwashing scores — vague composite "sustainability ratings" customers can't audit
- Aggressive peer resale — wrong shape; the brand is buy-less-buy-better, not flip-and-trade
- Discount-heavy loyalty — off-brand. Threads recognise customers; they don't bribe them
- Body-tracking metrics — off-brand
- Generic AI customer-service chatbot before a human team can escalate

## 9. Recommended SEYSO MaaS package

### Phase 1 launch — **Growth ($3,500/mo)** + **Studio add-on ($750/mo)** = **$4,250/mo**

| Growth feature                                | Why it fits Kotn                                                                                              |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Both stores, React Native + Expo              | Customer base across CA/US/UK/EU mixed-OS; single codebase; OTA updates fit drop cadence                      |
| Claude Sonnet & Haiku AI                      | Sonnet powers the Origin/Atelier chat in EN/FR; Haiku batches passport draft summaries and translation        |
| RevenueCat (StoreKit 2 + Google Play Billing) | Future-proofs subscription mending-kit boxes or "Threads Plus" membership                                     |
| Sign in with Apple + Google                   | Reduces install friction                                                                                      |
| ASO quarterly                                 | "Egyptian cotton t-shirt," "ethical basics," "B Corp clothing" all matter for discovery                       |
| 2 releases / month                            | Drop cadence + store-event timing                                                                             |
| Shared Slack, 4h response                     | Right level for a values-led brand at launch                                                                  |

**Starter is disqualified** — single platform, 5-screen ceiling, no
AI, 24h email support. None of those work for a multi-region brand
whose proposition depends on multilingual provenance storytelling and
an evolving impact ledger.

**Studio add-on ($750/mo)** covers infra + editorial AI usage, ~5
maintenance hours/month, dependency upgrades, and small editor-driven
feature requests. The Studio is doubly important for Kotn — the
provenance ledger needs careful editorial oversight.

### Year 2 trigger — upgrade to **Enterprise (from $8,000/mo)**

Upgrade when *any one* of these becomes a hard requirement:

1. **AR provenance overlay** — native Swift/SwiftUI + Kotlin/Compose modules for stable AR
2. **Wholesale / corporate gifting portal** — SSO + audit logging + RLS hardening for B2B
3. **EU/UK GDPR data residency** — EU storage and processing requirements as European volume grows
4. **24/7 SLA with 1h response** — when a major retail partner makes uptime contractual

### Contract notes for Year 1

- 12-month term on Growth + Studio (single combined invoice)
- Pre-negotiated upgrade path to Enterprise; build credit prorated
- AI overage clause: usage above the Growth quota billed at cost +20%
- Editorial-content review is brand-side — every customer-facing maker / farm / impact claim approved by Kotn before publish
- Studio one-time build cost: **$30–45K** included in the Phase 1 build (separate from monthly platform fees)

## 10. Suggested next step

A two-week paid discovery — confirm e-commerce platform (Shopify),
audit existing customer and provenance data, run 5 customer interviews
(ideally one Toronto, one NYC, one LA, one new sustainability-focused
buyer, one wholesale account), and validate the impact-ledger feed
into the app before any build cost is committed.
