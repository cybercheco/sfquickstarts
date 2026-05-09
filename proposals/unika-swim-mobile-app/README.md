# Ūnika Swim — Mobile App MVP Proposal

> Note: unikaswimwear.com was researched via public sources — Toronto
> Guardian, blogTO, Trend Hunter, Setting Mind, Vicki Duong's Canadian
> ethical-swim list, and the brand's IFundWomen profile. Validate
> against internal materials before committing budget.

## 1. Strategy in one paragraph

Ūnika Swim is the rare swimwear brand that does three things almost
no one else does: makes-to-order in Toronto, fits cup sizes AAA–H,
and accommodates mastectomy, ostomy, and surgical-recovery customers
without making a feature of their bodies. **The app should make the
brand's most personal service — an in-store custom-design appointment
— possible from the customer's couch.** A booking flow that
understands surgical-recovery needs without flagging them, a fabric
and print library where ECONYL® is searchable by texture and color, a
live order tracker for custom pieces, and a Closet that respects the
fact that for some customers, finding the right swimsuit is a year of
work after surgery. The brand's customer is loyal because the brand
saw her when no one else did. The app makes that visible at scale.

## 2. The six product pillars

### 1. The Atelier — book the appointment, design it first
Custom is the brand's flagship service. Most customers walk in
without knowing what they want. The app changes that.

- Browse the fabric and print library (search by texture, color, ECONYL® source)
- Pick cuts: one-piece, bikini top/bottom, cover-up
- Save a draft design before the appointment
- Book in-store appointment at 101 Yorkville with the right specialist
- Or book a remote video consult for out-of-Toronto customers

### 2. The Body — fit that respects the body it's for
Cup sizes AAA–H. Mastectomy / ostomy / scar accommodation. Body
shape opt-in. Never assumed, never made into a marketing hook.

- Optional sensitive-fit profile: post-mastectomy, ostomy, scars / burns
- Discreet — the data informs the appointment specialist, never the marketing AI
- Fit notes per cut + cup size
- Linked to the Atelier appointment so the specialist arrives prepared

### 3. The Order Tracker — custom is slow by design
Made-to-order means weeks, not days. The app makes the wait
transparent.

- Stage-by-stage: design confirmed · fabric cut · sewing · hand-finishing · ships
- Photo updates from the Toronto boutique at key milestones
- ECONYL® sourcing transparency — which post-industrial waste batch
- Realistic timeline (4–6 weeks for custom; faster for pre-made)

### 4. The Closet — register every piece, custom and pre-made
For long-time customers, this is a five-year archive of one-of-a-kind
work.

- Register every piece (auto-fill from order history; scan-to-add)
- Wear log (beach, pool, special occasion)
- Per-fabric care guides (ECONYL® is durable but not infinite)
- Repair / restoration workflow — bring an aging piece back to the boutique

### 5. The Shop — pre-made + cultural content
Calm shop for customers who don't want to wait six weeks for custom.

- Pre-made one-pieces, bikinis, cover-ups, scrunchies, accessories
- Multi-currency (CAD, USD, BRL); multilingual EN / PT / ES
- Beach-culture content — Brazilian heritage, Toronto-made, lifestyle
- Bundle with custom appointment booking

### 6. The Studio — internal-facing web admin portal
The brand's internal twin. Catalog and orders stay in Shopify; The
Studio owns everything new the app introduces.

- Fabric & print library editor — ECONYL® source, texture, availability
- Custom-order tracker — design status, fabric cut, sewing queue,
  hand-finishing, photo updates
- Appointment scheduler — match specialists to customer fit needs
  (cup size, surgical-recovery accommodation)
- Concierge inbox — fit questions, custom-design questions, sensitive
  fit conversations
- Multilingual translation workflow — EN / PT / ES
- Phase 1 analytics — appointment-to-order conversion, custom vs
  pre-made mix, ECONYL® batch utilisation, repair/restoration volume

Built in the same brand palette so the team that uses it daily isn't
working in an off-brand admin tool.

## 3. Suggested screens (Phase 1)

> Visual wireframes:
> - **Mobile app** — open `mockups.html` for the Phase 1 phone screens
> - **The Studio (web admin portal)** — open `studio-mockups.html` for
>   the four core admin views: dashboard, custom-order tracker, fabric
>   library editor, concierge inbox.

