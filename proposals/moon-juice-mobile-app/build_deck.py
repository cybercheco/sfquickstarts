"""Build the Moon Juice client pitch deck (.pptx). Features-only."""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pathlib import Path

INK         = RGBColor(0x2a, 0x1f, 0x3d)
MUTED       = RGBColor(0x8b, 0x81, 0x94)
LINE        = RGBColor(0xe6, 0xdf, 0xd0)
BG          = RGBColor(0xf5, 0xf0, 0xeb)
ACCENT      = RGBColor(0x8b, 0x6f, 0xbf)
ACCENT_DEEP = RGBColor(0x4a, 0x38, 0x78)
ACCENT_SOFT = RGBColor(0xe7, 0xde, 0xfa)
GOLD        = RGBColor(0xc9, 0xa8, 0x5e)
GOLD_SOFT   = RGBColor(0xf3, 0xe8, 0xc7)
PINK        = RGBColor(0xd8, 0xa8, 0xb5)
PINK_SOFT   = RGBColor(0xf5, 0xe2, 0xe6)
MINT        = RGBColor(0x9b, 0xb8, 0xa0)
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
             "Moon Juice · Mobile App Pitch", size=9, color=color)
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
             "MOBILE APP · PITCH", size=11, bold=True, color=ACCENT)
    add_text(s, Inches(0.85), Inches(1.45), Inches(8), Inches(2.0),
             "Moon Juice.", font=SERIF, size=66, color=INK)
    add_text(s, Inches(0.85), Inches(2.7), Inches(7.5), Inches(1.6),
             "Your daily ritual,\nguided.",
             font=SERIF, size=28, color=ACCENT)
    add_text(s, Inches(0.85), Inches(5.6), Inches(7.5), Inches(0.4),
             "An adaptogen coach in the customer's pocket.",
             size=14, color=MUTED)
    add_text(s, Inches(0.85), Inches(6.0), Inches(7.5), Inches(0.3),
             "Prepared for the Moon Juice team",
             size=11, color=MUTED)
slide_cover()

