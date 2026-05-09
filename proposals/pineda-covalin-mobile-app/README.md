# Pineda Covalín — Mobile App MVP Proposal

> Note: pinedacovalin.com blocked the automated content fetch. Brand
> understanding is drawn from public sources — Wikipedia, the official US
> site, retail directories, and press coverage — and should be validated
> against any internal materials the brand shares.

## 1. Strategy in one paragraph

Erth to Erth's app stewards a wardrobe. **Pineda Covalín's app should be a
pocket museum, a luxury gift concierge, and a traveler's companion.** The
brand's product is not silk — it is the cultural story woven into silk. Most
of that story is invisible to the international tourist who buys at an
airport boutique, takes the piece home, and never connects with the brand
again. The app turns that one-time purchase into an ongoing relationship,
elevates the gift (which is half their volume), and gives the existing
40+-store retail footprint a digital companion that tourists can use before,
during, and long after their trip.

## 2. The six product pillars

### 1. The Atelier — every piece carries its story

Scan a piece's tag (or open from order history) and unlock:

- The motif's meaning — Huichol cosmology, the monarch's migration, pre-Hispanic codices
- The artist or collaboration — Frida estate, museum partnerships, contemporary artists
- The technique — silk-screen process, regional craft, artisan community
- A 90-second audio guide in the customer's language
- Care guide — silk-specific, color-aware, climate-aware

### 2. The Mercado — luxury shop curated like a museum

- Browse by **collection** (Monarcas · Huichol · Frida · Día de Muertos · Diego · Codices) rather than category alone
- Artist & collaboration spotlights with editorial pages
- Limited drops — numbered collector pieces, museum-store exclusives
- Cultural-calendar drops — Día de Muertos, monarch migration, Frida's birthday, Independence Day
- Multi-currency, multi-language, multi-region (MX / US / EU / Asia-Pacific)

### 3. The Gift Concierge — gifting as a first-class flow

Half their volume is gifting. Most apps treat this as an afterthought.

- Gift-mode checkout — signature wrapping, handwritten-style card, 30-second video message
- Schedule the unboxing — recipient unlocks the Atelier story when they confirm "I just opened it"
- Gift registry / wishlist — shareable link
- Predictive gift reminders — learns each customer's gifting cadence
- Corporate & diplomatic gifting portal (Phase 2) — bulk orders, dedications, white-glove handler

### 4. The Traveler — designed for tourist reality

40% of Mexican sales come from tourism. The app should be built around that.

- "I'm visiting Mexico" mode — surfaces airport boutiques, museum stores, hotel locations, the Polanco studio
- Boutique appointments — private viewing booking
- Tax-refund flow — country-by-country guidance
- Buy-in-city, collect-at-airport on departure

### 5. The Collector's Archive

- Register every owned piece (auto-fill from order history; scan-to-add for older pieces)
- See the full series; preview the next collection
- Digital certificate of authenticity — replaces the paper certificate
- Collector tiers as monarch lifecycle: **Huevo → Oruga → Crisálida → Mariposa**
  Rewards are *access*, not discounts: studio visits, advance drops, signed pieces, behind-the-scenes prints

### 6. El Estudio — the brand's web admin portal

The mobile app is the customer-facing surface. **El Estudio** is the
internal-facing twin: a web app the editorial team, curators, concierge,
B2B account managers, and analysts use every day. Catalog and orders stay
in Shopify / VTEX. El Estudio owns everything new the app introduces.

- **Atelier passport editor** — motif, story, technique, artist bio, audio guide upload, multilingual fields with curator review
- **Translation workflow** — Spanish-first; Claude drafts EN/FR/IT/JP/ZH; curator approves per locale; one-click publish
- **Cultural calendar & drop scheduler** — push copy, hero imagery, schedule per region
- **Concierge inbox** — escalations from the cultural docent, B2B requests, VIP messages
- **VIP / collector tier admin** — comp invitations, signed-piece allocation, Mariposa-tier overrides
- **Authenticity & moderation queue** — review NFC tags, flag counterfeits, moderate user-generated content
- **Heritage archive editor** (Phase 2) — vintage piece details, edition numbers, certificates
- **B2B corporate gifting portal** (Phase 2 — triggers Enterprise upgrade)
- **Analytics dashboards** — tourist retention, gift uptake, recipient activation, cross-language reach

Same backend API as the mobile app — different UI for different users.
Built in the same brand palette so the team that uses it daily isn't
working in an off-brand admin tool.

