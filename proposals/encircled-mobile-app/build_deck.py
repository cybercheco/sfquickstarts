"""Build the Encircled client pitch deck (.pptx). Features-only."""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pathlib import Path

INK         = RGBColor(0x2b, 0x2a, 0x26)
MUTED       = RGBColor(0x88, 0x83, 0x79)
LINE        = RGBColor(0xe6, 0xdf, 0xd3)
BG          = RGBColor(0xf4, 0xef, 0xea)
ACCENT      = RGBColor(0x5d, 0x6e, 0x54)
ACCENT_DEEP = RGBColor(0x36, 0x42, 0x2f)
ACCENT_SOFT = RGBColor(0xdf, 0xe5, 0xd6)
GOLD        = RGBColor(0xb8, 0x99, 0x68)
GOLD_SOFT   = RGBColor(0xec, 0xde, 0xc3)
TERRA       = RGBColor(0xb9, 0x6a, 0x4f)
PLUM        = RGBColor(0x6f, 0x4d, 0x62)
WHITE       = RGBColor(0xff, 0xff, 0xff)

SERIF = "Georgia"; SANS = "Calibri"

prs = Presentation()
prs.slide_width  = Inches(13.333); prs.slide_height = Inches(7.5)
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
        run.text = line; run.font.name = font
        run.font.size = Pt(size); run.font.bold = bold
        run.font.color.rgb = color
    return tb


def add_rect(slide, x, y, w, h, *, fill=WHITE, line=None, line_w=0.75, corner=False):
    shp = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE if corner else MSO_SHAPE.RECTANGLE, x, y, w, h)
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
             "Encircled · Mobile App Pitch", size=9, color=color)
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
    add_rect(s, Inches(8.5), 0, Inches(4.833), SH, fill=ACCENT_DEEP)
    add_rect(s, Inches(8.5), 0, Inches(4.833), Inches(2.0), fill=ACCENT)
    add_rect(s, Inches(8.5), 0, Inches(4.833), Inches(0.5), fill=GOLD)
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
             "Encircled.", font=SERIF, size=66, color=INK)
    add_text(s, Inches(0.85), Inches(2.7), Inches(7.5), Inches(1.6),
             "Fewer pieces.\nMore ways to wear them.",
             font=SERIF, size=28, color=ACCENT)
    add_text(s, Inches(0.85), Inches(5.6), Inches(7.5), Inches(0.4),
             "A transformation engine — multi-way styles, capsules, lifetime repair.",
             size=14, color=MUTED)
    add_text(s, Inches(0.85), Inches(6.0), Inches(7.5), Inches(0.3),
             "Prepared for the Encircled team",
             size=11, color=MUTED)

slide_cover()

# 2. OPPORTUNITY
def slide_opportunity():
    s = add_slide()
    add_section_header(s, "Why now", "Slow fashion has matured — and the apps haven't.")
    stats = [
        ("8", "documented styles in the Chrysalis Cardi —\nmost owners use 2 or 3",
         "The hidden value is already in the closet."),
        ("∞", "your lifetime repair guarantee\nis the strongest in the category",
         "Most customers don't know how to use it."),
        ("30km", "from the Toronto studio to every\nfactory you work with",
         "A real, audit-ready supply chain. The app makes that visible."),
    ]
    x = Inches(0.6); y = Inches(2.4); w = Inches(4); gap = Inches(0.2)
    for i, (big, mid, small) in enumerate(stats):
        cx = x + (w + gap) * i
        add_rect(s, cx, y, w, Inches(4.0), fill=WHITE, line=LINE, corner=True)
        add_text(s, cx + Inches(0.4), y + Inches(0.4), w - Inches(0.8),
                 Inches(1.4), big, font=SERIF, size=64, color=ACCENT)
        add_text(s, cx + Inches(0.4), y + Inches(1.7), w - Inches(0.8),
                 Inches(1.0), mid, size=14, bold=True, color=INK)
        add_text(s, cx + Inches(0.4), y + Inches(2.9), w - Inches(0.8),
                 Inches(1.0), small, size=12, color=MUTED)
    add_footer(s, 2, slides_total)

slide_opportunity()