# OPPORTUNITY
def slide_opportunity():
    s = add_slide()
    add_section_header(s, "Why now", "Adaptogens went mainstream. The education didn't keep up.")
    stats = [
        ("8", "Moon Dusts in the canon —\nmost customers can name 2",
         "Brain. Beauty. Sex. Spirit. Power. Sleep. Dream. Cosmic."),
        ("5+", "supplements layered by\nyour average wellness customer",
         "Stacking guidance happens on Reddit and DMs. It deserves the app."),
        ("$20M", "annual sales (2021)\nbuilt on cult brand mythology",
         "An app turns mythology into daily ritual — and lifetime LTV."),
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

# VISION
def slide_vision():
    s = add_slide()
    add_section_header(s, "The vision", "Not another store — an adaptogen coach.")
    add_text(s, Inches(0.6), Inches(2.3), Inches(12), Inches(2.5),
             ("Moon Juice's customer asks the same three questions every "
              "time she shops: which Moon Dust is for me, when do I take "
              "it, and can I combine it with what I'm already taking?\n\n"
              "Today she answers them by reading Amanda's Instagram, the "
              "Moon Juice Manual, and a tab full of forum posts. The app "
              "should be the answer — a Ritual coach that guides her stack, "
              "an Apothecary that explains every adaptogen, a goal-driven "
              "recommender, and a Refill Vault that manages her "
              "subscriptions calmly."),
             font=SERIF, size=20, color=INK)
    add_text(s, Inches(0.6), Inches(5.8), Inches(12), Inches(0.4),
             "WHY IT MATTERS", size=10, bold=True, color=ACCENT)
    add_text(s, Inches(0.6), Inches(6.1), Inches(12), Inches(1.5),
             ("• Turns one-time supplement buyers into daily ritual practitioners — highest-LTV shape in the category\n"
              "• Surfaces the Moon Dust mythology with science, sourcing, and citations — the brand's actual moat\n"
              "• Makes refill subscriptions humane (skip / pause / accelerate) and reduces churn"),
             size=13, color=INK)
    add_footer(s, 3, slides_total)
slide_vision()

# 4. SIX PILLARS
def slide_pillars():
    s = add_slide()
    add_section_header(s, "Product overview", "Six pillars — five customer-facing, one internal.")
    pillars = [
        ("The Ritual", "Daily morning / midday / evening routines — guided audio, no streaks.", ACCENT),
        ("The Apothecary", "Per-product passport with adaptogen sourcing, dosing, citations, interactions.", GOLD),
        ("The Goals", "Pick goals — calm, sleep, beauty, brain, energy, libido — get a stack with rationale.", PINK),
        ("The Refill Vault", "Calm subscription management — skip, pause, bundle, vacation mode.", MINT),
        ("The Shop", "DTC, multi-currency, drops, refill credit redemption.", ACCENT_DEEP),
        ("The Studio", "Internal-facing web admin portal — Apothecary editor, ritual library, refill ops, compliance review.", INK),
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
              "Foundations: Ritual, Apothecary, Goals, Refill Vault, Shop, Glow.",
              "Everything a customer needs in their first 90 days.", [
    ("Multilingual onboarding", "EN + ES at launch · FR expandable."),
    ("Multi-currency storefront", "USD · CAD · GBP · EUR."),
    ("The Ritual cards", "Morning / midday / evening routines — guided audio, no streaks."),
    ("Calm reminders", "Opt-in nudges; never gamified or shaming."),
    ("The Apothecary passport", "Per-product adaptogens, dosing, sourcing, citations."),
    ("Adaptogen reference library", "Per-adaptogen page with evidence and contraindications."),
    ("Goal-to-stack AI", "Pick calm, sleep, brain, beauty, energy, libido → stack with rationale."),
    ("Refill Vault", "Skip / pause / accelerate / bundle / vacation mode."),
    ("Smart refill prediction", "Usage-based — never pushy."),
    ("Refill bottle returns + credit", "Sustainable bottle program tracked in-app."),
    ("Apothecary chat (AI)", "Multilingual coach with strict compliance guardrails."),
    ("Rx interaction warnings", "AI flags interactions when customer enters medication; never overrides physician."),
    ("Drops + restock alerts", "Region-aware push."),
    ("Bundle builder", "Pair Moon Dusts + supplements with refill credit redemption."),
    ("Glow loyalty", "Recognition for ritual completion, refill returns, reviews — never streaks."),
    ("The Studio (web admin)", "Apothecary editor, ritual library, refill ops, compliance review, concierge, analytics."),
])

feature_slide(6, slides_total, "Phase 2 · Depth (months 5–9)",
              "AR ritual, practitioner B2B, health-data integrations.",
              "Features that turn launch into a category-defining wellness brand experience.", [
    ("AR ritual visualization", "See your stack laid out for the day in your kitchen."),
    ("Smart-stack adapter", "Adjusts based on cycle, sleep, stress (opt-in)."),
    ("Practitioner B2B portal", "Naturopaths / coaches with white-label client tracking."),
    ("Apple Health / Google Fit integration", "Sleep + steps inform Ritual nudges (opt-in)."),
    ("Live coach Q&A", "Quarterly with Amanda + practitioners."),
    ("Adaptogen library expansion", "Full evidence base, peer-reviewed citations."),
    ("Custom blends (curated)", "Staff-blends for specific goals; no full personalisation."),
    ("Returns triage AI", "Routes refund vs replacement vs adjustment."),
])

feature_slide(7, slides_total, "Phase 3 · Cultural authority (months 10+)",
              "From an app to a wellness institution.",
              "Long-form storytelling, education, operational AI.", [
    ("Editorial / journal", "Long-form on adaptogens, ritual, science."),
    ("Annual VOICES film series", "Amanda + practitioners + scientists."),
    ("Multilingual content scaling AI", "EN-first, AI drafts ES/FR/IT/JP/DE for editor review."),
    ("Demand-sensing AI", "Wishlist + Stack signals feed harvest planning."),
    ("Counterfeit listing detection", "Amazon, eBay, AliExpress."),
    ("Practitioner certification", "Moon Juice-trained wellness coaches."),
    ("VIP signal detection", "Concierge welcomes top-tier supporters."),
    ("Cycle + hormone awareness (opt-in, careful)", "Stack adapts to phase; FDA / FTC review on every claim."),
])

# 8. ONBOARDING
def slide_onboarding():
    s = add_slide()
    add_section_header(s, "User experience", "Onboarding — under 90 seconds, in EN or ES.")
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.4),
             "The first screen earns trust by asking what the customer is working on — and what she's already taking.",
             size=14, color=MUTED)
    steps = [
        ("01", "Hola", "Welcome in three languages.\nTap your language; everything follows."),
        ("02", "Sign in", "Apple, Google, or email.\nNo forms."),
        ("03", "Goals", "Pick 1–3 from calm, sleep, beauty,\nbrain, energy, libido, focus."),
        ("04", "What you're already taking", "Current supplements + (optional)\nRx medications · safety filter."),
        ("05", "First moment", "Today's Ritual is yours —\nor explore the Apothecary."),
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
             "DESIGN PRINCIPLE   —   Rx disclosure is opt-in. Never diagnose. Always cite. Always defer to physicians.",
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
    "First Moon Dust → daily ritual.",
    "From an Instagram tap to a daily practice in three weeks.",
    [
        ("DISCOVER", "Sees Brain Dust",
         "Instagram post. Taps in. Reads the Apothecary passport — 7 adaptogens, citations, dosing."),
        ("BUILD", "Picks goals",
         "Calm + Brain. App proposes a stack: Brain Dust + SuperYou + SuperHair. Editable."),
        ("BUY", "Apple Pay checkout",
         "Two taps. Subscribes to Brain Dust + SuperYou. Order tracked in-app."),
        ("RITUAL", "Day 1",
         "Morning push: 'Brain Dust in your coffee.' 1:32 audio with Amanda. Marks complete (no streak)."),
        ("HABIT", "Day 21",
         "Three weeks of completed mornings. Customer is no longer buying supplements — she has a daily practice."),
    ])

