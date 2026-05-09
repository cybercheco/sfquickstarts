"""Build the Cocokind client pitch deck (.pptx). Features-only."""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pathlib import Path

INK         = RGBColor(0x2c, 0x3a, 0x2e)
MUTED       = RGBColor(0x8a, 0x90, 0x85)
LINE        = RGBColor(0xe0, 0xd8, 0xc8)
BG          = RGBColor(0xf4, 0xef, 0xe6)
ACCENT      = RGBColor(0x6e, 0x8b, 0x6a)
ACCENT_DEEP = RGBColor(0x3e, 0x4f, 0x3b)
ACCENT_SOFT = RGBColor(0xd8, 0xe4, 0xd4)
GOLD        = RGBColor(0xc9, 0xa8, 0x5e)
GOLD_SOFT   = RGBColor(0xf1, 0xe7, 0xc9)
ROSE        = RGBColor(0xd8, 0xa5, 0x94)
BLUE        = RGBColor(0x7d, 0x97, 0xa7)
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
             "Cocokind · Mobile App Pitch", size=9, color=color)
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
             "Cocokind.", font=SERIF, size=66, color=INK)
    add_text(s, Inches(0.85), Inches(2.7), Inches(7.5), Inches(1.6),
             "Skincare you can\nread in full.",
             font=SERIF, size=28, color=ACCENT_DEEP)
    add_text(s, Inches(0.85), Inches(5.6), Inches(7.5), Inches(0.4),
             "Sustainability Facts in your customer's pocket.",
             size=14, color=MUTED)
    add_text(s, Inches(0.85), Inches(6.0), Inches(7.5), Inches(0.3),
             "Prepared for the Cocokind team",
             size=11, color=MUTED)
slide_cover()

