"""Build The Ten Spot client pitch deck (.pptx). Features-only."""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pathlib import Path

INK         = RGBColor(0x1a, 0x1a, 0x1a)
MUTED       = RGBColor(0x8a, 0x84, 0x85)
LINE        = RGBColor(0xeb, 0xd9, 0xda)
BG          = RGBColor(0xfa, 0xf6, 0xf4)
ACCENT      = RGBColor(0xe8, 0x5a, 0x8c)
ACCENT_DEEP = RGBColor(0xa8, 0x2e, 0x60)
ACCENT_SOFT = RGBColor(0xfc, 0xe0, 0xeb)
GOLD        = RGBColor(0xd4, 0xa8, 0x5a)
GOLD_SOFT   = RGBColor(0xf3, 0xe8, 0xc7)
MINT        = RGBColor(0xb5, 0xd4, 0xc4)
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
             "The Ten Spot · Mobile App Pitch", size=9, color=color)
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
    add_rect(s, Inches(8.5), 0, Inches(4.833), SH, fill=INK)
    add_rect(s, Inches(8.5), 0, Inches(4.833), Inches(2.0), fill=ACCENT_DEEP)
    add_rect(s, Inches(8.5), 0, Inches(4.833), Inches(0.5), fill=ACCENT)
    for cx, cy, r in [(11.2, 1.4, 0.20), (12.5, 3.0, 0.12), (10.4, 4.2, 0.18), (12.0, 5.6, 0.14), (11.6, 6.7, 0.10)]:
        d = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(cx-r), Inches(cy-r), Inches(2*r), Inches(2*r))
        d.fill.solid(); d.fill.fore_color.rgb = GOLD; d.line.fill.background(); d.shadow.inherit = False
    add_rect(s, Inches(0.6), Inches(1.0), Inches(0.08), Inches(2.4), fill=ACCENT)
    add_text(s, Inches(0.85), Inches(1.0), Inches(7), Inches(0.4), "MOBILE APP · PITCH", size=11, bold=True, color=ACCENT_DEEP)
    add_text(s, Inches(0.85), Inches(1.45), Inches(8), Inches(2.0), "The Ten Spot.", font=SERIF, size=66, color=INK)
    add_text(s, Inches(0.85), Inches(2.7), Inches(7.5), Inches(1.6), "Book the spot.\nSkip the spa.", font=SERIF, size=28, color=ACCENT_DEEP)
    add_text(s, Inches(0.85), Inches(5.6), Inches(7.5), Inches(0.4), "33+ beauty bars across North America. One app.", size=14, color=MUTED)
    add_text(s, Inches(0.85), Inches(6.0), Inches(7.5), Inches(0.3), "Prepared for the Ten Spot team", size=11, color=MUTED)
slide_cover()

# OPPORTUNITY
def slide_opportunity():
    s = add_slide()
    add_section_header(s, "Why now", "Booking is the product. The brand has earned 33+ locations.")
    stats = [
        ("33+", "beauty bars across\nNorth America", "Largest multi-service beauty-bar franchise in NA. Largest opportunity to lead on app-booking."),
        ("4 wk", "average customer cadence —\nwax, lash, brow", "Recurring customer = highest LTV in the category. The app keeps her in the loop."),
        ("68%", "of bookings can be self-served\non a great app (industry data)", "Each location saves 10–15 hr/week of phone-bound staff time."),
    ]
    x = Inches(0.6); y = Inches(2.4); w = Inches(4); gap = Inches(0.2)
    for i, (big, mid, small) in enumerate(stats):
        cx = x + (w + gap) * i
        add_rect(s, cx, y, w, Inches(4.0), fill=WHITE, line=LINE, corner=True)
        add_text(s, cx + Inches(0.4), y + Inches(0.4), w - Inches(0.8), Inches(1.4), big, font=SERIF, size=58, color=ACCENT_DEEP)
        add_text(s, cx + Inches(0.4), y + Inches(1.7), w - Inches(0.8), Inches(1.0), mid, size=14, bold=True, color=INK)
        add_text(s, cx + Inches(0.4), y + Inches(2.9), w - Inches(0.8), Inches(1.0), small, size=12, color=MUTED)
    add_footer(s, 2, slides_total)
slide_opportunity()

# VISION
def slide_vision():
    s = add_slide()
    add_section_header(s, "The vision", "Not another store — a booking + relationship engine.")
    add_text(s, Inches(0.6), Inches(2.3), Inches(12), Inches(2.5),
             ("The Ten Spot's customer books recurring services every 3–4 weeks "
              "across multiple locations. The app should make booking effortless "
              "and the prep + aftercare educational. A flow that knows your "
              "favorite location and favorite technician. An automated calendar "
              "of \"your next appointments are due.\" Service-specific prep guides "
              "(don't shave 24 hours before a wax) and aftercare (no sun for 48 "
              "hours after laser). And a membership wallet that travels across "
              "all 33+ locations."),
             font=SERIF, size=20, color=INK)
    add_text(s, Inches(0.6), Inches(5.8), Inches(12), Inches(0.4), "WHY IT MATTERS", size=10, bold=True, color=ACCENT_DEEP)
    add_text(s, Inches(0.6), Inches(6.1), Inches(12), Inches(1.5),
             ("• Self-served booking saves each franchise 10–15 hr/week of phone-bound staff time\n"
              "• Cadence-aware push notifications keep customers booking on the brand's natural rhythm\n"
              "• Multi-location wallet + membership lets customers move between locations without friction"),
             size=13, color=INK)
    add_footer(s, 3, slides_total)