journey_slide(10, slides_total,
    "User flow · 2 of 3",
    "Rx-aware Apothecary chat — when to defer to a physician.",
    "The brand's reputation depends on never giving medical advice. The app makes that automatic.",
    [
        ("ASK", "Customer asks",
         "Sasha, on Adderall, asks if she can add Brain Dust to her stack."),
        ("DETECT", "AI flags interaction",
         "Rhodiola in Brain Dust may interact with stimulants. AI declines to recommend until physician confirmation."),
        ("ESCALATE", "Concierge picks up",
         "AI escalates to human concierge. Sasha is asked for written physician confirmation via the practitioner portal."),
        ("CONFIRM", "Physician note",
         "Sasha's doctor responds via the app. Concierge updates Sasha's stack rules. Brain Dust unlocks."),
        ("TRUST", "Brand earns it",
         "What another brand might have answered casually, Moon Juice handled correctly. Sasha tells three friends."),
    ])

journey_slide(11, slides_total,
    "User flow · 3 of 3",
    "Refill Vault — turning a churned subscriber into a paused subscriber.",
    "Most brands lose customers on the cancel button. The Vault makes that rare.",
    [
        ("SIGNAL", "Skipped twice",
         "Customer skipped two consecutive refills of SuperHair. Studio flags as at-risk."),
        ("REACH", "Calm message",
         "Push notification: 'Notice you've been skipping. Want to pause for a season instead?'"),
        ("PAUSE", "Vacation mode",
         "Customer taps Pause for 60 days. No card charge. App keeps her stack visible."),
        ("RETURN", "Auto-restart",
         "60 days later, refill resumes. Customer didn't lift a finger and didn't have to phone customer service."),
        ("LTV", "Saved",
         "What would have been a churn is a 60-day pause. LTV protected. Trust intact."),
    ])

