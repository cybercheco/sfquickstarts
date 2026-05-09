# Free Label — Mobile App MVP Proposal

> Note: freelabel.com was researched via public sources — Vancouver Mag,
> Good On You sustainability rating, the brand's own product pages
> (Andie Bra, Carrie Bra, bamboo collection), and founder interviews
> (My Green Closet, Vancouver Is Awesome). Validate against internal
> materials before committing budget.

## 1. Strategy in one paragraph

Free Label sells the bra most women buy wrong the first time — wire-free,
elastic-free, made in Vancouver from bamboo, sized from A to L cup and
up to 5X. Fitting that bra by guessing on a website is hard; that's why
the brand has a cult following among customers who eventually got it
right and never went back. **The app should make the right fit easier
the first time.** A guided Fit Finder for the brand's signature bras, a
Wardrobe that tracks how each piece feels (not just how many wears), a
Drop calendar that respects the small-batch ethic, and a Comfort Lab
with care videos for bamboo. The customer who finds her bra on the app
is a customer for life — and the app is what gets her there before she
returns the wrong size.

## 2. The six product pillars

### 1. The Fit Finder — solving the bra problem
Wire-free bras need different sizing logic than wired bras. Most
customers under-size or over-size on the first try. The Fit Finder
guides them through the brand's actual sizing methodology.

- 4-question guided fit (cup feel, band feel, support level, neckline preference)
- Per-style fit notes for the 8 signature bras (Andie, Carrie, etc.)
- Compare to bras the customer already owns ("if you wore X in size Y…")
- Photo of how the bra should sit (where the band lies, where the cup hits)
- Free size-swap returns flow tied to the loyalty wallet

### 2. The Wardrobe — feel, not just wears
Different from athleisure closets. A Free Label customer wants to know
which pieces actually felt good — not just how many times she wore them.

- Register every piece (auto-fill from order history; scan-to-add)
- Quick-tap "felt good today" / "felt off today" — no guilt, no streaks
- Pair-with suggestions for matching bamboo sets
- Per-fabric care guides (bamboo, organic cotton, lyocell)

### 3. The Drop — small-batch transparency
Free Label produces in small batches based on real demand. The Drop
pillar makes that visible — not as scarcity marketing, but as honest
operations.

- Per-drop count: "this drop is 220 Carrie bras"
- Restock-when-sold-out alerts (real, not fake urgency)
- Production progress: "in production · ships May 24"
- Bamboo origin and OEKO-TEX certification per drop
- Pre-order option for cult favourites

### 4. The Comfort Lab — care, fit, longevity
Bamboo lasts when cared for. The Lab teaches it.

- Care videos (gentle wash, no fabric softener, line-dry)
- Bra-fitting tips (where the band sits, how to adjust straps)
- Bamboo science (why it feels different, why it lasts)
- 30-day "find-your-fit" guarantee — videos for the swap process

### 5. The Shop — calm, multi-region
Free Label sells in CA and US directly; UK and EU on the way.

- Multi-currency (CAD, USD; GBP/EUR expandable)
- Drop calendar with notify-me on each
- Bundle builder (matching bamboo sets are the cult product)
- Notify-me on size-swap availability

### 6. The Studio — internal-facing web admin portal
The brand's internal twin. Catalog and orders stay in Shopify;
The Studio owns everything new the app introduces.

- Fit-Finder rules engine (per-style, per-cup-size guidance)
- Drop scheduler with production-batch tracker
- Wardrobe / passport editor (fit notes, fabric, OEKO-TEX certs)
- Concierge inbox (fit questions, size-swap requests, restock asks)
- Multilingual translation workflow (EN-first, FR for Quebec)
- Phase 1 analytics — fit-finder conversion, return rate by style,
  drop sell-through, restock-request volume

Built in the same brand palette so the team that uses it daily isn't
working in an off-brand admin tool.

## 3. Suggested screens (Phase 1)

> Visual wireframes:
> - **Mobile app** — open `mockups.html` for the Phase 1 phone screens
> - **The Studio (web admin portal)** — open `studio-mockups.html` for
>   the four core admin views: dashboard, Fit-Finder rules editor,
>   drop scheduler, concierge inbox.