slide_vision()

# 4. SIX PILLARS
def slide_pillars():
    s = add_slide()
    add_section_header(s, "Product overview", "Six pillars — five customer-facing, one internal.")
    pillars = [
        ("Book", "One-tap re-book. Location + technician + service. Wait-list when full.", ACCENT),
        ("Your Spot", "Favorite location, favorite tech, service history. Cadence-aware.", GOLD),
        ("Prep + After", "Service-specific care: don't shave before wax, no sun after laser.", MINT),
        ("The Calendar", "Recurring care, automated. Series tracking (laser 3 of 6).", ACCENT_DEEP),
        ("Membership / Shop", "Member tier. Gift cards. Multi-location credit.", INK),
        ("The Studio", "Internal-facing web admin — multi-location dashboard, scheduling, franchise admin.", RGBColor(0x4a, 0x4a, 0x4a)),
    ]
    cols = 3; cw = Inches(4.0); ch = Inches(2.25); gx = Inches(0.15); gy = Inches(0.18)
    x0 = Inches(0.6); y0 = Inches(2.4)
    for i, (title, desc, accent) in enumerate(pillars):
        c = i % cols; r = i // cols
        cx = x0 + (cw + gx) * c; cy = y0 + (ch + gy) * r
        add_rect(s, cx, cy, cw, ch, fill=WHITE, line=LINE, corner=True)
        add_rect(s, cx, cy, Inches(0.1), ch, fill=accent, corner=True)
        add_text(s, cx + Inches(0.3), cy + Inches(0.2), cw - Inches(0.6), Inches(0.4), str(i + 1), font=SERIF, size=20, bold=True, color=accent)
        add_text(s, cx + Inches(0.3), cy + Inches(0.7), cw - Inches(0.6), Inches(0.5), title, font=SERIF, size=20, color=INK)
        add_text(s, cx + Inches(0.3), cy + Inches(1.25), cw - Inches(0.6), Inches(1.0), desc, size=11, color=MUTED)
    add_footer(s, 4, slides_total)
slide_pillars()

# Phase features
def feature_slide(num, total, eyebrow, title, intro, items):
    s = add_slide()
    add_section_header(s, eyebrow, title)
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.6), intro, size=14, color=MUTED)
    cols = 2; cw = Inches(6.0); ch = Inches(0.95); gap = Inches(0.15)
    for i, (name, desc) in enumerate(items):
        c = i % cols; r = i // cols
        cx = Inches(0.6) + (cw + gap) * c; cy = Inches(2.9) + (ch + gap) * r
        add_rect(s, cx, cy, cw, ch, fill=WHITE, line=LINE, corner=True)
        add_rect(s, cx + Inches(0.3), cy + Inches(0.4), Inches(0.18), Inches(0.18), fill=ACCENT, corner=True)
        add_text(s, cx + Inches(0.6), cy + Inches(0.12), cw - Inches(0.8), Inches(0.4), name, size=14, bold=True, color=INK)
        add_text(s, cx + Inches(0.6), cy + Inches(0.45), cw - Inches(0.8), Inches(0.5), desc, size=11, color=MUTED)
    add_footer(s, num, total)

feature_slide(5, slides_total, "Phase 1 · Launch (months 0–4)",
              "Foundations: Book, Your Spot, Prep+After, Calendar, Wallet.",
              "Everything a customer needs in their first 90 days.", [
    ("Multilingual onboarding", "EN + FR at launch."),
    ("Location auto-detect", "Home location set; cross-location travel mode."),
    ("Book flow · multi-service", "Combo bookings (wax + brow, etc.) in one slot."),
    ("Wait-list", "Push notification when a slot opens."),
    ("Service browser", "Nails · wax · laser · skin. Filter by location."),
    ("Technician selection", "Photo + bio (opt-in by tech). Re-book the same person."),
    ("One-tap re-book", "\"Same as last time.\""),
    ("Your Spot · favorites", "Home location, favorite tech, history."),
    ("Cadence-aware push", "\"Your wax is due in 6 days.\""),
    ("Prep guides per service", "\"Don't shave 24 hr before wax.\""),
    ("Aftercare push", "\"Your laser was yesterday — read this 2-min guide.\""),
    ("The Calendar", "Recurring schedule + laser series tracking."),
    ("Membership wallet", "Multi-location credit + gift card balance."),
    ("Concierge chat (AI)", "Bilingual EN/FR booking + prep coach."),
    ("Visual search", "Nail look from Instagram → matching service."),
    ("The Studio (web admin)", "Multi-location dashboard, scheduling, franchise admin."),
])