## 3. Suggested screens (Phase 1)

> Visual wireframes:
> - **Mobile app** — open `mockups.html` for the Phase 1 phone screens
> - **Studio (web admin portal)** — open `studio-mockups.html` for the four
>   core admin views: dashboard, Atelier editor with translation workflow,
>   cultural calendar, and concierge inbox.
>
> Both in the brand palette (warm cream + cochineal red + saffron).

1. Onboarding — language, region, motif preferences, gift-vs-self mode
2. Home — drop hero, cultural calendar, your collection shortcut
3. Collection page (Mercado) — browse by Huichol / Frida / Monarcas
4. Product detail — passport pills, "ask the docent" CTA
5. The Atelier — cultural passport with audio guide
6. Scan / authenticity verification
7. Cultural docent chat (multilingual)
8. Gift concierge — wrap, message, schedule unboxing
9. The Collector's Archive
10. Travel mode — boutiques, appointments, tax-refund

## 4. Phase 1 feature set (months 0–4)

**Foundation**
- Sign-in with Apple / Google / email; multilingual onboarding (EN/ES, expandable)
- Multi-currency, multi-region storefront
- Profile: language, region, motif preferences, gift-vs-self, occasion patterns

**Atelier (cultural passport)**
- Scan QR / NFC tag or open from order history
- Motif meaning, technique, artist, artisan community
- Audio guide (90-sec narration, customer's language)
- Care guide — silk + color + climate

**Mercado**
- Browse by collection
- Artist / collaboration spotlights
- Limited drops + cultural-calendar push
- Visual search

**Gift Concierge**
- Gift-mode checkout — wrapping, card, video message
- Scheduled delivery & unbox-triggered story unlock
- Gift registry / wishlist
- Predictive gift reminders

**Traveler**
- "Visiting Mexico" mode — boutiques, museums, hotels, studio
- Boutique appointment booking
- Tax-refund flow
- Buy-in-city, collect-at-airport

**Collector's Archive**
- Register every piece (order auto-fill; scan-to-add)
- Full-series view
- Digital certificate of authenticity
- Mariposa-cycle tiers

**Service & community**
- Scarf-tying studio (video library, 30+ techniques)
- Cultural calendar push notifications
- Atelier services booking — cleaning, restoration, edge repair (hotel pickup for tourists)

**AI · Tier 1**
- Cultural docent chat (multilingual, Sonnet 4.6)
- Multilingual translation with cultural fidelity (Haiku batch + brand glossary)
- Gift recommender
- Outfit / occasion advisor
- Visual search

**El Estudio (web admin portal)**
- Atelier passport editor (multilingual fields, curator review)
- Translation workflow — Spanish-first, Claude drafts, one-click publish per locale
- Cultural calendar / drop scheduler (push, hero imagery, region targeting)
- Concierge inbox — docent escalations, B2B requests, VIP messages
- VIP / Mariposa-tier admin (comp invitations, signed-piece allocation)
- Authenticity & moderation queue
- Phase 1 analytics — tourist retention, gift uptake, recipient activation, language reach

## 5. Phase 2 — Depth (months 5–9)

- ⬆ **AR scarf try-on** (cloth-drape simulation) — *triggers Enterprise upgrade*
- ⬆ **AR framing preview** (scarf as wall art)
- **Tour-mode docent** — private curatorial essay on the customer's own collection
- **Voice-driven shopping** for customers not literate in current UI languages
- **Image-to-occasion matcher** (upload outfit, get recommendation)
- **Photo-based authenticity check** (vision model trained on real pieces)
- **Heritage archive marketplace** — brand-curated vintage / discontinued releases
- **Gift-narration video** — auto-generated 60-sec film at the unbox moment
- ⬆ **Corporate / diplomatic gifting portal** — *triggers Enterprise upgrade*

## 6. Phase 3 — Cultural authority (months 10+)

- Editorial / culture content engine (long-form journal, artisan profiles)
- Behind-the-scenes / atelier livestreams
- Limited-edition lottery / waitlist for collaborations
- AI-assisted bespoke concept (VIP-only, strict guardrails — concept sketches routed to atelier for human design; never AI as final art)
- ⬆ Demand-sensing AI for production runs
- ⬆ Multilingual content scaling AI (Spanish-first, AI drafts EN/FR/IT/JP/ZH for editor review)
- Counterfeit-listing detection — scans Mercado Libre, eBay, Amazon, Instagram
- VIP signal detection — surfaces emerging high-value collectors before they self-identify

## 7. Data we'd collect (with consent)

| Category               | Examples                                                | Use                                          |
| ---------------------- | ------------------------------------------------------- | -------------------------------------------- |
| Identity & contact     | email, name, address                                    | orders, shipping                             |
| Language & region      | UI language, country, currency                          | multi-region experience                      |
| Motif preferences      | Frida / Huichol / monarcas / codices / Día de Muertos   | recommendations, drop targeting              |
| Buyer mode             | gift vs self                                            | drives the entire UX                         |
| Travel signals         | "visiting Mexico in November"                           | boutique appointments, tourist features      |
| Collection size        | registered pieces                                       | collector recognition, completion suggestions|
| Occasion patterns      | mother's day, anniversary, holiday cadence              | predictive gift reminders                    |
| Channel of origin      | airport / museum / boutique / hotel / online            | attribution, re-engagement                   |
| Engagement             | views, wishlists, push response                         | personalisation                              |

**Won't collect**: precise GPS, contacts, social-graph imports, third-party
ad-tracking IDs.

## 8. What to deliberately NOT build

- AI-generated final designs or motifs of any kind — existential threat to a brand whose value is authentic Mexican craft
- Open peer-to-peer resale — wrong shape for luxury; brand-curated archive only
- Discount-heavy loyalty — off-brand. Access-and-recognition only
- Aggressive gamification — luxury demands calm
- Sustainability dashboards (off-brand — Pineda Covalín is craft, not circular)

## 9. Recommended SEYSO MaaS package

### Phase 1 launch — **Growth ($3,500/mo)** + **Studio add-on ($750/mo)** = **$4,250/mo**

| Growth feature                                | Why it fits Pineda Covalín                                                                                                |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Both stores, React Native + Expo              | Tourists are mixed Android (heavy in MX) + iOS (heavy in US/JP); single codebase, OTA updates suit cultural-calendar drops|
| Claude Sonnet & Haiku AI                      | Sonnet powers the cultural docent in 6 languages; Haiku batch-summarises Atelier stories and runs cheap translation       |
| RevenueCat (StoreKit 2 + Google Play Billing) | Future-proofs digital-certificate or VIP-membership monetisation                                                          |
| Sign in with Apple + Google                   | Required for tourist users — friction to a luxury-brand login is real                                                     |
| ASO quarterly                                 | Tourist discovery — "Mexico souvenir," "silk scarves Mexico City," "Frida Kahlo gift"                                     |
| 2 releases / month                            | Cultural-calendar drops demand a regular cadence                                                                          |
| Shared Slack, 4h response                     | Right level for a luxury brand at launch — not over-engineered                                                            |

**Starter is disqualified** — single platform, 5-screen ceiling, no AI, 24h
email support. None of those work for an international luxury brand whose
proposition depends on multilingual AI storytelling.

**Studio add-on ($750/mo)** covers infra + editorial AI usage, ~5
maintenance hours/month, dependency upgrades, and small editor-driven
feature requests. Two Studio releases per month aligned with the mobile
cadence. The Studio fee folds into the Enterprise total when the brand
upgrades — no double-billing.

### Year 2 trigger — upgrade to **Enterprise (from $8,000/mo)**

Upgrade when *any one* of these becomes a hard requirement:

1. **AR scarf try-on at high fidelity** — native Swift/SwiftUI + Kotlin/Compose modules (Enterprise) deliver smoother cloth-drape than React Native AR
2. **Corporate / diplomatic gifting portal** — SSO + audit logging + RLS hardening (Enterprise-only) is the right home for B2B
3. **EU/Asia data residency** — GDPR + APAC localisation rules eventually become contractual
4. **24/7 SLA with 1h response** — when a museum-store partner or luxury hotel contractually requires it (their airport stores are genuinely 24/7 globally)

### Contract notes for Year 1

- 12-month term on Growth + Studio (single combined invoice)
- Pre-negotiated upgrade path to Enterprise with build credit prorated against the Enterprise tier
- AI overage clause: usage above the Growth quota billed at cost +20% — caps exposure to a viral moment in the docent
- Studio one-time build cost: **$30–45K** included in the Phase 1 build (separate from monthly platform fees)

## 10. Suggested next step

A two-week paid discovery — confirm e-commerce platform (likely VTEX or
Shopify), audit the existing customer data, run 5 customer interviews
(ideally one tourist, one collector, one corporate gifter, one EU buyer,
one US buyer), and lock the Phase 1 scope before any build cost is
committed.
