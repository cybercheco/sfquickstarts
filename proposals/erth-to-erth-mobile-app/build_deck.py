"""Build the Erth to Erth client pitch deck (.pptx).

Features-focused pitch — intentionally excludes pricing/cost slides.
Run from the repo root:
    python3 proposals/erth-to-erth-mobile-app/build_deck.py
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pathlib import Path

# Brand palette (matches the HTML mockups)
INK        = RGBColor(0x1f, 0x1d, 0x18)
MUTED      = RGBColor(0x6b, 0x66, 0x5c)
LINE       = RGBColor(0xd9, 0xd2, 0xc4)
BG         = RGBColor(0xf3, 0xef, 0xe7)
ACCENT     = RGBColor(0x2f, 0x4a, 0x36)
ACCENT2    = RGBColor(0x5a, 0x6e, 0x44)
ACCENT_SO  = RGBColor(0xe3, 0xea, 0xd0)
GOLD       = RGBColor(0xb9, 0x91, 0x4c)
WARN       = RGBColor(0xb6, 0x64, 0x3c)
WHITE      = RGBColor(0xff, 0xff, 0xff)

SERIF = "Georgia"
SANS  = "Calibri"

prs = Presentation()
prs.slide_width  = Inches(13.333)
prs.slide_height = Inches(7.5)
SW, SH = prs.slide_width, prs.slide_height

BLANK = prs.slide_layouts[6]


def add_slide():
    s = prs.slides.add_slide(BLANK)
    bg = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SW, SH)
    bg.line.fill.background()
    bg.fill.solid()
    bg.fill.fore_color.rgb = BG
    bg.shadow.inherit = False
    return s


def add_text(slide, x, y, w, h, text, *, font=SANS, size=14, bold=False,
             color=INK, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Emu(0)
    tf.margin_top = tf.margin_bottom = Emu(0)
    tf.vertical_anchor = anchor
    lines = text.split("\n") if isinstance(text, str) else text
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        run = p.add_run()
        run.text = line
        run.font.name = font
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.color.rgb = color
    return tb


def add_rect(slide, x, y, w, h, *, fill=WHITE, line=None, line_w=0.75,
             corner=False):
    shp = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE if corner else MSO_SHAPE.RECTANGLE,
        x, y, w, h,
    )
    if corner:
        shp.adjustments[0] = 0.12
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill
    if line is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = line
        shp.line.width = Pt(line_w)
    shp.shadow.inherit = False
    return shp


def add_pill(slide, x, y, w, h, text, *, fill=ACCENT_SO, color=ACCENT, size=10):
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
    shp.adjustments[0] = 0.5
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill
    shp.line.fill.background()
    shp.shadow.inherit = False
    tf = shp.text_frame
    tf.margin_left = tf.margin_right = Emu(60000)
    tf.margin_top = tf.margin_bottom = Emu(20000)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = text
    r.font.name = SANS
    r.font.size = Pt(size)
    r.font.bold = True
    r.font.color.rgb = color
    return shp


def add_arrow(slide, x, y, w, h, *, color=ACCENT):
    shp = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, x, y, w, h)
    shp.fill.solid()
    shp.fill.fore_color.rgb = color
    shp.line.fill.background()
    shp.shadow.inherit = False
    return shp


def add_footer(slide, page, total):
    add_text(slide, Inches(0.6), Inches(7.05), Inches(6), Inches(0.3),
             "Erth to Erth · Mobile App Pitch",
             size=9, color=MUTED)
    add_text(slide, Inches(11.7), Inches(7.05), Inches(1), Inches(0.3),
             f"{page} / {total}",
             size=9, color=MUTED, align=PP_ALIGN.RIGHT)


def add_section_header(slide, eyebrow, title):
    add_text(slide, Inches(0.6), Inches(0.55), Inches(8), Inches(0.3),
             eyebrow.upper(), size=10, bold=True, color=ACCENT)
    add_text(slide, Inches(0.6), Inches(0.85), Inches(12), Inches(1.0),
             title, font=SERIF, size=34, color=INK)
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                  Inches(0.6), Inches(1.85),
                                  Inches(0.7), Pt(2))
    line.fill.solid(); line.fill.fore_color.rgb = ACCENT
    line.line.fill.background()


# ---------------------------------------------------------------- slides
slides_total = 23  # placeholder, footer will be re-rendered

# 1. COVER --------------------------------------------------------
def slide_cover():
    s = add_slide()
    # gradient-ish hero band
    band = add_rect(s, 0, 0, SW, Inches(7.5), fill=BG)
    # accent strip
    strip = add_rect(s, 0, Inches(6.7), SW, Inches(0.05), fill=ACCENT)
    # left accent block
    add_rect(s, Inches(0.6), Inches(1.0), Inches(0.08), Inches(2.4),
             fill=ACCENT)

    add_text(s, Inches(0.85), Inches(1.0), Inches(6), Inches(0.4),
             "MOBILE APP · PITCH",
             size=11, bold=True, color=ACCENT)
    add_text(s, Inches(0.85), Inches(1.45), Inches(11), Inches(2.0),
             "Erth to Erth", font=SERIF, size=72, color=INK)
    add_text(s, Inches(0.85), Inches(2.7), Inches(11), Inches(1.6),
             "Clothes that come back to the earth —\nand to the people who wear them.",
             font=SERIF, size=28, color=ACCENT)
    add_text(s, Inches(0.85), Inches(5.6), Inches(10), Inches(0.4),
             "A companion app for a circular wardrobe.",
             size=14, color=MUTED)
    add_text(s, Inches(0.85), Inches(6.0), Inches(10), Inches(0.3),
             "Prepared for the Erth to Erth team",
             size=11, color=MUTED)

slide_cover()

# 2. THE OPPORTUNITY ---------------------------------------------
def slide_opportunity():
    s = add_slide()
    add_section_header(s, "Why now", "The wardrobe is becoming circular.")
    stats = [
        ("92M", "tonnes of textile waste\ngenerated globally each year",
         "Customers want brands that close the loop."),
        ("73%", "of Gen Z & Millennials say\nsustainability shapes purchases",
         "But they need help making it concrete."),
        ("3×", "engagement on apps with\nlifecycle features vs. shop-only",
         "A passport + closet beats yet another store."),
    ]
    x = Inches(0.6); y = Inches(2.4); w = Inches(4); gap = Inches(0.2)
    for i, (big, mid, small) in enumerate(stats):
        cx = x + (w + gap) * i
        card = add_rect(s, cx, y, w, Inches(4.0), fill=WHITE,
                        line=LINE, corner=True)
        add_text(s, cx + Inches(0.4), y + Inches(0.4), w - Inches(0.8),
                 Inches(1.4), big, font=SERIF, size=64, color=ACCENT)
        add_text(s, cx + Inches(0.4), y + Inches(1.7), w - Inches(0.8),
                 Inches(1.0), mid, size=14, bold=True, color=INK)
        add_text(s, cx + Inches(0.4), y + Inches(2.9), w - Inches(0.8),
                 Inches(1.0), small, size=12, color=MUTED)
    add_footer(s, 2, slides_total)

slide_opportunity()

# 3. VISION -------------------------------------------------------
def slide_vision():
    s = add_slide()
    add_section_header(s, "The vision", "Not another store — a wardrobe companion.")
    add_text(s, Inches(0.6), Inches(2.3), Inches(12), Inches(2.0),
             ("The web store sells. The app stewards.\n\n"
              "Customers scan a tag on any Erth to Erth piece to open its "
              "garment passport — origin, materials, care, lifecycle. "
              "They build a digital closet of what they own, earn rewards "
              "for circular actions, and are guided to the right size, the "
              "right repair, the right next life for every piece."),
             font=SERIF, size=22, color=INK)
    add_text(s, Inches(0.6), Inches(5.5), Inches(12), Inches(0.4),
             "WHY IT MATTERS", size=10, bold=True, color=ACCENT)
    add_text(s, Inches(0.6), Inches(5.8), Inches(12), Inches(1.5),
             ("• Deepens the relationship with the most engaged customers\n"
              "• Creates proof — and content — for the brand's circular story\n"
              "• Turns every garment sold into the start of a recurring relationship"),
             size=14, color=INK)
    add_footer(s, 3, slides_total)

slide_vision()

# 4. FOUR PILLARS -------------------------------------------------
def slide_pillars():
    s = add_slide()
    add_section_header(s, "Product overview", "Four pillars — three customer-facing, one internal.")
    pillars = [
        ("Shop", "A curated mobile storefront — drops, look-books, fast checkout — that feels like the brand, not a generic Shopify wrapper.",
         ["Drops & restock alerts", "Look-books & stories", "One-tap checkout"]),
        ("Closet & Passport", "Every piece a customer owns gets a digital twin — its story, its care, its wear count, its next life.",
         ["Scan-to-register (QR / NFC)", "Wear log & care reminders", "Material & origin transparency"]),
        ("Circular Rewards", "Points, tiers, and recognition for the actions that matter — return, repair, resell, refer.",
         ["Soil → Compost → Bloom tiers", "Earn for circular actions", "Redeem on new pieces"]),
        ("The Studio", "Internal-facing web admin portal — passport editor, repair queue, drop scheduler, sustainability report.",
         ["Built for ops & editorial", "Same brand palette", "Audit-ready reporting"]),
    ]
    cw = Inches(2.95); ch = Inches(4.6); gap = Inches(0.15)
    x0 = Inches(0.6); y0 = Inches(2.3)
    for i, (title, desc, bullets) in enumerate(pillars):
        cx = x0 + (cw + gap) * i
        is_studio = (i == 3)
        add_rect(s, cx, y0, cw, ch, fill=WHITE, line=LINE, corner=True)
        # Number badge — Studio gets the dark badge to mark it as internal
        badge_fill = INK if is_studio else ACCENT_SO
        badge_color = WHITE if is_studio else ACCENT
        add_rect(s, cx + Inches(0.3), y0 + Inches(0.3), Inches(0.55),
                 Inches(0.55), fill=badge_fill, corner=True)
        add_text(s, cx + Inches(0.3), y0 + Inches(0.3), Inches(0.55),
                 Inches(0.55), str(i + 1), font=SERIF, size=20, bold=True,
                 color=badge_color, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        add_text(s, cx + Inches(0.3), y0 + Inches(1.0), cw - Inches(0.6),
                 Inches(0.5), title, font=SERIF, size=20, color=INK)
        add_text(s, cx + Inches(0.3), y0 + Inches(1.55), cw - Inches(0.6),
                 Inches(1.6), desc, size=11, color=MUTED)
        bx = cx + Inches(0.3); by = y0 + Inches(3.3)
        for b in bullets:
            add_text(s, bx, by, cw - Inches(0.6), Inches(0.3),
                     "•  " + b, size=10, color=INK)
            by += Inches(0.36)
    add_footer(s, 4, slides_total)

slide_pillars()

# 5–7. FEATURES BY PHASE -----------------------------------------
def feature_slide(num, total, eyebrow, title, intro, items):
    s = add_slide()
    add_section_header(s, eyebrow, title)
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.6),
             intro, size=14, color=MUTED)
    cols = 2
    rows = (len(items) + cols - 1) // cols
    cw = Inches(6.0); ch = Inches(0.95); gap = Inches(0.15)
    for i, (name, desc) in enumerate(items):
        c = i % cols; r = i // cols
        cx = Inches(0.6) + (cw + gap) * c
        cy = Inches(2.9) + (ch + gap) * r
        add_rect(s, cx, cy, cw, ch, fill=WHITE, line=LINE, corner=True)
        # green dot
        add_rect(s, cx + Inches(0.3), cy + Inches(0.4), Inches(0.18),
                 Inches(0.18), fill=ACCENT, corner=True)
        add_text(s, cx + Inches(0.6), cy + Inches(0.12), cw - Inches(0.8),
                 Inches(0.4), name, size=14, bold=True, color=INK)
        add_text(s, cx + Inches(0.6), cy + Inches(0.45), cw - Inches(0.8),
                 Inches(0.5), desc, size=11, color=MUTED)
    add_footer(s, num, total)

feature_slide(5, slides_total, "Phase 1 · Launch (months 0–3)",
              "Foundations: shop, closet, rewards.",
              "The minimum app worth installing.", [
    ("Sign-in & profile", "Apple/Google/email, sizes, style preferences, notification opt-ins."),
    ("Mobile shop", "Catalog, drops, product detail, cart, checkout via Shopify."),
    ("Garment passport", "Scan a QR or NFC tag to open materials, origin, care, CO₂e."),
    ("My Closet", "Every piece registered, wear logs, care reminders."),
    ("Loyalty wallet", "Points balance, tiers, history, redeem on next purchase."),
    ("Push notifications", "Drops, restocks of saved items, lifecycle nudges."),
    ("Fit assistant (AI)", "Chat that recommends the right size from your past orders."),
    ("Smart recommendations", "Catalog tuned to your closet and your style profile."),
])

feature_slide(6, slides_total, "Phase 2 · Circular (months 4–6)",
              "Closing the loop, in the customer's hand.",
              "The features that make Erth to Erth different.", [
    ("Take-back & recycle", "Book a return label in two taps, points credited on receipt."),
    ("Repair requests", "Photo + issue, get a quote, mail in for service."),
    ("Repair triage (AI)", "Vision model classifies damage and offers DIY guides for small fixes."),
    ("Peer resale", "List a registered garment in-app, brand earns a small take."),
    ("Resale assistant (AI)", "Auto-fill title, condition, price and listing copy from photos."),
    ("Visual search", "Photograph a piece — find similar in catalog or resale."),
    ("Style quiz", "Adaptive quiz that refines style profile and recommendations."),
    ("Care reminders", "Contextual nudges — weather-aware, fabric-specific."),
])

feature_slide(7, slides_total, "Phase 3 · Community (months 7+)",
              "From wardrobe to community.",
              "Stories, swaps, and shared craft.", [
    ("User looks", "Customers post outfits tagged to their registered garments."),
    ("Events", "Pop-ups, swap parties, repair clinics — RSVP in-app."),
    ("Stories from the field", "Behind-the-scenes from factories, growers, makers."),
    ("Swap circles", "Closed groups for trading among trusted members."),
    ("Brand journal", "Long-form reads from the team, in a calm reading view."),
    ("Referrals & gifting", "Send a friend a piece, both earn points."),
    ("Live drop alerts", "Geofenced alerts for in-person drops and pop-ups."),
    ("Moderation (AI)", "Auto-screen user posts and resale photos before publish."),
])

# 8. ONBOARDING FLOW ---------------------------------------------
def slide_onboarding():
    s = add_slide()
    add_section_header(s, "User experience", "Onboarding — under 90 seconds.")
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.4),
             "Five screens. No forms. The customer is shopping or scanning by step five.",
             size=14, color=MUTED)

    steps = [
        ("01", "Welcome", "Brand promise in one sentence.\nApple / Google / email."),
        ("02", "Why we ask", "Plain-language privacy note.\nOpt-in to each data category."),
        ("03", "Sizes", "Pull from past Shopify orders\nor 4 quick taps."),
        ("04", "Style spark", "Pick 3 looks you love.\nPowers your home feed."),
        ("05", "First moment", "Scan an item you own —\nor explore the new drop."),
    ]
    x = Inches(0.6); y = Inches(2.9); w = Inches(2.3); h = Inches(3.6)
    gap = Inches(0.2)
    for i, (n, t, d) in enumerate(steps):
        cx = x + (w + gap) * i
        add_rect(s, cx, y, w, h, fill=WHITE, line=LINE, corner=True)
        add_text(s, cx + Inches(0.3), y + Inches(0.3), w - Inches(0.6),
                 Inches(0.5), n, font=SERIF, size=28, color=ACCENT)
        add_text(s, cx + Inches(0.3), y + Inches(1.0), w - Inches(0.6),
                 Inches(0.5), t, size=14, bold=True, color=INK)
        add_text(s, cx + Inches(0.3), y + Inches(1.55), w - Inches(0.6),
                 Inches(2.0), d, size=11, color=MUTED)
        if i < len(steps) - 1:
            add_arrow(s, cx + w + Inches(0.01), y + Inches(1.6),
                      Inches(0.18), Inches(0.4), color=ACCENT)

    add_text(s, Inches(0.6), Inches(6.7), Inches(12), Inches(0.4),
             "DESIGN PRINCIPLE   —   Earn permission before asking for data. Show value before asking for time.",
             size=11, bold=True, color=ACCENT)
    add_footer(s, 8, slides_total)

slide_onboarding()

# 9. JOURNEY: FIRST PURCHASE + REGISTER --------------------------
def journey_slide(num, total, eyebrow, title, intro, steps):
    s = add_slide()
    add_section_header(s, eyebrow, title)
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.4),
             intro, size=14, color=MUTED)
    n = len(steps)
    total_w = Inches(12.0)
    arrow_w = Inches(0.25); arrow_gap = Inches(0.05)
    box_w = (total_w - arrow_w * (n - 1) - arrow_gap * 2 * (n - 1)) / n
    box_h = Inches(3.7)
    y = Inches(2.8)
    x = Inches(0.6)
    for i, (label, what, ux) in enumerate(steps):
        add_rect(s, x, y, box_w, box_h, fill=WHITE, line=LINE, corner=True)
        # label tab
        add_rect(s, x, y, box_w, Inches(0.55), fill=ACCENT, corner=True)
        add_text(s, x + Inches(0.2), y + Inches(0.05), box_w - Inches(0.4),
                 Inches(0.45), label, size=11, bold=True, color=WHITE,
                 anchor=MSO_ANCHOR.MIDDLE)
        add_text(s, x + Inches(0.25), y + Inches(0.75), box_w - Inches(0.5),
                 Inches(0.7), what, size=13, bold=True, color=INK)
        add_text(s, x + Inches(0.25), y + Inches(1.6), box_w - Inches(0.5),
                 Inches(2.0), ux, size=10, color=MUTED)
        if i < n - 1:
            add_arrow(s, x + box_w + arrow_gap, y + Inches(1.65),
                      arrow_w, Inches(0.4), color=ACCENT)
            x = x + box_w + arrow_w + arrow_gap * 2
        else:
            x = x + box_w
    add_footer(s, num, total)

journey_slide(9, slides_total,
    "User flow · 1 of 3",
    "First purchase → registered garment.",
    "From discovery to digital twin in the same week.",
    [
        ("DISCOVER", "Sees the drop",
         "Push notification or home-feed hero. Taps in to a look-book story; saves favorites."),
        ("DECIDE", "Asks the fit assistant",
         "Opens chat from the product page. AI uses past orders and the SKU's measurements to recommend a size."),
        ("BUY", "Checkout in two taps",
         "Shopify checkout via Apple Pay. Order + shipping update push to the app, no email mining required."),
        ("RECEIVE", "Scans the tag",
         "Item arrives with a QR on the hangtag. One scan opens the passport and adds it to My Closet."),
        ("LIVE WITH IT", "Wears, logs, earns",
         "Wear count grows; care reminders arrive; +50 points credited for registering. The relationship has begun."),
    ])

# 10. JOURNEY: DAILY ENGAGEMENT ----------------------------------
journey_slide(10, slides_total,
    "User flow · 2 of 3",
    "The weekly rhythm — what brings a customer back.",
    "We don't need them every day. We need them every week, with a reason.",
    [
        ("MONDAY", "Care nudge",
         "\"It's been raining — here's the right way to dry your wool coat.\" Opens the garment passport with a one-tap care guide."),
        ("WEDNESDAY", "Drop preview",
         "Members get the new drop 24 hours early. Save items; restock alerts when sizes go live."),
        ("FRIDAY", "Style spark",
         "Adaptive feed — a few looks built around pieces already in their closet, plus one stretch idea."),
        ("SUNDAY", "Reflection",
         "\"You wore your hemp overshirt 6 times this month — your most-loved piece.\" Quiet, not gamified."),
        ("ANY DAY", "Scan to act",
         "Camera tab is always one tap away. Scan any garment to repair, recycle, or resell — that's the loop."),
    ])

# 11. JOURNEY: CIRCULAR ACTION -----------------------------------
journey_slide(11, slides_total,
    "User flow · 3 of 3",
    "The circular action — the moment that defines the brand.",
    "Every existing piece is an opportunity. The app makes it effortless to take it.",
    [
        ("TRIGGER", "Damage or fatigue",
         "Customer notices a tear or a piece they no longer wear. Opens the app, taps Scan, and reads the garment passport."),
        ("CHOOSE", "Repair · Resell · Recycle",
         "Three clear options. AI suggests the best one based on condition, age, and demand."),
        ("ACT", "Two-tap booking",
         "Print a label or schedule pickup. Repair quote and DIY guide returned in seconds via vision AI."),
        ("REWARD", "Points & story",
         "Action confirmed; points credited; a private \"thank you\" with the impact (kg saved, piece's next life)."),
        ("CLOSE THE LOOP", "Renewed value",
         "Repaired piece returns; resale piece finds a new owner; recycled fibres re-enter production. Customer earns trust in the brand."),
    ])

# 12. SCREEN PREVIEW ---------------------------------------------
def slide_screens():
    s = add_slide()
    add_section_header(s, "Visual reference", "What it looks like in hand.")
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.4),
             "Wireframe-fidelity mockups of the nine core Phase 1 screens.",
             size=14, color=MUTED)

    screens = [
        ("Onboarding", "Welcome · sign-in"),
        ("Home", "Drop hero · for-you"),
        ("Product", "Passport pills · ask AI"),
        ("Scan", "Camera · QR / NFC"),
        ("Passport", "Wears · CO₂e · timeline"),
        ("Closet", "Wear-bars · per piece"),
        ("Rewards", "Tier · earn list"),
        ("Fit chat", "AI sizing · care"),
        ("Profile", "Data · privacy"),
    ]
    cols = 5; rows = 2
    cw = Inches(2.3); ch = Inches(2.0); gx = Inches(0.15); gy = Inches(0.25)
    x0 = Inches(0.6); y0 = Inches(2.7)
    for i, (name, sub) in enumerate(screens):
        c = i % cols; r = i // cols
        x = x0 + (cw + gx) * c
        y = y0 + (ch + gy) * r
        # phone shape
        add_rect(s, x, y, cw, ch, fill=INK, corner=True)
        add_rect(s, x + Inches(0.1), y + Inches(0.1),
                 cw - Inches(0.2), ch - Inches(0.2),
                 fill=BG, corner=True)
        # tiny header band
        add_rect(s, x + Inches(0.1), y + Inches(0.1),
                 cw - Inches(0.2), Inches(0.4), fill=ACCENT, corner=True)
        add_text(s, x + Inches(0.2), y + Inches(0.13),
                 cw - Inches(0.4), Inches(0.35),
                 name, size=10, bold=True, color=WHITE,
                 anchor=MSO_ANCHOR.MIDDLE)
        add_text(s, x + Inches(0.2), y + Inches(0.7),
                 cw - Inches(0.4), Inches(1.2),
                 sub, size=10, color=MUTED)
    add_text(s, Inches(0.6), Inches(7.0), Inches(12), Inches(0.4),
             "Full interactive HTML mockup available — opens in any browser.",
             size=10, color=ACCENT)
    add_footer(s, 12, slides_total)

slide_screens()

# 13. AI TIER 1 --------------------------------------------------
def ai_tier_slide(num, total, eyebrow, title, intro, items):
    s = add_slide()
    add_section_header(s, eyebrow, title)
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.4),
             intro, size=14, color=MUTED)
    cols = 2
    cw = Inches(6.0); ch = Inches(1.0); gap = Inches(0.15)
    x0 = Inches(0.6); y0 = Inches(2.9)
    for i, (name, desc) in enumerate(items):
        c = i % cols; r = i // cols
        x = x0 + (cw + gap) * c
        y = y0 + (ch + gap) * r
        add_rect(s, x, y, cw, ch, fill=WHITE, line=LINE, corner=True)
        # sparkle indicator
        add_rect(s, x + Inches(0.25), y + Inches(0.25),
                 Inches(0.5), Inches(0.5), fill=ACCENT_SO, corner=True)
        add_text(s, x + Inches(0.25), y + Inches(0.25),
                 Inches(0.5), Inches(0.5), "✦",
                 font=SERIF, size=18, color=ACCENT,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        add_text(s, x + Inches(0.85), y + Inches(0.15),
                 cw - Inches(1.1), Inches(0.4),
                 name, size=14, bold=True, color=INK)
        add_text(s, x + Inches(0.85), y + Inches(0.5),
                 cw - Inches(1.1), Inches(0.5),
                 desc, size=11, color=MUTED)
    add_footer(s, num, total)

ai_tier_slide(13, slides_total,
    "Intelligence · Tier 1",
    "AI that earns its keep on day one.",
    "Reduces returns, raises conversion, makes the passport feel alive.",
    [
        ("Fit & size assistant", "Chat that knows your past orders and recommends the right size for the SKU you're viewing."),
        ("Smart recommendations", "Catalog tuned to your closet, wear log, and style spark — not a generic 'You may also like'."),
        ("Visual search", "Photograph anything; surface similar pieces from new stock and resale."),
        ("Passport summaries", "One-paragraph plain-language origin stories for every SKU, editor-reviewed."),
    ])

# 14. AI TIER 2 + 3 ----------------------------------------------
ai_tier_slide(14, slides_total,
    "Intelligence · Tier 2 & 3",
    "AI that powers the loop — and the back office.",
    "Phase 2 customer-facing AI plus operational AI the customer never sees.",
    [
        ("Repair triage from a photo", "Vision model classifies damage, returns instant quote, offers DIY guides for small fixes."),
        ("Resale listing assistant", "Auto-fills title, condition, suggested price and copy from three photos."),
        ("Adaptive style quiz", "Each answer reshapes the next question — ends with a profile that drives recommendations."),
        ("Contextual care reminders", "Weather + fabric aware. Specific, never generic."),
        ("Demand forecasting", "Wishlists + drop signups + view-to-buy → guides production runs. Highest sustainability impact."),
        ("Return-reason clustering", "Free-text returns clustered weekly into actionable patterns for merchandising."),
    ])

# 15. WHAT WE COLLECT --------------------------------------------
def slide_data():
    s = add_slide()
    add_section_header(s, "Data with consent", "What we collect — and what we won't.")
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.4),
             "Default to opt-in per category. A self-serve \"what we know about you\" screen, always.",
             size=14, color=MUTED)
    items = [
        ("Identity & contact", "email, name, address — for orders and shipping."),
        ("Fit", "sizes, body measurements (opt-in), return reasons — to reduce returns."),
        ("Purchase history", "orders, AOV, channel — to understand value and segment."),
        ("Engagement", "views, wishlists, push response — to personalise."),
        ("Closet (app-unique)", "registered items, wear count, photos — proof of durability."),
        ("Sustainability actions", "recycle, repair, resale — for impact reporting."),
        ("Preferences", "style quiz, favoured materials, fit notes — for recommendations."),
        ("Coarse location", "city / region — for demand planning, not tracking."),
    ]
    cols = 2; cw = Inches(6.0); ch = Inches(0.85); gap = Inches(0.12)
    x0 = Inches(0.6); y0 = Inches(2.9)
    for i, (name, desc) in enumerate(items):
        c = i % cols; r = i // cols
        x = x0 + (cw + gap) * c
        y = y0 + (ch + gap) * r
        add_rect(s, x, y, cw, ch, fill=WHITE, line=LINE, corner=True)
        add_rect(s, x + Inches(0.3), y + Inches(0.32),
                 Inches(0.18), Inches(0.18), fill=ACCENT, corner=True)
        add_text(s, x + Inches(0.6), y + Inches(0.1),
                 cw - Inches(0.8), Inches(0.4),
                 name, size=13, bold=True, color=INK)
        add_text(s, x + Inches(0.6), y + Inches(0.42),
                 cw - Inches(0.8), Inches(0.4),
                 desc, size=11, color=MUTED)
    # do-not band
    y = Inches(6.65)
    add_rect(s, Inches(0.6), y, Inches(12.1), Inches(0.5),
             fill=WARN, corner=True)
    add_text(s, Inches(0.85), y + Inches(0.05), Inches(11.8), Inches(0.4),
             "WE DO NOT COLLECT  ·  precise GPS  ·  contacts  ·  social-graph imports  ·  third-party ad-tracking IDs",
             size=11, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    add_footer(s, 15, slides_total)

slide_data()

# 16. TECH STACK -------------------------------------------------
def slide_stack():
    s = add_slide()
    add_section_header(s, "How it's built", "A modern stack — boring where it should be, sharp where it counts.")
    groups = [
        ("Mobile", ["React Native + Expo (iOS & Android)",
                     "Over-the-air updates",
                     "Apple / Google sign-in"]),
        ("Commerce", ["Shopify storefront API (source of truth)",
                       "Klaviyo / Postmark for transactional",
                       "Loyalty: in-house ledger or Smile.io"]),
        ("Lifecycle backend", ["Node + TypeScript API",
                                "Postgres (Supabase / Neon)",
                                "QR for v1, NFC for premium pieces"]),
        ("Intelligence", ["Claude (Sonnet 4.6 chat, Haiku 4.5 batch)",
                           "Embeddings + pgvector",
                           "PostHog analytics, Sentry errors"]),
    ]
    x0 = Inches(0.6); y0 = Inches(2.5); cw = Inches(3.0); ch = Inches(4.0); gap = Inches(0.15)
    for i, (title, items) in enumerate(groups):
        x = x0 + (cw + gap) * i
        add_rect(s, x, y0, cw, ch, fill=WHITE, line=LINE, corner=True)
        add_rect(s, x, y0, cw, Inches(0.7), fill=ACCENT, corner=True)
        add_text(s, x + Inches(0.3), y0 + Inches(0.1),
                 cw - Inches(0.6), Inches(0.55),
                 title, font=SERIF, size=18, color=WHITE,
                 anchor=MSO_ANCHOR.MIDDLE)
        by = y0 + Inches(0.95)
        for itm in items:
            add_text(s, x + Inches(0.25), by, cw - Inches(0.4), Inches(0.35),
                     "•  " + itm, size=11, color=INK)
            by += Inches(0.45)
    add_footer(s, 16, slides_total)

slide_stack()

# 17. STUDIO ARCHITECTURE ----------------------------------------
def slide_studio():
    s = add_slide()
    add_section_header(s, "The Studio · web admin portal",
                       "The internal twin of the mobile app.")
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.8),
             ("Customers use the mobile app. Your team uses the Studio. "
              "Same backend, same brand language — different surface for "
              "different users."),
             size=14, color=MUTED)

    # Top: Shopify
    add_rect(s, Inches(4.5), Inches(3.0), Inches(4.3), Inches(0.85),
             fill=WHITE, line=LINE, corner=True)
    add_text(s, Inches(4.7), Inches(3.05), Inches(3.9), Inches(0.4),
             "SHOPIFY", size=10, bold=True, color=ACCENT)
    add_text(s, Inches(4.7), Inches(3.40), Inches(3.9), Inches(0.4),
             "Catalog · orders · payments — unchanged",
             size=11, color=MUTED)

    # Middle: shared API
    add_rect(s, Inches(0.6), Inches(4.2), Inches(12.1), Inches(0.7),
             fill=ACCENT_SO, corner=True)
    add_text(s, Inches(0.85), Inches(4.27), Inches(11.6), Inches(0.4),
             "SHARED API · Postgres · Auth · AI gateway · Object storage",
             size=11, bold=True, color=ACCENT,
             anchor=MSO_ANCHOR.MIDDLE)

    # Bottom: mobile | studio
    add_rect(s, Inches(0.6), Inches(5.2), Inches(5.95), Inches(1.6),
             fill=WHITE, line=LINE, corner=True)
    add_rect(s, Inches(0.6), Inches(5.2), Inches(5.95), Inches(0.4),
             fill=ACCENT, corner=True)
    add_text(s, Inches(0.85), Inches(5.22), Inches(5.45), Inches(0.4),
             "MOBILE APP — IOS & ANDROID",
             size=10, bold=True, color=WHITE,
             anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(0.85), Inches(5.7), Inches(5.45), Inches(1.0),
             ("Customer-facing · Shop · Closet · Passport · Rewards · "
              "Scan · Fit assistant"),
             size=11, color=INK)

    add_rect(s, Inches(6.75), Inches(5.2), Inches(5.95), Inches(1.6),
             fill=WHITE, line=LINE, corner=True)
    add_rect(s, Inches(6.75), Inches(5.2), Inches(5.95), Inches(0.4),
             fill=INK, corner=True)
    add_text(s, Inches(7.0), Inches(5.22), Inches(5.45), Inches(0.4),
             "THE STUDIO — WEB ADMIN PORTAL",
             size=10, bold=True, color=WHITE,
             anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(7.0), Inches(5.7), Inches(5.45), Inches(1.0),
             ("Internal · Passport editor · take-back queue · repair queue · "
              "resale listings · loyalty admin · sustainability report"),
             size=11, color=INK)

    add_text(s, Inches(0.6), Inches(7.0), Inches(12), Inches(0.4),
             ("BUILT FOR YOUR TEAM   —   editors, ops, customer concierge, "
              "analysts. Audit-ready sustainability data for marketing & regulators."),
             size=10, bold=True, color=ACCENT)
    add_footer(s, 17, slides_total)

slide_studio()

# 18. ROADMAP / TIMELINE -----------------------------------------
def slide_roadmap():
    s = add_slide()
    add_section_header(s, "How we'll deliver", "Roadmap — first nine months.")
    phases = [
        ("Discovery", "Weeks 1–2",
         "Audit current data, interview customers, lock Phase 1 scope, design system kickoff."),
        ("Phase 1 build", "Weeks 3–14",
         "Ship the foundation app: shop, closet, passport, rewards, Tier 1 AI. Launch in week 14."),
        ("Phase 2 build", "Weeks 15–26",
         "Layer in take-back, repair, peer resale, Tier 2 AI. Soft launch the loop."),
        ("Phase 3 build", "Weeks 27–36+",
         "Community, events, swap circles, ongoing optimisation."),
    ]
    # timeline track
    y = Inches(2.5)
    add_rect(s, Inches(0.6), y + Inches(0.5), Inches(12.1), Pt(2),
             fill=LINE)
    cw = Inches(3.0); gap = Inches(0.05); x0 = Inches(0.6)
    for i, (name, when, detail) in enumerate(phases):
        x = x0 + (cw + gap) * i
        add_rect(s, x + cw/2 - Inches(0.1), y + Inches(0.4),
                 Inches(0.2), Inches(0.2), fill=ACCENT, corner=True)
        add_rect(s, x, y + Inches(0.85), cw, Inches(3.6),
                 fill=WHITE, line=LINE, corner=True)
        add_text(s, x + Inches(0.3), y + Inches(1.0), cw - Inches(0.6),
                 Inches(0.4), when, size=10, bold=True, color=ACCENT)
        add_text(s, x + Inches(0.3), y + Inches(1.4), cw - Inches(0.6),
                 Inches(0.6), name, font=SERIF, size=22, color=INK)
        add_text(s, x + Inches(0.3), y + Inches(2.3), cw - Inches(0.6),
                 Inches(2.0), detail, size=12, color=MUTED)
    add_footer(s, 18, slides_total)

slide_roadmap()

# 19. SUCCESS METRICS --------------------------------------------
def slide_metrics():
    s = add_slide()
    add_section_header(s, "How we'll know it's working", "The metrics that matter.")
    metrics = [
        ("Activation", "% of buyers who install the app and register at least one garment in 30 days",
         "Target ≥ 35% by month 6"),
        ("Repeat rate", "% of app users who place a second order within 90 days",
         "Target +25% vs. non-app cohort"),
        ("Return rate", "Returns / orders, app cohort vs. control",
         "Target -20% on app users with fit assistant"),
        ("Closet depth", "Average garments registered per active user",
         "Target ≥ 4 by month 9"),
        ("Circular actions", "Repair / resale / recycle events per active user / quarter",
         "Target ≥ 1 by month 12"),
        ("NPS", "App-cohort net promoter score",
         "Target ≥ 60"),
    ]
    cols = 3; cw = Inches(4.0); ch = Inches(2.0); gap = Inches(0.1)
    x0 = Inches(0.6); y0 = Inches(2.8)
    for i, (name, desc, target) in enumerate(metrics):
        c = i % cols; r = i // cols
        x = x0 + (cw + gap) * c
        y = y0 + (ch + gap) * r
        add_rect(s, x, y, cw, ch, fill=WHITE, line=LINE, corner=True)
        add_text(s, x + Inches(0.3), y + Inches(0.2), cw - Inches(0.6),
                 Inches(0.4), name, size=14, bold=True, color=ACCENT)
        add_text(s, x + Inches(0.3), y + Inches(0.65), cw - Inches(0.6),
                 Inches(0.9), desc, size=11, color=MUTED)
        add_text(s, x + Inches(0.3), y + Inches(1.5), cw - Inches(0.6),
                 Inches(0.4), target, font=SERIF, size=14, color=INK)
    add_footer(s, 19, slides_total)

slide_metrics()

# 20. PRINCIPLES --------------------------------------------------
def slide_principles():
    s = add_slide()
    add_section_header(s, "How it will feel", "Design principles.")
    items = [
        ("Calm, not addictive",
         "No streaks, no anxiety design, no infinite scroll. The app should make customers feel grounded, not hooked."),
        ("Permission before data",
         "Every data category is opt-in with a plain-English reason. The customer can read what we know, anytime."),
        ("Material honesty",
         "When the materials, origin, or impact are imperfect, we say so. The brand's credibility is in the honesty."),
        ("Slow tech",
         "Fast where it matters (checkout, scan), unhurried where it doesn't (reading, reflection)."),
        ("AI in service of people",
         "AI helps customers choose, repair, and resell — never to manipulate, upsell, or replace human craft."),
        ("Earth-first language",
         "The brand voice is steady, generous, never alarmist or preachy."),
    ]
    cols = 2; cw = Inches(6.0); ch = Inches(1.4); gap = Inches(0.15)
    x0 = Inches(0.6); y0 = Inches(2.7)
    for i, (name, desc) in enumerate(items):
        c = i % cols; r = i // cols
        x = x0 + (cw + gap) * c
        y = y0 + (ch + gap) * r
        add_rect(s, x, y, cw, ch, fill=WHITE, line=LINE, corner=True)
        add_text(s, x + Inches(0.3), y + Inches(0.2),
                 cw - Inches(0.6), Inches(0.4),
                 name, size=14, bold=True, color=ACCENT)
        add_text(s, x + Inches(0.3), y + Inches(0.65),
                 cw - Inches(0.6), Inches(1.0),
                 desc, size=11, color=MUTED)
    add_footer(s, 20, slides_total)

slide_principles()

# 21. THE TEAM / WHO WE ARE  -------------------------------------
def slide_team():
    s = add_slide()
    add_section_header(s, "Working together", "How we'd partner.")
    cards = [
        ("Discovery sprint", "Two weeks. Customer interviews, data audit, scope-locking. Walks away with a signed Phase 1 spec — even if you don't build with us."),
        ("Embedded delivery", "A small team — a lead engineer, a mobile engineer, a designer — works as an extension of yours. Weekly demos, never a black box."),
        ("Steady operations", "After launch, one engineer maintains the app, one analyst watches the metrics, the team is on call for incidents."),
        ("Always your data", "Source code, customer data, model logs all live in your accounts — Shopify, Supabase, your cloud. We hold no lock-in."),
    ]
    cols = 2; cw = Inches(6.0); ch = Inches(2.0); gap = Inches(0.15)
    x0 = Inches(0.6); y0 = Inches(2.5)
    for i, (name, desc) in enumerate(cards):
        c = i % cols; r = i // cols
        x = x0 + (cw + gap) * c
        y = y0 + (ch + gap) * r
        add_rect(s, x, y, cw, ch, fill=WHITE, line=LINE, corner=True)
        add_text(s, x + Inches(0.3), y + Inches(0.3),
                 cw - Inches(0.6), Inches(0.5),
                 name, font=SERIF, size=20, color=ACCENT)
        add_text(s, x + Inches(0.3), y + Inches(0.95),
                 cw - Inches(0.6), Inches(1.1),
                 desc, size=12, color=MUTED)
    add_footer(s, 21, slides_total)

slide_team()

# 22. WHY IT WILL WORK -------------------------------------------
def slide_why():
    s = add_slide()
    add_section_header(s, "Why this works for Erth to Erth", "The bet behind the build.")
    pts = [
        ("Your story is your moat",
         "Most fashion apps are bigger, faster, glossier — but none of them can tell your story honestly. The passport is yours to own."),
        ("The most engaged customer is the next purchase",
         "App users buy more, return less, and refer better — not because of dark patterns, but because the relationship is deeper."),
        ("Circular features generate proof, not just rhetoric",
         "Every repair, resale, and recycle event becomes data, content, and credibility — for marketing, regulators, and investors."),
        ("Built to grow with you",
         "Start small in Phase 1. Every later phase compounds the closet you've already built. No throwaway work."),
    ]
    y = Inches(2.5)
    for i, (head, body) in enumerate(pts):
        cy = y + Inches(1.05) * i
        add_rect(s, Inches(0.6), cy, Inches(0.08), Inches(0.95), fill=ACCENT)
        add_text(s, Inches(0.95), cy + Inches(0.05),
                 Inches(11.5), Inches(0.4),
                 head, font=SERIF, size=20, color=INK)
        add_text(s, Inches(0.95), cy + Inches(0.55),
                 Inches(11.5), Inches(0.4),
                 body, size=12, color=MUTED)
    add_footer(s, 22, slides_total)

slide_why()

# 23. NEXT STEP / CLOSING -----------------------------------------
def slide_next():
    s = add_slide()
    # full-bleed accent
    add_rect(s, 0, 0, SW, SH, fill=ACCENT)
    add_text(s, Inches(0.6), Inches(0.55), Inches(8), Inches(0.3),
             "NEXT STEP",
             size=11, bold=True, color=ACCENT_SO)
    add_text(s, Inches(0.6), Inches(1.1), Inches(12), Inches(2.0),
             "A two-week paid discovery.",
             font=SERIF, size=54, color=WHITE)
    add_text(s, Inches(0.6), Inches(2.7), Inches(11), Inches(2.0),
             ("We sit with your team. We talk to ten of your customers. We "
              "audit what you already know about them. We come back with a "
              "lockable Phase 1 scope — and a working interactive prototype "
              "of three core flows."),
             size=18, color=ACCENT_SO)
    add_text(s, Inches(0.6), Inches(5.0), Inches(11), Inches(0.5),
             "WHAT YOU GET",
             size=11, bold=True, color=ACCENT_SO)
    add_text(s, Inches(0.6), Inches(5.4), Inches(11), Inches(2.0),
             ("•  A lockable feature scope, costed and timeboxed\n"
              "•  An interactive prototype of onboarding, scan, and rewards\n"
              "•  A list of the customer interviews and what we heard\n"
              "•  A go / no-go recommendation. Yours either way."),
             size=14, color=WHITE)
    add_footer(s, 23, slides_total)
    # override footer color
    # (re-add over the dark band)
    add_text(s, Inches(0.6), Inches(7.05), Inches(6), Inches(0.3),
             "Erth to Erth · Mobile App Pitch",
             size=9, color=ACCENT_SO)
    add_text(s, Inches(11.7), Inches(7.05), Inches(1), Inches(0.3),
             f"23 / {slides_total}",
             size=9, color=ACCENT_SO, align=PP_ALIGN.RIGHT)

slide_next()

# write -----------------------------------------------------------
out = Path(__file__).parent / "Erth-to-Erth-Pitch.pptx"
prs.save(out)
print(f"wrote {out}  ({len(prs.slides)} slides)")
