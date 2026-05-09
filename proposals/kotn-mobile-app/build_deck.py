"""Build the Kotn client pitch deck (.pptx). Features-only."""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pathlib import Path

INK         = RGBColor(0x1d, 0x2a, 0x3a)
MUTED       = RGBColor(0x7a, 0x75, 0x69)
LINE        = RGBColor(0xe2, 0xdc, 0xcd)
BG          = RGBColor(0xf4, 0xf1, 0xea)
ACCENT      = RGBColor(0x2f, 0x5a, 0x78)
ACCENT_DEEP = RGBColor(0x14, 0x32, 0x47)
ACCENT_SOFT = RGBColor(0xd6, 0xe3, 0xed)
GOLD        = RGBColor(0xc8, 0x98, 0x68)
GOLD_SOFT   = RGBColor(0xf0, 0xe0, 0xc7)
GREEN       = RGBColor(0x6b, 0x8e, 0x63)
TERRA       = RGBColor(0xb8, 0x64, 0x2a)
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
             "Kotn · Mobile App Pitch", size=9, color=color)
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
             "Kotn.", font=SERIF, size=72, color=INK)
    add_text(s, Inches(0.85), Inches(2.7), Inches(7.5), Inches(1.6),
             "From the Nile,\nto your wardrobe.",
             font=SERIF, size=28, color=ACCENT)
    add_text(s, Inches(0.85), Inches(5.6), Inches(7.5), Inches(0.4),
             "A thread between the customer and the people who made what she wears.",
             size=14, color=MUTED)
    add_text(s, Inches(0.85), Inches(6.0), Inches(7.5), Inches(0.3),
             "Prepared for the Kotn team",
             size=11, color=MUTED)

slide_cover()

