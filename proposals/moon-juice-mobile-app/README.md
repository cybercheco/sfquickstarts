# Moon Juice — Mobile App MVP Proposal

> Note: moonjuice.com was researched via public sources — Sephora /
> Amazon listings, founder interviews, brand directories, and the
> Moon Juice Manual (Amanda Chantal Bacon, Penguin Random House).
> Validate against internal materials before committing budget.

> Categorical note — this is a **wellness / adaptogen / supplement
> brand**, not a clothing brand. The proposal departs structurally
> from the previous five (which were apparel-led). The risks are
> different: regulatory (FTC / FDA), health claims, supplement
> interactions, subscription mechanics. Read the "what NOT to build"
> section carefully.

## 1. Strategy in one paragraph

Moon Juice's customer asks the same three questions every time she
shops: *which Moon Dust is for me*, *when do I take it*, and *can I
combine it with what I'm already taking*. Today she answers them by
reading Amanda's Instagram, the Moon Juice Manual, and a tab full of
forum posts. **The app should be the answer.** A Ritual coach that
guides her stack, a per-product Apothecary that explains every
adaptogen with sourcing and dosing, a goal-driven recommender that
replaces "which Moon Dust for me" guesswork, and a Refill Vault that
manages her subscriptions calmly. The brand turns one-time supplement
buyers into daily ritual practitioners — which is the highest-LTV
shape in the category.

## 2. The six product pillars

### 1. The Ritual — your daily practice, guided
The brand sells the powders. The app teaches the practice.

- Morning / midday / evening routine cards built from your stack
- When to take what · what to combine · what to space apart
- Habit gentle reminders (calm, opt-in, never gamified)
- Streak-free design — wellness isn't punishment
- Audio-guided rituals (60–90 sec) by Amanda and team

### 2. The Apothecary — every product, every adaptogen explained
The Moon Dusts are mythologised but under-explained. The Apothecary
is the public-facing reference.

- Per-product passport: adaptogens, dosing, sourcing, citation links
- Per-adaptogen page (Ashwagandha, Reishi, Cordyceps, etc.) with what
  it does, when to take, evidence base, contraindications
- "Layer with" suggestions — Moon Dust + supplement compatibility
- "Don't take with" warnings — flagged interactions, Rx caveats
- All claims sourced; never invented

### 3. The Goals — input what you want, get a stack
Replaces the "which Moon Dust" guesswork.

- Pick goals: calm · sleep · beauty · brain · energy · libido · focus
- App proposes a stack with rationale, dosing, timing
- Editable; save as your starting Ritual
- Update goals seasonally — stack adapts

### 4. The Refill Vault — calm subscription management
Refillable supplements are the brand's subscription play. The Vault
makes it humane.

- See every active subscription
- Smart-refill prediction based on usage
- Skip / pause / accelerate without phone calls
- Bundle deliveries to reduce shipping
- Refillable bottle program — track returns and credits

### 5. The Shop — DTC, multi-currency, drop-aware
Calm shop for new collections, limited drops, and full catalog.

- Multi-currency (USD, CAD, GBP, EUR)
- Drops & limited collaborations
- Bundle builder — pair Moon Dusts with supplements
- Refill-credit redemption at checkout
- Connection to Sephora / Amazon orders for closet coherence

### 6. The Studio — internal-facing web admin portal
The brand's internal twin. Catalog and orders stay in Shopify;
The Studio owns everything new the app introduces.

- Apothecary content editor — products, adaptogens, citation manager
- Ritual library admin — routine cards, audio uploads
- Goal-to-stack rules — staff-curated, AI-augmented
- Refill subscription admin — at-risk subs, refill predictions
- Concierge inbox — adaptogen questions, Rx interaction queries,
  refill requests
- Multilingual translation workflow — EN-first, AI drafts ES/FR
- Phase 1 analytics — Ritual completion rate, goal-stack adoption,
  refill churn, adaptogen-page engagement

Built in the same brand palette so the team that uses it daily isn't
working in an off-brand admin tool.

## 3. Suggested screens (Phase 1)

> Visual wireframes:
> - **Mobile app** — open `mockups.html` for the Phase 1 phone screens
> - **The Studio (web admin portal)** — open `studio-mockups.html` for
>   the four core admin views: dashboard, Apothecary editor, Ritual
>   library, concierge inbox.

