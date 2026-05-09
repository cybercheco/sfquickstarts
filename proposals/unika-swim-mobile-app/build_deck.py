"""Build the Unika Swim client pitch deck (.pptx). Features-only."""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pathlib import Path

INK         = RGBColor(0x2a, 0x2a, 0x26)
MUTED       = RGBColor(0x8a, 0x85, 0x7a)
LINE        = RGBColor(0xe6, 0xdc, 0xcb)
BG          = RGBColor(0xf7, 0xf1, 0xe8)
ACCENT      = RGBColor(0xd8, 0x70, 0x4a)
ACCENT_DEEP = RGBColor(0x8a, 0x3e, 0x22)
ACCENT_SOFT = RGBColor(0xf5, 0xdf, 0xd3)
GOLD        = RGBColor(0xd4, 0xa8, 0x5a)
GOLD_SOFT   = RGBColor(0xf3, 0xe6, 0xc7)
OCEAN       = RGBColor(0x4a, 0x7e, 0x8c)
OCEAN_SOFT  = RGBColor(0xcf, 0xdf, 0xe2)
SAND        = RGBColor(0xd8, 0xc4, 0xa0)
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
             "Ūnika Swim · Mobile App Pitch", size=9, color=color)
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
             "Ūnika Swim.", font=SERIF, size=66, color=INK)
    add_text(s, Inches(0.85), Inches(2.7), Inches(7.5), Inches(1.6),
             "Made for the body\nyou're in.",
             font=SERIF, size=28, color=ACCENT_DEEP)
    add_text(s, Inches(0.85), Inches(5.6), Inches(7.5), Inches(0.4),
             "Custom swimwear in Toronto. Cup AAA–H. ECONYL® regenerated nylon.",
             size=14, color=MUTED)
    add_text(s, Inches(0.85), Inches(6.0), Inches(7.5), Inches(0.3),
             "Prepared for the Ūnika Swim team",
             size=11, color=MUTED)
slide_cover()