feature_slide(6, slides_total, "Phase 2 · Depth (months 5–9)",
              "Booking integration deepening, B2B, multi-city.",
              "Features that turn launch into the booking standard for the category.", [
    ("Booker / Mindbody two-way sync", "Real-time tech availability across systems."),
    ("Photo skin-prep check (cautious)", "Opt-in pre-laser flag. Never diagnostic."),
    ("Franchise-owner B2B portal", "Per-franchise dashboard with revenue + retention."),
    ("Multi-city travel mode", "\"I'm in NYC for the weekend — find a Ten Spot.\""),
    ("Loyalty redesign", "Cadence-based tiers, not just dollars."),
    ("Gift card scheduled-delivery", "Wedding / shower / birthday rituals."),
    ("Returns triage AI", "No-show vs cancel-fee dispute resolution."),
    ("Demand-sensing AI", "Surfaces under-utilised time slots."),
])

feature_slide(7, slides_total, "Phase 3 · Cultural authority (months 10+)",
              "From an app to the booking standard.",
              "Long-form storytelling, community, operational AI.", [
    ("Editorial / journal", "Long-form on bodily autonomy, beauty-bar history, technician craft."),
    ("Annual VOICES film series", "Long-tenure technicians, founder stories."),
    ("Multilingual content scaling AI", "EN-first, AI drafts FR/ES for editor review."),
    ("Counterfeit gift-card detection", "Resale market monitoring."),
    ("VIP signal detection", "Concierge welcomes high-frequency customers."),
    ("Franchise-recruitment portal", "Prospective franchise owner pipeline."),
    ("Demand-sensing for pricing", "Surfaces optimal pricing per service per location."),
    ("Multi-state data residency", "As US expansion grows — separate data store per state if required."),
])

# 8. ONBOARDING
def slide_onboarding():
    s = add_slide()
    add_section_header(s, "User experience", "Onboarding — under 90 seconds, in EN or FR.")
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.4), "First screen is location-aware. Your home location auto-set. Your favorite services surface first.", size=14, color=MUTED)
    steps = [
        ("01", "Bonjour", "Welcome in two languages.\nTap your language; everything follows."),
        ("02", "Sign in", "Apple, Google, or email.\nPhone optional (text reminders)."),
        ("03", "Your home", "Auto-detect or pick from\n33+ locations."),
        ("04", "Your services", "Nails · wax · laser · skin.\nWhich do you book?"),
        ("05", "First moment", "See the next due appointment —\nor book a fresh one."),
    ]
    x = Inches(0.6); y = Inches(2.9); w = Inches(2.3); h = Inches(3.6); gap = Inches(0.2)
    for i, (n, t, d) in enumerate(steps):
        cx = x + (w + gap) * i
        add_rect(s, cx, y, w, h, fill=WHITE, line=LINE, corner=True)
        add_text(s, cx + Inches(0.3), y + Inches(0.3), w - Inches(0.6), Inches(0.5), n, font=SERIF, size=28, color=ACCENT_DEEP)
        add_text(s, cx + Inches(0.3), y + Inches(1.0), w - Inches(0.6), Inches(0.5), t, size=14, bold=True, color=INK)
        add_text(s, cx + Inches(0.3), y + Inches(1.55), w - Inches(0.6), Inches(2.0), d, size=11, color=MUTED)
        if i < len(steps) - 1:
            add_arrow(s, cx + w + Inches(0.01), y + Inches(1.6), Inches(0.18), Inches(0.4), color=ACCENT)
    add_text(s, Inches(0.6), Inches(6.7), Inches(12), Inches(0.4), "DESIGN PRINCIPLE   —   Body data is opt-in. Sensitive flags route to technician, never to marketing AI.", size=11, bold=True, color=ACCENT_DEEP)
    add_footer(s, 8, slides_total)
slide_onboarding()

