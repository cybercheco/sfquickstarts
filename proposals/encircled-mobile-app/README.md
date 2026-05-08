# Encircled — Mobile App MVP Proposal

> Note: encircled.ca was researched via public sources — the brand's
> About page, founder interviews, third-party reviews of the
> Chrysalis Cardi, and B Corp / sustainable-fashion directories.
> Validate against internal materials before committing budget.

## 1. Strategy in one paragraph

Erth to Erth stewards a wardrobe. Pineda Covalín is a pocket museum.
Titika Active is a daily companion. Kotn is a thread to the people
who made it. **Encircled's app should be a transformation engine.**
The brand's defining piece is the Chrysalis Cardi — eight garments in
one — and the brand's promise is that every piece works harder than
it looks: multi-way silhouettes, a lifetime repair guarantee, factories
30 km from the studio. The app makes that promise visible. It teaches
customers the styles they own without knowing it, builds capsules for
their next trip, and turns the brand's "guaranteed for life" pledge
into a one-tap workflow. The customer ends up owning fewer pieces, but
wearing them more — exactly what the brand has been arguing since 2012.

## 2. The six product pillars

### 1. The Many — every piece, every way to wear it
The Chrysalis Cardi has eight documented styles. Most owners use two
or three. The app teaches the rest.

- Per-piece "ways to wear" gallery (photos + 30-sec videos)
- AR overlay (Phase 2) — see a style before you try it
- Save your favourite styles per piece
- Style-of-the-week notification
- Cross-piece pairings ("Chrysalis Cardi → Wide-leg pant → 4 outfits")

### 2. The Capsule — curate, then travel
Encircled's customer is the traveller who wants to pack light. The
Capsule pillar makes that effortless.

- Trip planner: destination, length, weather, dress code → capsule
  built from your owned pieces
- Pack-light score (weight, volume, outfit count)
- Save capsules by trip type (work travel, beach, city break)
- Climate-aware fabric guidance (merino for cold; tencel for hot)
- Share a capsule with a friend who's about to travel

### 3. The Atelier — guaranteed for life, in one tap
The lifetime repair guarantee is the brand's proof of slow fashion.
The app makes it as easy as a return label.

- Scan a piece → photo the damage → repair quote and turnaround
- Free repair request flow (book pickup or use a label)
- Repair history per piece — visible in the Wardrobe
- Care + style longevity videos (how to wash, how to fold)
- Drop-off at the Toronto studio for local customers

### 4. The Wardrobe — register every piece
Foundation for The Many, The Capsule, and The Atelier. Without it
the rest doesn't work.

- Register every piece (auto-fill from order history; scan-to-add)
- Wear log with cost-per-wear
- Outfit grid showing all combinations
- Repair history, multi-way styles unlocked, capsules used in

### 5. The Shop — slow drops, deeper stories
Encircled is a small-collections brand. The shop reflects that.

- Multi-currency (CAD, USD), bilingual EN/FR (Quebec)
- Drop hero + restock alerts
- Founder-narrated story per drop
- Style quiz powered by your travel and lifestyle answers

### 6. The Studio — internal-facing web admin portal
The brand's internal twin. Catalog and orders stay in Shopify;
The Studio owns everything new the app introduces.

- Multi-way style library — author the styles for each piece
- Repair queue — incoming requests, photos, AI triage, repair tracking
- Capsule template library — staff-curated trip presets
- Drop scheduler — small-collection cadence, narrated
- Concierge inbox — fit, repair, capsule questions
- Multilingual translation workflow — EN-first, FR drafts via Claude
- Phase 1 analytics — multi-way unlock rate, repair conversion,
  capsule adoption, cost-per-wear distribution

Built in the same brand palette so the team that uses it daily isn't
working in an off-brand admin tool.

## 3. Suggested screens (Phase 1)

> Visual wireframes:
> - **Mobile app** — open `mockups.html` for the Phase 1 phone screens
> - **The Studio (web admin portal)** — open `studio-mockups.html` for
>   the four core admin views: dashboard, multi-way style editor,
>   repair queue, concierge inbox.