1. Onboarding — language, goals, current supplements, allergies, preferences
2. Home — today's Ritual, refill alerts, drop hero
3. The Apothecary — product passport for a Moon Dust
4. The Goals — calm · sleep · beauty (with stack preview)
5. The Stack — your personal stack with timing
6. The Ritual — morning · midday · evening routine
7. The Refill Vault — subscription management
8. Apothecary chat (multilingual adaptogen + ritual coach)
9. Profile — preferences, language, privacy, "what we know about you"

## 4. Phase 1 feature set (months 0–4)

**Foundation**
- Apple / Google / email sign-in
- Multilingual onboarding (EN / ES at launch; FR expandable)
- Multi-currency (USD, CAD, GBP, EUR)
- Profile: goals, allergies, current supplements, Rx caveats (opt-in)

**The Ritual**
- Morning / midday / evening routine cards
- Calm reminders (opt-in, not gamified)
- 60–90-sec audio rituals
- Progress without streaks — wellness without punishment

**The Apothecary**
- Per-product passport (adaptogens, dosing, sourcing, citations)
- Per-adaptogen reference (what it does, evidence, contraindications)
- "Layer with" / "don't take with" guidance
- Audio narration optional

**The Goals → The Stack**
- Goal selection (calm, sleep, beauty, brain, energy, libido, focus)
- AI-proposed stack with rationale
- Editable; save as Ritual
- Seasonal stack refresh

**The Refill Vault**
- Subscription management (skip / pause / accelerate / bundle)
- Smart refill prediction
- Refillable bottle returns + credits
- Pause-for-vacation flow

**The Shop**
- Multi-currency
- Drop hero + restock alerts
- Bundle builder
- Refill credit redemption

**Loyalty**
- "Glow" — points for ritual completion, refill returns, reviews
- Refill-bottle returns earn credit
- Refer-a-friend (give-and-get a credit)

**AI · Tier 1**
- Apothecary chat — multilingual adaptogen / ritual coach (Sonnet)
- Goal-to-stack AI — proposes stacks with citations (editor-curated rules)
- Refill timing AI — usage-based prediction
- Routine builder — morning/midday/evening from your stack
- Multilingual brand-voice translation (Haiku + brand glossary)
- Visual search — photograph a Moon Dust, find it

**Compliance guardrails (non-negotiable)**
- Never diagnose, treat, cure, or prevent disease
- Always cite sources; never invent claims
- Always flag Rx interactions when a customer enters a medication
- Refer to a healthcare provider for any symptom-driven question
- FDA / FTC supplement-marketing rules baked into the AI's system prompt

**The Studio (web admin portal)**
- Apothecary editor with citation manager
- Ritual library admin (audio uploads, routine cards)
- Goal-to-stack rules (staff-curated)
- Refill subscription admin
- Concierge inbox
- Multilingual translation workflow
- Phase 1 analytics

## 5. Phase 2 — Depth (months 5–9)

- ⬆ **AR ritual visualization** — point camera, see your stack laid out for the day (triggers Enterprise upgrade for native modules)
- **Smart-stack adapter** — adjusts based on cycle, sleep, stress markers (with opt-in)
- **Practitioner B2B portal** — naturopaths / wellness coaches with white-label client tracking (triggers Enterprise upgrade for SSO + audit logging + HIPAA-adjacent data handling)
- **Apple Health / Google Fit integration** — opt-in only, sleep + steps inform Ritual nudges
- **Live coach Q&A** — quarterly live with Amanda + practitioners
- **Adaptogen library expansion** — full evidence base with citation links, peer-reviewed studies indexed
- **Custom blend (limited)** — under strict editorial review; not full personalisation, but curated staff-blends for specific goals

## 6. Phase 3 — Cultural authority (months 10+)

- Editorial / journal — long-form on adaptogens, ritual, science
- Annual VOICES film series — Amanda + practitioners + scientists
- ⬆ Demand-sensing AI — informs production, harvest planning
- ⬆ Multilingual content scaling AI — EN-first, AI drafts ES/FR/IT/JP/DE for editor review
- Counterfeit-listing detection (Amazon, eBay, AliExpress)
- VIP signal detection — concierge welcomes top-tier supporters
- Practitioner certification program — Moon Juice-trained wellness coaches

## 7. Data we'd collect (with consent)

