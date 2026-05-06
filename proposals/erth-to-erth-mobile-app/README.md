# Erth to Erth — Mobile App MVP Proposal

> Note: erthtoerth.com blocked the automated content fetch during drafting, so
> the product assumptions below are based on the brand name (circular /
> regenerative fashion). Validate the catalog and platform assumptions against
> the live site before committing budget.

## 1. Strategy in one paragraph

A native mobile app should not duplicate the web store; it should give Erth to
Erth's most engaged customers something the web cannot: a **garment passport**
(scan a tag on any item to see its origin, materials, repair guide, and resale
value) tied to a **circular-rewards loyalty program** (earn credit for
returning, repairing, or reselling items). The shop is secondary — it lives in
the app for convenience, but the lifecycle features are the reason a customer
installs it.

## 2. MVP feature set

### Phase 1 — Launch (3 months)
- **Auth & profile**: email + Apple/Google sign-in, size profile, style
  preferences, notification opt-ins.
- **Shop**: catalog, product detail, cart, checkout (delegated to the
  e-commerce backend — Shopify storefront API assumed).
- **Garment passport**: each item carries a QR code (printed care label or
  sewn-in NFC tag). Scan opens a screen with materials, factory/origin,
  carbon-equivalent estimate, care guide, and a "register to my closet" CTA.
- **Loyalty wallet**: points balance, tier, history. Points awarded for
  purchase, registering items, returning for recycling, completing a style
  profile, and referrals.
- **Push notifications**: drops, restocks of saved items, and lifecycle
  reminders ("You've worn this item 30 times — share your fit").

### Phase 2 — Circular features (months 4–6)
- **Take-back / recycle flow**: book a return label, get points on receipt.
- **Repair requests**: photo + issue, get a quote, mail in.
- **Resale**: list a registered garment to a peer marketplace; brand takes a
  cut and offers a credit bonus for staying in the ecosystem.
- **Style quiz** that tunes recommendations and feeds production planning.

### Phase 3 — Community (months 7+)
- User looks / outfit posts tagged to garments, with opt-in moderation.
- In-app events for pop-ups, swap parties, repair clinics.

### Always — The Studio (web admin portal)
The brand needs a way to maintain content, run drops, and manage the loop.
Catalog and orders stay in Shopify. **The Studio** is a custom web app that
sits alongside it and owns everything new the mobile app introduces:

- **Garment passport editor** — materials, origin, factory, care, carbon-equivalent
- **Loyalty admin** — points overrides, tier rules, comp credits
- **Take-back / repair / resale queues** — operations team workflow
- **Drop scheduler** — push copy, hero imagery, scheduled releases
- **Customer concierge inbox** — repair questions, recycle escalations
- **Sustainability reporting** — kg saved, items recycled, lifecycle data for
  marketing and regulatory disclosures
- **Phase 1 analytics** — activation, repeat rate, return rate, closet depth

Same backend API as the mobile app — different UI for different users.
Built in the same brand palette so the team that uses it daily isn't
working in an off-brand admin tool.

> Visual wireframes:
> - **Mobile app** — open `mockups.html` for the Phase 1 phone screens
> - **Studio (web admin portal)** — open `studio-mockups.html` for the four
>   core admin views: dashboard, passport editor, take-back queue, and
>   sustainability reporting.

## 3. Suggested screens (Phase 1)

1. Onboarding (3 slides) → sign-in
2. Home (drops, your closet shortcut, points)
3. Shop → Category → PDP → Cart → Checkout
4. Scan tab (camera with QR/NFC)
5. Garment passport detail
6. My Closet (registered items, wear count, care reminders)
7. Rewards (balance, how to earn, redeem)
8. Profile / Settings (sizes, address, notifications, privacy)

## 4. Data model (high level)

| Entity            | Key fields                                                                 |
| ----------------- | -------------------------------------------------------------------------- |
| `customer`        | id, email, auth_provider, created_at, marketing_consent, sustainability_consent |
| `size_profile`    | customer_id, top, bottom, shoe, fit_notes, body_measurements (opt-in)      |
| `product`         | id, sku, name, category, price, materials[], origin, carbon_kg, care      |
| `garment`         | id (unique per physical item), product_id, qr_code, current_owner_id, status (new/owned/returned/recycled/resold) |
| `ownership_event` | garment_id, customer_id, event (purchase/register/transfer/return), ts    |
| `wear_log`        | garment_id, customer_id, ts, optional photo_id                             |
| `points_ledger`   | customer_id, delta, reason, ref_id, ts                                     |
| `repair_request`  | garment_id, photos[], issue, quote, status                                 |
| `resale_listing`  | garment_id, asking_price, condition, status, buyer_id                      |

## 5. Recommended stack

- **Mobile**: React Native + Expo (single codebase iOS/Android, OTA updates).
- **Backend**: Shopify as commerce source of truth + a thin Node/TypeScript
  API (Fastify on Fly.io or Render) for passport, closet, loyalty ledger,
  repair, resale.
