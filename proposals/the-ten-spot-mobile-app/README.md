# The Ten Spot — Mobile App MVP Proposal

> Note: thetenspot.com was researched via public sources — Franchise
> Canada profiles, the brand's About and Franchise pages, LinkedIn,
> and the brand's own franchise marketing materials. Validate
> against internal materials before committing budget.

> Categorical note — this is the **first service-and-multi-location
> franchise brand** in the proposal series. Previous nine clients
> were product brands (apparel, accessories, swim, skincare, supps).
> The Ten Spot is a 33+ location beauty-bar franchise with nails,
> waxing, laser, skin services. The proposal departs structurally:
> booking is the primary feature, not shopping.

## 1. Strategy in one paragraph

The Ten Spot is North America's largest multi-service beauty-bar
franchise — 33+ locations doing nails, waxing, laser hair removal,
and skin. Customers book recurring services (waxes every 4 weeks,
lash refills every 3, laser series of 6) at multiple locations
depending on where they are that day. **The app should make
recurring booking effortless and the prep + aftercare educational.**
A booking flow that knows your favorite location and favorite
technician, an automated calendar of "your next appointments are
due," service-specific prep guides (don't shave 24 hours before a
wax) and aftercare (no sun for 48 hours after laser), and a
membership wallet that travels across all 33+ locations. The brand's
customer is loyal because the brand sees her every 3–4 weeks. The
app is what keeps her there for 5 years.

## 2. The six product pillars

### 1. Book — the primary feature
Booking is what brings the customer in. Make it the fastest one in
the category.

- One-tap re-book ("same as last time")
- Location-aware: home location + nearby locations
- Service-aware: filter by nails, wax, laser, skin
- Technician-aware: book with the same person (or anyone)
- Wait-list: get notified when a spot opens
- Multi-service combos ("brow wax + lash lift") in one booking

### 2. Your Spot — your relationships
The brand's strength is the relationship between technician and
customer. The app surfaces it.

- Favorite location · favorite technician · favorite service combo
- Service history (last 12 months, exportable)
- Recurring schedule view: "your wax is due in 6 days"
- Birthday + anniversary recognition

### 3. Prep + After — service-specific care
Most service brands treat prep as a footnote. The Ten Spot can lead
on it.

- Pre-service guides: "no shaving 24 hr before wax", "no caffeine
  before laser", "exfoliate the night before"
- Post-service guides: "no sun for 48 hr", "no swimming for 24 hr"
- Push reminders: "your laser appt is tomorrow — read this 2-min guide"
- Sensitive-skin alerts when a customer profile flags reactivity

### 4. The Calendar — recurring care, automated
Beauty maintenance is recurring. Most customers under-book.

- Auto-suggest the next appointment based on your past cadence
- Series tracking: "you're 3 of 6 laser sessions in"
- Membership benefits visible per service
- Multi-service planning: "schedule your wax + lash refill same day"

### 5. The Shop — gift cards, memberships, retail
- Gift card purchase + redemption (huge driver for the category)
- Membership tier purchase / management
- Retail aftercare products (if/when carried)
- Multi-location credit balance

### 6. The Studio — internal-facing web admin portal
Multi-location franchise = complex Studio. Catalog and bookings
likely sync with existing booking software (Booker / Mindbody);
The Studio sits on top.

- Per-location dashboard: bookings today, no-shows, technician
  utilisation, revenue
- Master calendar across all locations
- Technician schedule editor + skill matrix (who can do laser,
  who specializes in lash)
- Service catalog editor (per-location pricing variation)
- Membership / loyalty admin
- Concierge inbox — customer questions, escalations from app chat
- Franchise corporate vs franchise-owner view (RBAC)
- Multilingual translation workflow — EN-first, FR for Quebec
- Phase 1 analytics — booking conversion, no-show rate, recurring
  cadence adherence, multi-location spread

Built in the same brand palette so the team that uses it daily isn't
working in an off-brand admin tool.

## 3. Suggested screens (Phase 1)

> Visual wireframes:
> - **Mobile app** — open `mockups.html` for the Phase 1 phone screens
> - **The Studio (web admin portal)** — open `studio-mockups.html` for
>   the four core admin views: per-location dashboard, multi-location
>   master calendar, technician scheduler, concierge inbox.

