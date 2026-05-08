"""Build the Free Label client pitch deck (.pptx). Features-only."""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pathlib import Path

INK         = RGBColor(0x2a, 0x25, 0x20)
MUTED       = RGBColor(0x8a, 0x7e, 0x72)
LINE        = RGBColor(0xe6, 0xdc, 0xd0)
BG          = RGBColor(0xf7, 0xf3, 0xed)
ACCENT      = RGBColor(0xc0, 0x8f, 0x7a)
ACCENT_DEEP = RGBColor(0x7a, 0x4d, 0x3d)
ACCENT_SOFT = RGBColor(0xf0, 0xdf, 0xd2)
GOLD        = RGBColor(0xc9, 0xa8, 0x5e)
GOLD_SOFT   = RGBColor(0xf3, 0xe8, 0xc7)
SAGE        = RGBColor(0x9b, 0xb0, 0xa0)
BLUSH       = RGBColor(0xd8, 0xa5, 0xa5)
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
             "Free Label · Mobile App Pitch", size=9, color=color)
    add_text(slide, Inches(11.7), Inches(7.05), Inches(1), Inches(0.3),
             f"{page} / {total}", size=9, color=color, align=PP_ALIGN.RIGHT)


def add_section_header(slide, eyebrow, title):
    add_text(slide, Inches(0.6), Inches(0.55), Inches(8), Inches(0.3),
             eyebrow.upper(), size=10, bold=True, color=ACCENT_DEEP)
    add_text(slide, Inches(0.6), Inches(0.85), Inches(12), Inches(1.0),
             title, font=SERIF, size=34, color=INK)
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                  Inches(0.6), Inches(1.85),
                                  Inches(0.7), Pt(2))
    line.fill.solid(); line.fill.fore_color.rgb = ACCENT
    line.line.fill.background()


slides_total = 23

# COVER
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
             "MOBILE APP · PITCH", size=11, bold=True, color=ACCENT_DEEP)
    add_text(s, Inches(0.85), Inches(1.45), Inches(8), Inches(2.0),
             "Free Label.", font=SERIF, size=66, color=INK)
    add_text(s, Inches(0.85), Inches(2.7), Inches(7.5), Inches(1.6),
             "The bra that\nfinally fits.",
             font=SERIF, size=28, color=ACCENT_DEEP)
    add_text(s, Inches(0.85), Inches(5.6), Inches(7.5), Inches(0.4),
             "Wire-free. Bamboo. Sized A to L. Made in Vancouver.",
             size=14, color=MUTED)
    add_text(s, Inches(0.85), Inches(6.0), Inches(7.5), Inches(0.3),
             "Prepared for the Free Label team",
             size=11, color=MUTED)
slide_cover()

# OPPORTUNITY
def slide_opportunity():
    s = add_slide()
    add_section_header(s, "Why now", "Wire-free is winning. Sizing it is still hard.")
    stats = [
        ("A–L", "cup sizes plus bands XS–5X.\nMost inclusive in category.",
         "Most customers under-size on first try. Fit AI fixes that."),
        ("220", "made per drop.\nReal demand, not predictions.",
         "Small-batch is the brand promise. The Drop pillar makes it visible."),
        ("100%", "cut and sewn in Vancouver\n+ Toronto",
         "Local production is the moat. Free size-swap is the customer trust."),
    ]
    x = Inches(0.6); y = Inches(2.4); w = Inches(4); gap = Inches(0.2)
    for i, (big, mid, small) in enumerate(stats):
        cx = x + (w + gap) * i
        add_rect(s, cx, y, w, Inches(4.0), fill=WHITE, line=LINE, corner=True)
        add_text(s, cx + Inches(0.4), y + Inches(0.4), w - Inches(0.8),
                 Inches(1.4), big, font=SERIF, size=58, color=ACCENT_DEEP)
        add_text(s, cx + Inches(0.4), y + Inches(1.7), w - Inches(0.8),
                 Inches(1.0), mid, size=14, bold=True, color=INK)
        add_text(s, cx + Inches(0.4), y + Inches(2.9), w - Inches(0.8),
                 Inches(1.0), small, size=12, color=MUTED)
    add_footer(s, 2, slides_total)
slide_opportunity()

