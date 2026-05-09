# Titika Active — Mobile App MVP Proposal

> Note: titikaactive.com blocked the automated content fetch. Brand
> understanding is drawn from public sources — the Asia site
> (titikaactive.hk), brand directories, retail listings, and
> Cathay/Asia Miles partnerships — and should be validated against
> internal materials.

## 1. Strategy in one paragraph

Erth to Erth's app stewards a wardrobe. Pineda Covalín's app is a pocket
museum. **Titika Active's app should be a daily companion to a versatile
life — gym, yoga, brunch, errands — for women who care about how their
activewear looks and performs.** "VERSATILE. ACTIVE. LIFE." is the brand
line, and the app should make those three words concrete: a closet that
shows you how to wear what you own across contexts, a practice library
that meets you wherever you are, a fit assistant that ends the legging-
sizing lottery, and a tribe that travels with you between Toronto, Hong
Kong, and beyond.

## 2. The six product pillars

### 1. The Closet — versatile by design
The brand's value proposition in one feature: every piece you own,
shown three ways. Studio. Street. Sunday.

- Register every piece (auto-fill from order history; scan-to-add for older pieces)
- "Wear it three ways" outfit grid — same piece across contexts
- Wear log with workout type, weather, and what worked
- Care guide per fabric

### 2. The Practice — your in-app studio
Activewear lives or dies on the workout adjacent to it. The app hosts
guided sessions tied to the pieces you own.

- Curated yoga, mobility, strength, low-impact, and "just-moving" sessions
- 10 / 20 / 45 minute formats — meets the customer where they are
- Audio-only mode for walks and runs
- Session recommendations by mood, energy, time
- Featured ambassador / instructor sessions

### 3. The Fit Atelier — end the sizing lottery
Leggings sizing is the highest-stakes friction in activewear. Solve
it once.

- Fit assistant chat with full size profile and past-order context
- Photo-based fit check — upload a mirror shot, get specific feedback
- Per-style fit notes ("runs small," "high compression," "best for short rise")
- Easy size-swap returns flow tied to the loyalty wallet

### 4. The Tribe — community without the noise
Activewear thrives on community. We design it to be calm, not loud.

- Local meetups (Toronto · Hong Kong · NYC · Vancouver as starter cities)
- Ambassador-led challenges, opt-in only
- "Fit looks" gallery — customers post how they wore a piece, with light moderation
- Cathay Asia Miles tie-in for redemption / earn (existing partnership)

### 5. The Shop — multi-region by default
Titika's customer base is split between Canada/US and Hong Kong/Asia.
The app respects that from screen one.

- Multi-currency (CAD, USD, HKD, JPY, AUD), multi-language (EN / 繁中 launch)
- Region-aware drop scheduling
- Style quiz that powers home recommendations
- Restock alerts and limited-edition push

### 6. The Studio — the brand's web admin portal
Internal-facing twin of the mobile app. Catalog and orders stay in
Shopify; The Studio owns everything new the app introduces.

- Closet & passport editor (fabric, fit, "wear it three ways" copy)
- Practice library admin (sessions, videos, instructors, schedule)
- Drop & cultural-calendar scheduler (region-aware push)
- Ambassador program — applications, comp pieces, content review
- Community moderation queue (looks, comments, reports)
- Customer concierge inbox — fit escalations, returns, ambassador DMs
- Analytics — fit-assist conversion, return rate by SKU, practice
  completion, regional adoption

Built in the same brand palette so the team that uses it daily isn't
working in an off-brand admin tool.

## 3. Suggested screens (Phase 1)

> Visual wireframes:
> - **Mobile app** — open `mockups.html` for the Phase 1 phone screens
> - **The Studio (web admin portal)** — open `studio-mockups.html` for the four
>   core admin views: dashboard, closet/passport editor, practice library,
>   community moderation queue.