1. Onboarding — language, fit profile, body comfort preferences
2. Home — restock alerts, drop hero, "find your fit"
3. The Fit Finder — 4-question guided flow
4. Product detail — fit notes, "ask the Lab" CTA
5. The Wardrobe — registered pieces, "felt good" log
6. The Drop — current drop with batch count + production progress
7. The Comfort Lab — care videos, fit tips
8. Lab chat (multilingual fit + fabric assistant)
9. Profile — sizes, language, privacy, "what we know about you"

## 4. Phase 1 feature set (months 0–4)

**Foundation**
- Apple / Google / email sign-in
- Multilingual onboarding (EN / FR at launch)
- Multi-currency (CAD, USD)
- Profile: cup + band + body comfort preferences (opt-in body shape)

**The Fit Finder**
- 4-question guided flow
- Per-style fit notes (8 signature bras)
- "Compare to a bra you own" anchor
- Visual fit guide per style
- Free size-swap returns

**The Wardrobe**
- Register every piece (order auto-fill; scan-to-add)
- "Felt good today" / "felt off today" quick log
- Pair-with suggestions for matching sets
- Per-fabric care guides

**The Drop**
- Per-drop batch count visible
- Restock-when-sold-out alerts
- Production progress per batch
- Pre-order for cult favourites

**The Comfort Lab**
- Care videos for bamboo, cotton, lyocell
- Bra-fitting tips per style
- Bamboo science explainers
- Find-your-fit swap process video

**The Shop**
- Multi-currency (CAD, USD)
- Drop calendar
- Bundle builder for matching sets
- Notify-me on size-swap availability

**Loyalty**
- "Free" rewards — points for fit-finder completion, reviews, referrals
- Free size-swap baked in as default — not a perk, a standard
- Refer-a-friend (give-and-get a credit)

**AI · Tier 1**
- Lab chat — multilingual fit + fabric coach (Sonnet)
- Fit-finder AI — proposes size from past orders + body comfort answers
- Visual search — photograph a bra style, find it
- Multilingual brand-voice translation (Haiku + brand glossary)
- Wardrobe-gap analyser — "you have 3 Andies but no everyday Carrie"

**The Studio (web admin portal)**
- Fit-Finder rules engine
- Drop scheduler with batch tracker
- Passport editor (fit notes, fabric, OEKO-TEX certs)
- Concierge inbox
- Multilingual translation workflow
- Phase 1 analytics

## 5. Phase 2 — Depth (months 5–9)