# VISION
def slide_vision():
    s = add_slide()
    add_section_header(s, "The vision", "Not another store — a fit engine.")
    add_text(s, Inches(0.6), Inches(2.3), Inches(12), Inches(2.5),
             ("Free Label sells the bra most women buy wrong the first time "
              "— wire-free, elastic-free, made in Vancouver from bamboo, "
              "sized from A to L cup and up to 5X.\n\n"
              "The customer who finds her bra on the app is a customer "
              "for life. The Fit Finder gets her there before she returns "
              "the wrong size. The Wardrobe tracks how each piece felt. "
              "The Drop calendar respects the small-batch ethic. The "
              "Comfort Lab teaches care. Everything in service of the "
              "fit that finally works."),
             font=SERIF, size=20, color=INK)
    add_text(s, Inches(0.6), Inches(5.8), Inches(12), Inches(0.4),
             "WHY IT MATTERS", size=10, bold=True, color=ACCENT_DEEP)
    add_text(s, Inches(0.6), Inches(6.1), Inches(12), Inches(1.5),
             ("• Reduces returns — fit AI is worth more than any other feature dollar-for-dollar in this category\n"
              "• Surfaces the small-batch story honestly — production transparency without fake urgency\n"
              "• Makes free size-swap feel like a feature, not a cost — turns expected friction into trust"),
             size=13, color=INK)
    add_footer(s, 3, slides_total)
slide_vision()

# 4. SIX PILLARS
def slide_pillars():
    s = add_slide()
    add_section_header(s, "Product overview", "Six pillars — five customer-facing, one internal.")
    pillars = [
        ("The Fit Finder", "4-question guided flow. Per-style fit notes. \"Compare to a bra you own.\"", ACCENT),
        ("The Wardrobe", "Register every piece. \"Felt good\" / \"felt off\" log — not wear count.", BLUSH),
        ("The Drop", "Per-drop batch count visible. Production progress. Real, not fake urgency.", GOLD),
        ("The Comfort Lab", "Care videos for bamboo. Bra-fitting tips. Find-your-fit guarantee process.", SAGE),
        ("The Shop", "Multi-currency. Drop calendar. Notify-me on size-swap availability.", ACCENT_DEEP),
        ("The Studio", "Internal-facing web admin portal — Fit-Finder rules, drops, swaps, concierge.", INK),
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

# Phase features
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
              "Foundations: Fit Finder, Wardrobe, Drop, Comfort Lab, Shop, Free.",
              "Everything a customer needs in their first 90 days.", [
    ("Multilingual onboarding", "EN + FR at launch."),
    ("Multi-currency storefront", "CAD + USD."),
    ("Fit Finder · 4-question flow", "Cup feel · band feel · support level · neckline."),
    ("Per-style fit notes", "Andie, Carrie, and 6 more — each with visual fit guide."),
    ("\"Compare to a bra you own\"", "Anchor sizing to a brand the customer already wears."),
    ("Free size-swap", "Tied to loyalty wallet · 30-day window · default not perk."),
    ("Wardrobe · \"felt good\" log", "Quick tap, no shaming, no streaks."),
    ("Pair-with suggestions", "Matching bamboo sets are the cult product."),
    ("The Drop · batch count", "\"This drop is 220 Carrie bras.\" Real demand, not fake urgency."),
    ("Restock alerts", "Notify-me when sold-out drops re-batch."),
    ("Pre-order for cult favourites", "Andie pre-orders fund production."),
    ("Comfort Lab · care videos", "Bamboo wash + care · bra-fitting tips · with founder."),
    ("Lab chat (AI)", "Multilingual fit + fabric coach with size-swap baked in."),
    ("Visual search", "Photograph a bra, find it."),
    ("Wardrobe-gap analyser", "\"You have 3 Andies but no everyday Carrie.\""),
    ("The Studio (web admin)", "Fit-Finder rules, drops, batch tracker, swaps, concierge."),
])