- **DB**: Postgres (Supabase or Neon) for the lifecycle data; Shopify keeps
  orders & catalog.
- **Auth**: Shopify Customer Account API + Apple/Google sign-in.
- **Loyalty**: build in-house on the points_ledger, OR integrate Smile.io /
  Yotpo for speed.
- **Tagging**: QR for v1 (cheap, printed on hangtag), NFC for premium drops
  in v2 (~$0.15–0.40/tag).
- **Analytics**: PostHog (events + funnels, self-host option) and Shopify's
  native reports.
- **Push**: Expo Notifications → APNs/FCM.

## 6. Cost estimate (build + year 1 run)

| Option                                           | Build           | Year-1 run         | Best for                   |
| ------------------------------------------------ | --------------- | ------------------ | -------------------------- |
| **A. Shopify Mobile App Builder + Smile.io**     | $5–15K          | ~$3K (apps + fees) | Validate demand fast, no passport feature |
| **B. React Native MVP (Phase 1 only)**           | $40–60K         | ~$15–25K           | Differentiated launch      |
| **C. Full Phase 1+2 custom (passport + resale)** | $80–130K        | ~$25–40K           | Brand commits to circular DNA |

Run-cost line items (Option B/C): Apple Developer ($99), Google Play ($25
once), Postgres (~$25–100/mo), API host ($25–50/mo), PostHog ($0–200/mo),
push (free–$50/mo), Sentry ($26/mo), one part-time maintainer.

### 6.1 Per-month run cost breakdown (Option B, Phase 1, ~5K MAU)

| Line item                        | Provider (example)         | Monthly cost   | Notes                                       |
| -------------------------------- | -------------------------- | -------------- | ------------------------------------------- |
| Apple Developer Program          | Apple                      | $8             | $99/yr amortized                            |
| Google Play Developer            | Google                     | $0             | $25 one-time                                |
| API hosting                      | Render / Fly.io            | $25–50         | 1–2 small instances + autoscale             |
| Database                         | Supabase / Neon (Postgres) | $25–100        | scales with closet/event volume             |
| Object storage (photos)          | Cloudflare R2 / S3         | $5–25          | repair photos, user looks                   |
| CDN / edge                       | Cloudflare                 | $0–20          | free tier covers most                       |
| Push notifications               | Expo Push / OneSignal      | $0–50          | free under ~10K subs                        |
| Auth (social sign-in)            | Apple/Google + Shopify     | $0             | included                                    |
| Loyalty engine                   | Smile.io (Starter→Growth)  | $0–199         | free if built in-house on points_ledger     |
| Email + transactional            | Klaviyo / Postmark         | $50–150        | order, lifecycle, points emails             |
| Analytics                        | PostHog Cloud              | $0–200         | free under 1M events/mo                     |
| Crash & errors                   | Sentry Team                | $26            | mobile + backend                            |
| Feature flags / A/B              | PostHog (incl.)            | $0             | bundled                                     |
| App Store / Play commission      | Apple / Google             | 0–30% of IAP   | n/a if checkout stays in Shopify web view   |
| Shopify plan delta               | Shopify                    | $0             | usually already paid for web                |
| **Subtotal infra & SaaS**        |                            | **~$140–820**  |                                             |
| Maintenance dev (0.2 FTE)        | contractor                 | $2,500–5,000   | bug fixes, OS updates, small features       |
| **Total monthly run**            |                            | **~$2,640–5,820** | scales sub-linearly with users           |

Phase 2 adds (resale + repair): payments fees (Stripe ~2.9% + 30¢),
shipping-label API ($0–100/mo), trust & safety moderation tooling
($0–200/mo), and ~+0.1 FTE ops.

### 6.2 AI cost line items (see §8)

| AI line item                            | Provider                | Monthly at 5K MAU |
| --------------------------------------- | ----------------------- | ----------------- |
| Recommendations & semantic search       | Claude Haiku 4.5 + embeddings | $50–200       |
| Visual search (image embeddings)        | Cohere Embed / OpenAI CLIP | $20–80          |
| Style chat / fit assistant              | Claude Sonnet 4.6, cached | $100–400        |
| Garment passport summaries (batch)      | Claude Haiku, prompt-cached | $10–40          |
| Moderation (user posts, resale photos)  | OpenAI / Hive moderation | $20–100         |
| **AI subtotal**                         |                         | **~$200–820**     |

Heavy prompt caching (system prompt with brand voice + product catalog
cached for ≥5 min) typically cuts the chat line 3–5×; budget assumes
caching is on from day 1.

## 7. Customer data — what to collect, why, and how to do it ethically

Default to **explicit opt-in per category**, store only what is used, expose
a self-serve "what we know about you" screen. GDPR/CCPA-aligned.