# OPPORTUNITY
def slide_opportunity():
    s = add_slide()
    add_section_header(s, "Why now", "Cocokind already publishes Sustainability Facts. The mobile app makes them readable.")
    stats = [
        ("9", "ingredients in the Vitamin C serum —\nevery one citation-linked",
         "The brand has done the science. The customer just doesn't see it."),
        ("0.014", "kg CO₂e per use — published.\nCompetitors won't say.",
         "Transparency is the moat. The app is the loudspeaker."),
        ("150+", "Target locations + Whole Foods\n+ DTC + international",
         "An app gives the omnichannel customer one routine across all of them."),
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
    add_section_header(s, "The vision", "Not another store — a transparency engine.")
    add_text(s, Inches(0.6), Inches(2.3), Inches(12), Inches(2.5),
             ("Priscilla pioneered Sustainability Facts labels — the first "
              "skincare brand to publish per-product carbon-per-use, full "
              "ingredient sourcing, and end-of-life packaging detail. She "
              "also publicly stopped calling Cocokind \"clean\" or "
              "\"sustainable\" because those words have lost meaning.\n\n"
              "The app is the natural home for that stance. A digital "
              "Facts label every customer can verify, a Routine builder "
              "from the existing catalog without invented claims, and an "
              "Ingredient library where every component cites real "
              "evidence. The customer is informed, sceptical, and rewarded "
              "by depth."),
             font=SERIF, size=20, color=INK)
    add_text(s, Inches(0.6), Inches(5.8), Inches(12), Inches(0.4),
             "WHY IT MATTERS", size=10, bold=True, color=ACCENT_DEEP)
    add_text(s, Inches(0.6), Inches(6.1), Inches(12), Inches(1.5),
             ("• Brings the brand's existing transparency work into the customer's daily routine\n"
              "• Turns a one-time purchase into a routine practice — the highest-LTV shape in skincare\n"
              "• Closes the packaging loop with refill mechanics that respect the brand's ethic"),
             size=13, color=INK)
    add_footer(s, 3, slides_total)
slide_vision()

# 4. SIX PILLARS
def slide_pillars():
    s = add_slide()
    add_section_header(s, "Product overview", "Six pillars — five customer-facing, one internal.")
    pillars = [
        ("The Routine", "Daily AM + PM step-by-step — calm reminders, no streaks.", ACCENT),
        ("The Facts", "Per-product Sustainability Facts: carbon, packaging, ingredients, citations.", GOLD),
        ("The Match", "Pick goals — hydration, glow, barrier, acne, age — get a routine from the catalog.", ROSE),
        ("The Refill", "Calm subscription management — skip, pause, bottle returns + credit.", BLUE),
        ("The Shop", "DTC + Target / Whole Foods finder; multi-currency.", ACCENT_DEEP),
        ("The Studio", "Internal-facing web admin portal — Facts editor, ingredient library, refill ops, compliance review.", INK),
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
              "Foundations: Routine, Facts, Match, Refill, Shop, Honest.",
              "Everything a customer needs in their first 90 days.", [
    ("Multilingual onboarding", "EN + ES at launch."),
    ("Multi-currency storefront", "USD + CAD."),
    ("AM + PM Routine cards", "Steps with order rationale, calm reminders, no streaks."),
    ("Sustainability Facts (digital)", "Carbon, water, energy per use; packaging breakdown; ingredient list."),
    ("Per-ingredient evidence pages", "Source, role, peer-reviewed citations."),
    ("Match → Routine AI", "Goal selection (hydration, glow, barrier, acne) → routine from catalog."),
    ("Refill subscription mgmt", "Skip / pause / accelerate / bundle / vacation mode."),
    ("Smart refill prediction", "Usage-based — never pushy."),
    ("Bottle returns + credit", "Track returns, post credit at checkout."),
    ("Target / Whole Foods finder", "In-store availability with map."),
    ("Bundle builder", "Routines as bundles."),
    ("Honest loyalty", "Recognition for routine completion, refill returns, reviews."),
    ("Studio chat (AI)", "Multilingual ingredient + routine assistant with strict guardrails."),
    ("Multilingual translation", "Brand-voice EN→ES drafts via Claude."),
    ("Visual search", "Photograph a product, find it."),
    ("The Studio (web admin)", "Facts editor, ingredient library, refill ops, compliance review, concierge."),
])

feature_slide(6, slides_total, "Phase 2 · Depth (months 5–9)",
              "AR try-on, photo skin analysis, esthetician portal.",
              "Features that turn launch into a category-defining transparency platform.", [
    ("AR product try-on", "Texture and finish for makeup-adjacent items."),
    ("Photo skin analysis (cautious)", "Opt-in, never diagnostic, surfaces routine adjustments."),
    ("Esthetician B2B portal", "Partnered estheticians with white-label client tracking."),
    ("Cocokind Impact Foundation in-app", "Featured grantees, donation flow at checkout."),
    ("Live Q&A with Priscilla", "Quarterly with founder + dermatologists."),
    ("Heritage / archive sale", "Past favourites re-released with Facts intact."),
    ("Multi-region expansion", "Add EU storefront with GDPR data residency."),
    ("Returns triage AI", "Routes refund vs replacement vs adjustment."),
])

feature_slide(7, slides_total, "Phase 3 · Cultural authority (months 10+)",
              "From an app to a transparency standard.",
              "Long-form storytelling, education, operational AI.", [
    ("Editorial / journal", "Long-form on skincare science, transparency, packaging."),
    ("Annual VOICES film series", "Priscilla, Foundation grantees, scientists."),
    ("Multilingual content scaling AI", "EN-first, AI drafts ES/FR/PT for editor review."),
    ("Demand-sensing AI", "Wishlist + routine signals feed production planning."),
    ("Counterfeit listing detection", "Amazon, eBay, AliExpress."),
    ("Carbon-per-use leaderboard", "Most-improved products year over year."),
    ("VIP signal detection", "Concierge welcomes top-tier supporters."),
    ("CSRD-ready data export", "EU sustainability disclosure rules will tighten — get ahead."),
])

# 8. ONBOARDING
def slide_onboarding():
    s = add_slide()
    add_section_header(s, "User experience", "Onboarding — under 90 seconds, in EN or ES.")
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.4),
             "The first screen earns trust by asking what the customer is working on — not making assumptions about her.",
             size=14, color=MUTED)
    steps = [
        ("01", "Hola", "Welcome in two languages.\nTap your language; everything follows."),
        ("02", "Sign in", "Apple, Google, or email.\nNo forms."),
        ("03", "Goals", "Pick 1–3 from hydration, glow,\nbarrier, acne, age, sensitivity."),
        ("04", "Sensitivities", "Fragrance? Retinol? Anything\nyou know reacts? · safety filter"),
        ("05", "First moment", "Today's Routine is yours —\nor explore the Facts."),
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
             "DESIGN PRINCIPLE   —   Never diagnose skin conditions. Always cite. Always defer to dermatologists.",
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
    "First product → daily routine.",
    "From a Whole Foods aisle to a daily AM/PM in three weeks.",
    [
        ("DISCOVER", "Sees Vitamin C serum",
         "At Whole Foods. Scans the QR on the box. App opens with full Sustainability Facts label."),
        ("BUILD", "Picks goals",
         "Hydration + Glow. App proposes a routine: cleansing oil → toner → vitamin C → ceramide → SPF."),
        ("BUY", "Apple Pay checkout",
         "DTC checkout. Subscribes to Vitamin C serum + ceramide moisturiser. Order tracked in-app."),
        ("ROUTINE", "Day 1",
         "Morning push: 'Step 1 of your routine.' 60-sec audio with technique tips. Marks complete (no streak)."),
        ("HABIT", "Day 21",
         "Three weeks of completed mornings. Customer stops experimenting; her routine stuck."),
    ])