# 9-11 journeys
def journey_slide(num, total, eyebrow, title, intro, steps):
    s = add_slide()
    add_section_header(s, eyebrow, title)
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.4), intro, size=14, color=MUTED)
    n = len(steps)
    arrow_w = Inches(0.25); arrow_gap = Inches(0.05)
    box_w = (Inches(12.0) - arrow_w * (n - 1) - arrow_gap * 2 * (n - 1)) / n
    box_h = Inches(3.7); y = Inches(2.8); x = Inches(0.6)
    for i, (label, what, ux) in enumerate(steps):
        add_rect(s, x, y, box_w, box_h, fill=WHITE, line=LINE, corner=True)
        add_rect(s, x, y, box_w, Inches(0.55), fill=ACCENT, corner=True)
        add_text(s, x + Inches(0.2), y + Inches(0.05), box_w - Inches(0.4), Inches(0.45), label, size=11, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
        add_text(s, x + Inches(0.25), y + Inches(0.75), box_w - Inches(0.5), Inches(0.7), what, size=13, bold=True, color=INK)
        add_text(s, x + Inches(0.25), y + Inches(1.6), box_w - Inches(0.5), Inches(2.0), ux, size=10, color=MUTED)
        if i < n - 1:
            add_arrow(s, x + box_w + arrow_gap, y + Inches(1.65), arrow_w, Inches(0.4), color=ACCENT)
            x = x + box_w + arrow_w + arrow_gap * 2
        else: x = x + box_w
    add_footer(s, num, total)

journey_slide(9, slides_total, "User flow · 1 of 3", "First booking → recurring customer.",
    "From a curious tap to a 4-week wax cadence in three months.",
    [
        ("DISCOVER", "Sees the brand", "Friend recommends. Installs the app. Picks Leslieville as home location."),
        ("BOOK", "First Brazilian wax", "Picks first-time-friendly Jess. Reads the 24-hour prep guide. Books Sat 2pm."),
        ("PREP", "Day-before push", "App reminds: don't shave, exfoliate tonight, skip caffeine tomorrow. Customer arrives prepared."),
        ("AFTER", "48-hr aftercare", "Push: \"No sun for 24 hr. Apply post-wax oil tonight.\" Care continues."),
        ("CADENCE", "4 weeks later", "Push: \"Your wax is due — same time, same Jess?\" Books in 3 taps. Now a recurring customer."),
    ])

journey_slide(10, slides_total, "User flow · 2 of 3", "Cross-location customer — the traveling regular.",
    "The app turns 33 separate locations into one brand experience.",
    [
        ("HOME", "Books at Leslieville", "Em is a Toronto local. Home location: Leslieville. Books wax + brow there every 4 weeks."),
        ("TRAVEL", "Weekend in Yorkville", "Saturday plans take her to Yorkville. App suggests: \"Yorkville also has Lara — she does your same lash style.\""),
        ("BOOK", "One-tap cross-location", "Books lash refill at Yorkville without leaving the app. Member credit applies."),
        ("HISTORY", "Both locations in archive", "Service history shows both. Cadence detection still works across locations."),
        ("LOYALTY", "Multi-location LTV", "Em is now a 2-location customer. Brand earns more visits, more LTV."),
    ])

journey_slide(11, slides_total, "User flow · 3 of 3", "Sensitive-skin customer pre-laser — when to defer.",
    "The brand's reputation depends on never giving medical advice.",
    [
        ("DISCLOSE", "Sensitive skin opt-in", "Tia notes she has reactive skin. App stores it (specialist-only access)."),
        ("BOOK", "Books laser session 4 of 6", "App routes booking to Mia, who's done sensitive-skin work for 3 yr."),
        ("AI FLAG", "Recent sunburn detected", "Customer mentions \"I got a bit of sun last weekend.\" AI: \"Recommend rescheduling — sun + laser is risk.\""),
        ("TECH CONSULT", "Mia confirms", "Mia (specialist) reviews. Reschedules to next week. Customer thanks brand for not damaging her skin."),
        ("TRUST", "Brand earned it", "What another brand might have run as scheduled, Ten Spot handled correctly. Tia stays loyal."),
    ])

# 12. SCREENS
def slide_screens():
    s = add_slide()
    add_section_header(s, "Visual reference", "What it looks like in hand.")
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.4), "Wireframe-fidelity mockups in the brand palette — soft pink-cream, hot pink, matte black, gold.", size=14, color=MUTED)
    screens = [
        ("Onboarding", "EN/FR · sign-in"), ("Home", "Next + due"), ("Book", "Multi-service combo"),
        ("Your Spot", "Favs + history"), ("Service", "Prep + after"), ("Calendar", "Recurring schedule"),
        ("Wallet", "Member + gift card"), ("Concierge", "Booking AI"), ("Profile", "Data · privacy"),
    ]
    cols = 5; cw = Inches(2.3); ch = Inches(2.0); gx = Inches(0.15); gy = Inches(0.25)
    x0 = Inches(0.6); y0 = Inches(2.7)
    for i, (name, sub) in enumerate(screens):
        c = i % cols; r = i // cols
        x = x0 + (cw + gx) * c; y = y0 + (ch + gy) * r
        add_rect(s, x, y, cw, ch, fill=INK, corner=True)
        add_rect(s, x + Inches(0.1), y + Inches(0.1), cw - Inches(0.2), ch - Inches(0.2), fill=BG, corner=True)
        add_rect(s, x + Inches(0.1), y + Inches(0.1), cw - Inches(0.2), Inches(0.4), fill=ACCENT, corner=True)
        add_text(s, x + Inches(0.2), y + Inches(0.13), cw - Inches(0.4), Inches(0.35), name, size=10, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
        add_text(s, x + Inches(0.2), y + Inches(0.7), cw - Inches(0.4), Inches(1.2), sub, size=10, color=MUTED)
    add_text(s, Inches(0.6), Inches(7.0), Inches(12), Inches(0.4), "Full interactive HTML mockup available — opens in any browser.", size=10, color=ACCENT_DEEP)
    add_footer(s, 12, slides_total)
slide_screens()

# 13. AI Tier 1
def ai_tier_slide(num, total, eyebrow, title, intro, items):
    s = add_slide()
    add_section_header(s, eyebrow, title)
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.4), intro, size=14, color=MUTED)
    cols = 2; cw = Inches(6.0); ch = Inches(1.0); gap = Inches(0.15)
    x0 = Inches(0.6); y0 = Inches(2.9)
    for i, (name, desc) in enumerate(items):
        c = i % cols; r = i // cols
        x = x0 + (cw + gap) * c; y = y0 + (ch + gap) * r
        add_rect(s, x, y, cw, ch, fill=WHITE, line=LINE, corner=True)
        add_rect(s, x + Inches(0.25), y + Inches(0.25), Inches(0.5), Inches(0.5), fill=GOLD_SOFT, corner=True)
        add_text(s, x + Inches(0.25), y + Inches(0.25), Inches(0.5), Inches(0.5), "✦", font=SERIF, size=18, color=ACCENT_DEEP, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        add_text(s, x + Inches(0.85), y + Inches(0.15), cw - Inches(1.1), Inches(0.4), name, size=14, bold=True, color=INK)
        add_text(s, x + Inches(0.85), y + Inches(0.5), cw - Inches(1.1), Inches(0.5), desc, size=11, color=MUTED)
    add_footer(s, num, total)

ai_tier_slide(13, slides_total, "Intelligence · Tier 1", "AI in service of booking and prep, not body data.",
    "Every Tier 1 feature reduces friction or deepens trust.",
    [
        ("Concierge chat (Sonnet)", "Bilingual EN/FR. Books, prepares, answers — never diagnoses."),
        ("Cadence-aware push", "Detects \"your wax is due\" from booking history."),
        ("First-time-friendly walk-through", "AI walks new customers through what to expect."),
        ("Multilingual translation (EN/FR)", "Brand glossary preserves Spotted, Ten Spot."),
        ("Visual search", "Photograph a nail look — find the matching service."),
        ("Prep guide retrieval", "Service-aware: AI surfaces the right prep guide before booking."),
    ])

ai_tier_slide(14, slides_total, "Intelligence · Tier 2 & 3", "AI that powers integrations and the back office.",
    "Phase 2 customer-facing AI plus operational AI the customer never sees.",
    [
        ("Booker/Mindbody two-way sync", "SLA-grade real-time tech availability."),
        ("Photo skin-prep check (cautious)", "Opt-in, never diagnostic, surfaces \"reschedule\" recommendations."),
        ("Demand-sensing AI", "Surfaces under-utilised time slots, optimal pricing."),
        ("Returns triage AI", "Routes no-show disputes vs cancel-fee disputes."),
        ("Multilingual content scaling", "EN-first, AI drafts FR/ES, editors approve."),
        ("Counterfeit gift-card detection", "Resale market monitoring."),
        ("Franchise-recruitment AI", "Lead-quality scoring for prospective franchise owners."),
        ("Multi-state data residency enforcement", "Audit-log monitor as US expansion grows."),
    ])

# 15. DATA
def slide_data():
    s = add_slide()
    add_section_header(s, "Data with consent", "What we collect — and what we won't.")
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.4), "Default to opt-in per category. Sensitivity flags route to technician, never to marketing AI.", size=14, color=MUTED)
    items = [
        ("Identity & contact", "email, name, phone — bookings, reminders."),
        ("Location", "home location; current location opt-in for travel mode."),
        ("Service history", "what, where, when, with whom."),
        ("Sensitivities (opt-in)", "skin reactivity, pregnancy, medications — specialist-only."),
        ("Membership / billing", "tier, gift cards, credit balance."),
        ("Preferences", "favorite location, technician, services."),
        ("Engagement", "booking funnel, prep-guide views."),
        ("Channel of origin", "online / referral / walk-in."),
    ]
    cols = 2; cw = Inches(6.0); ch = Inches(0.85); gap = Inches(0.12)
    x0 = Inches(0.6); y0 = Inches(2.9)
    for i, (name, desc) in enumerate(items):
        c = i % cols; r = i // cols
        x = x0 + (cw + gap) * c; y = y0 + (ch + gap) * r
        add_rect(s, x, y, cw, ch, fill=WHITE, line=LINE, corner=True)
        add_rect(s, x + Inches(0.3), y + Inches(0.32), Inches(0.18), Inches(0.18), fill=ACCENT, corner=True)
        add_text(s, x + Inches(0.6), y + Inches(0.1), cw - Inches(0.8), Inches(0.4), name, size=13, bold=True, color=INK)
        add_text(s, x + Inches(0.6), y + Inches(0.42), cw - Inches(0.8), Inches(0.4), desc, size=11, color=MUTED)
    y = Inches(6.65)
    add_rect(s, Inches(0.6), y, Inches(12.1), Inches(0.5), fill=ACCENT, corner=True)
    add_text(s, Inches(0.85), y + Inches(0.05), Inches(11.8), Inches(0.4), "WE DO NOT COLLECT  ·  weight or BMI  ·  before/after body photos  ·  precise GPS without explicit opt-in  ·  diagnosed conditions", size=11, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    add_footer(s, 15, slides_total)
slide_data()

# 16. STACK
def slide_stack():
    s = add_slide()
    add_section_header(s, "How it's built", "A modern stack — boring where it should be, sharp where it counts.")
    groups = [
        ("Mobile", ["React Native + Expo (iOS & Android)", "OTA updates for booking-flow iteration", "Apple / Google sign-in"]),
        ("Booking", ["Booker or Mindbody integration (TBD)", "Real-time tech availability sync", "Multi-location credit + gift card"]),
        ("Studio backend", ["Node + TypeScript API", "Postgres + pgvector for visual search", "RBAC: corporate vs franchise-owner"]),
        ("Intelligence", ["Claude (Sonnet 4.6 chat, Haiku 4.5 batch)", "Bilingual prompts EN/FR", "PostHog analytics, Sentry errors"]),
    ]
    x0 = Inches(0.6); y0 = Inches(2.5); cw = Inches(3.0); ch = Inches(4.0); gap = Inches(0.15)
    for i, (title, items) in enumerate(groups):
        x = x0 + (cw + gap) * i
        add_rect(s, x, y0, cw, ch, fill=WHITE, line=LINE, corner=True)
        add_rect(s, x, y0, cw, Inches(0.7), fill=ACCENT, corner=True)
        add_text(s, x + Inches(0.3), y0 + Inches(0.1), cw - Inches(0.6), Inches(0.55), title, font=SERIF, size=18, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
        by = y0 + Inches(0.95)
        for itm in items:
            add_text(s, x + Inches(0.25), by, cw - Inches(0.4), Inches(0.35), "•  " + itm, size=11, color=INK)
            by += Inches(0.45)
    add_footer(s, 16, slides_total)
slide_stack()

# 17. STUDIO
def slide_studio():
    s = add_slide()
    add_section_header(s, "The Studio · web admin portal", "Multi-location franchise admin — most complex Studio in the SEYSO portfolio.")
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.8),
             ("Customers use the mobile app. Your team uses The Studio. "
              "Same backend, same brand language. RBAC for corporate vs "
              "franchise-owner views."),
             size=14, color=MUTED)
    add_rect(s, Inches(4.5), Inches(3.0), Inches(4.3), Inches(0.85), fill=WHITE, line=LINE, corner=True)
    add_text(s, Inches(4.7), Inches(3.05), Inches(3.9), Inches(0.4), "BOOKER / MINDBODY", size=10, bold=True, color=ACCENT_DEEP)
    add_text(s, Inches(4.7), Inches(3.40), Inches(3.9), Inches(0.4), "Existing booking system — sync, never replace", size=11, color=MUTED)
    add_rect(s, Inches(0.6), Inches(4.2), Inches(12.1), Inches(0.7), fill=ACCENT_SOFT, corner=True)
    add_text(s, Inches(0.85), Inches(4.27), Inches(11.6), Inches(0.4), "SHARED API · Postgres · Auth · AI gateway · Multi-location calendar · RBAC · Per-franchise pricing", size=11, bold=True, color=ACCENT_DEEP, anchor=MSO_ANCHOR.MIDDLE)
    add_rect(s, Inches(0.6), Inches(5.2), Inches(5.95), Inches(1.6), fill=WHITE, line=LINE, corner=True)
    add_rect(s, Inches(0.6), Inches(5.2), Inches(5.95), Inches(0.4), fill=ACCENT, corner=True)
    add_text(s, Inches(0.85), Inches(5.22), Inches(5.45), Inches(0.4), "MOBILE APP — IOS & ANDROID", size=10, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(0.85), Inches(5.7), Inches(5.45), Inches(1.0), ("Customer-facing · Book · Your Spot · Prep+After · Calendar · Wallet · Spotted"), size=11, color=INK)
    add_rect(s, Inches(6.75), Inches(5.2), Inches(5.95), Inches(1.6), fill=WHITE, line=LINE, corner=True)
    add_rect(s, Inches(6.75), Inches(5.2), Inches(5.95), Inches(0.4), fill=INK, corner=True)
    add_text(s, Inches(7.0), Inches(5.22), Inches(5.45), Inches(0.4), "THE STUDIO — WEB ADMIN PORTAL", size=10, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(7.0), Inches(5.7), Inches(5.45), Inches(1.0), ("Internal · multi-location dashboard · scheduling · franchise admin · catalog (per-location pricing) · concierge"), size=11, color=INK)
    add_text(s, Inches(0.6), Inches(7.0), Inches(12), Inches(0.4), ("BUILT FOR YOUR TEAM   —   Kristen + corporate ops + 33+ franchise owners + technicians. RBAC throughout."), size=10, bold=True, color=ACCENT_DEEP)
    add_footer(s, 17, slides_total)