# OPPORTUNITY
def slide_opportunity():
    s = add_slide()
    add_section_header(s, "Why now", "The most personal garment, in the brand that does the work.")
    stats = [
        ("AAA-H", "cup sizes supported.\nMastectomy / ostomy fit accommodated.",
         "Almost no swimwear brand does this. Ūnika has, since 2018."),
        ("100%", "ECONYL® regenerated nylon\nfrom fishing nets and waste",
         "Sustainability that's measurable, not marketing copy."),
        ("4–6", "weeks for custom-made.\nMost customers will wait.",
         "An app makes the wait visible — and the design choice better."),
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
    add_section_header(s, "The vision", "Not another store — an Atelier you can visit from your phone.")
    add_text(s, Inches(0.6), Inches(2.3), Inches(12), Inches(2.5),
             ("Ūnika Swim is the rare swimwear brand that does three "
              "things almost no one else does: makes-to-order in Toronto, "
              "fits cup sizes AAA–H, and accommodates mastectomy, ostomy, "
              "and surgical-recovery customers without making a feature "
              "of their bodies.\n\n"
              "The app should make the brand's most personal service — "
              "an in-store custom-design appointment — possible from the "
              "customer's couch. A booking flow that understands "
              "sensitive fit needs without flagging them. A live order "
              "tracker for custom pieces. A Closet that respects that "
              "for some customers, finding the right swimsuit is a year "
              "of work after surgery."),
             font=SERIF, size=20, color=INK)
    add_text(s, Inches(0.6), Inches(5.8), Inches(12), Inches(0.4),
             "WHY IT MATTERS", size=10, bold=True, color=ACCENT_DEEP)
    add_text(s, Inches(0.6), Inches(6.1), Inches(12), Inches(1.5),
             ("• Brings the in-store custom-design experience to anyone outside Toronto — multiplies the boutique's reach\n"
              "• Surfaces the brand's sensitive-fit work as service, not marketing — protects what makes it special\n"
              "• Closes the trust loop: appointment booking → live order tracking → restoration over years"),
             size=13, color=INK)
    add_footer(s, 3, slides_total)
slide_vision()

# 4. SIX PILLARS
def slide_pillars():
    s = add_slide()
    add_section_header(s, "Product overview", "Six pillars — five customer-facing, one internal.")
    pillars = [
        ("The Atelier", "Browse fabrics, draft your design, book the appointment. Custom from couch.", ACCENT),
        ("The Body", "Cup AAA–H. Sensitive-fit profile (mastectomy, ostomy, scars). Specialist-only access.", OCEAN),
        ("The Order Tracker", "Stage-by-stage on a 4–6-week custom build. Photo updates, ECONYL® batch.", GOLD),
        ("The Closet", "Register every piece — custom or pre-made. Repair / restoration workflow.", SAND),
        ("The Shop", "Pre-made + multilingual EN/PT/ES. Brazilian beachwear soul.", ACCENT_DEEP),
        ("The Studio", "Internal-facing web admin portal — custom orders, fabric library, appointments, concierge.", INK),
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
              "Foundations: Atelier, Body, Order Tracker, Closet, Shop, Sun.",
              "Everything a customer needs in their first 90 days.", [
    ("Multilingual onboarding", "EN / PT / ES at launch — Brazilian heritage + Latina audience."),
    ("Multi-currency storefront", "CAD · USD · BRL."),
    ("Atelier · fabric library", "Searchable ECONYL® fabrics + 6 brand prints."),
    ("Custom design draft", "Cut · fabric · color · embellishment, saved across sessions."),
    ("In-store appointment booking", "101 Yorkville · matched to specialist."),
    ("Remote video consult", "For out-of-Toronto and out-of-country customers."),
    ("Body · cup AAA–H sizing", "Cup-specific fit guidance per cut."),
    ("Body · sensitive-fit (opt-in)", "Mastectomy · ostomy · scars · specialist-only access."),
    ("Order tracker · 6 stages", "Design · fabric reserved · cut · sewing · finishing · ship."),
    ("Photo updates per stage", "Real photos from the Yorkville boutique."),
    ("Closet · register every piece", "Custom + pre-made archive."),
    ("Repair / restoration", "Bring an aging piece back to the boutique for restoration."),
    ("Atelier chat (AI)", "Trilingual EN/PT/ES design + fit coach."),
    ("Visual search", "Photograph a swim look, find similar Ūnika fabric."),
    ("Sun loyalty", "Recognition for appointments, restorations, anniversaries — never discounts."),
    ("The Studio (web admin)", "Custom orders, fabric library, appointments, concierge."),
])

feature_slide(6, slides_total, "Phase 2 · Depth (months 5–9)",
              "AR design preview, in-store iPad, B2B.",
              "Features that turn launch into a full Atelier-anywhere experience.", [
    ("AR custom-design preview", "Render fabric + print on body silhouette before booking — opt-in."),
    ("In-store iPad mode", "Studio mode for the boutique team to co-design with the customer."),
    ("Remote video consult upgrades", "Built-in fabric-cam for out-of-Toronto customers."),
    ("Wholesale + boutique B2B portal", "Yorkville and partner boutiques."),
    ("Heritage / archive sale", "Past-season custom designs re-released as limited pre-made."),
    ("Bilingual influencer content", "Culturally-aware brand collaborations."),
    ("Returns triage AI", "Routes pre-made refund vs custom alteration."),
    ("Demand-sensing on fabrics", "Wishlist + saved-design signals feed ECONYL® batch ordering."),
])

feature_slide(7, slides_total, "Phase 3 · Cultural authority (months 10+)",
              "From an app to a brand world.",
              "Long-form storytelling, community, operational AI.", [
    ("Editorial / journal", "Long-form on swimwear fit, post-surgery confidence, ECONYL® supply chain."),
    ("Annual VOICES film series", "Long-time customers' stories (with consent), founder story."),
    ("Multilingual content scaling AI", "EN-first, AI drafts PT/ES/IT/FR for editor review."),
    ("Counterfeit listing detection", "Amazon, Etsy, AliExpress."),
    ("VIP signal detection", "Concierge welcomes 5+ year customers."),
    ("Mastectomy / ostomy advocacy", "Featured charity collaborations."),
    ("ECONYL® batch transparency", "Per-piece batch lookup with provenance story."),
    ("Brazilian collab calendar", "Carnaval, Réveillon, summer — culturally-aware drops."),
])

# 8. ONBOARDING
def slide_onboarding():
    s = add_slide()
    add_section_header(s, "User experience", "Onboarding — under 90 seconds, in EN, PT, or ES.")
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.4),
             "The first screen earns trust by asking what fits. Sensitive-fit fields are opt-in only.",
             size=14, color=MUTED)
    steps = [
        ("01", "Bem-vinda", "Welcome in three languages.\nTap your language; everything follows."),
        ("02", "Sign in", "Apple, Google, or email.\nNo forms."),
        ("03", "Body basics", "Cup AAA–H · band size.\nBody comfort opt-in."),
        ("04", "Sensitive-fit (opt-in)", "Post-mastectomy · ostomy · scars.\nNever required. Specialist-only access."),
        ("05", "First moment", "Browse fabrics — or book\nyour Yorkville appointment."),
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
             "DESIGN PRINCIPLE   —   Sensitive-fit data lives in a segregated, audit-logged store and never trains AI.",
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
    "Custom design from couch to Yorkville.",
    "From browsing fabrics on the train to the design appointment two weeks later.",
    [
        ("DISCOVER", "Saves a fabric",
         "Sofia is on the streetcar. Saves the coral matte ECONYL® in the fabric library."),
        ("DRAFT", "Builds a design",
         "Atelier draft: one-piece · halter · low back · coral matte. Saves it."),
        ("BOOK", "Appointment in-store",
         "Books Saturday 2pm with Maria. Maria sees the draft a day before and prepares."),
        ("APPOINTMENT", "Co-designs in-store",
         "Sofia walks in. Maria already knows what she wants. They refine together. Order placed."),
        ("TRACK", "Watches it made",
         "App shows fabric cut · sewing · finishing · ships. Photo updates from the boutique. Trust builds week over week."),
    ])