journey_slide(10, slides_total,
    "User flow · 2 of 3",
    "Sensitive-skin customer with rosacea — when to defer to dermatologists.",
    "The brand's reputation depends on never giving medical advice.",
    [
        ("ASK", "Customer asks",
         "Maya, with rosacea, wants to add Vitamin C to her routine."),
        ("DETECT", "AI flags caution",
         "Even gentle vitamin C may trigger flares. AI gives general guidance; refers to dermatologist."),
        ("ESCALATE", "Concierge follows",
         "AI logs escalation. Maya gets a calm human reply confirming the dermatologist deferral."),
        ("CONFIRM", "Derm note",
         "Maya's dermatologist clears the gentle ascorbyl glucoside formulation. Stack rules update."),
        ("TRUST", "Brand earns it",
         "What another brand might have answered casually, Cocokind handled correctly. Maya tells two friends."),
    ])

journey_slide(11, slides_total,
    "User flow · 3 of 3",
    "Refill management — the customer who thought she'd cancel.",
    "Most brands lose customers on the cancel button. The Vault makes that rare.",
    [
        ("SIGNAL", "Skipped twice",
         "Customer skipped two consecutive ceramide moisturiser refills."),
        ("REACH", "Calm message",
         "Push: 'Notice you've been skipping. Want to pause for a season instead?'"),
        ("PAUSE", "Vacation mode",
         "Customer taps Pause for 60 days. No charge. Routine still visible."),
        ("RETURN", "Auto-restart",
         "60 days later, refill resumes. Customer didn't lift a finger."),
        ("LTV", "Saved",
         "What would have been a churn is a 60-day pause. LTV protected."),
    ])

# 12. SCREENS
def slide_screens():
    s = add_slide()
    add_section_header(s, "Visual reference", "What it looks like in hand.")
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.4),
             "Wireframe-fidelity mockups in the brand palette — warm cream, matcha sage, amber, soft rose.",
             size=14, color=MUTED)
    screens = [
        ("Onboarding", "EN/ES · sign-in"),
        ("Home", "Today's routine"),
        ("Facts", "Digital Sustainability Facts"),
        ("Match", "Multi-select goals"),
        ("Routine", "AM + PM steps"),
        ("Refill", "Subscription mgmt"),
        ("Product", "Facts pills"),
        ("Studio chat", "Ingredient AI"),
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
    "AI in service of transparency — never of diagnosis.",
    "Every Tier 1 feature operates inside compliance guardrails. Sources cited; never invented.",
    [
        ("Studio chat (Sonnet)", "Multilingual ingredient + routine coach. Strict cosmetic-rule guardrails."),
        ("Goal-to-routine recommender", "Curated rules engine + AI. Cites ingredients and step rationale."),
        ("Sensitivity-aware filtering", "Customer-disclosed sensitivities filter routine recommendations."),
        ("Smart refill prediction", "Usage-based; never pushy."),
        ("Multilingual brand-voice translation", "EN-first; AI drafts ES; brand glossary preserves Cocokind, Honest."),
        ("Ingredient explainer", "Tap any ingredient → sourced summary, role in formula, evidence base."),
    ])