slide_studio()

# 18. ROADMAP
def slide_roadmap():
    s = add_slide()
    add_section_header(s, "How we'll deliver", "Roadmap — first nine months.")
    phases = [
        ("Discovery", "Weeks 1–2", "Customer interviews — high-frequency cult-fan, new customer post-first-visit, Quebec-FR customer, franchise owner, corporate ops staff. Audit existing booking system. Confirm Booker/Mindbody integration. Lock Phase 1 scope."),
        ("Phase 1 build", "Weeks 3–18", "Book · Your Spot · Prep+After · Calendar · Wallet · Spotted · Tier 1 AI · The Studio. EN/FR at launch. Booking-system integration scoped separately."),
        ("Phase 2 build", "Weeks 19–32", "Booker/Mindbody two-way sync at SLA-grade, franchise B2B portal, multi-city travel mode, demand-sensing."),
        ("Phase 3 build", "Weeks 33–40+", "Editorial, VOICES films, content scaling, counterfeit gift-card detection, franchise-recruitment portal."),
    ]
    y = Inches(2.5)
    add_rect(s, Inches(0.6), y + Inches(0.5), Inches(12.1), Pt(2), fill=LINE)
    cw = Inches(3.0); gap = Inches(0.05); x0 = Inches(0.6)
    for i, (name, when, detail) in enumerate(phases):
        x = x0 + (cw + gap) * i
        add_rect(s, x + cw/2 - Inches(0.1), y + Inches(0.4), Inches(0.2), Inches(0.2), fill=ACCENT, corner=True)
        add_rect(s, x, y + Inches(0.85), cw, Inches(3.6), fill=WHITE, line=LINE, corner=True)
        add_text(s, x + Inches(0.3), y + Inches(1.0), cw - Inches(0.6), Inches(0.4), when, size=10, bold=True, color=ACCENT_DEEP)
        add_text(s, x + Inches(0.3), y + Inches(1.4), cw - Inches(0.6), Inches(0.6), name, font=SERIF, size=22, color=INK)
        add_text(s, x + Inches(0.3), y + Inches(2.3), cw - Inches(0.6), Inches(2.0), detail, size=11, color=MUTED)
    add_footer(s, 18, slides_total)