# 3. VISION
def slide_vision():
    s = add_slide()
    add_section_header(s, "The vision", "Not another store — a transformation engine.")
    add_text(s, Inches(0.6), Inches(2.3), Inches(12), Inches(2.5),
             ("Encircled's promise is that every piece works harder than "
              "it looks: multi-way silhouettes, a lifetime repair guarantee, "
              "factories thirty kilometres from the studio.\n\n"
              "The app makes that promise visible. It teaches customers the "
              "styles they own without knowing it, builds capsules for their "
              "next trip, and turns the brand's \"guaranteed for life\" "
              "pledge into a one-tap workflow. The customer ends up owning "
              "fewer pieces, but wearing them more — exactly what the brand "
              "has been arguing since 2012."),
             font=SERIF, size=20, color=INK)
    add_text(s, Inches(0.6), Inches(5.8), Inches(12), Inches(0.4),
             "WHY IT MATTERS", size=10, bold=True, color=ACCENT)
    add_text(s, Inches(0.6), Inches(6.1), Inches(12), Inches(1.5),
             ("• Unlocks the brand's documented multi-way style library — most owners use 30% of it\n"
              "• Turns the lifetime repair guarantee from PDF policy into one-tap workflow\n"
              "• Captures the traveller customer with capsule planning that builds from owned pieces"),
             size=13, color=INK)
    add_footer(s, 3, slides_total)

slide_vision()

# 4. SIX PILLARS
def slide_pillars():
    s = add_slide()
    add_section_header(s, "Product overview", "Six pillars — five customer-facing, one internal.")
    pillars = [
        ("The Many", "Every piece, every way to wear it. The Chrysalis Cardi has 8 styles. The app teaches the rest.", ACCENT),
        ("The Capsule", "Trip planner that builds a packing capsule from your own closet.", GOLD),
        ("The Atelier", "Lifetime repair — scan a piece, photo the damage, get a free fix.", TERRA),
        ("The Wardrobe", "Register every piece. Cost-per-wear, multi-way unlocks, repair history.", PLUM),
        ("The Shop", "Slow drops, founder-narrated, multi-currency, bilingual EN/FR.", ACCENT_DEEP),
        ("The Studio", "Internal-facing web admin portal — multi-way library, repair queue, capsule templates, concierge.", INK),
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
              "Foundations: The Many, Capsule, Atelier, Wardrobe, Shop, Loops.",
              "Everything a customer needs in their first 90 days.", [
    ("Multilingual onboarding", "EN + FR at launch."),
    ("Multi-currency storefront", "CAD + USD; international shipping."),
    ("The Many · 8 ways per piece", "Per-piece style library, photo + 30-sec videos."),
    ("Style of the week push", "Surfaces a new way to wear pieces you already own."),
    ("The Capsule trip planner", "Destination + length + weather + dress code → capsule from your closet."),
    ("Pack-light score", "Weight, volume, outfit count per capsule."),
    ("The Atelier repair flow", "Scan → photo → quote → free pickup or mail-in."),
    ("AI repair triage (basic)", "Vision classification routes between DIY guide and atelier work."),
    ("The Wardrobe", "Register every piece, log wears, see cost-per-wear."),
    ("Multi-way unlock tracking", "Show 3 of 8 styles unlocked per piece, encourage exploration."),
    ("Founder-narrated drops", "Kristi short videos per collection."),
    ("Loops loyalty", "Recognition for long-term ownership; not bribery for new buys."),
    ("Multi-way styler chat (AI)", "Recognise a piece from photo, walk through documented styles."),
    ("Capsule builder AI", "Auto-build trip capsules from owned pieces."),
    ("Atelier care + fit chat (AI)", "Multilingual EN/FR with past-order context."),
    ("The Studio (web admin)", "Multi-way library, repair queue, capsule templates, concierge, analytics."),
])

feature_slide(6, slides_total, "Phase 2 · Depth (months 5–9)",
              "AR multi-way, photo fit-check, wholesale.",
              "Features that turn launch into a category-defining experience.", [
    ("AR multi-way preview", "See a Chrysalis Cardi style on a body silhouette before you try it."),
    ("Photo-based fit check", "Upload a mirror photo, get fit feedback."),
    ("Photo-based repair triage (advanced)", "Vision AI classifies wear/damage, returns DIY or atelier quote."),
    ("Wholesale + travel-retail portal", "MEC, Away, hotel-shops with B2B + SSO."),
    ("Heritage / archive sale", "Past-season Chrysalis variants re-released."),
    ("Multi-traveler capsules", "Co-edit a packing capsule with a partner."),
    ("Founder dispatches", "Kristi short videos tied to drops and milestones."),
    ("Returns triage AI", "Fit-related vs damage-related routing."),
])