ai_tier_slide(14, slides_total,
    "Intelligence · Tier 2 & 3",
    "AI that powers the practice and the back office.",
    "Phase 2 customer-facing AI plus operational AI the customer never sees.",
    [
        ("AR product try-on", "Texture and finish for makeup-adjacent items."),
        ("Photo skin analysis (cautious)", "Opt-in, never diagnostic; surfaces routine adjustments only."),
        ("Returns triage AI", "Routes refund vs replacement vs adjustment."),
        ("Demand-sensing AI", "Wishlist + Routine signals feed production planning."),
        ("Multilingual content scaling", "EN-first, AI drafts ES/FR/PT, editor approval."),
        ("Counterfeit-listing detection", "Amazon / eBay / AliExpress."),
        ("Carbon-per-use leaderboard", "Year-over-year LCA improvements published."),
        ("CSRD-aware export", "EU sustainability disclosure data export."),
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
        ("Skin goals", "hydration / glow / barrier / acne / age / sensitivity."),
        ("Sensitivities", "for safety filters on routine recommendations."),
        ("Language & region", "UI language, country, currency."),
        ("Subscriptions", "active refills, usage rate."),
        ("Routine engagement", "step completions — no shaming, no streaks."),
        ("Routine history", "products used, when, paired."),
        ("Channel of origin", "online / Target / Whole Foods / referral."),
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
             "WE DO NOT COLLECT  ·  weight  ·  BMI  ·  before/after photos without explicit consent  ·  precise GPS  ·  diagnosed conditions  ·  social-graph",
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
                       "Multi-currency USD/CAD",
                       "RevenueCat for subscriptions"]),
        ("Facts backend", ["Node + TypeScript API",
                             "Postgres + pgvector for visual search",
                             "Citation-linked claims engine"]),
        ("Intelligence", ["Claude (Sonnet 4.6 chat, Haiku 4.5 batch)",
                           "Strict cosmetic-rule system prompts",
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
             "SHARED API · Postgres · Auth · AI gateway · Citation engine · Refill ops",
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
             ("Customer-facing · Routine · Facts · Match · Refill · Shop · Honest"),
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
             ("Internal · Facts editor · Ingredient library · Compliance review · Refill ops · concierge · analytics"),
             size=11, color=INK)
    add_text(s, Inches(0.6), Inches(7.0), Inches(12), Inches(0.4),
             ("BUILT FOR YOUR TEAM   —   editors, sustainability ops, "
              "concierge, and brand-side compliance review. Bilingual EN/ES."),
             size=10, bold=True, color=ACCENT_DEEP)
    add_footer(s, 17, slides_total)
slide_studio()

# 18. ROADMAP
def slide_roadmap():
    s = add_slide()
    add_section_header(s, "How we'll deliver", "Roadmap — first nine months.")
    phases = [
        ("Discovery", "Weeks 1–2",
         "Customer interviews (DTC subscriber, Target buyer, Whole Foods buyer, new buyer, competitor user). Audit Sustainability Facts data + LCA citations. Brand-side compliance alignment. Lock Phase 1 scope."),
        ("Phase 1 build", "Weeks 3–18",
         "Routine, Facts, Match, Refill, Shop, Honest, Tier 1 AI with compliance guardrails, The Studio. EN/ES at launch."),
        ("Phase 2 build", "Weeks 19–32",
         "AR try-on, photo skin analysis (cautious), esthetician B2B portal, EU multi-region expansion."),
        ("Phase 3 build", "Weeks 33–40+",
         "Editorial, VOICES films, content scaling, demand sensing, counterfeit detection, CSRD-ready export."),
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
        ("Routine completion rate", "% of users completing both AM and PM ≥3x/week, month 3",
         "Target ≥ 50%"),
        ("Match → routine adoption", "% of users with a saved Routine, month 3",
         "Target ≥ 65%"),
        ("Refill churn", "% of subs churning quarterly",
         "Target −30% vs current baseline"),
        ("Pause-to-cancel ratio", "% of would-be cancels who pause instead",
         "Target ≥ 60%"),
        ("Studio chat completion", "% of chats resolved without escalation",
         "Target ≥ 75%"),
        ("Compliance flags caught pre-publish", "% of cosmetic-rule issues caught in Studio review",
         "Target 100%"),
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
        ("Calm, never punishing",
         "No streaks, no FOMO. Skincare is a practice, not a leaderboard."),
        ("Cite, never invent",
         "Every ingredient and sustainability claim sources to evidence. AI never makes up science."),
        ("Defer to dermatologists",
         "When customers raise skin conditions, the AI offers general guidance and refers to the derm."),
        ("Subscription is a relationship",
         "One-tap pause, skip, vacation. Never auto-charge a customer who asked you not to."),
        ("Transparency over branding",
         "We don't say \"clean\" or \"sustainable\" without published criteria — Priscilla's stance, baked in."),
        ("Recognition over discount",
         "Honest rewards routine practice and bottle returns. Not new-buy bribes."),
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
        ("Discovery sprint", "Two weeks. Customer interviews — DTC subscriber, Target, Whole Foods, new buyer, competitor user. Brand-side compliance alignment on AI claims."),
        ("Embedded delivery", "A small team — lead engineer, mobile engineer, designer, bilingual QA — works as an extension of yours. Weekly demos."),
        ("Brand-side compliance review", "Every customer-facing ingredient, sustainability, or routine claim reviewed by your editorial / legal team. Non-negotiable."),
        ("Always your data", "Source code, customer data, AI logs, the Sustainability Facts library all live in your accounts."),
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
    add_section_header(s, "Why this works for Cocokind", "The bet behind the build.")
    pts = [
        ("Transparency is your moat",
         "You stopped calling the brand 'clean' because the word is meaningless. The app is where 'meaningful' lives — Sustainability Facts, peer-reviewed evidence, end-of-life data. Competitors can't fake it."),
        ("Routine is the LTV story",
         "A daily-routine customer with 3+ subscriptions is the highest LTV in skincare. The Routine + Refill flow makes that easier to keep."),
        ("Compliance is a feature",
         "Most skincare brands run until the FDA notices. Building cosmetic-rule guardrails into the AI from day one is what lets you grow safely past Target into international."),
        ("AI in service of evidence",
         "We use AI to coach, recommend, translate, predict. Never to diagnose. Never to invent. The brand's reputation is safer for the building."),
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
              "DTC subscriber, Target, Whole Foods, new buyer, competitor "
              "user. We sit with your editorial team and align on what "
              "the AI can and can't say about ingredients and packaging. "
              "We come back with a lockable Phase 1 scope and a working "
              "prototype of the Facts and Routine flows in EN and ES."),
             size=18, color=GOLD_SOFT)
    add_text(s, Inches(0.6), Inches(5.1), Inches(11), Inches(0.5),
             "WHAT YOU GET", size=11, bold=True, color=GOLD)
    add_text(s, Inches(0.6), Inches(5.5), Inches(11), Inches(2.0),
             ("•  A lockable feature scope, costed and timeboxed\n"
              "•  An interactive prototype of two core flows\n"
              "•  Brand-side compliance alignment on AI claims\n"
              "•  A go / no-go recommendation. Yours either way."),
             size=14, color=WHITE)
    add_footer(s, 23, slides_total, on_dark=True)
slide_next()

out = Path(__file__).parent / "Cocokind-Pitch.pptx"
prs.save(out)
print(f"wrote {out}  ({len(prs.slides)} slides)")