slide_roadmap()

# 19. METRICS
def slide_metrics():
    s = add_slide()
    add_section_header(s, "How we'll know it's working", "The metrics that matter.")
    metrics = [
        ("App-booked %", "% of total bookings via app vs phone", "Target ≥ 70% by month 12"),
        ("Booking conversion", "% of booking funnel completed", "Target ≥ 75%"),
        ("No-show rate", "Bookings missed without notice", "Target ≤ 4% across all locations"),
        ("Cadence adherence", "% of customers booking on detected cadence", "Target ≥ 60%"),
        ("Multi-location spread", "Avg locations per active customer", "Target ≥ 1.4 by month 9"),
        ("Bilingual reach", "% of sessions in FR (Quebec)", "Target ≥ 12% by month 12"),
    ]
    cols = 3; cw = Inches(4.0); ch = Inches(2.0); gap = Inches(0.1)
    x0 = Inches(0.6); y0 = Inches(2.8)
    for i, (name, desc, target) in enumerate(metrics):
        c = i % cols; r = i // cols
        x = x0 + (cw + gap) * c; y = y0 + (ch + gap) * r
        add_rect(s, x, y, cw, ch, fill=WHITE, line=LINE, corner=True)
        add_text(s, x + Inches(0.3), y + Inches(0.2), cw - Inches(0.6), Inches(0.4), name, size=14, bold=True, color=ACCENT_DEEP)
        add_text(s, x + Inches(0.3), y + Inches(0.65), cw - Inches(0.6), Inches(0.9), desc, size=11, color=MUTED)
        add_text(s, x + Inches(0.3), y + Inches(1.5), cw - Inches(0.6), Inches(0.4), target, font=SERIF, size=14, color=INK)
    add_footer(s, 19, slides_total)