# 12. SCREENS
def slide_screens():
    s = add_slide()
    add_section_header(s, "Visual reference", "What it looks like in hand.")
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.4),
             "Wireframe-fidelity mockups in the brand palette — cosmic lavender, dusty rose, amber, sage.",
             size=14, color=MUTED)
    screens = [
        ("Onboarding", "EN/ES/FR · sign-in"),
        ("Home", "Today's ritual"),
        ("Apothecary", "Per-product passport"),
        ("Goals", "Multi-select"),
        ("Stack", "Timed routines"),
        ("Refill Vault", "Subscription mgmt"),
        ("Product", "Adaptogen pills"),
        ("Apothecary chat", "Rx-aware AI"),
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
    "AI in service of the ritual — never the diagnosis.",
    "Every Tier 1 feature operates inside compliance guardrails. Sources cited; never invented.",
    [
        ("Apothecary chat (Sonnet)", "Multilingual adaptogen + dosing coach. Strict compliance guardrails."),
        ("Goal-to-stack recommender", "Curated rules engine + AI. Cites adaptogens and timing."),
        ("Rx interaction detection", "Customer-disclosed medications flag relevant adaptogens; routes to concierge."),
        ("Smart refill prediction", "Usage-based; never pushy."),
        ("Multilingual brand-voice translation", "EN-first; AI drafts ES/FR; brand glossary preserves Moon Dust, Dust, Glow."),
        ("Visual search", "Photograph a Moon Dust on Instagram, find it in the catalog."),
    ])

