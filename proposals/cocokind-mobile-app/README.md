# Cocokind — Mobile App MVP Proposal

> Note: cocokind.com was researched via public sources — Whole Foods
> and Target listings, founder interviews (Allure, Create & Cultivate,
> Chalkboard Mag, Glossy, Gloss Angeles podcast), and the brand's own
> public stance on "clean" and "sustainable" labelling. Validate
> against internal materials before committing budget.

> Categorical note — this is a **skincare brand with a radical
> transparency proposition**, not a clothing brand. The risks are
> different from apparel: cosmetic-product regulation (FDA cosmetic
> rules + FTC), ingredient-claims accuracy, end-of-life packaging
> claims. Lighter regulatory exposure than Moon Juice (no
> Rx-interaction territory) but Sustainability Facts labelling is
> the brand's moat — the app must protect it.

## 1. Strategy in one paragraph

Priscilla Tsai pioneered "Sustainability Facts" labels — the first
skincare brand to publish per-product carbon-per-use figures, full
ingredient transparency, and end-of-life packaging detail. She also
publicly stopped calling Cocokind "clean" and "sustainable" because
those words have become meaningless. **The app is the natural home
for that stance.** A digital Facts label every customer can verify, a
Routine builder that pulls from the catalog without invented claims,
an Ingredient library where every component cites peer-reviewed
sources, and a Refill flow that closes the loop on packaging. The
brand's customer is informed, sceptical, and rewarded by depth — the
app is what rewards her further.

## 2. The six product pillars

### 1. The Routine — your AM and PM, guided
Skincare lives or dies on consistency. The app makes the routine
visible, customisable, and calmly reminded.

- AM: cleanser → toner → serum → moisturiser → SPF
- PM: cleanser → treatment → serum → moisturiser
- Personalised by skin goals (hydration, glow, barrier, acne, age)
- Calm reminders (opt-in; no streaks, no shame)
- "Why this order" notes per step, citation-linked

### 2. The Facts — every product, every claim
Cocokind's Sustainability Facts label, brought to life digitally.

- Full ingredient list with source, role, peer-reviewed evidence
- Carbon-per-use figure (cradle-to-grave LCA)
- Packaging breakdown: % recyclable / refillable / bio-based
- USDA Organic certification status (when applicable)
- "What we don't say" section — transparent about limits of evidence

### 3. The Match — skin goals → routine
Replaces "which Cocokind product for me" guesswork.

- Pick goals: hydration, glow, barrier, acne, age, sensitivity
- App proposes a routine from the existing catalog with rationale
- Editable; save as your AM / PM
- Updates seasonally — adapts to climate

### 4. The Refill — close the loop on packaging
Cocokind's refillable lines deserve a refill flow that respects them.

- Subscribe to staples (SPF, cleanser, ceramide serum)
- Refill predictions based on usage
- Skip / pause / accelerate / vacation mode
- Bottle-return tracking and credit
- Recyclability lookup by packaging code

### 5. The Shop — DTC + retail finder
Calm shop with multi-region awareness.

- Multi-currency (USD, CAD)
- Drops & restock alerts
- Bundle builder (routines as bundles)
- Find at Target / Whole Foods nearest you
- Refill credit redemption at checkout

### 6. The Studio — internal-facing web admin portal
The brand's internal twin. Catalog stays in Shopify; The Studio owns
everything new the app introduces.

- Facts editor — Sustainability Facts label authoring with citation manager
- Ingredient library admin — peer-reviewed evidence per ingredient
- Routine library — staff-curated AM/PM templates per goal
- Refill ops dashboard — at-risk subs, predictions, bottle returns
- Concierge inbox — ingredient questions, Sustainability questions, refill issues
- Multilingual translation workflow — EN-first, AI drafts ES
- Phase 1 analytics — routine completion, refill churn, Facts engagement

Built in the same brand palette so the team that uses it daily isn't
working in an off-brand admin tool.

## 3. Suggested screens (Phase 1)

> Visual wireframes:
> - **Mobile app** — open `mockups.html` for the Phase 1 phone screens
> - **The Studio (web admin portal)** — open `studio-mockups.html` for
>   the four core admin views: dashboard, Facts editor with citation
>   manager, ingredient library, concierge inbox.