1. Onboarding — language, travel style, capsule motivation, sizes
2. Home — today's style, upcoming trip, drop hero
3. The Many — Chrysalis Cardi · 8 ways to wear
4. The Wardrobe — registered pieces, multi-way unlocked, cost-per-wear
5. Product detail — multi-way preview, "ask the Atelier" CTA
6. The Capsule — trip planner with auto-built capsule
7. The Atelier — repair request flow
8. Atelier chat (multilingual fit + care + repair)
9. Profile — sizes, language, privacy, "what we know about you"

## 4. Phase 1 feature set (months 0–4)

**Foundation**
- Apple / Google / email sign-in
- Multilingual onboarding (EN / FR at launch)
- Multi-currency (CAD, USD), shipping to CA / US / intl
- Profile: sizes, travel style, lifestyle, motivation tags

**The Many**
- Per-piece ways-to-wear gallery (photos + 30-sec video)
- "Style of the week" push notification
- Save favourites per piece
- Cross-piece outfit suggestions

**The Capsule**
- Trip planner: destination, length, weather, dress code → capsule
- Pack-light score per capsule
- Save and rename capsules
- Climate-aware fabric guidance

**The Atelier (lifetime repair)**
- Scan a piece → photo damage → repair quote + turnaround
- Booking flow (pickup or mail-in label)
- Repair history per piece in The Wardrobe
- Care + longevity videos

**The Wardrobe**
- Register every piece (order auto-fill; scan-to-add)
- Wear log + cost-per-wear
- Outfit grid + multi-way unlocks
- Repair history visible

**The Shop**
- Multi-currency, bilingual EN/FR
- Drop hero + restock alerts
- Founder-narrated drop story
- Style quiz

**Rewards**
- "Loops" — points for registering pieces, completing styles, posting reviews
- Repair credits redeemable via points
- Refer-a-friend (give-and-get a credit)

**AI · Tier 1**
- Multi-way styler chat — recognises a Chrysalis Cardi from a photo,
  walks through all 8 styles
- Capsule builder AI — destination + length + weather → capsule
- Atelier care + repair chat (Sonnet, multilingual)
- Fit assistant chat — past-order context
- Multilingual brand-voice translation (Haiku + brand glossary)
- Wardrobe-gap analyser — "you're missing a black wide-leg for travel"

**The Studio (web admin portal)**
- Multi-way style library editor
- Repair queue with AI triage
- Capsule template library
- Drop scheduler
- Concierge inbox
- Multilingual translation workflow
- Phase 1 analytics

## 5. Phase 2 — Depth (months 5–9)

- ⬆ **AR multi-way preview** — see a Chrysalis Cardi style on a body silhouette before you try it (triggers Enterprise upgrade for native modules)
- **Photo-based repair triage** — vision AI classifies damage, returns DIY guide for tiny fixes or atelier quote
- **Photo-based fit check** — upload a mirror shot, get fit feedback
- **Wholesale + travel-retail portal** — partners like MEC, Away, hotel-shops (triggers Enterprise upgrade for SSO + audit logging)
- **Heritage / archive sale** — past-season Chrysalis variants re-released
- **Founder dispatches** — Kristi-narrated short videos per collection drop
- **Multi-traveler capsules** — share & co-edit a capsule with a partner

## 6. Phase 3 — Cultural authority (months 10+)

- Editorial / journal — long-form on slow fashion, multi-way design, travel
- Annual VOICES film series — short docs on long-life ownership
- ⬆ Demand-sensing AI — drives small-collection production planning
- ⬆ Multilingual content scaling AI — EN-first, AI drafts FR/ES/IT for editor review
- Counterfeit-listing detection — Amazon, Poshmark, eBay
- VIP signal detection — concierge welcomes top-loyal customers
- Long-term wear study — anonymised aggregate data on pieces worn ≥ 5 years

## 7. Data we'd collect (with consent)