slide_metrics()

# 20. PRINCIPLES
def slide_principles():
    s = add_slide()
    add_section_header(s, "How it will feel", "Design principles.")
    items = [
        ("Booking is the product", "Make it the fastest one in the category. One-tap re-book is the win."),
        ("Cadence over urgency", "\"Your wax is due\" is calm. No fake urgency, no countdown timers."),
        ("Sensitive flags route to humans", "Skin reactivity, pregnancy, meds → technician. Never marketing AI."),
        ("Multi-location is one brand", "Em moves between Leslieville and Yorkville without re-onboarding."),
        ("Recognition over discount", "Spotted rewards visits, reviews, referrals. Not new-customer bribes."),
        ("Cosmetic, never medical", "Laser is cosmetic. AI never diagnoses skin conditions."),
    ]
    cols = 2; cw = Inches(6.0); ch = Inches(1.4); gap = Inches(0.15)
    x0 = Inches(0.6); y0 = Inches(2.7)
    for i, (name, desc) in enumerate(items):
        c = i % cols; r = i // cols
        x = x0 + (cw + gap) * c; y = y0 + (ch + gap) * r
        add_rect(s, x, y, cw, ch, fill=WHITE, line=LINE, corner=True)
        add_text(s, x + Inches(0.3), y + Inches(0.2), cw - Inches(0.6), Inches(0.4), name, size=14, bold=True, color=ACCENT_DEEP)
        add_text(s, x + Inches(0.3), y + Inches(0.65), cw - Inches(0.6), Inches(1.0), desc, size=11, color=MUTED)
    add_footer(s, 20, slides_total)
slide_principles()