1. Onboarding — language, skin goals, current routine, sensitivities
2. Home — today's routine progress, refill alerts, drop hero
3. The Facts — full Sustainability Facts label (digital)
4. The Match — skin goals (multi-select with routine preview)
5. The Routine — AM / PM with timed reminders
6. The Refill — subscription management
7. Product detail — ingredients pills, "ask the Studio" CTA
8. Studio chat — multilingual ingredient + routine assistant
9. Profile — preferences, language, privacy, "what we know about you"

## 4. Phase 1 feature set (months 0–4)

**Foundation**
- Apple / Google / email sign-in
- Multilingual onboarding (EN / ES at launch)
- Multi-currency (USD, CAD)
- Profile: skin goals, sensitivities, current routine, preferences

**The Routine**
- AM / PM routine cards with order rationale
- Calm reminders (opt-in, never gamified)
- Audio guidance (60 sec) for technique tips
- Progress without streaks

**The Facts**
- Full Sustainability Facts per product (carbon, packaging, ingredients)
- Per-ingredient detail page (source, role, evidence)
- USDA Organic + audit citations
- "What we don't say" transparency section

**The Match → Routine**
- Goal selection (hydration, glow, barrier, acne, age, sensitivity)
- AI-proposed routine from existing catalog with rationale
- Editable; save as AM / PM
- Seasonal refresh

**The Refill**
- Subscription management (skip / pause / accelerate / bundle / vacation)
- Smart refill prediction
- Bottle-return tracking + credit
- Recyclability lookup

**The Shop**
- Multi-currency
- Drop hero + restock alerts
- Bundle builder
- Target / Whole Foods finder

**Loyalty**
- "Honest" rewards — points for routine completion, refill returns, reviews
- Refill bottle returns earn credit
- Refer-a-friend (give-and-get)

**AI · Tier 1**
- Studio chat — multilingual ingredient + routine assistant (Sonnet)
- Goal-to-routine AI — proposes from catalog with citations
- Refill timing AI — usage-based prediction
- Multilingual brand-voice translation (Haiku + brand glossary)
- Visual search — photograph a product, find it
- Ingredient explainer — tap any ingredient for sourced detail

**Compliance guardrails (non-negotiable)**
- Never claim to "treat", "cure", or "prevent" skin conditions
- Always cite ingredient evidence; never invent claims
- Refer to a dermatologist for any condition-driven question
- Use "supports" / "may help" structure-function language only
- Never call products "clean" or "sustainable" without defined criteria

**The Studio (web admin portal)**
- Facts editor with citation manager
- Ingredient library admin
- Routine library admin (AM/PM templates per goal)
- Refill ops dashboard
- Concierge inbox
- Multilingual translation workflow
- Phase 1 analytics

## 5. Phase 2 — Depth (months 5–9)

- ⬆ **AR product try-on** — textures, finishes, undertones for makeup-adjacent items (triggers Enterprise upgrade for native modules)
- **Photo skin analysis (cautious)** — opt-in, never diagnostic, explicitly "not medical advice"; surfaces routine adjustments only
- **Esthetician B2B portal** — partnered estheticians with white-label client tracking (triggers Enterprise upgrade for SSO + audit logging)
- **Cocokind Impact Foundation in-app** — featured grantees, donation flow at checkout
- **Heritage / archive sale** — limited re-releases of past favourites with Facts intact
- **Live Q&A with Priscilla** — quarterly with founder + dermatologists (with disclaimer)

## 6. Phase 3 — Cultural authority (months 10+)

- Editorial / journal — long-form on skincare science, transparency, packaging
- Annual VOICES film series — Priscilla, founders the Foundation supports, scientists
- ⬆ Demand-sensing AI — production planning across DTC + Target + Whole Foods
- ⬆ Multilingual content scaling AI — EN-first, AI drafts ES/FR/PT for editor review
- Counterfeit-listing detection (Amazon, eBay, AliExpress)
- VIP signal detection — concierge welcomes high-value supporters
- Carbon-per-use leaderboard — most-improved products year over year (annual transparency report)

## 7. Data we'd collect (with consent)

| Category               | Examples                                                | Use                                          |
| ---------------------- | ------------------------------------------------------- | -------------------------------------------- |
| Identity & contact     | email, name, address                                    | orders, shipping                             |
| Skin goals             | hydration / glow / barrier / acne / age / sensitivity   | routine recommendations                      |
| Sensitivities          | fragrance, retinol, etc.                                | safety filters on routine recommendations    |
| Language & region      | UI language, country, currency                          | multi-region storefront                      |
| Routine engagement     | step completions (no shaming)                           | gentle nudges                                |
| Subscriptions          | active refills, usage rate                              | refill prediction                            |
| Channel of origin      | online / Target / Whole Foods / referral                | attribution                                  |