journey_slide(10, slides_total,
    "User flow · 2 of 3",
    "Post-mastectomy customer — service, not marketing.",
    "How sensitive-fit works without making the customer's body the product.",
    [
        ("DISCLOSE", "Opts in privately",
         "Maria, post-mastectomy, completes the sensitive-fit profile. Lock icon. Specialist-only access. Audit-logged."),
        ("APPOINTMENT", "Booked with Betsy",
         "App routes the appointment to Betsy specifically — she's done this work for years."),
        ("DESIGN", "Pocket lining requested",
         "Custom design includes a discreet pocket for prosthesis. The customer doesn't have to explain it again."),
        ("PRODUCED", "Quietly made",
         "Custom-order tracker shows the work happening. Marketing AI never sees that the lining is medical — only that it's a lining."),
        ("TRUST", "Customer for life",
         "Maria refers two friends post-mastectomy. The brand becomes the one place she's seen, not flagged."),
    ])

journey_slide(11, slides_total,
    "User flow · 3 of 3",
    "Brazilian customer in São Paulo — remote consult, real connection.",
    "Brazilian heritage is the brand's DNA. The app respects that — in Portuguese, with a video consult, with cultural fluency.",
    [
        ("DISCOVER", "Sees Ūnika on Instagram",
         "Beatriz follows the brand from Brazil. Sees ECONYL® and the Brazilian-Toronto story."),
        ("LANGUAGE", "App opens in PT",
         "Detects locale. UI in Portuguese. Atelier chat in Portuguese. No friction."),
        ("CONSULT", "Books video consult",
         "Books a video consult with Betsy directly. Discusses ostomy fit privately."),
        ("ORDER", "Custom shipped to São Paulo",
         "Order tracker in PT. Photo updates. Ships internationally. Trust crosses borders."),
        ("RETURN", "Annual ritual",
         "Beatriz becomes a yearly customer. Custom for each summer. Brings the brand to her circle."),
    ])