| Category               | Examples                                                | Use                                          |
| ---------------------- | ------------------------------------------------------- | -------------------------------------------- |
| Identity & contact     | email, name, address                                    | orders, shipping                             |
| Goals                  | calm / sleep / beauty / brain / energy / libido / focus | stack recommendations                        |
| Allergies & sensitivities | nuts, shellfish, etc.                                  | safety filters on stack recommendations      |
| Current Rx (opt-in)    | medications you're taking                                | interaction warnings                         |
| Subscriptions          | active refills, usage rate                              | refill prediction                            |
| Ritual engagement      | routine completions (no shaming)                        | gentle nudges                                |
| Stack history          | adaptogens used, when, paired                            | seasonal recommendations                     |
| Channel of origin      | online / Sephora / Amazon / referral                     | attribution                                  |

**Won't collect**: weight / BMI / symptom logs unless explicitly
opted-in for a specific feature with clear value, contacts,
social-graph imports, third-party ad-tracking IDs, precise GPS,
diagnosed conditions (we refer customers to their physician).

## 8. What to deliberately NOT build

- **Medical claims AI** — existential brand and regulatory risk
- **"Cure" / "treat" / "prevent disease" language** — illegal under FTC/FDA supplement rules
- **AI advising on diagnosed conditions** — refers to physician, never engages
- **Aggressive personalisation based on undisclosed health data**
- **Body-tracking metrics** — weight, BMI, symptoms unless opted-in
- **Anti-aging or fertility / hormone claims** — FDA gray area; brand-side legal review required
- **Auto-renewing subscriptions without one-tap pause / cancel** — California + UK law concerns
- **Streaks, shame, FOMO design** — wellness deserves calm

## 9. Recommended SEYSO MaaS package

### Phase 1 launch — **Growth ($3,500/mo)** + **Studio add-on ($750/mo)** = **$4,250/mo**

| Growth feature                                | Why it fits Moon Juice                                                                                         |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Both stores, React Native + Expo              | LA-heavy iOS customer base; international + US-wide Android. Single codebase; OTA fits drop cadence            |
| Claude Sonnet & Haiku AI                      | Sonnet powers Apothecary chat with strict guardrails; Haiku batches translations and product summaries         |
| RevenueCat (StoreKit 2 + Google Play Billing) | Subscription management is core — RevenueCat critical for refill subscriptions                                 |
| Sign in with Apple + Google                   | Reduces install friction                                                                                       |
| ASO quarterly                                 | "Adaptogens", "ashwagandha", "wellness supplements" all matter for discovery                                   |
| 2 releases / month                            | Drop cadence + content updates demand a regular rhythm                                                         |
| Shared Slack, 4h response                     | Right level for a values-led wellness brand at launch                                                          |

**Starter is disqualified** — single platform, 5-screen ceiling, no
AI, 24h email support. None of those work for a wellness brand whose
proposition depends on multilingual ritual coaching with strict
compliance guardrails.

**Studio add-on ($750/mo)** is mandatory and especially important
here. The Apothecary editor with citation manager + the goal-to-stack
rules engine + refill subscription admin together form the brand's
operational nervous system. Without it, the brand's claims live in
spreadsheets and Instagram captions — not auditable.

### Year 2 trigger — upgrade to **Enterprise (from $8,000/mo)**

Upgrade when *any one* of these becomes a hard requirement:

1. **Practitioner B2B portal** — naturopaths / wellness coaches with white-label client tracking; SSO + audit logging + RLS hardening
2. **Apple Health / Google Fit + cycle data integration** — health-data integration may approach HIPAA / state-level (CA CCPA-HIPAA hybrid) regulations as scale grows
3. **AR ritual visualization** — native Swift/SwiftUI + Kotlin/Compose modules
4. **EU / UK GDPR data residency** — health data is special-category under GDPR; storage requirements get strict fast
5. **24/7 SLA with 1h response** — when Sephora or another major retail partner makes uptime contractual

### Contract notes for Year 1

- 12-month term on Growth + Studio (single combined invoice)
- Pre-negotiated upgrade path to Enterprise; build credit prorated
- AI overage clause: usage above the Growth quota billed at cost +20%
- **Brand-side legal review on every customer-facing claim** — adaptogen statements, dosing, interactions, especially anything FDA / FTC sensitive. Non-negotiable.
- Studio one-time build cost: **$35–55K** included in the Phase 1 build (separate from monthly platform fees) — higher end of range due to citation manager + interaction-warning system

## 10. Suggested next step

A two-week paid discovery — confirm e-commerce platform (Shopify),
audit existing customer + subscription data, run 5 customer interviews
(ideally one DTC subscriber, one Sephora-acquired customer, one
practitioner, one new buyer, one customer who churned a refill), and
lock the Phase 1 scope before any build cost is committed. Critical
output: alignment with the brand's legal team on what the AI can and
can't say.