ai_tier_slide(14, slides_total,
    "Intelligence · Tier 2 & 3",
    "AI that powers the practice and the back office.",
    "Phase 2 customer-facing AI plus operational AI the customer never sees.",
    [
        ("AR ritual visualization", "On-counter AR layout of your morning stack."),
        ("Smart-stack adapter", "Adjusts based on cycle, sleep, stress signals (opt-in)."),
        ("Returns triage AI", "Routes refund vs replacement vs adjustment."),
        ("Demand-sensing AI", "Wishlists + Stack signals feed harvest planning."),
        ("Multilingual content scaling", "EN-first, AI drafts six languages, editor approval."),
        ("Counterfeit-listing detection", "Amazon / eBay / AliExpress vigilance."),
        ("Cycle-aware stack (cautious)", "Phase 3 only; FDA / FTC review on every claim."),
        ("Practitioner-portal client tracking AI", "Naturopath dashboards (with HIPAA-adjacent guardrails)."),
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
        ("Goals", "calm / sleep / beauty / brain / energy / libido / focus."),
        ("Allergies & sensitivities", "for safety filters on stack recommendations."),
        ("Current Rx (opt-in)", "for interaction warnings — never shared, never sold."),
        ("Subscriptions", "active refills, usage rate."),
        ("Ritual engagement", "completions — no shaming, no streaks."),
        ("Stack history", "adaptogens used, when, paired."),
        ("Channel of origin", "online / Sephora / Amazon / referral."),
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
             "WE DO NOT COLLECT  ·  weight  ·  BMI  ·  symptom logs  ·  precise GPS  ·  contacts  ·  social-graph  ·  diagnosed conditions",
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
                       "Multi-currency USD/CAD/GBP/EUR",
                       "RevenueCat for subscriptions"]),
        ("Apothecary backend", ["Node + TypeScript API",
                                  "Postgres + pgvector for visual search",
                                  "Citation-linked claims engine"]),
        ("Intelligence", ["Claude (Sonnet 4.6 chat, Haiku 4.5 batch)",
                           "Strict compliance system prompts",
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
             "SHARED API · Postgres · Auth · AI gateway · Compliance engine · Refill ops",
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
             ("Customer-facing · Ritual · Apothecary · Goals · Stack · Refill Vault · Shop"),
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
             ("Internal · Apothecary editor · Ritual library · Compliance review · Refill ops · concierge · analytics"),
             size=11, color=INK)
    add_text(s, Inches(0.6), Inches(7.0), Inches(12), Inches(0.4),
             ("BUILT FOR YOUR TEAM   —   editors, refill ops, concierge, "
              "and brand-side compliance review. Bilingual EN/ES."),
             size=10, bold=True, color=ACCENT)
    add_footer(s, 17, slides_total)
slide_studio()

# 18. ROADMAP
def slide_roadmap():
    s = add_slide()
    add_section_header(s, "How we'll deliver", "Roadmap — first nine months.")
    phases = [
        ("Discovery", "Weeks 1–2",
         "Customer interviews (DTC subscriber, Sephora-acquired, practitioner, churned, new). Audit subscription + claims data. Brand-side legal alignment. Lock Phase 1 scope."),
        ("Phase 1 build", "Weeks 3–18",
         "Ritual, Apothecary, Goals, Refill Vault, Shop, Glow, Tier 1 AI with compliance guardrails, The Studio. EN/ES at launch."),
        ("Phase 2 build", "Weeks 19–34",
         "AR ritual, smart-stack, practitioner B2B portal, health-data integration, multilingual expansion."),
        ("Phase 3 build", "Weeks 35–42+",
         "Editorial, VOICES films, content scaling, demand sensing, counterfeit detection, certification program."),
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
        ("Ritual completion rate", "% of users completing ≥1 ritual per week, month 3",
         "Target ≥ 50%"),
        ("Stack adoption", "% of users with a saved Stack, month 3",
         "Target ≥ 65%"),
        ("Refill churn", "% of subscriptions churning quarterly",
         "Target −30% vs current baseline"),
        ("Pause-to-cancel ratio", "% of would-be cancels who pause instead",
         "Target ≥ 60%"),
        ("Apothecary chat completion", "% of chats resolved without escalation",
         "Target ≥ 75% — escalations are signal, not failure"),
        ("Compliance flags caught pre-publish", "% of FDA/FTC issues caught by Studio review",
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
        ("Calm, never punishing",
         "No streaks, no FOMO, no shame. Wellness is a practice, not a leaderboard."),
        ("Cite, never invent",
         "Every adaptogen claim sources to peer-reviewed evidence. The AI never makes up science."),
        ("Defer to physicians",
         "When customers disclose Rx, the AI flags interactions and waits for physician confirmation."),
        ("Subscription is a relationship",
         "One-tap pause, skip, vacation. Never auto-charge the customer who asked you not to."),
        ("Recognition over discount",
         "Glow rewards ritual practice and bottle returns. Not new-buy bribes."),
        ("FTC-compliant by default",
         "Structure-function language only. No 'cure', 'treat', 'prevent disease.'"),
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
        ("Discovery sprint", "Two weeks. Customer interviews — DTC subscriber, Sephora-acquired, practitioner, churned, new buyer. Brand-side legal alignment on AI claims."),
        ("Embedded delivery", "A small team — lead engineer, mobile engineer, designer, bilingual QA — works as an extension of yours. Weekly demos."),
        ("Brand-side compliance review", "Every customer-facing adaptogen, dosing, or interaction claim reviewed by your editorial / legal team. Non-negotiable."),
        ("Always your data", "Source code, customer data, AI logs, the Apothecary citation library all live in your accounts."),
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
    add_section_header(s, "Why this works for Moon Juice", "The bet behind the build.")
    pts = [
        ("Education is your moat",
         "The Moon Dust mythology is brilliant marketing. The app turns it into education — and education is what keeps a customer for 10 years."),
        ("Refill is the LTV story",
         "A daily-ritual customer with 3+ subscriptions and pause-not-cancel mechanics is the highest LTV in wellness. The Vault makes that easier."),
        ("Compliance is a feature",
         "Most wellness brands grow until the FDA / FTC notices. Building compliance into the AI from day one is what lets the brand grow safely past Sephora into Whole Foods, Target, EU."),
        ("AI in service of practice",
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
              "DTC subscriber, Sephora-acquired, practitioner, churned, "
              "new buyer. We sit with your legal team and align on what "
              "the AI can and can't say. We come back with a lockable "
              "Phase 1 scope and a working prototype of the Apothecary "
              "and Refill Vault flows in EN and ES."),
             size=18, color=GOLD_SOFT)
    add_text(s, Inches(0.6), Inches(5.1), Inches(11), Inches(0.5),
             "WHAT YOU GET", size=11, bold=True, color=GOLD)
    add_text(s, Inches(0.6), Inches(5.5), Inches(11), Inches(2.0),
             ("•  A lockable feature scope, costed and timeboxed\n"
              "•  An interactive prototype of two core flows\n"
              "•  Brand-side legal alignment on AI claims\n"
              "•  A go / no-go recommendation. Yours either way."),
             size=14, color=WHITE)
    add_footer(s, 23, slides_total, on_dark=True)
slide_next()

out = Path(__file__).parent / "Moon-Juice-Pitch.pptx"
prs.save(out)
print(f"wrote {out}  ({len(prs.slides)} slides)")