feature_slide(7, slides_total, "Phase 3 · Cultural authority (months 10+)",
              "From an app to a slow-fashion movement.",
              "Long-form storytelling, community, operational AI.", [
    ("Editorial / journal", "Long-form on multi-way design, slow fashion, travel."),
    ("Annual VOICES film series", "Short docs on long-life ownership — 10+ year customers."),
    ("Multilingual content scaling AI", "EN-first, AI drafts FR/ES/IT for editor review."),
    ("Demand-sensing AI", "Wishlists + capsule data feeds small-collection planning."),
    ("Counterfeit-listing detection", "Amazon, Poshmark, eBay."),
    ("VIP signal detection", "Surfaces customers about to hit Loops top tier."),
    ("Long-term wear study", "Anonymised aggregate on pieces worn 5+ years."),
    ("Multi-way library AI extension", "AI proposes new style #9 for human review on legacy pieces."),
])

# 8. ONBOARDING
def slide_onboarding():
    s = add_slide()
    add_section_header(s, "User experience", "Onboarding — under 90 seconds, in EN or FR.")
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.4),
             "The first screen earns trust by asking what travel and life look like — not what you weigh.",
             size=14, color=MUTED)
    steps = [
        ("01", "Bonjour", "Welcome in two languages.\nTap your language; everything follows."),
        ("02", "Sign in", "Apple, Google, or email.\nNo forms."),
        ("03", "Travel style", "Trip frequency, common destinations,\npacking preferences. All optional."),
        ("04", "Sizes", "Pull from past Shopify orders\nor 4 quick taps. No body shape required."),
        ("05", "First moment", "See today's style of the week,\nor scan a piece you own."),
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
             "DESIGN PRINCIPLE   —   Never collect weight, BMI, or body shape without explicit opt-in.",
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
    "Unlocking the Chrysalis — owner of 2 years, still discovering.",
    "Most Chrysalis Cardi owners use 2 or 3 of the 8 styles. The app changes that ratio.",
    [
        ("OWN", "Two years in",
         "Madeleine has worn her Chrysalis Cardi as a cardigan and a wrap top. The other six styles are theoretical."),
        ("DISCOVER", "Style of the week push",
         "Saturday morning push: \"Try the Halter Dress this week. 30 seconds to learn.\""),
        ("LEARN", "Watch the how-to",
         "30-sec video. The 6 hidden snaps make sense for the first time. She tries it in the bedroom."),
        ("CAPSULE", "Lisbon trip planning",
         "Builds her trip capsule. The Halter Dress unlocks an evening outfit she didn't know she had."),
        ("LOOP", "Posts the look",
         "After Lisbon she posts a Tribe look. Style #5 becomes her favourite. She replaces a fast-fashion dress with what she already owned."),
    ])

journey_slide(10, slides_total,
    "User flow · 2 of 3",
    "Lifetime repair — turning a PDF policy into a one-tap workflow.",
    "Most lifetime guarantees fail because customers don't use them. The Atelier flow makes them use them.",
    [
        ("DAMAGE", "Seam separation",
         "Sarah's Chrysalis Cardi seam splits after 4 years. Old answer: assume it's the end."),
        ("SCAN", "Opens The Atelier",
         "Scans the QR. Photo the seam. AI: \"In-house repair, 7-day turnaround, $0 — covered by lifetime guarantee.\""),
        ("BOOK", "Free pickup or mail-in",
         "Toronto pickup booked for Tuesday. Sarah does nothing else."),
        ("REPAIR", "In-house atelier",
         "30km from the studio, an Encircled tailor fixes the seam. Photo update sent to Sarah."),
        ("RETURN", "Wear count resumes",
         "Repaired piece logged in The Wardrobe. Cost-per-wear drops further. Sarah trusts the brand more than before the damage."),
    ])