1. Onboarding — language (EN/PT/ES), body comfort preferences, sensitive-fit opt-in
2. Home — your appointment, your custom order in production, drop hero
3. The Atelier — book + design tool with fabric library
4. Fabric library — searchable ECONYL® fabrics + prints
5. Body / fit profile — cup, sizing, sensitive accommodation (opt-in)
6. Order tracker — stage-by-stage with photo updates
7. Product detail — pre-made shop with fit notes
8. Atelier chat (multilingual fit + design AI)
9. Profile — sizes, language, privacy, "what we know about you"

## 4. Phase 1 feature set (months 0–4)

**Foundation**
- Apple / Google / email sign-in
- Multilingual onboarding (EN / PT / ES at launch)
- Multi-currency (CAD, USD, BRL)
- Profile: cup, sizing, body comfort preferences, sensitive-fit opt-in

**The Atelier**
- Fabric & print library — searchable
- Custom design draft (cut · fabric · color · embellishment)
- In-store appointment booking at 101 Yorkville
- Remote video consult for out-of-Toronto customers
- Save designs across sessions

**The Body**
- Cup AAA–H sizing guide
- Surgical-recovery fit profile (post-mastectomy, ostomy, scars)
- Discreet handling: data informs specialist, never the AI's marketing copy
- Per-cut fit notes

**The Order Tracker**
- Stage-by-stage progress
- Photo updates at key milestones
- ECONYL® batch transparency
- Realistic timeline communication

**The Closet**
- Register every piece (order auto-fill; scan-to-add)
- Wear log
- Per-fabric care guides
- Repair / restoration request flow

**The Shop**
- Pre-made catalog
- Drop calendar
- Bundle with custom appointment
- Multi-currency

**Loyalty**
- "Sun" — points for appointments completed, restorations, referrals
- Anniversary recognition (5+ year customers honoured)
- Refer-a-friend (give-and-get a credit)

**AI · Tier 1**
- Atelier chat — multilingual custom-design coach (Sonnet)
- Fit assistant — cup AAA–H with surgical-recovery awareness
- Fabric explorer — describe what you want, AI surfaces matching ECONYL® fabrics
- Visual search — see a swim look, find similar at Ūnika
- Multilingual brand-voice translation (Haiku + brand glossary)
- Wardrobe-gap analyser — "you have 3 one-pieces but no cover-up"

**Compliance / sensitivity guardrails (non-negotiable)**
- Surgical-recovery profile data NEVER feeds marketing AI
- AI never assumes body shape; opt-in on every sensitive field
- Never "slimming" / "flattering" / "summer body" / "bikini body" copy
- Sensitive-fit content reviewed by Betsy before publish
- AI never recommends a product based on undisclosed body data

**The Studio (web admin portal)**
- Fabric & print library editor
- Custom-order tracker with photo upload at each stage
- Appointment scheduler with specialist matching
- Concierge inbox
- Multilingual translation workflow
- Phase 1 analytics

## 5. Phase 2 — Depth (months 5–9)

- ⬆ **AR custom-design preview** — render fabric + print on a body silhouette before booking (triggers Enterprise upgrade for native modules)
- **In-store iPad mode** — Studio mode for the boutique team to co-design with the customer in person
- **Remote video consult upgrades** — built-in fabric-cam for out-of-Toronto customers
- **Wholesale + boutique B2B portal** — partnered Yorkville / boutique resellers (triggers Enterprise upgrade for SSO + audit logging)
- **Heritage / archive sale** — past-season custom designs re-released as limited pre-made
- **Bilingual influencer / partnership content** — culturally-aware brand collaborations

## 6. Phase 3 — Cultural authority (months 10+)

- Editorial / journal — long-form on swimwear fit, post-surgery confidence, ECONYL® supply chain
- Annual VOICES film series — long-time customers' stories (with consent), founder story
- ⬆ Demand-sensing AI — drives fabric inventory + ECONYL® batch ordering
- ⬆ Multilingual content scaling AI — EN-first, AI drafts PT/ES/IT/FR for editor review
- Counterfeit-listing detection — Amazon, Etsy, AliExpress
- VIP signal detection — concierge welcomes 5+ year customers
- Mastectomy / ostomy advocacy partnerships — featured charity collaborations

## 7. Data we'd collect (with consent)