# 2. OPPORTUNITY
def slide_opportunity():
    s = add_slide()
    add_section_header(s, "Why now", "Sustainable essentials are now expected to prove themselves.")
    stats = [
        ("100%", "of Kotn cotton is direct-trade,\ntraceable from farm to hanger",
         "No competitor in the category can say this."),
        ("15", "primary schools funded\nin Egyptian farming villages",
         "A real, audited social outcome — not a marketing claim."),
        ("8", "stores across Toronto, Montréal,\nVancouver, Calgary, NYC, LA",
         "Each is a community. The app is what links them."),
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
    add_section_header(s, "The vision", "Not another store — a thread to the people who made it.")
    add_text(s, Inches(0.6), Inches(2.3), Inches(12), Inches(2.5),
             ("Kotn's product is essential clothing in 100% Egyptian cotton; "
              "the brand's moat is that every step from cotton boll to hanger "
              "is traceable, and every purchase funds a measurable social "
              "outcome.\n\n"
              "Most of that story is lost in a checkout flow. The app surfaces "
              "it — calmly, honestly, without guilt-tripping — and turns the "
              "buyer of a t-shirt into the ally of a community."),
             font=SERIF, size=20, color=INK)
    add_text(s, Inches(0.6), Inches(5.8), Inches(12), Inches(0.4),
             "WHY IT MATTERS", size=10, bold=True, color=ACCENT)
    add_text(s, Inches(0.6), Inches(6.1), Inches(12), Inches(1.5),
             ("• Surfaces the brand's strongest moat — verifiable provenance — at the moment of use\n"
              "• Turns the customer into a long-term ally, not a one-time buyer\n"
              "• Builds the audit-ready impact ledger the brand already has — and lets it travel"),
             size=13, color=INK)
    add_footer(s, 3, slides_total)

slide_vision()

# 4. SIX PILLARS
def slide_pillars():
    s = add_slide()
    add_section_header(s, "Product overview", "Six pillars — five customer-facing, one internal.")
    pillars = [
        ("The Origin", "Every piece scannable to its full provenance ledger — farm, mill, maker, citations.", ACCENT),
        ("The Wardrobe", "Register every piece. Cost-per-wear. Outfit grid. Slow-fashion bedrock.", GREEN),
        ("The Atelier", "Care, repair, mending kits. Make it last.", TERRA),
        ("The Field", "Personal impact. Schools funded. Dispatches from the Delta.", GOLD),
        ("The Shop", "Calm, multi-region, drop-aware. Store-event push.", ACCENT_DEEP),
        ("The Studio", "Internal-facing web admin portal — origin editor, education ledger, concierge.", INK),
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
              "Foundations: Origin, Wardrobe, Atelier, Field, Shop, Threads.",
              "Everything a customer needs to feel the brand's story in their first 90 days.", [
    ("Multilingual onboarding", "EN + FR at launch · AR / GB / EU expandable."),
    ("Multi-region storefront", "CA · US · UK · EU. Currency follows the customer."),
    ("The Origin passport", "Scan QR/NFC tag — farm, mill, maker, citation links."),
    ("Maker audio (90-sec)", "Voiced by the farmer or sewer, AR with EN/FR subtitles."),
    ("The Wardrobe", "Register every piece, see cost-per-wear, build outfits."),
    ("The Atelier", "Care guides, repair videos, order mending kits, book repair drop-off."),
    ("The Field", "Personal impact summary — schools funded, days of education."),
    ("Maker dispatches", "Curator-approved, opt-in stories from the Nile Delta."),
    ("Annual transparency report", "Citation-linked, exportable as PDF."),
    ("Drops + restock alerts", "Region-aware push notifications."),
    ("Store-event push", "Block parties, mending workshops, supplier visits."),
    ("Threads loyalty", "Recognition, not bribery — points for registering pieces, store visits."),
    ("Origin summary AI", "Claude drafts passport stories; editors approve before publish."),
    ("Atelier care + fit chat", "Multilingual, past-order context."),
    ("Wardrobe-gap analyser", "\"You're missing a true-white tee.\""),
    ("The Studio (web admin)", "Origin editor, education ledger, drop scheduler, concierge, analytics."),
])

feature_slide(6, slides_total, "Phase 2 · Depth (months 5–9)",
              "AR provenance, repair triage, in-store at scale.",
              "Features that turn the launch into a category-defining brand experience.", [
    ("AR provenance overlay", "Point camera at piece, see origin region overlaid on the garment."),
    ("Photo-based repair triage", "Vision AI classifies wear/damage, returns DIY guide or atelier quote."),
    ("In-store events at scale", "Mending workshops, cotton-tasting, livestreamed supplier visits."),
    ("Heritage / archive sale", "Past-season pieces re-released with full provenance."),
    ("Wholesale / corporate gifting portal", "Bulk orders, hotel partners, B2B with SSO."),
    ("Maker-direct video Q&A", "Quarterly live sessions from the Delta · EN/FR/AR."),
    ("Returns triage AI", "Fit-related vs damage-related routing; reduces handling cost."),
    ("Demand-sensing AI", "Wishlists + waitlists + cultural calendar feed planting plans."),
])

feature_slide(7, slides_total, "Phase 3 · Cultural authority (months 10+)",
              "From an app to a movement.",
              "Long-form storytelling, community, operational AI.", [
    ("Editorial / journal", "Long-form on slow fashion, supply chain, education."),
    ("Annual VOICES film series", "Short docs from the field — farmers, makers, school kids."),
    ("Multilingual content scaling AI", "EN-first, AI drafts FR/AR/ES/IT for editor review."),
    ("Counterfeit listing detection", "Amazon, eBay, Asian marketplaces."),
    ("VIP signal detection", "Concierge welcomes high-value supporters early."),
    ("School-impact narrative AI", "Auto-builds annual letter to customers from real ledger data."),
    ("Maker-community marketplace", "Direct-from-the-source small-batch craft, audited."),
    ("Carbon-tariff readiness", "Audit-ready data export for EU CBAM and similar regulations."),
])

# 8. ONBOARDING
def slide_onboarding():
    s = add_slide()
    add_section_header(s, "User experience", "Onboarding — under 90 seconds, in any language.")
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.4),
             "The first screen earns trust by asking what the customer cares about — not what they look like.",
             size=14, color=MUTED)
    steps = [
        ("01", "Bonjour", "Welcome in four languages.\nTap your language; everything follows."),
        ("02", "Sign in", "Apple, Google, or email.\nNo forms."),
        ("03", "What matters?", "Sustainability · craft · minimalism\n· supply chain · maker stories."),
        ("04", "Sizes", "Pull from past Shopify orders\nor 4 quick taps. No body shape required."),
        ("05", "First moment", "Scan a piece you own —\nor see your impact this year."),
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
             "DESIGN PRINCIPLE   —   Earn trust by asking what matters before asking who you are.",
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
    "First purchase → ally of the community.",
    "From a curious tap on Instagram to a customer who knows the names of the people who made what she wears.",
    [
        ("DISCOVER", "Sees a maker dispatch",
         "Instagram post: Mahmoud Soliman talks about the harvest. She taps in. Saves a Field Tee."),
        ("DECIDE", "Asks the Atelier",
         "AI uses past order context. Recommends size S in regular fit. Confidence builds."),
        ("BUY", "Apple Pay checkout",
         "Two taps. Order tracked in-app. Confirmation says: \"3.2 days of school funded by this order.\""),
        ("UNBOX", "Scans the QR tag",
         "One scan opens The Origin — the Soliman farm, the Mahalla mill, the Cairo collective. 90-sec audio in Mahmoud's voice."),
        ("ALLY", "Watches the impact grow",
         "Three months in: 14 pieces in wardrobe, 47 days of school funded, first dispatch from the Cairo collective lands in The Field."),
    ])

