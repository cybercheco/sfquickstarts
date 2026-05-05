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

## 8. Decision points for the brand

1. **Passport tagging strategy**: QR-only at launch, or budget for NFC on
   flagship pieces?
2. **Loyalty build vs buy**: Smile.io now and migrate later, or build native
   from day 1?
3. **Resale**: in-app peer-to-peer, or send returns to a partner like
   Trove/Archive?
4. **Data residency**: EU customers will expect EU-hosted data — pick
   Supabase EU region if so.

## 9. Suggested next step

Two-week paid discovery: confirm the e-commerce platform, audit the existing
customer data, run 5 customer interviews on whether the lifecycle features
would actually be used, and lock the Phase 1 scope before any build cost is
committed. Typical cost: $6–12K.