| Category               | Examples                                                | Use                                          |
| ---------------------- | ------------------------------------------------------- | -------------------------------------------- |
| Identity & contact     | email, name, address                                    | orders, shipping                             |
| Fit profile            | sizes, fit notes (body shape opt-in)                    | reduce returns, recommend size               |
| Language & region      | UI language, country, currency                          | multi-region storefront                      |
| Travel style           | trip frequency, common destinations, packing preferences| capsule recommendations                      |
| Wardrobe               | registered pieces, wear count, multi-way unlocked, repair history | personalisation                  |
| Motivation tags        | sustainability / capsule / travel / lifetime-design     | content + product targeting                  |
| Engagement             | views, wishlists, push response                         | personalisation                              |
| Channel of origin      | online / Toronto studio / referral                      | attribution                                  |

**Won't collect**: precise GPS, contacts, social-graph imports,
third-party ad-tracking IDs, weight / BMI, body-shape data without
explicit opt-in.

## 8. What to deliberately NOT build

- AI-generated styling that ignores the brand's documented multi-way library — the styles are part of the design IP
- Aggressive resale (the brand promise is "guaranteed for life," not "flip and replace")
- Discount-heavy loyalty — off-brand. Loops recognise long-term ownership; they don't bribe new buyers
- Body-tracking metrics
- Generic AI customer-service chatbot before a human team can escalate
- Anything that puts repair-pickup logistics ahead of the repair experience itself

## 9. Recommended SEYSO MaaS package

### Phase 1 launch — **Growth ($3,500/mo)** + **Studio add-on ($750/mo)** = **$4,250/mo**

| Growth feature                                | Why it fits Encircled                                                                                          |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Both stores, React Native + Expo              | CA/US customer base mixed iOS/Android. Single codebase. OTA updates fit small-collection drop cadence          |
| Claude Sonnet & Haiku AI                      | Sonnet powers the multi-way styler and Atelier chat in EN/FR. Haiku batches translation drafts                 |
| RevenueCat (StoreKit 2 + Google Play Billing) | Future-proofs subscription capsule-curation or "Loops Plus" membership                                         |
| Sign in with Apple + Google                   | Reduces install friction                                                                                       |
| ASO quarterly                                 | "Travel clothing", "multi-way", "Canadian sustainable basics" all matter for discovery                         |
| 2 releases / month                            | Small-collection drop cadence demands a regular rhythm                                                         |
| Shared Slack, 4h response                     | Right level for a values-led brand at launch                                                                   |

**Starter is disqualified** — single platform, 5-screen ceiling, no
AI, 24h email support. None of those work for a brand whose value
proposition depends on AI styling and an evolving repair ledger.

**Studio add-on ($750/mo)** is mandatory. Encircled has more editorial
volume than other brands at this scale because every piece needs a
multi-way style library and a repair workflow. The Studio is where
that lives.

### Year 2 trigger — upgrade to **Enterprise (from $8,000/mo)**

Upgrade when *any one* of these becomes a hard requirement:

1. **AR multi-way preview** — native Swift/SwiftUI + Kotlin/Compose modules for stable on-body AR
2. **Wholesale / travel-retail B2B portal** — SSO + audit logging + RLS hardening for partners like MEC, Away, hotel-shops
3. **EU / UK GDPR data residency** — when European traveller volume grows
4. **24/7 SLA with 1h response** — when a major retail or platform partner makes uptime contractual

### Contract notes for Year 1

- 12-month term on Growth + Studio (single combined invoice)
- Pre-negotiated upgrade path to Enterprise; build credit prorated
- AI overage clause: usage above the Growth quota billed at cost +20%
- Brand-side approval on every customer-facing styling/care/repair claim
- Studio one-time build cost: **$30–45K** included in the Phase 1 build (separate from monthly platform fees)

## 10. Suggested next step

A two-week paid discovery — confirm e-commerce platform (Shopify),
audit existing customer + repair data, run 5 customer interviews
(ideally one Toronto local, one US frequent-traveller, one new buyer,
one long-time owner with 10+ pieces, one repair customer), and lock
the Phase 1 scope before any build cost is committed.