journey_slide(10, slides_total,
    "User flow · 2 of 3",
    "Make it last — care, repair, return to wear.",
    "The opposite of fast fashion: the app celebrates the seam-fix, the patina, the cost-per-wear.",
    [
        ("WEAR", "Logs each wear",
         "Quick tap when she puts on the Field Tee. Wear count grows; cost-per-wear visible in the Wardrobe."),
        ("DAMAGE", "A small hole",
         "Snags on a chair. Opens The Atelier, films the damage. Vision AI: \"DIY guide, 4-min repair.\""),
        ("REPAIR", "Orders a kit",
         "Mending kit · cotton · CA$18 or 200 Threads. Brief explains the technique. Arrives in 3 days."),
        ("FIX", "Watches the video",
         "Soha from the Cairo collective demonstrates the stitch. The customer learns a craft she didn't know she wanted."),
        ("RETURN TO WEAR", "Logs the repair",
         "Repaired piece flagged in the Wardrobe. Cost-per-wear drops further. The app says: \"Made better, enjoyed longer.\""),
    ])

journey_slide(11, slides_total,
    "User flow · 3 of 3",
    "The transparency-conscious customer's husband.",
    "Some customers buy because their partner pushes back. The app gives them the receipts.",
    [
        ("TRIGGER", "\"Are you sure?\"",
         "Anaïs's husband questions the provenance claims on her new linen shirt. Reasonable scepticism."),
        ("SHOW", "Opens The Origin",
         "Scans the tag. Full ledger appears — farm, mill, collective, with audit citations. He clicks the BSCI audit link."),
        ("VERIFY", "Audit document loads",
         "Q3 2025 BSCI audit · score A · maker living wage confirmed. \"OK.\""),
        ("CONVERT", "Asks the Atelier",
         "Five minutes later he's asking Atelier about a Crew Sweat for himself. Concierge gets a +1 quietly added."),
        ("BUY", "Becomes a customer",
         "Two months later he owns three pieces. The customer he was sceptical of is now the customer who told him about the brand."),
    ])