# 12. SCREENS
def slide_screens():
    s = add_slide()
    add_section_header(s, "Visual reference", "What it looks like in hand.")
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.4),
             "Wireframe-fidelity mockups in the brand palette — sun, coral, ocean, sand.",
             size=14, color=MUTED)
    screens = [
        ("Onboarding", "EN/PT/ES · sign-in"),
        ("Home", "Appointment · order"),
        ("Atelier", "Custom design draft"),
        ("Fabrics", "ECONYL® library"),
        ("Body", "Sensitive-fit segregated"),
        ("Order tracker", "6-stage with photos"),
        ("Product", "Pre-made or custom"),
        ("Atelier chat", "Trilingual AI"),
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
    "AI in service of design and fit, not of body data.",
    "Every Tier 1 feature operates inside the sensitive-fit segregation boundary.",
    [
        ("Atelier chat (Sonnet)", "Trilingual EN/PT/ES design + fit coach. Routes to specialist when sensitive."),
        ("Fabric explorer", "Describe what you want, AI surfaces matching ECONYL® fabrics + prints."),
        ("Cup AAA–H fit guide", "Per-cut fit notes. Body shape opt-in only."),
        ("Visual search", "Photograph a swim look, find similar Ūnika fabric or pre-made piece."),
        ("Multilingual brand-voice translation", "EN-first; AI drafts PT/ES; brand glossary preserves Ūnika, Atelier, Sun."),
        ("Wardrobe-gap analyser", "\"You have 3 one-pieces but no cover-up\" — recommends from your real wardrobe."),
    ])

ai_tier_slide(14, slides_total,
    "Intelligence · Tier 2 & 3",
    "AI that powers AR, in-store iPad, and the back office.",
    "Phase 2 customer-facing AI plus operational AI the customer never sees.",
    [
        ("AR custom-design preview", "Phone camera renders fabric + print on body silhouette."),
        ("In-store iPad co-design", "Studio mode for the boutique team to co-design with the customer."),
        ("Demand-sensing on fabrics", "Wishlist + saved-design signals feed ECONYL® batch ordering."),
        ("Returns triage AI", "Routes pre-made refund vs custom alteration."),
        ("Multilingual content scaling", "EN-first, AI drafts PT/ES/IT/FR, editors approve."),
        ("Counterfeit listing detection", "Amazon · Etsy · AliExpress."),
        ("Brazilian cultural calendar AI", "Carnaval, Réveillon, summer drops — culturally-aware push."),
        ("Sensitive-fit segregation enforcement", "Audit-log monitor flags any AI prompt touching segregated data."),
    ])