1. Onboarding — language, home location, services you book
2. Home — your next appointment, what's due, drop hero
3. Book flow — service → date → technician → confirm
4. Your Spot — location + technician + history
5. Service detail — Brazilian wax with prep + after content
6. The Calendar — recurring schedule view
7. Membership wallet — tier, credits, gift card balance
8. Concierge chat (multilingual booking + prep AI)
9. Profile — preferences, language, privacy

## 4. Phase 1 feature set (months 0–4)

**Foundation**
- Apple / Google / email sign-in
- Multilingual onboarding (EN / FR at launch)
- Location detection (with permission) — home location auto-set
- Profile: preferred services, technician preferences, sensitivities

**Book**
- One-tap re-book
- Service browser (nails, wax, laser, skin)
- Location finder (33+ locations) with distance + ratings
- Technician selection (with bio + photo, opt-in)
- Wait-list when fully booked
- Multi-service combo bookings

**Your Spot**
- Favorite location + technician
- Service history
- Recurring cadence detection ("your wax is due")
- Birthday / anniversary recognition

**Prep + After**
- Service-specific prep guides
- Post-service aftercare push reminders
- Sensitive-skin / reactive flag (opt-in)
- Bookmarkable for next time

**The Calendar**
- Auto-suggest next appointment
- Laser series tracking (1 of 6, 3 of 6, etc.)
- Membership benefits visible
- Multi-service same-day planning

**Membership / Shop**
- Tier purchase + management
- Gift card buy / redeem
- Multi-location credit
- (Retail / aftercare products if/when in scope)

**Loyalty**
- "Spotted" — points for visits, reviews, referrals
- Birthday treatment unlock
- Refer-a-friend (give-and-get a credit)

**AI · Tier 1**
- Concierge chat — multilingual booking + prep coach (Sonnet)
- "Ask before booking" — first-time customers get walked through
  what to expect
- Recurring cadence detection — "you're due for your wax"
- Multilingual translation (EN/FR)
- Visual search — see a nail look, find the matching service

**Compliance / sensitivity guardrails**
- Never claim the services treat / cure / improve skin conditions
- Laser is cosmetic, not medical — never frame as treatment
- AI never diagnoses; refers to dermatologist for skin questions
- No body-shape or "hairless = better" language
- Sensitive-skin / pregnancy / medication flags flow to technician,
  never to marketing AI

**The Studio (web admin portal)**
- Per-location dashboard
- Multi-location master calendar
- Technician scheduler with skill matrix
- Service catalog editor
- Membership / loyalty admin
- Concierge inbox
- RBAC (corporate vs franchise-owner)
- Phase 1 analytics

## 5. Phase 2 — Depth (months 5–9)

- ⬆ **Booker / Mindbody integration deepening** — two-way sync, real-time technician availability (triggers Enterprise upgrade for SLA-grade integration)
- **Photo skin-prep check (cautious)** — opt-in, never diagnostic, surfaces "you might want to delay laser this session"
- **Franchise-owner B2B portal** — per-franchise dashboard with revenue, technician hours, customer retention (triggers Enterprise upgrade for SSO + audit logging)
- **Multi-city travel mode** — "I'm in NYC for the weekend — find a Ten Spot"
- **Loyalty program redesign** — tiers based on visit cadence, not just dollars
- **Gift card scheduled-delivery** — wedding / shower / birthday rituals

## 6. Phase 3 — Cultural authority (months 10+)

- Editorial / journal — long-form on bodily autonomy, beauty-bar history, technician craft
- Annual VOICES film series — long-tenure technicians, founder stories
- ⬆ Demand-sensing AI — surfaces under-utilised time slots, optimal pricing
- ⬆ Multilingual content scaling AI — EN-first, AI drafts FR/ES for editor review
- Counterfeit-listing detection (gift card resale, etc.)
- VIP signal detection — concierge welcomes high-frequency customers
- Franchise-recruitment portal — prospective franchise owner pipeline

## 7. Data we'd collect (with consent)