journey_slide(11, slides_total,
    "User flow · 3 of 3",
    "The traveler — packing for a 6-day Lisbon trip in 4 pieces.",
    "Encircled's traveler customer wants to pack light. The Capsule flow is the most useful feature in her phone.",
    [
        ("INPUT", "Trip details",
         "Lisbon · 6 days · mid-November · mild · mix of beach and dinner."),
        ("BUILD", "AI capsule from her closet",
         "4 pieces selected from her 11-piece wardrobe. 11 outfit combinations. Pack-light score: 92/100."),
        ("REVIEW", "Swap one piece",
         "Wants the Wide-leg Pant in black instead of sage. App rebalances; outfit count drops to 9. She accepts."),
        ("PACK", "Save and share",
         "Saves \"Lisbon mild · 6d\" capsule. Shares with her mother who's joining the trip."),
        ("WEAR", "Daily outfit suggestion",
         "Each morning in Lisbon, app suggests the day's outfit based on weather. Same Chrysalis Cardi worn 3 different ways across 6 days."),
    ])

# 12. SCREENS
def slide_screens():
    s = add_slide()
    add_section_header(s, "Visual reference", "What it looks like in hand.")
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.4),
             "Wireframe-fidelity mockups in the brand palette — warm cream, sage, caramel, terracotta.",
             size=14, color=MUTED)
    screens = [
        ("Onboarding", "EN/FR · sign-in"),
        ("Home", "Style of the week + drops"),
        ("The Many", "8 ways to wear"),
        ("Wardrobe", "Multi-way unlocks · CPW"),
        ("Product", "8 ways · lifetime repair"),
        ("Capsule", "Trip-built outfit set"),
        ("Atelier", "Repair flow"),
        ("Atelier chat", "Multilingual fit + style"),
        ("Profile", "Data · privacy"),
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
    "AI in service of multi-way design and lifetime repair.",
    "Every Tier 1 feature unlocks value the customer already paid for.",
    [
        ("Multi-way styler chat", "Recognise a piece from photo, walk through the brand's documented styles."),
        ("Capsule builder", "Destination + length + weather → capsule from owned pieces with pack-light score."),
        ("Atelier care + fit chat", "Multilingual EN/FR with past-order context."),
        ("Repair triage (basic)", "Vision classification routes DIY vs atelier."),
        ("Multilingual brand-voice translation", "EN-first; Claude drafts FR; brand glossary preserves Chrysalis, Atelier, Loops."),
        ("Wardrobe-gap analyser", "\"You're missing a black wide-leg for travel\" — recommends from your real wardrobe."),
    ])