feature_slide(6, slides_total, "Phase 2 · Depth (months 5–9)",
              "AR fit, body inclusivity expansion, B2B.",
              "Features that turn launch into the most-trusted fit experience in the category.", [
    ("AR fit visualisation", "See a bra silhouette on body proportions before you order."),
    ("Photo-based fit check", "Upload a mirror photo, get specific feedback (band, cup, strap)."),
    ("Plus-cup (G–L) confidence content", "Dedicated guidance for larger-cup customers."),
    ("Trans + nonbinary fit guidance", "Opt-in, sensitive content for binders, post-top-surgery."),
    ("Wholesale + boutique B2B portal", "Vancouver / Toronto boutique partners."),
    ("Heritage / archive sale", "Past-season cult favourites re-released."),
    ("Founder dispatches", "Jess short videos per drop."),
    ("Returns triage AI", "Fit-related vs damage-related routing."),
])

feature_slide(7, slides_total, "Phase 3 · Cultural authority (months 10+)",
              "From an app to the bra-fitting standard.",
              "Long-form storytelling, community, operational AI.", [
    ("Editorial / journal", "Long-form on bra fitting, body comfort, bamboo science."),
    ("Annual VOICES film series", "Real customers in their pieces, all body sizes."),
    ("Multilingual content scaling AI", "EN-first, AI drafts FR/ES/IT/JP for editor review."),
    ("Demand-sensing AI", "Wishlists + Drop signals feed small-batch production planning."),
    ("Counterfeit listing detection", "Amazon, eBay, Poshmark."),
    ("VIP signal detection", "Concierge welcomes top-loyal customers."),
    ("Long-term wear study", "Anonymised data on which bras last 3+ years."),
    ("Wholesale demand-sensing", "Boutique waitlist signal informs production allocation."),
])

# 8. ONBOARDING
def slide_onboarding():
    s = add_slide()
    add_section_header(s, "User experience", "Onboarding — under 90 seconds, in EN or FR.")
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.4),
             "The first screen earns trust by asking what feels good — not what looks slimming.",
             size=14, color=MUTED)
    steps = [
        ("01", "Bonjour", "Welcome in two languages.\nTap your language; everything follows."),
        ("02", "Sign in", "Apple, Google, or email.\nNo forms."),
        ("03", "Your fit profile", "Cup, band, body comfort\npreferences. Body shape opt-in."),
        ("04", "What you wear now", "What brands fit you well?\nAnchors the Fit Finder."),
        ("05", "First moment", "Run the Fit Finder for any bra —\nor browse the current drop."),
    ]
    x = Inches(0.6); y = Inches(2.9); w = Inches(2.3); h = Inches(3.6); gap = Inches(0.2)
    for i, (n, t, d) in enumerate(steps):
        cx = x + (w + gap) * i
        add_rect(s, cx, y, w, h, fill=WHITE, line=LINE, corner=True)
        add_text(s, cx + Inches(0.3), y + Inches(0.3), w - Inches(0.6),
                 Inches(0.5), n, font=SERIF, size=28, color=ACCENT_DEEP)
        add_text(s, cx + Inches(0.3), y + Inches(1.0), w - Inches(0.6),
                 Inches(0.5), t, size=14, bold=True, color=INK)
        add_text(s, cx + Inches(0.3), y + Inches(1.55), w - Inches(0.6),
                 Inches(2.0), d, size=11, color=MUTED)
        if i < len(steps) - 1:
            add_arrow(s, cx + w + Inches(0.01), y + Inches(1.6),
                      Inches(0.18), Inches(0.4), color=ACCENT)
    add_text(s, Inches(0.6), Inches(6.7), Inches(12), Inches(0.4),
             "DESIGN PRINCIPLE   —   Body shape is opt-in. Never weight or BMI. Never \"slimming\" language.",
             size=11, bold=True, color=ACCENT_DEEP)
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
    "First bra → cult customer.",
    "From a wired-bra refugee to a Free Label loyalist in two swaps.",
    [
        ("DISCOVER", "Sees the Andie",
         "Instagram. Saves the listing. Notes the A-L sizing range."),
        ("FIT FINDER", "Runs the 4-question flow",
         "Anchors to her current 36DD wired bra. AI: \"Try L cup, M band — drop one cup wire-free.\""),
        ("BUY", "Apple Pay checkout",
         "Two taps. Free size-swap noted at checkout — no anxiety."),
        ("SWAP", "Second size lands",
         "L was a touch tight in band. Swaps to L cup, L band — free, ships next day."),
        ("LOYAL", "Six months in",
         "4 Free Label bras. Wears nothing else. Refers two friends. Cult formed."),
    ])