| Category               | Examples                                                | Use                                          |
| ---------------------- | ------------------------------------------------------- | -------------------------------------------- |
| Identity & contact     | email, name, phone, address                              | bookings, reminders                          |
| Location               | home location, current location (opt-in for travel)      | location-aware booking                       |
| Service history        | which services, where, when, with whom                   | recurring cadence, recommendations           |
| Sensitivities (opt-in) | skin reactivity, pregnancy, medications                  | informs technician; never marketing AI       |
| Membership / billing   | tier, gift cards, credit balance                         | wallet                                       |
| Preferences            | favorite location, technician, services                  | one-tap re-book                              |
| Engagement             | booking funnel, prep-guide views                         | personalisation                              |
| Channel of origin      | online / referral / walk-in                              | attribution                                  |

**Won't collect**: weight or BMI, before-after body photos without
explicit narrow opt-in, precise GPS without explicit opt-in, contacts,
social-graph imports, third-party ad-tracking IDs, diagnosed skin
conditions (we refer to dermatologist).

## 8. What to deliberately NOT build

- **Medical / diagnostic claims** — laser is cosmetic, not medical
- **Body-shaming or "hairless / smooth = better" language**
- **Aggressive upsell at booking** — each franchise has its own incentives; respect them
- **AI dermatologist replacement** — refers to human derm for any skin condition
- **Photo-based AI features without narrow, explicit opt-in** — privacy
- **Auto-renewing memberships without one-tap pause / cancel** — California + UK law
- **Surveillance-marketing based on undisclosed health data**

## 9. Recommended SEYSO MaaS package

### Phase 1 launch — **Growth ($3,500/mo)** + **Studio add-on ($750/mo)** = **$4,250/mo**

| Growth feature                                | Why it fits The Ten Spot                                                                                       |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Both stores, React Native + Expo              | Mixed CA/US customer base; single codebase; OTA fits booking-flow iteration                                    |
| Claude Sonnet & Haiku AI                      | Sonnet powers Concierge chat in EN/FR; Haiku batches prep guides + translation                                 |
| RevenueCat (StoreKit 2 + Google Play Billing) | Membership tier purchases + gift cards in-app                                                                  |
| Sign in with Apple + Google                   | Reduces install friction                                                                                       |
| ASO quarterly                                 | "Brazilian wax Toronto", "laser hair removal near me", "nail salon" all matter for discovery                   |
| 2 releases / month                            | Booking-flow iteration cadence demands a regular rhythm                                                        |
| Shared Slack, 4h response                     | Right level for a franchise brand at launch                                                                    |

**Starter is disqualified** — single platform, 5-screen ceiling, no
AI, 24h email support. None of those work for a multi-location
franchise whose value proposition depends on multilingual booking
concierge and per-location data segregation.

**Studio add-on ($750/mo)** is mandatory and especially important
here — multi-location franchise admin (per-location dashboards,
RBAC, technician scheduling) is the most operationally complex Studio
of any client to date.

### Year 2 trigger — upgrade to **Enterprise (from $8,000/mo)**

Likely faster than other clients (12 months expected) because of:

1. **Booker / Mindbody two-way sync at SLA-grade** — needs Enterprise SLA
2. **Franchise-owner B2B portal** — SSO + audit logging + RLS hardening for 33+ owners
3. **Multi-state US data residency** — as US expansion grows
4. **24/7 SLA with 1h response** — multi-location franchise + booking-critical app
5. **PCI compliance hardening** — gift card + membership payment volume

### Contract notes for Year 1

- 12-month term on Growth + Studio (single combined invoice)
- Pre-negotiated upgrade path to Enterprise; build credit prorated
- AI overage clause: usage above the Growth quota billed at cost +20%
- **Booking-system integration as separate scope** — Booker / Mindbody / current system migration is its own project
- Brand-side approval on every customer-facing service / prep / aftercare claim
- Studio one-time build cost: **$45–65K** included in the Phase 1 build (most complex Studio in the proposal series — multi-location RBAC + technician scheduling + per-location pricing variation)

## 10. Suggested next step

A two-week paid discovery — confirm e-commerce platform + booking
system (likely Booker or Mindbody), audit existing customer +
booking + franchise data, run 5 customer interviews (ideally one
high-frequency cult-fan, one new customer post-first-visit, one
Quebec-FR customer, one franchise owner, one corporate ops staff),
and lock the Phase 1 scope before any build cost is committed.