1. Onboarding — language, region, body & fit profile, motivation
2. Home — today's practice suggestion, your closet shortcut, drop hero
3. The Practice — session library by mood / time / type
4. Closet — registered pieces with "three ways" looks
5. Product detail — fit pills, "ask the atelier" CTA, real-fit photos
6. Fit Atelier chat (multilingual, photo upload)
7. Tribe — feed of looks + local meetups
8. Rewards / Asia Miles wallet
9. Profile — sizes, fit history, language, privacy

## 4. Phase 1 feature set (months 0–4)

**Foundation**
- Apple / Google / email sign-in
- Multilingual onboarding (EN / 繁中 at launch; SC, JP, KR, FR expandable)
- Multi-currency, multi-region storefront (CA / US / HK / wider Asia)
- Profile: sizes, fit preferences, motivation tags, region, opt-ins

**Closet**
- Register every piece (order auto-fill; scan-to-add)
- "Wear it three ways" outfit grid per piece
- Wear log (workout type, weather)
- Care guide per fabric

**Practice**
- 10 / 20 / 45-minute guided sessions
- Yoga · mobility · strength · low-impact · just-moving categories
- Audio-only mode for walks / runs
- Mood + energy + time recommender

**Fit Atelier**
- AI fit chat with size profile + past-order context
- Photo-based fit check (Phase 1 — text-only feedback; vision-based in Phase 2)
- Per-style fit notes
- Easy size-swap returns flow

**Tribe**
- Local meetup browser (Toronto · HK · NYC · Vancouver to start)
- Ambassador-led challenges (opt-in)
- Looks gallery (light moderation)

**Shop**
- Multi-currency, multi-region
- Drop hero + restock alerts
- Style quiz → home feed

**Rewards**
- Points wallet — Titika tier ladder
- Cathay Asia Miles earn / redeem integration (HK customers)
- Birthday + anniversary surprise

**AI · Tier 1**
- Fit assistant chat (Sonnet 4.6) — multilingual
- Practice recommender (Haiku) — mood, energy, time
- Visual search — see a look, find the piece
- Outfit-builder AI — three contexts per piece
- Multilingual brand-voice translation (Spanish — wait, EN/繁中 + others)

**The Studio (web admin portal)**
- Closet/passport editor with multilingual fields
- Practice library admin (upload sessions, schedule, instructor profiles)
- Drop & calendar scheduler (region-aware)
- Ambassador program admin
- Community moderation queue
- Concierge inbox
- Phase 1 analytics

## 5. Phase 2 — Depth (months 5–9)

- ⬆ **AR fit visualisation** — see leggings on a body silhouette using your size profile (triggers Enterprise upgrade for native modules)
- **Vision-based fit check** — AI analyses a mirror photo for waistband fit, length, compression
- **Live classes** — scheduled live yoga / mobility with chat
- **Recovery + wellness coach (AI)** — sleep / mood / soreness inputs, recommended practice
- **Local studio partner program** — partnered yoga / pilates studios; Titika rewards for visiting
- **Wholesale & ambassador portal (B2B)** — applications, comp pieces, content review (triggers Enterprise upgrade for SSO + audit logging)
- **Heritage / archive sale** — past-season pieces re-released with provenance

## 6. Phase 3 — Cultural authority (months 10+)

- Editorial / journal — long-form content on sport, design, training
- Branded events — pop-up classes in Toronto, HK, NYC
- Annual VERSATILE film series — short documentaries on ambassadors
- ⬆ Demand-sensing AI — drives reprints across CA / US / HK / wider Asia
- ⬆ Multilingual content scaling AI — EN-first, AI drafts 繁中 / 简中 / JP / KR / FR
- Ambassador-revenue-share marketplace — content that converts
- Counterfeit listing detection (Amazon / ThredUp / Asian marketplaces)

## 7. Data we'd collect (with consent)