journey_slide(10, slides_total,
    "User flow · 2 of 3",
    "Plus-cup customer (G–L) — the underserved category.",
    "Most brands fail plus-cup customers on confidence. Free Label's app makes that the strength.",
    [
        ("ARRIVE", "Looking for L cup",
         "Tired of brands that stop at H. Sees Free Label's L-cup range, cautiously interested."),
        ("EDUCATE", "Plus-cup confidence content",
         "Watches Sarah's video on larger-cup support. AI confirms wire-free works for her shape."),
        ("FIT FINDER", "Plus-cup specific flow",
         "Different question set. Surfaces the Andie's reinforced-band variant. Recommends trying L."),
        ("BUY", "First L-cup wire-free",
         "Skeptical but tries it. App pre-emptively offers swap window: \"Most plus-cup customers swap once. Expected.\""),
        ("LOYAL", "Cup-size advocate",
         "Becomes a power user. Posts a fit-look in the Tribe (Phase 2). Brand earns a hard-won segment."),
    ])

journey_slide(11, slides_total,
    "User flow · 3 of 3",
    "The Drop — small-batch transparency without fake urgency.",
    "The brand's small-batch story is real. The app surfaces it honestly.",
    [
        ("PLAN", "Drop scheduled",
         "Studio shows: \"220 Carrie bras, ships May 24.\" Customer sees real production count, not made-up scarcity."),
        ("LAUNCH", "Drop goes live",
         "Push: \"Carrie bras back in stock — 220 made.\" Calm, factual, never urgent."),
        ("PROGRESS", "Mid-drop transparency",
         "After 7 days: \"140 sold, 80 left.\" Customer makes informed decision, not pressured."),
        ("RESTOCK", "Sold-out flow",
         "Last unit goes. Customer joins waitlist. \"We restock when 200 customers ask. Currently at 142.\""),
        ("HONESTY", "Trust earned",
         "Customer knows the brand isn't faking scarcity to sell faster. Brand earns trust competitors can't fake."),
    ])

# 12. SCREENS
def slide_screens():
    s = add_slide()
    add_section_header(s, "Visual reference", "What it looks like in hand.")
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.4),
             "Wireframe-fidelity mockups in the brand palette — warm cream, terracotta, sage, blush.",
             size=14, color=MUTED)
    screens = [
        ("Onboarding", "EN/FR · sign-in"),
        ("Home", "Restock alert · drop"),
        ("Fit Finder", "4-question flow"),
        ("Product", "A-L sizing badge"),
        ("Wardrobe", "\"Felt good\" log"),
        ("The Drop", "Small-batch transparency"),
        ("Comfort Lab", "Care + fit videos"),
        ("Lab chat", "Multilingual fit AI"),
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
             size=10, color=ACCENT_DEEP)
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
                 font=SERIF, size=18, color=ACCENT_DEEP,
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
    "AI in service of the right fit, not the prettier silhouette.",
    "Every Tier 1 feature reduces returns or deepens trust.",
    [
        ("Lab chat (Sonnet)", "Multilingual fit + fabric coach. Past-order context. Free size-swap baked in."),
        ("Fit-Finder algorithm", "4-question flow + body comfort + brand anchor → recommended size."),
        ("Multilingual brand-voice translation", "EN-first; AI drafts FR; brand glossary preserves Andie, Carrie, Free."),
        ("Visual search", "Photograph a bra style — find it in catalog."),
        ("Wardrobe-gap analyser", "\"You have 3 Andies but no Carrie\" — recommends from your real wardrobe."),
        ("Restock prediction", "Waitlist + viewer interest signal feeds Drop scheduler — never fake urgency."),
    ])

