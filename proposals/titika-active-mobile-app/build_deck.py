"""Build the Titika Active client pitch deck (.pptx). Features-only.
Run: python3 proposals/titika-active-mobile-app/build_deck.py
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pathlib import Path

# Brand palette (matches the HTML mockups)
INK         = RGBColor(0x1a, 0x1a, 0x1a)
MUTED       = RGBColor(0x77, 0x77, 0x77)
LINE        = RGBColor(0xe6, 0xe3, 0xdd)
BG          = RGBColor(0xf6, 0xf4, 0xf0)
ACCENT      = RGBColor(0xc4, 0x3e, 0x54)   # couture wine-rose
ACCENT_DEEP = RGBColor(0x8a, 0x22, 0x36)
ACCENT_SOFT = RGBColor(0xf8, 0xe0, 0xe4)
GOLD        = RGBColor(0xd4, 0xa8, 0x5a)
GOLD_SOFT   = RGBColor(0xf5, 0xe8, 0xc8)
TEAL        = RGBColor(0x2d, 0x6e, 0x7e)
PINK        = RGBColor(0xef, 0x6f, 0x8b)
WHITE       = RGBColor(0xff, 0xff, 0xff)

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
    bg.line.fill.background(); bg.fill.solid(); bg.fill.fore_color.rgb = BG
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


def add_rect(slide, x, y, w, h, *, fill=WHITE, line=None, line_w=0.75, corner=False):
    shp = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE if corner else MSO_SHAPE.RECTANGLE,
        x, y, w, h,
    )
    if corner: shp.adjustments[0] = 0.12
    shp.fill.solid(); shp.fill.fore_color.rgb = fill
    if line is None: shp.line.fill.background()
    else: shp.line.color.rgb = line; shp.line.width = Pt(line_w)
    shp.shadow.inherit = False
    return shp


def add_arrow(slide, x, y, w, h, *, color=ACCENT):
    shp = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, x, y, w, h)
    shp.fill.solid(); shp.fill.fore_color.rgb = color
    shp.line.fill.background(); shp.shadow.inherit = False
    return shp


def add_footer(slide, page, total, *, on_dark=False):
    color = GOLD_SOFT if on_dark else MUTED
    add_text(slide, Inches(0.6), Inches(7.05), Inches(6), Inches(0.3),
             "Titika Active · Mobile App Pitch", size=9, color=color)
    add_text(slide, Inches(11.7), Inches(7.05), Inches(1), Inches(0.3),
             f"{page} / {total}", size=9, color=color, align=PP_ALIGN.RIGHT)


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


slides_total = 23

# 1. COVER
def slide_cover():
    s = add_slide()
    # right-side dark band
    add_rect(s, Inches(8.5), 0, Inches(4.833), SH, fill=INK)
    add_rect(s, Inches(8.5), 0, Inches(4.833), Inches(2.0), fill=ACCENT_DEEP)
    add_rect(s, Inches(8.5), 0, Inches(4.833), Inches(0.5), fill=GOLD)
    # decorative dots
    for cx, cy, r in [(11.2, 1.4, 0.20), (12.5, 3.0, 0.12),
                       (10.4, 4.2, 0.18), (12.0, 5.6, 0.14),
                       (11.6, 6.7, 0.10)]:
        d = s.shapes.add_shape(MSO_SHAPE.OVAL,
                               Inches(cx-r), Inches(cy-r),
                               Inches(2*r), Inches(2*r))
        d.fill.solid(); d.fill.fore_color.rgb = GOLD
        d.line.fill.background(); d.shadow.inherit = False

    add_rect(s, Inches(0.6), Inches(1.0), Inches(0.08), Inches(2.4), fill=ACCENT)
    add_text(s, Inches(0.85), Inches(1.0), Inches(7), Inches(0.4),
             "MOBILE APP · PITCH", size=11, bold=True, color=ACCENT)
    add_text(s, Inches(0.85), Inches(1.45), Inches(8), Inches(2.0),
             "Titika Active.", font=SERIF, size=66, color=INK)
    add_text(s, Inches(0.85), Inches(2.7), Inches(7.5), Inches(1.6),
             "VERSATILE.\nACTIVE.\nLIFE.",
             font=SERIF, size=26, color=ACCENT)
    add_text(s, Inches(0.85), Inches(5.6), Inches(7.5), Inches(0.4),
             "A daily companion to a versatile life — gym, yoga, brunch, errands.",
             size=14, color=MUTED)
    add_text(s, Inches(0.85), Inches(6.0), Inches(7.5), Inches(0.3),
             "Prepared for the Titika Active team",
             size=11, color=MUTED)

slide_cover()

# 2. THE OPPORTUNITY
def slide_opportunity():
    s = add_slide()
    add_section_header(s, "Why now", "Premium athleisure is now a daily-companion category.")
    stats = [
        ("$340B", "global activewear market\nby 2027",
         "And the leaders are app-native: Lululemon, Alo, Nike."),
        ("2", "anchor markets — Toronto\n+ Hong Kong, with global reach",
         "A multi-region app is the proposition, not an upgrade."),
        ("18%", "of activewear returns are\nfit-related — leggings, especially",
         "An AI Fit Atelier is the highest-ROI feature you ship."),
    ]
    x = Inches(0.6); y = Inches(2.4); w = Inches(4); gap = Inches(0.2)
    for i, (big, mid, small) in enumerate(stats):
        cx = x + (w + gap) * i
        add_rect(s, cx, y, w, Inches(4.0), fill=WHITE, line=LINE, corner=True)
        add_text(s, cx + Inches(0.4), y + Inches(0.4), w - Inches(0.8),
                 Inches(1.4), big, font=SERIF, size=58, color=ACCENT)
        add_text(s, cx + Inches(0.4), y + Inches(1.7), w - Inches(0.8),
                 Inches(1.0), mid, size=14, bold=True, color=INK)
        add_text(s, cx + Inches(0.4), y + Inches(2.9), w - Inches(0.8),
                 Inches(1.0), small, size=12, color=MUTED)
    add_footer(s, 2, slides_total)

slide_opportunity()

# 3. VISION
def slide_vision():
    s = add_slide()
    add_section_header(s, "The vision", "Not another store — a daily companion.")
    add_text(s, Inches(0.6), Inches(2.3), Inches(12), Inches(2.5),
             ("Titika's customer doesn't separate her gym life from her real "
              "life. She wears Couture Leggings to Pure Yoga, then to brunch, "
              "then to grocery runs.\n\n"
              "The app should make the brand's promise — VERSATILE. ACTIVE. "
              "LIFE. — concrete: a closet that shows her three ways to wear "
              "what she owns, a practice library that meets her wherever she "
              "is, a Fit Atelier that ends the legging-sizing lottery, and a "
              "tribe that travels with her between Toronto and Hong Kong."),
             font=SERIF, size=20, color=INK)
    add_text(s, Inches(0.6), Inches(5.8), Inches(12), Inches(0.4),
             "WHY IT MATTERS", size=10, bold=True, color=ACCENT)
    add_text(s, Inches(0.6), Inches(6.1), Inches(12), Inches(1.5),
             ("• Reduces returns — fit AI is worth more than any other feature dollar-for-dollar\n"
              "• Builds the daily habit Lululemon spent a decade perfecting — at app cost\n"
              "• Bridges Canadian and Asian markets natively, not as an afterthought"),
             size=13, color=INK)
    add_footer(s, 3, slides_total)

slide_vision()

# 4. SIX PILLARS
def slide_pillars():
    s = add_slide()
    add_section_header(s, "Product overview", "Six pillars — five customer-facing, one internal.")
    pillars = [
        ("The Closet", "Every piece you own, shown three ways. Studio · Street · Sunday.", ACCENT),
        ("The Practice", "Guided yoga, mobility, strength, low-impact, and audio walks — meets you where you are.", TEAL),
        ("The Fit Atelier", "AI fit assistant that ends the legging-sizing lottery. Photo-based fit checks.", PINK),
        ("The Tribe", "Local meetups, ambassador-led challenges, looks gallery — community without the noise.", GOLD),
        ("The Shop", "Multi-currency, multi-language, region-aware drops. Asia Miles tie-in.", ACCENT_DEEP),
        ("The Studio", "Internal-facing web admin portal — closet editor, practice library, moderation, concierge.", INK),
    ]
    cols = 3; cw = Inches(4.0); ch = Inches(2.25); gx = Inches(0.15); gy = Inches(0.18)
    x0 = Inches(0.6); y0 = Inches(2.4)
    for i, (title, desc, accent) in enumerate(pillars):
        c = i % cols; r = i // cols
        cx = x0 + (cw + gx) * c
        cy = y0 + (ch + gy) * r
        add_rect(s, cx, cy, cw, ch, fill=WHITE, line=LINE, corner=True)
        add_rect(s, cx, cy, Inches(0.1), ch, fill=accent, corner=True)
        add_text(s, cx + Inches(0.3), cy + Inches(0.2), cw - Inches(0.6),
                 Inches(0.4), str(i + 1), font=SERIF, size=20, bold=True, color=accent)
        add_text(s, cx + Inches(0.3), cy + Inches(0.7), cw - Inches(0.6),
                 Inches(0.5), title, font=SERIF, size=20, color=INK)
        add_text(s, cx + Inches(0.3), cy + Inches(1.25), cw - Inches(0.6),
                 Inches(1.0), desc, size=11, color=MUTED)
    add_footer(s, 4, slides_total)

slide_pillars()

# 5–7 features
def feature_slide(num, total, eyebrow, title, intro, items):
    s = add_slide()
    add_section_header(s, eyebrow, title)
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.6),
             intro, size=14, color=MUTED)
    cols = 2; cw = Inches(6.0); ch = Inches(0.95); gap = Inches(0.15)
    for i, (name, desc) in enumerate(items):
        c = i % cols; r = i // cols
        cx = Inches(0.6) + (cw + gap) * c
        cy = Inches(2.9) + (ch + gap) * r
        add_rect(s, cx, cy, cw, ch, fill=WHITE, line=LINE, corner=True)
        add_rect(s, cx + Inches(0.3), cy + Inches(0.4), Inches(0.18),
                 Inches(0.18), fill=ACCENT, corner=True)
        add_text(s, cx + Inches(0.6), cy + Inches(0.12), cw - Inches(0.8),
                 Inches(0.4), name, size=14, bold=True, color=INK)
        add_text(s, cx + Inches(0.6), cy + Inches(0.45), cw - Inches(0.8),
                 Inches(0.5), desc, size=11, color=MUTED)
    add_footer(s, num, total)

feature_slide(5, slides_total, "Phase 1 · Launch (months 0–4)",
              "Foundations: Closet, Practice, Fit, Tribe, Shop, Rewards.",
              "Everything a customer needs in their first 90 days.", [
    ("Multilingual onboarding", "EN + 繁中 at launch · JP / KR / FR / 简中 expandable."),
    ("Multi-region storefront", "CA · US · HK · wider Asia. Currency follows the customer."),
    ("Closet & 'three ways' looks", "Register every piece. Same item across Studio · Street · Sunday."),
    ("Practice library", "10/20/45-min yoga, mobility, strength, low-impact, audio walks."),
    ("Fit Atelier (AI)", "Multilingual chat with full size profile + past-order context."),
    ("Easy size-swap returns", "Tied to loyalty wallet. Returns shouldn't punish the customer."),
    ("Tribe meetups", "Toronto · HK · NYC · Vancouver as starter cities."),
    ("Looks gallery", "Customers post how they wore it. Light moderation."),
    ("Style quiz → home feed", "Calibrated recommendations from day one."),
    ("Asia Miles wallet", "Existing Cathay tie-in, native to the rewards screen."),
    ("Practice recommender (AI)", "Mood, energy, time → guided session."),
    ("Visual search (AI)", "See a look, find the piece."),
    ("Outfit-builder (AI)", "Three contexts per piece, with auto-generated copy."),
    ("Push by region", "EN to NA · 繁中 to HK. Right copy, right time."),
    ("Multilingual brand-voice translation", "Claude drafts copy in 4 languages; editors approve."),
    ("The Studio (web admin portal)", "Closet editor, practice library, moderation, concierge, analytics."),
])

feature_slide(6, slides_total, "Phase 2 · Depth (months 5–9)",
              "AR fit, live classes, wholesale, recovery coach.",
              "Features that turn a great launch into a daily habit.", [
    ("AR fit visualisation", "See leggings on a body silhouette using your size profile."),
    ("Vision-based fit check", "AI analyses a mirror photo for waistband fit, length, compression."),
    ("Live classes", "Scheduled live yoga / mobility with chat. Recordings join the library."),
    ("Recovery + wellness coach", "Sleep / mood / soreness inputs → recommended practice."),
    ("Local studio partner program", "Partnered yoga / pilates studios; Titika rewards for visiting."),
    ("Wholesale & ambassador portal", "Applications, comp pieces, content review (B2B)."),
    ("Heritage / archive sale", "Past-season pieces re-released with provenance."),
    ("Multi-region demand sensing (AI)", "Drives reprints across CA / US / HK / wider Asia."),
])

feature_slide(7, slides_total, "Phase 3 · Cultural authority (months 10+)",
              "From an app to a brand world.",
              "Long-form storytelling, community, operational AI.", [
    ("Editorial / journal", "Long-form on sport, design, training. Multilingual."),
    ("Branded events", "Pop-up classes in Toronto, HK, NYC."),
    ("Annual VERSATILE film series", "Short documentaries on ambassadors and customers."),
    ("Multilingual content scaling AI", "EN-first, AI drafts 繁中 / 简中 / JP / KR / FR for editor review."),
    ("Ambassador-revenue marketplace", "Content that converts; revenue share built in."),
    ("Counterfeit listing detection", "Amazon · ThredUp · Asian marketplaces."),
    ("VIP signal detection", "Surfaces emerging high-value Couture-tier customers early."),
    ("Cathay co-branded experiences", "Asia Miles members get unlocks — branded yoga at 35,000 ft."),
])

# 8. ONBOARDING
def slide_onboarding():
    s = add_slide()
    add_section_header(s, "User experience", "Onboarding — under 90 seconds, in any language.")
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.4),
             "The international customer must feel at home in the first screen. Language is offered before anything else.",
             size=14, color=MUTED)
    steps = [
        ("01", "Bienvenue", "Welcome in six languages.\nTap your language; everything follows."),
        ("02", "Sign in", "Apple, Google, or email.\nNo forms."),
        ("03", "Fit profile", "Bra, top, bottom, inseam.\nOptional body shape, opt-in."),
        ("04", "What moves you?", "Pick three motivations:\nyoga · strength · running · lifestyle."),
        ("05", "First moment", "Today's 10-min flow —\nor explore the new drop."),
    ]
    x = Inches(0.6); y = Inches(2.9); w = Inches(2.3); h = Inches(3.6); gap = Inches(0.2)
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
             "DESIGN PRINCIPLE   —   Body data is opt-in. Motivation matters more than measurements.",
             size=11, bold=True, color=ACCENT)
    add_footer(s, 8, slides_total)

slide_onboarding()

# 9-11 journeys
def journey_slide(num, total, eyebrow, title, intro, steps):
    s = add_slide()
    add_section_header(s, eyebrow, title)
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.4),
             intro, size=14, color=MUTED)
    n = len(steps)
    arrow_w = Inches(0.25); arrow_gap = Inches(0.05)
    box_w = (Inches(12.0) - arrow_w * (n - 1) - arrow_gap * 2 * (n - 1)) / n
    box_h = Inches(3.7); y = Inches(2.8); x = Inches(0.6)
    for i, (label, what, ux) in enumerate(steps):
        add_rect(s, x, y, box_w, box_h, fill=WHITE, line=LINE, corner=True)
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
        else: x = x + box_w
    add_footer(s, num, total)

journey_slide(9, slides_total,
    "User flow · 1 of 3",
    "First purchase → daily companion.",
    "From an Instagram ad to a 10-minute morning practice.",
    [
        ("DISCOVER", "Sees the drop",
         "Instagram ad for the Couture Legging — Bordeaux. Taps in. Saves to wishlist."),
        ("DECIDE", "Asks the Fit Atelier",
         "AI uses past Lululemon size and inseam preference. Recommends S, 25\". Confidence builds."),
        ("BUY", "Apple Pay checkout",
         "Two taps. Order tracked in-app from the moment it ships."),
        ("UNBOX", "Scans the QR tag",
         "Item arrives. One scan registers it to her closet, opens 'wear it three ways,' offers a 10-min flow."),
        ("DAILY", "Practice + post",
         "Three weeks in: 14 sessions completed, 22 wears logged, first 'fit look' posted to The Tribe."),
    ])

journey_slide(10, slides_total,
    "User flow · 2 of 3",
    "The 7-day rhythm — what brings her back.",
    "We don't need her every day. We need a reason every other day.",
    [
        ("MONDAY", "Today's flow",
         "Push: \"Low energy? 20-min restorative.\" Audio-only mode for the school run / walk."),
        ("WEDNESDAY", "Fit follow-up",
         "Atelier: \"How are the Couture Leggings — true to size?\" One-tap feedback feeds the size guide."),
        ("FRIDAY", "Drop preview",
         "Members get the Saturday drop 12 hours early. Restock alerts on saved items."),
        ("SATURDAY", "Tribe meetup",
         "Park yoga, Trinity Bellwoods. RSVP in-app. Earns 100 points + a Tribe badge."),
        ("SUNDAY", "Three ways",
         "App suggests today's outfit from her closet — same Couture Legging, Sunday styling."),
    ])

journey_slide(11, slides_total,
    "User flow · 3 of 3",
    "The Hong Kong customer — multi-market by design.",
    "Toronto and Hong Kong are not 'localised English' — they're peers. The app is built that way.",
    [
        ("DISCOVERY", "Pinkoi → app",
         "Lands on Titika via Pinkoi marketplace. Installs the app, sets 繁中 + HKD."),
        ("ATELIER", "Asks in 繁中",
         "AI Fit Atelier responds in Traditional Chinese. Brand glossary keeps Couture, Active, Tribe untranslated."),
        ("BUY", "Asia Miles credit",
         "Checkout offers Asia Miles earn — Cathay tie-in. 100 miles per HK$100 spent."),
        ("PRACTICE", "Local instructor",
         "Practice library prioritises Mei's Cantonese sessions. Pure Yoga partner offers an unlock."),
        ("TRIBE", "Bowen Road run",
         "RSVPs to a Saturday morning Tribe run on Bowen Road. The brand's Toronto + HK customers see the same app, in their language."),
    ])

# 12. SCREENS
def slide_screens():
    s = add_slide()
    add_section_header(s, "Visual reference", "What it looks like in hand.")
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.4),
             "Wireframe-fidelity mockups in the brand palette — warm cream, couture wine, saffron gold.",
             size=14, color=MUTED)
    screens = [
        ("Onboarding", "6 languages · sign-in"),
        ("Home", "Today's practice + drop"),
        ("Practice", "Session library"),
        ("Closet", "Wear it three ways"),
        ("Product", "Fit pills · ask AI"),
        ("Fit Atelier", "Multilingual + photo"),
        ("Tribe", "Meetups · looks gallery"),
        ("Rewards", "Points + Asia Miles"),
        ("Profile", "Sizes · privacy"),
    ]
    cols = 5; cw = Inches(2.3); ch = Inches(2.0); gx = Inches(0.15); gy = Inches(0.25)
    x0 = Inches(0.6); y0 = Inches(2.7)
    for i, (name, sub) in enumerate(screens):
        c = i % cols; r = i // cols
        x = x0 + (cw + gx) * c
        y = y0 + (ch + gy) * r
        add_rect(s, x, y, cw, ch, fill=INK, corner=True)
        add_rect(s, x + Inches(0.1), y + Inches(0.1),
                 cw - Inches(0.2), ch - Inches(0.2), fill=BG, corner=True)
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

# 13. AI Tier 1
def ai_tier_slide(num, total, eyebrow, title, intro, items):
    s = add_slide()
    add_section_header(s, eyebrow, title)
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.4),
             intro, size=14, color=MUTED)
    cols = 2; cw = Inches(6.0); ch = Inches(1.0); gap = Inches(0.15)
    x0 = Inches(0.6); y0 = Inches(2.9)
    for i, (name, desc) in enumerate(items):
        c = i % cols; r = i // cols
        x = x0 + (cw + gap) * c
        y = y0 + (ch + gap) * r
        add_rect(s, x, y, cw, ch, fill=WHITE, line=LINE, corner=True)
        add_rect(s, x + Inches(0.25), y + Inches(0.25),
                 Inches(0.5), Inches(0.5), fill=GOLD_SOFT, corner=True)
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
    "AI that reduces returns and deepens the daily habit.",
    "Every Tier 1 feature pays back its cost in either avoided returns or repeat sessions.",
    [
        ("Fit Atelier (chat)", "Multilingual size + fabric assistant. Past orders + body profile + product fit chart in cached system prompt."),
        ("Practice recommender", "Mood, energy, time → 10/20/45-min session. Reduces the 'too much choice' tax."),
        ("Outfit-builder", "Generates the 'wear it three ways' copy per piece. Editors approve before publish."),
        ("Visual search", "Photograph any look — find the matching Titika piece."),
        ("Multilingual brand-voice translation", "Claude drafts EN/繁中/JP/FR. Brand glossary preserves Couture, Active, Tribe."),
        ("Closet wear analyser", "Notices favourites and forgotten pieces; suggests outfits to revive the wardrobe."),
    ])

# 14. AI Tier 2 + 3
ai_tier_slide(14, slides_total,
    "Intelligence · Tier 2 & 3",
    "AI that powers the wellness loop and the back office.",
    "Phase 2 customer-facing AI plus operational AI the customer never sees.",
    [
        ("Vision-based fit check", "Customer uploads a mirror photo; AI analyses waistband, length, compression."),
        ("Recovery coach", "Sleep + mood + soreness inputs → today's session. Avoids triggering metrics."),
        ("Live class translation", "Real-time captions in 繁中/JP for English live yoga classes."),
        ("Demand-sensing AI", "Wishlists + waitlists + cultural calendar → reprints across CA/US/HK/JP."),
        ("Return-reason clustering", "Free-text returns clustered weekly into actionable patterns for design."),
        ("Multilingual content scaling", "EN-first, AI drafts five languages, editors approve. 5× the editorial output."),
        ("Ambassador-content authenticity", "Vision model verifies a post is shot in real Titika garment, not a counterfeit."),
        ("VIP signal detection", "Surfaces customers about to hit Couture / Atelier tier so concierge can welcome them."),
    ])

# 15. DATA
def slide_data():
    s = add_slide()
    add_section_header(s, "Data with consent", "What we collect — and what we won't.")
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.4),
             "Default to opt-in per category. A self-serve \"what we know about you\" screen, always.",
             size=14, color=MUTED)
    items = [
        ("Identity & contact", "email, name, address — orders and shipping."),
        ("Fit profile", "bra/top/bottom sizes, inseam, fit notes (body shape opt-in)."),
        ("Language & region", "UI language, country, currency."),
        ("Practice", "sessions completed, durations, time-of-day."),
        ("Closet", "registered pieces, wear count, 'three ways' choices."),
        ("Motivation tags", "yoga / strength / running / lifestyle."),
        ("Tribe", "meetups attended, challenges joined, ambassador follows."),
        ("Channel of origin", "online / Amazon / Pinkoi / store / referral."),
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
    y = Inches(6.65)
    add_rect(s, Inches(0.6), y, Inches(12.1), Inches(0.5),
             fill=ACCENT, corner=True)
    add_text(s, Inches(0.85), y + Inches(0.05), Inches(11.8), Inches(0.4),
             "WE DO NOT COLLECT  ·  weight or BMI  ·  precise GPS  ·  contacts  ·  social-graph imports  ·  third-party ad-tracking IDs",
             size=11, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    add_footer(s, 15, slides_total)

slide_data()

# 16. STACK
def slide_stack():
    s = add_slide()
    add_section_header(s, "How it's built", "A modern stack — boring where it should be, sharp where it counts.")
    groups = [
        ("Mobile", ["React Native + Expo (iOS & Android)",
                     "OTA updates for drop cadence",
                     "Apple / Google sign-in"]),
        ("Commerce", ["Shopify storefront API",
                       "Multi-currency · multi-region",
                       "RevenueCat for any subscriptions"]),
        ("Wellness backend", ["Node + TypeScript API",
                                "Postgres + pgvector for visual search",
                                "Bunny / Mux for practice video"]),
        ("Intelligence", ["Claude (Sonnet 4.6 chat, Haiku 4.5 batch)",
                           "Embeddings for closet & motif",
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

# 17. STUDIO ARCHITECTURE
def slide_studio():
    s = add_slide()
    add_section_header(s, "The Studio · web admin portal",
                       "The internal twin of the mobile app.")
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.8),
             ("Customers use the mobile app. Your team uses The Studio. "
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
             fill=ACCENT_SOFT, corner=True)
    add_text(s, Inches(0.85), Inches(4.27), Inches(11.6), Inches(0.4),
             "SHARED API · Postgres · Auth · AI gateway · Video CDN · Object storage",
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
             ("Customer-facing · Closet · Practice · Fit Atelier · "
              "Tribe · Shop · Rewards"),
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
             ("Internal · Closet editor · practice library · drop scheduler · "
              "ambassadors · moderation · concierge · analytics"),
             size=11, color=INK)

    add_text(s, Inches(0.6), Inches(7.0), Inches(12), Inches(0.4),
             ("BUILT FOR YOUR TEAM   —   editors, ops, ambassadors, "
              "concierge. Bilingual EN/繁中. Brand-palette UI."),
             size=10, bold=True, color=ACCENT)
    add_footer(s, 17, slides_total)

slide_studio()

# 18. ROADMAP
def slide_roadmap():
    s = add_slide()
    add_section_header(s, "How we'll deliver", "Roadmap — first nine months.")
    phases = [
        ("Discovery", "Weeks 1–2",
         "Customer interviews (Toronto, HK, US, ambassador, new buyer). Audit existing data. Lock Phase 1 scope. Brand language + fit-glossary workshop."),
        ("Phase 1 build", "Weeks 3–16",
         "Closet, Practice, Fit Atelier, Tribe, Shop, Rewards, Asia Miles tie-in, Tier 1 AI, Studio. EN/繁中 at launch."),
        ("Phase 2 build", "Weeks 17–32",
         "AR fit, vision fit-check, live classes, recovery coach, wholesale portal. Add JP/KR/FR languages."),
        ("Phase 3 build", "Weeks 33–40+",
         "Editorial, branded events, demand-sensing, ambassador marketplace, counterfeit detection."),
    ]
    y = Inches(2.5)
    add_rect(s, Inches(0.6), y + Inches(0.5), Inches(12.1), Pt(2), fill=LINE)
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
                 Inches(2.0), detail, size=11, color=MUTED)
    add_footer(s, 18, slides_total)

slide_roadmap()

# 19. METRICS
def slide_metrics():
    s = add_slide()
    add_section_header(s, "How we'll know it's working", "The metrics that matter.")
    metrics = [
        ("Return rate", "Returns / orders, app cohort vs control, fit-related",
         "Target −20% on app cohort"),
        ("Practice retention", "% of installs completing ≥1 session per week, month 3",
         "Target ≥ 35%"),
        ("Closet depth", "Average pieces registered per active user",
         "Target ≥ 5 by month 9"),
        ("Cross-language reach", "% of sessions in 繁中 + future JP/KR/FR",
         "Target ≥ 35% by month 12"),
        ("Tribe activity", "Looks posted + meetups attended per active user / quarter",
         "Target ≥ 1 by month 9"),
        ("Asia Miles redemption", "% of HK customers earning or redeeming",
         "Target ≥ 60%"),
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

# 20. PRINCIPLES
def slide_principles():
    s = add_slide()
    add_section_header(s, "How it will feel", "Design principles.")
    items = [
        ("Calm, not punishing",
         "No streaks that shame, no daily-goal anxiety. Practice should feel like coming home."),
        ("Body data is opt-in",
         "We never collect weight, BMI, or body-fat. Motivation tags matter more than measurements."),
        ("Language is welcome",
         "EN and 繁中 are equals at launch. Translation is brand-aware, not literal."),
        ("AI in service of the practice",
         "AI helps you find the right session and the right size. It never replaces a teacher."),
        ("Recognition over discounts",
         "Tier rewards are access — early drops, ambassador status, branded experiences. Not coupons."),
        ("Multi-region by default",
         "Toronto and Hong Kong are peers, not localised English. The app respects that from screen one."),
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

# 21. PARTNERSHIP
def slide_team():
    s = add_slide()
    add_section_header(s, "Working together", "How we'd partner.")
    cards = [
        ("Discovery sprint", "Two weeks. Customer interviews in Toronto and HK. Walk away with a signed Phase 1 spec — even if you don't build with us."),
        ("Embedded delivery", "A small team — lead engineer, mobile engineer, designer, bilingual QA — works as an extension of yours. Weekly demos."),
        ("Brand-side approval", "Every customer-facing string of cultural / fit content reviewed by your editorial team. AI generates; humans approve."),
        ("Always your data", "Source code, customer data, model logs all live in your accounts. Multi-region storage to honour data-residency rules."),
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

# 22. WHY THIS WORKS
def slide_why():
    s = add_slide()
    add_section_header(s, "Why this works for Titika Active", "The bet behind the build.")
    pts = [
        ("Fit AI pays for the rest of the app",
         "An 18% return rate on activewear is real money. A Fit Atelier that cuts that by 5 points funds the entire build in year one."),
        ("Versatility is your moat",
         "Lululemon owns the gym. Alo owns the studio aesthetic. Titika owns the in-between. The 'wear it three ways' feature is the brand promise made concrete."),
        ("Multi-region is your edge",
         "Most North American brands fake their Asia presence. Titika has a real HK customer base. The app should reflect that — and competitors can't easily copy it."),
        ("The Practice creates the daily habit",
         "An app you open every day is worth ten apps you open every quarter. Practice is what turns this from a shopping app into a daily companion."),
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

# 23. NEXT STEP
def slide_next():
    s = add_slide()
    add_rect(s, 0, 0, SW, SH, fill=INK)
    add_rect(s, 0, 0, SW, Inches(0.25), fill=GOLD)
    for cx, cy, r in [(11.0, 1.4, 0.20), (12.4, 3.0, 0.14),
                       (10.4, 4.2, 0.22), (12.0, 5.6, 0.16),
                       (11.2, 6.4, 0.12)]:
        d = s.shapes.add_shape(MSO_SHAPE.OVAL,
                               Inches(cx-r), Inches(cy-r),
                               Inches(2*r), Inches(2*r))
        d.fill.solid(); d.fill.fore_color.rgb = ACCENT
        d.line.fill.background(); d.shadow.inherit = False

    add_text(s, Inches(0.6), Inches(0.55), Inches(8), Inches(0.3),
             "NEXT STEP", size=11, bold=True, color=GOLD)
    add_text(s, Inches(0.6), Inches(1.1), Inches(11), Inches(2.0),
             "A two-week paid discovery.",
             font=SERIF, size=54, color=WHITE)
    add_text(s, Inches(0.6), Inches(2.7), Inches(10.5), Inches(2.0),
             ("We sit with your team in Toronto. We talk to ten of your "
              "customers across CA, US, and HK. We audit what you already "
              "know about them. We come back with a lockable Phase 1 scope "
              "and a working interactive prototype of the Closet, the Fit "
              "Atelier, and the Practice library — in EN and 繁中."),
             size=18, color=GOLD_SOFT)
    add_text(s, Inches(0.6), Inches(5.1), Inches(11), Inches(0.5),
             "WHAT YOU GET", size=11, bold=True, color=GOLD)
    add_text(s, Inches(0.6), Inches(5.5), Inches(11), Inches(2.0),
             ("•  A lockable feature scope, costed and timeboxed\n"
              "•  An interactive prototype of three core flows\n"
              "•  A summary of the customer interviews and what we heard\n"
              "•  A go / no-go recommendation. Yours either way."),
             size=14, color=WHITE)
    add_footer(s, 23, slides_total, on_dark=True)

slide_next()

out = Path(__file__).parent / "Titika-Active-Pitch.pptx"
prs.save(out)
print(f"wrote {out}  ({len(prs.slides)} slides)")