**Won't collect**: weight / BMI / before-after photos without explicit
opt-in for a specific feature with clear value, contacts,
social-graph imports, third-party ad-tracking IDs, precise GPS,
diagnosed skin conditions (we refer customers to their dermatologist).

## 8. What to deliberately NOT build

- **Diagnostic AI** — never name a skin condition or grade severity; existential brand and FDA risk
- **"Treat acne / cure eczema / heal melasma" language** — illegal under FDA cosmetic rules
- **Use of "clean" or "sustainable" without published criteria** — the brand's own public stance
- **Vanity-driven personalisation based on undisclosed data**
- **Body-tracking metrics** unless explicitly opted-in
- **Auto-renewing subscriptions without one-tap pause / cancel** — California + UK law concerns
- **Streaks, shame, FOMO design** — wellness adjacent; calm by default
- **Carbon claims that aren't cradle-to-grave LCA-backed** — every figure must be auditable

## 9. Recommended SEYSO MaaS package

### Phase 1 launch — **Growth ($3,500/mo)** + **Studio add-on ($750/mo)** = **$4,250/mo**

| Growth feature                                | Why it fits Cocokind                                                                                          |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Both stores, React Native + Expo              | Mixed iOS/Android customer base across DTC + retail. Single codebase; OTA fits drop cadence                   |
| Claude Sonnet & Haiku AI                      | Sonnet powers Studio chat with strict compliance guardrails; Haiku batches translations and Facts summaries   |
| RevenueCat (StoreKit 2 + Google Play Billing) | Subscription management is core — RevenueCat critical for refills                                             |
| Sign in with Apple + Google                   | Reduces install friction                                                                                      |
| ASO quarterly                                 | "Clean skincare", "ingredient-conscious", "vitamin C serum" all matter for discovery                          |
| 2 releases / month                            | Drop cadence + Facts updates demand a regular rhythm                                                          |
| Shared Slack, 4h response                     | Right level for a transparency-led brand at launch                                                            |

**Starter is disqualified** — single platform, 5-screen ceiling, no
AI, 24h email support. None of those work for a brand whose
proposition depends on multilingual ingredient education with strict
compliance guardrails.

**Studio add-on ($750/mo)** is mandatory and especially important
here. The Facts editor with citation manager + ingredient library + refill
ops together form the brand's transparency backbone. Without it, the
Sustainability Facts story lives in spreadsheets and PDFs — not auditable
in real time, not usable by the customer.

### Year 2 trigger — upgrade to **Enterprise (from $8,000/mo)**

Upgrade when *any one* of these becomes a hard requirement:

1. **Esthetician B2B portal** — partnered estheticians with white-label client tracking; SSO + audit logging + RLS hardening
2. **AR product try-on** at flagship fidelity — native Swift/SwiftUI + Kotlin/Compose modules
3. **EU / UK GDPR data residency** — when European volume becomes material (plus EU CSRD-style sustainability disclosure rules tightening)
4. **Photo skin analysis at scale** — health-data adjacency requires Enterprise audit posture
5. **24/7 SLA with 1h response** — when Target, Whole Foods, or Sephora makes uptime contractual

### Contract notes for Year 1

- 12-month term on Growth + Studio (single combined invoice)
- Pre-negotiated upgrade path to Enterprise; build credit prorated
- AI overage clause: usage above the Growth quota billed at cost +20%
- **Brand-side review on every customer-facing claim** — ingredient claims, sustainability figures, anything FDA / FTC cosmetic-rule sensitive. Non-negotiable.
- Studio one-time build cost: **$35–50K** included in the Phase 1 build (separate from monthly platform fees) — citation manager + LCA data integration adds complexity vs apparel clients

## 10. Suggested next step

A two-week paid discovery — confirm e-commerce platform (Shopify
likely), audit existing customer + Sustainability Facts data, run 5
customer interviews (ideally one DTC subscriber, one Target buyer,
one Whole Foods buyer, one new buyer, one routine-builder using a
competing brand), and lock the Phase 1 scope before any build cost
is committed. Critical output: alignment with the brand's editorial
team on what the AI can and can't say about ingredients and packaging.