ai_tier_slide(14, slides_total,
    "Intelligence · Tier 2 & 3",
    "AI that powers AR fit, photo fit-check, and the back office.",
    "Phase 2 customer-facing AI plus operational AI the customer never sees.",
    [
        ("AR fit visualisation", "Phone camera shows bra silhouette on body proportions."),
        ("Vision-based fit check", "Mirror photo → fit feedback (band, cup, strap)."),
        ("Plus-cup (G–L) AI confidence content", "Dedicated content generation for under-served segment."),
        ("Returns triage AI", "Fit-related vs damage-related routing."),
        ("Demand-sensing AI", "Wishlists + Drop signals feed small-batch planning."),
        ("Multilingual content scaling", "EN-first, AI drafts FR/ES/IT/JP, editors approve."),
        ("Counterfeit listing detection", "Amazon / eBay / Poshmark."),
        ("Trans + nonbinary fit AI guidance", "Phase 3 — opt-in, careful, brand-side review on every claim."),
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
        ("Fit profile", "cup, band, body comfort preferences."),
        ("Body shape (opt-in)", "for fit-finder accuracy — never required."),
        ("Language & region", "UI language, country, currency."),
        ("Wardrobe", "registered pieces, \"felt good\" logs, return reasons."),
        ("Brand anchor", "what you wear now — for fit-finder accuracy."),
        ("Engagement", "views, wishlists, restock alerts opted into."),
        ("Channel of origin", "online / Vancouver studio / boutique referral."),
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
             "WE DO NOT COLLECT  ·  weight or BMI  ·  before/after photos  ·  precise GPS  ·  contacts  ·  social-graph",
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
                       "Multi-currency CAD/USD",
                       "RevenueCat for any subscriptions"]),
        ("Fit + production backend", ["Node + TypeScript API",
                                        "Postgres + pgvector for visual search",
                                        "Fit-Finder rules · Drop tracker · swap workflow"]),
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
             "SHOPIFY", size=10, bold=True, color=ACCENT_DEEP)
    add_text(s, Inches(4.7), Inches(3.40), Inches(3.9), Inches(0.4),
             "Catalog · orders · payments — unchanged",
             size=11, color=MUTED)
    add_rect(s, Inches(0.6), Inches(4.2), Inches(12.1), Inches(0.7),
             fill=ACCENT_SOFT, corner=True)
    add_text(s, Inches(0.85), Inches(4.27), Inches(11.6), Inches(0.4),
             "SHARED API · Postgres · Auth · AI gateway · Fit-Finder rules · Drop tracker · Swap workflow",
             size=11, bold=True, color=ACCENT_DEEP,
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
             ("Customer-facing · Fit Finder · Wardrobe · Drop · Comfort Lab · Shop · Free"),
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
             ("Internal · Fit-Finder rules · drops · production tracker · swaps · Lab content · concierge"),
             size=11, color=INK)
    add_text(s, Inches(0.6), Inches(7.0), Inches(12), Inches(0.4),
             ("BUILT FOR YOUR TEAM   —   Jess + production ops + concierge. Bilingual EN/FR. Brand-palette UI."),
             size=10, bold=True, color=ACCENT_DEEP)
    add_footer(s, 17, slides_total)
slide_studio()