- ⬆ **AR fit visualization** — see a bra silhouette on body proportions (triggers Enterprise upgrade for native modules)
- **Photo-based fit check** — upload a mirror photo, get specific feedback (band placement, cup fit, strap length)
- **Body inclusivity expansion** — guidance for plus-cup (G–L) customers with extra confidence
- **Wholesale + boutique B2B portal** — partnered Vancouver / Toronto boutiques (triggers Enterprise upgrade for SSO + audit logging)
- **Heritage / archive sale** — past-season cult favourites re-released
- **Trans + nonbinary fit guidance** — explicit, opt-in, sensitive content for chest binders + post-top-surgery customers (Free Label's customer base includes this group)

## 6. Phase 3 — Cultural authority (months 10+)

- Editorial / journal — long-form on bra fitting, body comfort, bamboo
- Annual VOICES film series — customers in their pieces, real bodies
- ⬆ Demand-sensing AI — drives small-batch production planning
- ⬆ Multilingual content scaling AI — EN-first, AI drafts FR/ES/IT/JP for editor review
- Counterfeit-listing detection — Amazon, eBay, Poshmark
- VIP signal detection — concierge welcomes top-loyal customers
- Long-term wear study — anonymised data on which bras last 3+ years

## 7. Data we'd collect (with consent)

| Category               | Examples                                                | Use                                          |
| ---------------------- | ------------------------------------------------------- | -------------------------------------------- |
| Identity & contact     | email, name, address                                    | orders, shipping                             |
| Fit profile            | cup, band, body comfort preferences                     | reduce returns, recommend size               |
| Body shape (opt-in)    | for fit-finder accuracy                                 | safety filters on size suggestions           |
| Language & region      | UI language, country, currency                          | multi-region storefront                      |
| Wardrobe               | registered pieces, "felt good" logs, return reasons     | personalisation, design feedback             |
| Engagement             | views, wishlists, restock alerts opted into             | personalisation                              |
| Channel of origin      | online / Vancouver studio / boutique referral            | attribution                                  |
| Drop preferences       | which drops you opt into, pre-orders                     | demand sensing                               |

**Won't collect**: weight or BMI, before-after body photos, precise
GPS, contacts, social-graph imports, third-party ad-tracking IDs.
Body shape only with explicit opt-in for the fit-finder feature.

## 8. What to deliberately NOT build

- "Slimming" / "flattering" language — off-brand. Free Label is comfort-first, not body-shaping
- Body-shaming content of any kind — existential brand risk
- Fake scarcity / FOMO design — the small-batch story is real, doesn't need fake urgency
- Compression / shapewear-positioned products — wrong category fit
- Discount-heavy loyalty — off-brand. "Free" tier rewards size-swap and review behaviour, not new buys
- Auto-renewing subscriptions without one-tap pause / cancel
- Body-photo-based AI without explicit, narrow opt-in — privacy nightmare

## 9. Recommended SEYSO MaaS package

### Phase 1 launch — **Growth ($3,500/mo)** + **Studio add-on ($750/mo)** = **$4,250/mo**

| Growth feature                                | Why it fits Free Label                                                                                          |
| --------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| Both stores, React Native + Expo              | CA/US customer base mixed iOS/Android. Single codebase. OTA fits drop cadence                                   |
| Claude Sonnet & Haiku AI                      | Sonnet powers the Lab chat in EN/FR. Haiku batches care guides and translation                                  |
| RevenueCat (StoreKit 2 + Google Play Billing) | Future-proofs subscription bundle programs                                                                      |
| Sign in with Apple + Google                   | Reduces install friction                                                                                        |
| ASO quarterly                                 | "Wire-free bra", "bamboo bra Canada", "size inclusive activewear" all matter for discovery                      |
| 2 releases / month                            | Drop cadence demands a regular rhythm                                                                           |
| Shared Slack, 4h response                     | Right level for an independent brand at launch                                                                  |

**Starter is disqualified** — single platform, 5-screen ceiling, no
AI, 24h email support. None of those work for a brand whose
proposition depends on AI fit guidance and a careful drop cadence.

**Studio add-on ($750/mo)** is mandatory. Fit-Finder rules + drop
scheduler + production batch tracker form the brand's operational
backbone. Without it, fit guidance lives in spreadsheets.

### Year 2 trigger — upgrade to **Enterprise (from $8,000/mo)**

Upgrade when *any one* of these becomes a hard requirement:

1. **AR fit visualization** — native Swift/SwiftUI + Kotlin/Compose modules for body silhouette
2. **Wholesale / boutique B2B portal** — SSO + audit logging + RLS hardening for partner boutiques
3. **EU / UK GDPR data residency** — when European volume becomes material
4. **24/7 SLA with 1h response** — when a major retailer makes uptime contractual
5. **Photo-based fit check at scale** — body-photo-data adjacency requires Enterprise audit posture

### Contract notes for Year 1

- 12-month term on Growth + Studio (single combined invoice)
- Pre-negotiated upgrade path to Enterprise; build credit prorated
- AI overage clause: usage above the Growth quota billed at cost +20%
- Brand-side approval on every customer-facing fit/care claim
- Studio one-time build cost: **$32–48K** included in the Phase 1 build (separate from monthly platform fees)

## 10. Suggested next step

A two-week paid discovery — confirm e-commerce platform (Shopify),
audit existing fit-related return data, run 5 customer interviews
(ideally one cult-fan with 6+ pieces, one new buyer with first
return, one plus-cup G-L customer, one trans/nonbinary customer
using bras as binders, one Vancouver-local), and lock the Phase 1
scope before any build cost is committed.