| Category               | Examples                                                | Use                                          |
| ---------------------- | ------------------------------------------------------- | -------------------------------------------- |
| Identity & contact     | email, name, address                                    | orders, shipping                             |
| Fit profile            | bra size, top, bottom, inseam, fit notes (opt-in body)  | reduce returns, recommend size               |
| Language & region      | UI language, country, currency                          | multi-region storefront                      |
| Practice               | sessions completed, durations, time-of-day              | smarter recommendations                      |
| Closet                 | registered pieces, wear count, "three ways" choices     | personalisation                              |
| Motivation tags        | yoga / strength / running / lifestyle                   | content + product targeting                  |
| Tribe                  | meetups attended, challenges joined, ambassador follows | community matching                           |
| Engagement             | views, wishlists, push response                         | personalisation                              |
| Channel of origin      | online / Amazon / Pinkoi / store / friend referral      | attribution                                  |

**Won't collect**: weight or BMI (off-brand), precise GPS, contacts,
social-graph imports, third-party ad-tracking IDs.

## 8. What to deliberately NOT build

- Body-tracking metrics (weight, BMI, body-fat) — triggering, off-brand
- AI-generated workouts that replace human teachers — diminishes The Practice
- Aggressive gamification of streaks / shaming — wrong tone
- Sustainability dashboards (off-brand — Titika is performance + couture, not circular)
- Generic AI chatbot for customer service before a human team can escalate

## 9. Recommended SEYSO MaaS package

### Phase 1 launch — **Growth ($3,500/mo)** + **Studio add-on ($750/mo)** = **$4,250/mo**

| Growth feature                                | Why it fits Titika Active                                                                              |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Both stores, React Native + Expo              | Mixed-OS reality (iOS heavy CA/HK; Android heavy in wider Asia); single codebase, OTA updates          |
| Claude Sonnet & Haiku AI                      | Sonnet powers the fit chat in EN + 繁中; Haiku batch-summarises fabrics, drafts translations           |
| RevenueCat (StoreKit 2 + Google Play Billing) | Future-proofs subscription practice content or VIP membership                                          |
| Sign in with Apple + Google                   | Activewear customers won't fill forms                                                                  |
| ASO quarterly                                 | "yoga leggings," "Hong Kong activewear," "Lululemon alternative" matter                                |
| 2 releases / month                            | Drop cadence + practice content updates demand a regular rhythm                                        |
| Shared Slack, 4h response                     | Right level for a premium brand at launch                                                              |

**Starter is disqualified** — single platform, 5-screen ceiling, no AI,
24h email support. None of those work for a multi-region athleisure
brand whose proposition depends on multilingual AI and a content library.

**Studio add-on ($750/mo)** covers infra + editorial AI usage, ~5
maintenance hours/month, dependency upgrades, and small editor-driven
feature requests. Folds into the Enterprise total when the brand
upgrades.

### Year 2 trigger — upgrade to **Enterprise (from $8,000/mo)**

Upgrade when *any one* of these becomes a hard requirement:

1. **AR fit visualisation** — native Swift/SwiftUI + Kotlin/Compose modules deliver smoother body simulation than React Native
2. **Wholesale / ambassador B2B portal** — SSO + audit logging + RLS hardening required for serious B2B
3. **Asia data residency** — APAC localisation rules eventually become contractual as HK / wider-Asia volume grows
4. **24/7 SLA with 1h response** — when a major retailer or platform partner makes uptime contractual

### Contract notes for Year 1

- 12-month term on Growth + Studio (single combined invoice)
- Pre-negotiated upgrade path to Enterprise; build credit prorated
- AI overage clause: usage above the Growth quota billed at cost +20% — caps exposure to a viral fit-chat moment
- Studio one-time build cost: **$30–45K** included in the Phase 1 build (separate from monthly platform fees)

## 10. Suggested next step

A two-week paid discovery — confirm e-commerce platform (Shopify
likely), audit existing customer data, run 5 customer interviews
(ideally one Toronto, one HK, one US, one new buyer, one ambassador),
and lock the Phase 1 scope before any build cost is committed.