# 21. PARTNERSHIP
def slide_team():
    s = add_slide()
    add_section_header(s, "Working together", "How we'd partner.")
    cards = [
        ("Discovery sprint", "Two weeks. Customer + franchise-owner + corporate ops interviews. Audit existing booking system. Walk away with a signed Phase 1 spec."),
        ("Embedded delivery", "A small team — lead engineer, mobile engineer, designer, bilingual QA — works as an extension of yours. Weekly demos."),
        ("Booking-system integration scoped separately", "Booker / Mindbody / current-system migration is its own project — typically 4-8 weeks of additional work."),
        ("Always your data", "Source code, customer data, AI logs, multi-location calendar all live in your accounts."),
    ]
    cols = 2; cw = Inches(6.0); ch = Inches(2.0); gap = Inches(0.15)
    x0 = Inches(0.6); y0 = Inches(2.5)
    for i, (name, desc) in enumerate(cards):
        c = i % cols; r = i // cols
        x = x0 + (cw + gap) * c; y = y0 + (ch + gap) * r
        add_rect(s, x, y, cw, ch, fill=WHITE, line=LINE, corner=True)
        add_text(s, x + Inches(0.3), y + Inches(0.3), cw - Inches(0.6), Inches(0.5), name, font=SERIF, size=20, color=ACCENT_DEEP)
        add_text(s, x + Inches(0.3), y + Inches(0.95), cw - Inches(0.6), Inches(1.1), desc, size=12, color=MUTED)
    add_footer(s, 21, slides_total)
slide_team()

# 22. WHY THIS WORKS
def slide_why():
    s = add_slide()
    add_section_header(s, "Why this works for The Ten Spot", "The bet behind the build.")
    pts = [
        ("Multi-location is your moat", "33+ locations is the largest in the category. The app makes them feel like one brand to the customer — competitors with 5–10 locations can't match."),
        ("Recurring is your LTV", "A wax customer at 4-week cadence = 13 visits/year. The Calendar's cadence detection lifts that by 1–2 visits per customer per year. Real money."),
        ("Self-service booking saves franchise hours", "10–15 hours/week of phone-bound staff time per location × 33 locations = serious operational savings."),
        ("AI in service of trust, not body data", "We use AI to book, prep, route. Never to diagnose skin or push services. The brand's reputation is safer for the building."),
    ]
    y = Inches(2.5)
    for i, (head, body) in enumerate(pts):
        cy = y + Inches(1.05) * i
        add_rect(s, Inches(0.6), cy, Inches(0.08), Inches(0.95), fill=ACCENT)
        add_text(s, Inches(0.95), cy + Inches(0.05), Inches(11.5), Inches(0.4), head, font=SERIF, size=20, color=INK)
        add_text(s, Inches(0.95), cy + Inches(0.55), Inches(11.5), Inches(0.4), body, size=12, color=MUTED)
    add_footer(s, 22, slides_total)
slide_why()

# 23. NEXT STEP
def slide_next():
    s = add_slide()
    add_rect(s, 0, 0, SW, SH, fill=INK)
    add_rect(s, 0, 0, SW, Inches(0.25), fill=ACCENT)
    for cx, cy, r in [(11.0, 1.4, 0.20), (12.4, 3.0, 0.14), (10.4, 4.2, 0.22), (12.0, 5.6, 0.16), (11.2, 6.4, 0.12)]:
        d = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(cx-r), Inches(cy-r), Inches(2*r), Inches(2*r))
        d.fill.solid(); d.fill.fore_color.rgb = ACCENT; d.line.fill.background(); d.shadow.inherit = False
    add_text(s, Inches(0.6), Inches(0.55), Inches(8), Inches(0.3), "NEXT STEP", size=11, bold=True, color=ACCENT)
    add_text(s, Inches(0.6), Inches(1.1), Inches(11), Inches(2.0), "A two-week paid discovery.", font=SERIF, size=54, color=WHITE)
    add_text(s, Inches(0.6), Inches(2.7), Inches(10.5), Inches(2.0),
             ("We sit with your team. We talk to ten of your customers and "
              "five of your franchise owners. We audit the existing booking "
              "system and confirm the integration approach. We come back "
              "with a lockable Phase 1 scope and a working prototype of "
              "the Book and Calendar flows in EN and FR."),
             size=18, color=GOLD_SOFT)
    add_text(s, Inches(0.6), Inches(5.1), Inches(11), Inches(0.5), "WHAT YOU GET", size=11, bold=True, color=ACCENT)
    add_text(s, Inches(0.6), Inches(5.5), Inches(11), Inches(2.0),
             ("•  A lockable feature scope, costed and timeboxed\n"
              "•  An interactive prototype of two core flows\n"
              "•  A summary of customer + franchise-owner interviews\n"
              "•  A go / no-go recommendation. Yours either way."),
             size=14, color=WHITE)
    add_footer(s, 23, slides_total, on_dark=True)
slide_next()

out = Path(__file__).parent / "The-Ten-Spot-Pitch.pptx"
prs.save(out)
print(f"wrote {out}  ({len(prs.slides)} slides)")