# 14. AI Tier 2 + 3
ai_tier_slide(14, slides_total,
    "Intelligence · Tier 2 & 3",
    "AI that powers AR, repair triage, and the back office.",
    "Phase 2 customer-facing AI plus operational AI the customer never sees.",
    [
        ("AR multi-way preview", "Phone camera shows a Chrysalis style on a body silhouette."),
        ("Vision-based fit check", "Mirror photo → fit feedback (waistband, length, drape)."),
        ("Photo-based repair triage (advanced)", "Damage classifier returns DIY guide or atelier quote with turnaround estimate."),
        ("Returns triage", "Fit-related vs damage-related routing."),
        ("Demand-sensing AI", "Wishlists + capsule signals feed small-collection planning."),
        ("Multilingual content scaling", "EN-first, AI drafts FR/ES/IT/JP; editors approve."),
        ("Multi-way library AI extension", "AI proposes potential new styles for legacy pieces; founder review only."),
        ("Counterfeit listing detection", "Amazon / Poshmark / eBay."),
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
        ("Fit profile", "sizes, fit notes (body shape opt-in)."),
        ("Language & region", "UI language, country, currency."),
        ("Travel style", "trip frequency, destinations, packing preferences."),
        ("Wardrobe", "registered pieces, wear count, multi-way unlocks, repair history."),
        ("Motivation tags", "sustainability / capsule / travel / lifetime-design."),
        ("Engagement", "views, wishlists, push response."),
        ("Channel of origin", "online / Toronto studio / referral."),
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
                       "Multi-currency CAD/USD/intl",
                       "RevenueCat for any subscriptions"]),
        ("Multi-way + repair backend", ["Node + TypeScript API",
                                          "Postgres + pgvector",
                                          "Multi-way library, repair queue, capsule store"]),
        ("Intelligence", ["Claude (Sonnet 4.6 chat, Haiku 4.5 batch)",
                           "Embeddings for visual search",
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

# 17. STUDIO
def slide_studio():
    s = add_slide()
    add_section_header(s, "The Studio · web admin portal",
                       "The internal twin of the mobile app.")
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.8),
             ("Customers use the mobile app. Your team uses The Studio. "
              "Same backend, same brand language — different surface for "
              "different users."),
             size=14, color=MUTED)
    add_rect(s, Inches(4.5), Inches(3.0), Inches(4.3), Inches(0.85),
             fill=WHITE, line=LINE, corner=True)
    add_text(s, Inches(4.7), Inches(3.05), Inches(3.9), Inches(0.4),
             "SHOPIFY", size=10, bold=True, color=ACCENT)
    add_text(s, Inches(4.7), Inches(3.40), Inches(3.9), Inches(0.4),
             "Catalog · orders · payments — unchanged",
             size=11, color=MUTED)
    add_rect(s, Inches(0.6), Inches(4.2), Inches(12.1), Inches(0.7),
             fill=ACCENT_SOFT, corner=True)
    add_text(s, Inches(0.85), Inches(4.27), Inches(11.6), Inches(0.4),
             "SHARED API · Postgres · Auth · AI gateway · Multi-way library · Repair ops · Capsule store",
             size=11, bold=True, color=ACCENT,
             anchor=MSO_ANCHOR.MIDDLE)
    add_rect(s, Inches(0.6), Inches(5.2), Inches(5.95), Inches(1.6),
             fill=WHITE, line=LINE, corner=True)
    add_rect(s, Inches(0.6), Inches(5.2), Inches(5.95), Inches(0.4),
             fill=ACCENT, corner=True)
    add_text(s, Inches(0.85), Inches(5.22), Inches(5.45), Inches(0.4),
             "MOBILE APP — IOS & ANDROID",
             size=10, bold=True, color=WHITE,
             anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(0.85), Inches(5.7), Inches(5.45), Inches(1.0),
             ("Customer-facing · The Many · Capsule · Atelier · Wardrobe · Shop · Loops"),
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
             ("Internal · Multi-way library editor · repair queue · capsule templates · concierge · drop scheduler · analytics"),
             size=11, color=INK)
    add_text(s, Inches(0.6), Inches(7.0), Inches(12), Inches(0.4),
             ("BUILT FOR YOUR TEAM   —   editors, repair ops, founder, concierge. "
              "Bilingual EN/FR. Brand-palette UI."),
             size=10, bold=True, color=ACCENT)
    add_footer(s, 17, slides_total)

slide_studio()