# 18. ROADMAP
def slide_roadmap():
    s = add_slide()
    add_section_header(s, "How we'll deliver", "Roadmap — first nine months.")
    phases = [
        ("Discovery", "Weeks 1–2",
         "Customer interviews — cult-fan with 6+ pieces, new buyer with first return, plus-cup G-L customer, trans/nonbinary customer using bra as binder, Vancouver-local. Audit fit-related return data. Lock Phase 1 scope."),
        ("Phase 1 build", "Weeks 3–16",
         "Fit Finder, Wardrobe, Drop, Comfort Lab, Shop, Free, Tier 1 AI, The Studio. EN/FR at launch."),
        ("Phase 2 build", "Weeks 17–30",
         "AR fit, vision fit-check, plus-cup confidence content, wholesale B2B, trans/nonbinary fit guidance."),
        ("Phase 3 build", "Weeks 31–40+",
         "Editorial, VOICES films, content scaling, demand sensing, counterfeit detection."),
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
                 Inches(0.4), when, size=10, bold=True, color=ACCENT_DEEP)
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
        ("Return rate · bras", "Returns / orders, app cohort vs control",
         "Target −30% on app cohort"),
        ("Fit Finder conversion", "% of users who buy after running the Fit Finder",
         "Target ≥ 70%"),
        ("Swap-to-keep ratio", "% of swaps that result in a kept piece (not a refund)",
         "Target ≥ 80%"),
        ("Wardrobe \"felt good\"", "Average \"felt good\" tags per registered piece",
         "Target ≥ 5 by month 9"),
        ("Drop sell-through", "% of drop sold before next batch",
         "Target ≥ 80% within 30 days"),
        ("Plus-cup share (G–L)", "% of customers in plus-cup range using app",
         "Target ≥ 25% by month 12"),
    ]
    cols = 3; cw = Inches(4.0); ch = Inches(2.0); gap = Inches(0.1)
    x0 = Inches(0.6); y0 = Inches(2.8)
    for i, (name, desc, target) in enumerate(metrics):
        c = i % cols; r = i // cols
        x = x0 + (cw + gap) * c
        y = y0 + (ch + gap) * r
        add_rect(s, x, y, cw, ch, fill=WHITE, line=LINE, corner=True)
        add_text(s, x + Inches(0.3), y + Inches(0.2), cw - Inches(0.6),
                 Inches(0.4), name, size=14, bold=True, color=ACCENT_DEEP)
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
        ("Comfort over compression",
         "Free Label is wire-free, elastic-free, body-first. Never \"slimming\" or \"flattering\" language."),
        ("Body shape is opt-in",
         "Never weight or BMI. Body comfort preferences only with explicit consent."),
        ("Real demand, not fake urgency",
         "The Drop shows real batch counts. No countdown timers, no fake \"only X left\" pressure."),
        ("Free swap is a feature",
         "Most customers find their fit on swap #2. The app makes that the expected path, not a failure."),
        ("Recognition over discounts",
         "Free tier rewards fit-finder use, reviews, referrals. Not new-buy bribes."),
        ("Inclusive by default",
         "A–L cup, 2X–5X, trans/nonbinary content. The default is welcome, not opt-in."),
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
                 name, size=14, bold=True, color=ACCENT_DEEP)
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
        ("Discovery sprint", "Two weeks. Customer interviews — cult-fan, new buyer with first return, plus-cup G-L customer, trans/nonbinary customer, Vancouver-local. Walk away with a signed Phase 1 spec."),
        ("Embedded delivery", "A small team — lead engineer, mobile engineer, designer, bilingual QA — works as an extension of yours. Weekly demos."),
        ("Brand-side approval", "Every customer-facing fit, care, or product claim reviewed by your editorial team. AI generates; humans approve."),
        ("Always your data", "Source code, customer data, AI logs, the Fit-Finder rules engine all live in your accounts."),
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
                 name, font=SERIF, size=20, color=ACCENT_DEEP)
        add_text(s, x + Inches(0.3), y + Inches(0.95),
                 cw - Inches(0.6), Inches(1.1),
                 desc, size=12, color=MUTED)
    add_footer(s, 21, slides_total)
slide_team()

# 22. WHY THIS WORKS
def slide_why():
    s = add_slide()
    add_section_header(s, "Why this works for Free Label", "The bet behind the build.")
    pts = [
        ("Fit AI pays for the rest of the app",
         "A 6-point return-rate drop on bras is real money. A Fit Finder that lands customers on the right size in 1–2 tries funds the entire build in year one."),
        ("Inclusivity is your moat",
         "A-L cup, up to 5X, trans/nonbinary content, plus-cup confidence. Most fast-fashion bra brands stop at H. Free Label wins the underserved 30% of the market."),
        ("Small-batch transparency builds trust competitors can't fake",
         "The Drop shows real batch counts and waitlist mechanics. Honest scarcity. The customer knows you're not gaming her."),
        ("AI in service of comfort, not body-shaping",
         "We use AI to recommend size, suggest fabric care, route swaps. Never to invent shapewear language. The brand's reputation is safer for the building."),
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
             ("We sit with your team in Vancouver. We talk to ten of your "
              "customers — cult-fan, plus-cup, first-time buyer, "
              "trans/nonbinary, repair customer. We audit the fit-related "
              "return data. We come back with a lockable Phase 1 scope "
              "and a working prototype of the Fit Finder and Drop flows "
              "in EN and FR."),
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

out = Path(__file__).parent / "Free-Label-Pitch.pptx"
prs.save(out)
print(f"wrote {out}  ({len(prs.slides)} slides)")