# 15. DATA
def slide_data():
    s = add_slide()
    add_section_header(s, "Data with consent", "What we collect — and what we won't.")
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.4),
             "Default to opt-in per category. Sensitive-fit data is segregated, audit-logged, never used for marketing AI.",
             size=14, color=MUTED)
    items = [
        ("Identity & contact", "email, name, address — orders and shipping."),
        ("Fit profile", "cup AAA–H, body comfort preferences."),
        ("Sensitive-fit (opt-in)", "post-mastectomy, ostomy, scars — specialist-only."),
        ("Language & region", "UI language, country, currency."),
        ("Custom orders", "designs, fabrics, prints, milestones."),
        ("Closet", "registered pieces, wear log."),
        ("Engagement", "views, wishlists, saved fabrics."),
        ("Channel of origin", "online / Yorkville studio / boutique."),
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
             "WE DO NOT COLLECT  ·  weight or BMI  ·  before/after body photos  ·  precise GPS  ·  contacts  ·  social-graph",
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
                       "Multi-currency CAD/USD/BRL",
                       "RevenueCat for any subscriptions"]),
        ("Atelier backend", ["Node + TypeScript API",
                              "Postgres + pgvector for visual search",
                              "Sensitive-fit data in segregated audit-logged store"]),
        ("Intelligence", ["Claude (Sonnet 4.6 chat, Haiku 4.5 batch)",
                           "Trilingual brand-voice prompts",
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
             "SHARED API · Postgres · Auth · AI gateway · Custom-order tracker · SEGREGATED sensitive-fit store",
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
             ("Customer-facing · Atelier · Body · Order Tracker · Closet · Shop · Sun"),
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
             ("Internal · custom orders · fabric library · appointments · concierge · sensitive-fit-aware specialist matching"),
             size=11, color=INK)
    add_text(s, Inches(0.6), Inches(7.0), Inches(12), Inches(0.4),
             ("BUILT FOR YOUR TEAM   —   Betsy + Yorkville specialists + custom-order ops + concierge. Trilingual EN/PT/ES."),
             size=10, bold=True, color=ACCENT_DEEP)
    add_footer(s, 17, slides_total)
slide_studio()

# 18. ROADMAP
def slide_roadmap():
    s = add_slide()
    add_section_header(s, "How we'll deliver", "Roadmap — first nine months.")
    phases = [
        ("Discovery", "Weeks 1–2",
         "Customer interviews — cult-fan with 5+ pieces, post-mastectomy, remote-Brazil, new buyer, Yorkville-local. Audit existing custom-order data + sensitive-fit consent flow. Lock Phase 1 scope."),
        ("Phase 1 build", "Weeks 3–18",
         "Atelier · Body · Order Tracker · Closet · Shop · Sun · Tier 1 AI · The Studio. EN/PT/ES at launch. Sensitive-fit segregation in production from day one."),
        ("Phase 2 build", "Weeks 19–32",
         "AR custom preview, in-store iPad mode, wholesale B2B, video-consult upgrades."),
        ("Phase 3 build", "Weeks 33–40+",
         "Editorial, VOICES films, content scaling, demand sensing, counterfeit detection, advocacy partnerships."),
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
        ("Appointment-to-order conv.", "% of appointments that become custom orders, month 3",
         "Target ≥ 80%"),
        ("Custom-design draft rate", "% of users who save a draft before booking",
         "Target ≥ 60%"),
        ("Order-tracker engagement", "% of customers checking the app during production",
         "Target ≥ 75%"),
        ("Sensitive-fit return rate", "Returns from customers using sensitive-fit profile",
         "Target ≤ 5% (vs 15% category)"),
        ("ECONYL® batch utilisation", "% of fabric used vs reserved",
         "Target ≥ 92%"),
        ("Trilingual reach", "% of sessions in PT or ES",
         "Target ≥ 30% by month 12"),
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
        ("Sensitive-fit is private",
         "Mastectomy, ostomy, scar data lives in a segregated, audit-logged store. Specialist-only access. Never trains AI."),
        ("Custom is slow by design",
         "Made-to-order means weeks. The app makes the wait visible — never apologetic."),
        ("Comfort over body shape",
         "Body comfort preferences, not body shape. No \"slimming.\" No \"summer body.\" Ever."),
        ("Brazilian heritage, Toronto craft",
         "Both, named, neither hidden. Trilingual EN/PT/ES from launch."),
        ("ECONYL® is a story, not a sticker",
         "Every fabric tied to its post-industrial waste source. Per-batch transparency."),
        ("Recognition over discounts",
         "Sun rewards appointments, restorations, anniversaries. Custom is an investment, not a transaction."),
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
        ("Discovery sprint", "Two weeks. Customer interviews — cult-fan, post-mastectomy, remote-Brazil, new buyer, Yorkville-local. Walk away with a signed Phase 1 spec."),
        ("Embedded delivery", "A small team — lead engineer, mobile engineer, designer, trilingual QA — works as an extension of yours. Weekly demos."),
        ("Sensitive-fit segregation as contract clause", "Audit-logged, specialist-only, never trains AI. Non-negotiable on day one."),
        ("Always your data", "Source code, customer data, AI logs, sensitive-fit store all live in your accounts."),
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
    add_section_header(s, "Why this works for Ūnika Swim", "The bet behind the build.")
    pts = [
        ("Custom-from-couch is your moat",
         "Almost no swimwear brand has both a real custom service AND the ability to run it remotely. The app extends Yorkville to São Paulo, Miami, Lisbon."),
        ("Sensitive-fit work is your reputation",
         "Mastectomy and ostomy customers tell their friends. The brand becomes the one place they're seen, not flagged. Highest-LTV segment in the category."),
        ("ECONYL® is your differentiator",
         "Competitors say \"sustainable.\" You say \"per-batch fishing-net source.\" The app makes that auditable."),
        ("AI in service of the Atelier, not the body",
         "We use AI to help customers design, find fabrics, navigate languages. Never to assume their bodies. The brand's reputation is safer for the building."),
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
             ("We sit with your team in Yorkville. We talk to ten of your "
              "customers — cult-fan, post-mastectomy, remote-Brazil, new "
              "buyer, Yorkville-local. We align on the sensitive-fit "
              "segregation boundary with you. We come back with a "
              "lockable Phase 1 scope and a working prototype of the "
              "Atelier draft → appointment booking flow in EN, PT, ES."),
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

out = Path(__file__).parent / "Unika-Swim-Pitch.pptx"
prs.save(out)
print(f"wrote {out}  ({len(prs.slides)} slides)")