# 12. SCREENS
def slide_screens():
    s = add_slide()
    add_section_header(s, "Visual reference", "What it looks like in hand.")
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.4),
             "Wireframe-fidelity mockups in the brand palette — unbleached cotton, Nile blue, sand, harvest green.",
             size=14, color=MUTED)
    screens = [
        ("Onboarding", "4 languages · sign-in"),
        ("Home", "Personal impact · drops"),
        ("Origin", "Provenance ledger"),
        ("Wardrobe", "Cost-per-wear"),
        ("Product", "Origin pills · ask AI"),
        ("Atelier", "Care · repair · kits"),
        ("The Field", "Impact · dispatches"),
        ("Atelier chat", "Multilingual fit + care"),
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
    "AI in service of the story — never replacing it.",
    "Every Tier 1 feature deepens trust. None invents provenance.",
    [
        ("Origin summary AI", "Claude drafts the per-piece passport story from real ledger data; editors approve before publish."),
        ("Atelier chat (fit + care)", "Multilingual conversational guide. Past-order context + fabric care library."),
        ("Multilingual brand-voice translation", "EN-first, Claude drafts FR/AR/ES; brand glossary preserves Kotn, Threads, Atelier."),
        ("Visual search", "Photograph any piece — find related products and their full origin."),
        ("Wardrobe-gap analyser", "\"You wear neutrals; you're missing a true-white tee.\" Recommends from your real wardrobe."),
        ("Care + repair recommender", "Stain rescue, hole patch, hem fray — DIY guide or atelier booking."),
    ])

# 14. AI Tier 2 + 3
ai_tier_slide(14, slides_total,
    "Intelligence · Tier 2 & 3",
    "AI that powers the loop and the back office.",
    "Phase 2 customer-facing AI plus operational AI the customer never sees.",
    [
        ("AR provenance overlay", "Phone camera reveals farm region, mill, maker on the piece. Native modules required."),
        ("Photo-based repair triage", "Vision AI classifies damage, returns instant DIY or atelier quote."),
        ("Returns triage", "Fit-related vs damage-related routing — reduces handling cost and turnaround."),
        ("Demand-sensing AI", "Wishlists + waitlists feed Egyptian-grower planting plans."),
        ("Multilingual content scaling", "EN-first, AI drafts FR/AR/ES/IT/JP; editors approve. 5× the editorial output."),
        ("School-impact narrative AI", "Auto-builds annual customer letter from real ledger data."),
        ("Counterfeit listing detection", "Scans Amazon / eBay / Asian marketplaces for suspected fakes."),
        ("VIP signal detection", "Surfaces customers about to hit Threads' top tier so concierge can welcome them."),
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
        ("Wardrobe", "registered pieces, wear count, repair history."),
        ("Care preferences", "fabric, repair vs replace, store visits."),
        ("Motivation tags", "sustainability / craft / minimalism / supply chain."),
        ("Maker-story consent", "opt-in to receive dispatches from the Delta."),
        ("Channel of origin", "online / store / referral."),
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
             "WE DO NOT COLLECT  ·  weight or BMI  ·  precise GPS  ·  contacts  ·  social-graph  ·  third-party ad-tracking IDs  ·  anything that compromises maker privacy",
             size=10, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
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
                       "RevenueCat for any subscription kits"]),
        ("Provenance backend", ["Node + TypeScript API",
                                "Postgres + pgvector",
                                "Citation-linked impact ledger"]),
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
             "SHARED API · Postgres · Auth · AI gateway · Citation-linked impact ledger · Object storage",
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
             ("Customer-facing · Origin · Wardrobe · Atelier · Field · Shop · Threads"),
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
             ("Internal · Origin editor · education ledger · drop scheduler · "
              "concierge · transparency report · analytics"),
             size=11, color=INK)
    add_text(s, Inches(0.6), Inches(7.0), Inches(12), Inches(0.4),
             ("BUILT FOR YOUR TEAM   —   editors, sustainability ops, "
              "concierge, wholesale. Bilingual EN/FR. Citation-aware UI."),
             size=10, bold=True, color=ACCENT)
    add_footer(s, 17, slides_total)

slide_studio()