| Category               | Examples                                                | Use                                          |
| ---------------------- | ------------------------------------------------------- | -------------------------------------------- |
| Identity & contact     | email, name, address                                    | orders, shipping                             |
| Fit profile            | cup AAA–H, body comfort preferences                     | recommend size, design, cut                  |
| Sensitive-fit (opt-in) | post-mastectomy, ostomy, scar accommodation             | informs specialist; never marketing AI       |
| Language & region      | UI language, country, currency                          | multi-region storefront                      |
| Custom orders          | designs, fabrics, prints, milestones                    | order tracker, restoration history           |
| Closet                 | registered pieces, wear log                             | personalisation                              |
| Engagement             | views, wishlists, fabric-saved                           | demand-sensing                               |
| Channel of origin      | online / Yorkville studio / boutique                     | attribution                                  |

**Won't collect**: weight or BMI, before-after body photos without
explicit narrow opt-in, precise GPS, contacts, social-graph imports,
third-party ad-tracking IDs. Surgical-recovery data lives in a
separate, restricted audit-logged store and never trains AI.

## 8. What to deliberately NOT build

- **"Slimming" / "flattering" / "bikini body" / "summer body" copy** — off-brand and harmful
- **Body-photo-based AI features** without narrow, explicit opt-in — body images in swim are deeply private
- **Surgical-recovery as a marketing hook** — must be a service, not a campaign
- **Aggressive resale or fast-fashion mechanics** — custom is slow by design
- **Discount-heavy loyalty** — off-brand for a custom maker
- **AI recommendations driven by undisclosed body data** — privacy nightmare and brand suicide
- **Auto-renewing subscriptions without one-tap pause / cancel**

## 9. Recommended SEYSO MaaS package

### Phase 1 launch — **Growth ($3,500/mo)** + **Studio add-on ($750/mo)** = **$4,250/mo**

| Growth feature                                | Why it fits Ūnika                                                                                              |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Both stores, React Native + Expo              | Mixed CA/US/Brazil customer base; single codebase; OTA fits drop cadence                                       |
| Claude Sonnet & Haiku AI                      | Sonnet powers Atelier chat in EN/PT/ES; Haiku batches fabric descriptions and translation                      |
| RevenueCat (StoreKit 2 + Google Play Billing) | Future-proofs subscription bundle programs                                                                     |
| Sign in with Apple + Google                   | Reduces install friction                                                                                       |
| ASO quarterly                                 | "Custom swimwear Toronto", "ECONYL bikini", "post-mastectomy swim" all matter for discovery                    |
| 2 releases / month                            | Drop cadence + fabric library updates demand a regular rhythm                                                  |
| Shared Slack, 4h response                     | Right level for an independent custom-maker at launch                                                          |

**Starter is disqualified** — single platform, 5-screen ceiling, no
AI, 24h email support. None of those work for a brand whose
proposition depends on multilingual custom-design AI and a sensitive
appointment scheduler.

**Studio add-on ($750/mo)** is mandatory and especially important
here. Custom-order tracker + fabric library + appointment scheduler
with sensitive-fit specialist matching together form the brand's
operational backbone.

### Year 2 trigger — upgrade to **Enterprise (from $8,000/mo)**

Upgrade when *any one* of these becomes a hard requirement:

1. **AR custom-design preview** — native Swift/SwiftUI + Kotlin/Compose modules for body silhouette
2. **Wholesale / boutique B2B portal** — SSO + audit logging + RLS hardening
3. **EU / Brazilian data residency** — GDPR + LGPD as European/Brazilian volume becomes material
4. **In-store iPad POS integration** — boutique team co-designs with customers; needs hardened device management
5. **24/7 SLA with 1h response** — when a major retailer or partner makes uptime contractual

### Contract notes for Year 1

- 12-month term on Growth + Studio (single combined invoice)
- Pre-negotiated upgrade path to Enterprise; build credit prorated
- AI overage clause: usage above the Growth quota billed at cost +20%
- **Sensitive-fit data segregation clause** — surgical-recovery data lives in a restricted, audit-logged store that never trains AI. Non-negotiable.
- Brand-side approval on every customer-facing fit / inclusivity / cultural claim
- Studio one-time build cost: **$35–55K** included in the Phase 1 build (custom-order tracker + fabric library + appointment scheduler are higher complexity than apparel clients)

## 10. Suggested next step

A two-week paid discovery — confirm e-commerce platform (Shopify),
audit existing custom-order data, run 5 customer interviews (ideally
one cult-fan with 5+ pieces, one post-mastectomy customer, one
remote-Brazil customer, one new buyer, one Yorkville-local), and
lock the Phase 1 scope before any build cost is committed. Critical
output: alignment with Betsy on the sensitive-fit data segregation
boundary.