# 18. ROADMAP
def slide_roadmap():
    s = add_slide()
    add_section_header(s, "How we'll deliver", "Roadmap — first nine months.")
    phases = [
        ("Discovery", "Weeks 1–2",
         "Customer interviews (Toronto local, US frequent-traveller, long-time owner, repair customer, new buyer). Audit existing repair + multi-way data. Lock Phase 1 scope."),
        ("Phase 1 build", "Weeks 3–16",
         "The Many, Capsule, Atelier, Wardrobe, Shop, Loops, Tier 1 AI, The Studio. EN/FR at launch."),
        ("Phase 2 build", "Weeks 17–32",
         "AR multi-way, vision fit-check, advanced repair triage, wholesale portal."),
        ("Phase 3 build", "Weeks 33–40+",
         "Editorial, VOICES films, content-scaling AI, demand-sensing, counterfeit detection."),
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
        ("Multi-way unlock rate", "Average styles unlocked per piece (vs 8 documented)",
         "Target ≥ 5 of 8 by month 12"),
        ("Repair conversion", "% of repair-triaged tickets converted to DIY or paid repair",
         "Target ≥ 75%"),
        ("Capsule adoption", "% of users who build a capsule in their first 90d",
         "Target ≥ 40% by month 9"),
        ("Cost-per-wear distribution", "Median CPW for app users vs non-app cohort",
         "Target 30% lower for app cohort"),
        ("Repeat rate", "% of app users placing 2nd order within 90d",
         "Target +25% vs non-app cohort"),
        ("Bilingual reach", "% of sessions in FR",
         "Target ≥ 18% by month 12"),
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
        ("Calm, not loud",
         "Slow fashion deserves a slow interface. No streaks, no FOMO, no urgency design."),
        ("Body data is opt-in",
         "Never weight or BMI. Body shape only with explicit consent."),
        ("Multi-way is the brand",
         "AI never invents new styles for live pieces — only proposes for human review."),
        ("Lifetime repair is one tap",
         "If it takes more than four screens to request a repair, we've failed."),
        ("Recognition over discounts",
         "Loops reward long-term ownership and repair use. Not bribes for new buys."),
        ("Bilingual by default",
         "EN and FR are equals. Translation is brand-aware, never literal."),
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
        ("Discovery sprint", "Two weeks. Customer interviews — Toronto local, US frequent-traveller, long-time owner, repair customer, new buyer. Walk away with a signed Phase 1 spec — even if you don't build with us."),
        ("Embedded delivery", "A small team — lead engineer, mobile engineer, designer, bilingual QA — works as an extension of yours. Weekly demos."),
        ("Brand-side approval", "Every customer-facing styling, care, and repair claim reviewed by your editorial team. AI generates; humans approve."),
        ("Always your data", "Source code, customer data, AI logs, multi-way library all live in your accounts."),
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
    add_section_header(s, "Why this works for Encircled", "The bet behind the build.")
    pts = [
        ("Multi-way is your moat",
         "No fast-fashion brand can answer the question 'how do I wear this in 8 ways?' — and they can't fake it. The Many makes Encircled's documented IP usable."),
        ("Lifetime repair pays for the rest",
         "A repair workflow that customers actually use raises NPS, raises repeat rate, and gives you the longest LTV in the category. The Atelier flow is the value."),
        ("Capsule turns travelers into evangelists",
         "Encircled's traveler customer wants to pack light. The Capsule feature does the work for her. She tells her friends."),
        ("AI in service of design, not replacement",
         "AI helps customers find the right size, the right style, the right repair. It never invents new multi-way styles for live pieces. The brand's design IP is safer for the building."),
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
    add_rect(s, 0, 0, SW, SH, fill=ACCENT_DEEP)
    add_rect(s, 0, 0, SW, Inches(0.25), fill=GOLD)
    for cx, cy, r in [(11.0, 1.4, 0.20), (12.4, 3.0, 0.14),
                       (10.4, 4.2, 0.22), (12.0, 5.6, 0.16),
                       (11.2, 6.4, 0.12)]:
        d = s.shapes.add_shape(MSO_SHAPE.OVAL,
                               Inches(cx-r), Inches(cy-r),
                               Inches(2*r), Inches(2*r))
        d.fill.solid(); d.fill.fore_color.rgb = GOLD
        d.line.fill.background(); d.shadow.inherit = False
    add_text(s, Inches(0.6), Inches(0.55), Inches(8), Inches(0.3),
             "NEXT STEP", size=11, bold=True, color=GOLD)
    add_text(s, Inches(0.6), Inches(1.1), Inches(11), Inches(2.0),
             "A two-week paid discovery.",
             font=SERIF, size=54, color=WHITE)
    add_text(s, Inches(0.6), Inches(2.7), Inches(10.5), Inches(2.0),
             ("We sit with your team in Toronto. We talk to ten of your "
              "customers — the long-time Chrysalis owner, the frequent "
              "traveller, the repair user, the new buyer. We audit the "
              "existing multi-way library and repair-ledger feed. We come "
              "back with a lockable Phase 1 scope and a working prototype "
              "of the Multi-way and Repair flows in EN and FR."),
             size=18, color=GOLD_SOFT)
    add_text(s, Inches(0.6), Inches(5.1), Inches(11), Inches(0.5),
             "WHAT YOU GET", size=11, bold=True, color=GOLD)
    add_text(s, Inches(0.6), Inches(5.5), Inches(11), Inches(2.0),
             ("•  A lockable feature scope, costed and timeboxed\n"
              "•  An interactive prototype of two core flows\n"
              "•  A summary of customer interviews and what we heard\n"
              "•  A go / no-go recommendation. Yours either way."),
             size=14, color=WHITE)
    add_footer(s, 23, slides_total, on_dark=True)

slide_next()

out = Path(__file__).parent / "Encircled-Pitch.pptx"
prs.save(out)
print(f"wrote {out}  ({len(prs.slides)} slides)")