# 18. ROADMAP
def slide_roadmap():
    s = add_slide()
    add_section_header(s, "How we'll deliver", "Roadmap — first nine months.")
    phases = [
        ("Discovery", "Weeks 1–2",
         "Customer interviews (Toronto, NYC, LA, Montréal). Audit existing data + impact ledger feed. Lock Phase 1 scope."),
        ("Phase 1 build", "Weeks 3–16",
         "Origin, Wardrobe, Atelier, Field, Shop, Threads, Tier 1 AI, Studio. EN/FR at launch."),
        ("Phase 2 build", "Weeks 17–32",
         "AR provenance, repair triage, wholesale portal, demand-sensing. Add AR/GB/EU languages."),
        ("Phase 3 build", "Weeks 33–40+",
         "Editorial, VOICES films, content-scaling AI, counterfeit detection, carbon-tariff readiness."),
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
        ("Origin scan rate", "% of buyers who scan their tag and open The Origin within 30d",
         "Target ≥ 60% by month 6"),
        ("Wardrobe registration", "Average pieces registered per active user",
         "Target ≥ 4 by month 9"),
        ("Repeat rate", "% of app users placing a 2nd order within 90 days",
         "Target +25% vs non-app cohort"),
        ("Repair conversion", "% of repair-triaged tickets converted to DIY or paid repair",
         "Target ≥ 70%"),
        ("Threads engagement", "% of users opening The Field at least once per quarter",
         "Target ≥ 50%"),
        ("Cross-language reach", "% of sessions in FR + future AR/EU langs",
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
        ("Calm, not preachy",
         "The brand's mission is the loudest thing it could say. The app whispers."),
        ("Every claim cited",
         "Provenance must be auditable. AI never invents — it summarises real ledger data."),
        ("Maker dignity",
         "No precise GPS for farms. No real names without consent. The app honours the people behind it."),
        ("Buy less, wear more",
         "Cost-per-wear visible. Repair encouraged. Long-life is the brand promise."),
        ("Recognition over discounts",
         "Threads is access — store events, mending kits, supplier visits. Not coupons."),
        ("Honest about imperfection",
         "When materials, origin, or impact aren't perfect, the brand says so. The credibility is in the honesty."),
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
        ("Discovery sprint", "Two weeks. Customer interviews across CA + US. We sit with your sustainability team. Walk away with a signed Phase 1 spec — even if you don't build with us."),
        ("Embedded delivery", "A small team — lead engineer, mobile engineer, designer, bilingual QA — works as an extension of yours. Weekly demos."),
        ("Brand-side approval", "Every customer-facing provenance / impact / maker claim reviewed by Kotn before publish. AI generates; humans approve. Always."),
        ("Always your data", "Source code, customer data, AI logs all live in your accounts. Multi-region storage to honour data-residency rules as you grow."),
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
    add_section_header(s, "Why this works for Kotn", "The bet behind the build.")
    pts = [
        ("Verifiable provenance is your moat",
         "No global brand can claim 100% direct-trade Egyptian cotton with audited makers and a real school program. The Origin makes that visible."),
        ("Slow fashion needs a daily surface",
         "Buy less, wear more is hard to remember at the checkout. The Wardrobe and the Atelier make it part of the daily ritual."),
        ("The Field turns customers into allies",
         "Once a customer sees the school-day count grow, they're not buying t-shirts anymore — they're funding a community. The lifetime value math changes."),
        ("AI in service of trust, not replacement",
         "We use AI to summarise real ledger data, draft translations, triage repairs. We never let it invent provenance. The brand's reputation is safer for the building."),
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
             ("We sit with your team. We talk to ten of your customers — "
              "Toronto, Montréal, Brooklyn, LA. We sit with your sustainability "
              "team and audit the impact-ledger feed. We come back with a "
              "lockable Phase 1 scope and an interactive prototype of three "
              "core flows in EN and FR."),
             size=18, color=GOLD_SOFT)
    add_text(s, Inches(0.6), Inches(5.1), Inches(11), Inches(0.5),
             "WHAT YOU GET", size=11, bold=True, color=GOLD)
    add_text(s, Inches(0.6), Inches(5.5), Inches(11), Inches(2.0),
             ("•  A lockable feature scope, costed and timeboxed\n"
              "•  An interactive prototype of three core flows\n"
              "•  A summary of customer interviews and what we heard\n"
              "•  A go / no-go recommendation. Yours either way."),
             size=14, color=WHITE)
    add_footer(s, 23, slides_total, on_dark=True)

slide_next()

out = Path(__file__).parent / "Kotn-Pitch.pptx"
prs.save(out)
print(f"wrote {out}  ({len(prs.slides)} slides)")