| Category               | Examples                                                | Use                                             |
| ---------------------- | ------------------------------------------------------- | ----------------------------------------------- |
| Identity & contact     | email, name, address                                    | orders, shipping                                |
| Fit                    | sizes, body measurements (opt-in), return reasons       | reduce returns, guide production runs           |
| Purchase               | order history, AOV, channel                             | LTV, segmentation                               |
| Engagement             | views, wishlists, time-to-purchase, push CTRs           | personalization, retention                      |
| Closet (app-unique)    | items registered, wear count, care actions, photos      | proof of value of durability, story content     |
| Sustainability actions | recycle returns, repairs, resale listings               | LCA reporting, marketing, reward scaling        |
| Preferences            | style quiz, materials cared about, fit preferences      | recommendations                                 |
| Location (coarse)      | city/region                                             | demand planning, pop-up targeting               |
| Device & app           | OS, version, crash data                                 | reliability                                     |

**Avoid** unless there's a concrete use: precise GPS, contacts, social graph
imports, third-party ad-tracking IDs.

## 8. Recommended AI features

Pick features that compound the brand's circular angle — AI should reduce
returns, extend garment life, and make the passport feel alive. Skip
gimmicks (AI-generated marketing copy, fake influencer chats).

### Tier 1 — High ROI, ship in Phase 1

1. **Fit & size assistant (chat)** — "I'm 5'9", usually a M in Patagonia,
   what size in this jacket?" Claude Sonnet 4.6 with the customer's size
   profile, return history, and the product's measurement table in a cached
   system prompt. Directly cuts return rate (typically 5–15%).
2. **Smart recommendations** — embeddings over the catalog + the customer's
   wear log and wishlist. Cohere/OpenAI embeddings stored in Postgres
   (pgvector). Reranked by an LLM only on the home screen, not every list.
3. **Visual search** — "find pieces like this photo." Image embedding + ANN
   search. Strong fit for a circular brand because it works across the
   resale catalog too.
4. **Garment passport auto-summary** — batch-generate a one-paragraph
   plain-language story per SKU from materials/origin/factory data.
   Editor-reviewed. Claude Haiku with prompt caching, ~$0.001 per item.

### Tier 2 — Phase 2 differentiators

5. **Repair triage from a photo** — customer uploads a photo of damage; a
   vision model classifies the issue (seam, hole, zipper) and returns an
   instant quote + DIY guide for small fixes. Reduces ops load.
6. **Resale listing assistant** — auto-fill title, condition, suggested
   price, and write a listing description from 3 photos + the garment's
   passport data. Lowers friction to list, increases supply.
7. **Care reminders, contextual** — "It rained yesterday — here's how to dry
   your wool coat." Template + LLM personalization, weather API, low cost.
8. **Style quiz that actually learns** — adaptive quiz where each answer is
   used to refine the next question via an LLM, ending with a fit/style
   profile that drives recommendations.

### Tier 3 — Operational AI (not user-facing)

9. **Demand forecasting** — feed wishlists, drop signups, and view-to-buy
   funnel into a forecasting model to guide production runs. Highest
   sustainability impact: produce closer to actual demand.
10. **Return-reason clustering** — LLM clusters free-text return reasons
    weekly, surfaces actionable patterns ("38% of returns of SKU 412 say
    'sleeves too long'") to merchandising.
11. **Moderation** — auto-moderate user looks and resale photos before they
    hit the feed.

### What to *not* build

- Generative product images / fake model try-on (off-brand for a
  sustainability story).
- AI chatbot for customer service before you have a human team to escalate
  to — bad bots hurt brand more than no bot.
- Personalized pricing — reputational risk far exceeds the lift.

### Implementation notes

- Default model: **Claude Haiku 4.5** for cost-sensitive paths
  (recommendations rerank, summaries, moderation prompts), **Claude Sonnet
  4.6** for the chat assistant.
- Turn on **prompt caching** for the brand voice + catalog context block;
  it is the single biggest cost lever.
- Keep a **server-side AI gateway** so the mobile app never holds an API
  key and you can swap models without an app release.
- Log every AI interaction with the customer's consent flag; never train
  on customer data without explicit opt-in.

## 9. Decision points for the brand

1. **Passport tagging strategy**: QR-only at launch, or budget for NFC on
   flagship pieces?
2. **Loyalty build vs buy**: Smile.io now and migrate later, or build native
   from day 1?
3. **Resale**: in-app peer-to-peer, or send returns to a partner like
   Trove/Archive?
4. **Data residency**: EU customers will expect EU-hosted data — pick
   Supabase EU region if so.

## 10. Suggested next step

Two-week paid discovery: confirm the e-commerce platform, audit the existing
customer data, run 5 customer interviews on whether the lifecycle features
would actually be used, and lock the Phase 1 scope before any build cost is
committed. Typical cost: $6–12K.
