"""Build the Pineda Covalin client pitch deck (.pptx).

Features-focused pitch — intentionally excludes pricing.
Run from the repo root:
    python3 proposals/pineda-covalin-mobile-app/build_deck.py
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pathlib import Path

# Brand palette (matches the HTML mockups)
INK         = RGBColor(0x2a, 0x1a, 0x14)
MUTED       = RGBColor(0x8a, 0x78, 0x66)
LINE        = RGBColor(0xe6, 0xd9, 0xc0)
BG          = RGBColor(0xf5, 0xed, 0xe0)
ACCENT      = RGBColor(0xa0, 0x27, 0x47)   # cochineal / carmine
ACCENT_DEEP = RGBColor(0x6e, 0x1a, 0x30)
ACCENT_SOFT = RGBColor(0xf7, 0xe0, 0xd8)
GOLD        = RGBColor(0xd8, 0x9b, 0x3d)   # saffron / cempasúchil
GOLD_SOFT   = RGBColor(0xf5, 0xe2, 0xbd)
TEAL        = RGBColor(0x2c, 0x6e, 0x6b)
PLUM        = RGBColor(0x5b, 0x2a, 0x52)
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


def add_arrow(slide, x, y, w, h, *, color=ACCENT):
    shp = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, x, y, w, h)
    shp.fill.solid()
    shp.fill.fore_color.rgb = color
    shp.line.fill.background()
    shp.shadow.inherit = False
    return shp


def add_footer(slide, page, total, *, on_dark=False):
    color = ACCENT_SOFT if on_dark else MUTED
    add_text(slide, Inches(0.6), Inches(7.05), Inches(6), Inches(0.3),
             "Pineda Covalín · Mobile App Pitch",
             size=9, color=color)
    add_text(slide, Inches(11.7), Inches(7.05), Inches(1), Inches(0.3),
             f"{page} / {total}",
             size=9, color=color, align=PP_ALIGN.RIGHT)


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

# 1. COVER --------------------------------------------------------
def slide_cover():
    s = add_slide()
    # gradient-ish hero band on right
    band = add_rect(s, Inches(8.5), 0, Inches(4.833), SH, fill=ACCENT_DEEP)
    band2 = add_rect(s, Inches(8.5), Inches(0), Inches(4.833), Inches(2.5), fill=ACCENT)
    band3 = add_rect(s, Inches(8.5), 0, Inches(4.833), Inches(0.8), fill=GOLD)
    # decorative dots (cempasúchil)
    for cx, cy, r in [(11.0, 1.5, 0.18), (12.4, 3.2, 0.14),
                       (10.2, 4.1, 0.22), (11.8, 5.6, 0.16),
                       (12.6, 6.6, 0.12)]:
        d = s.shapes.add_shape(MSO_SHAPE.OVAL,
                               Inches(cx-r), Inches(cy-r),
                               Inches(2*r), Inches(2*r))
        d.fill.solid(); d.fill.fore_color.rgb = GOLD
        d.line.fill.background(); d.shadow.inherit = False

    # left accent strip
    add_rect(s, Inches(0.6), Inches(1.0), Inches(0.08), Inches(2.4),
             fill=ACCENT)
    add_text(s, Inches(0.85), Inches(1.0), Inches(6), Inches(0.4),
             "MOBILE APP · PITCH",
             size=11, bold=True, color=ACCENT)
    add_text(s, Inches(0.85), Inches(1.45), Inches(7.5), Inches(2.0),
             "Pineda Covalín", font=SERIF, size=66, color=INK)
    add_text(s, Inches(0.85), Inches(2.7), Inches(7.5), Inches(1.6),
             "El alma de México,\nen el bolsillo de cada cliente.",
             font=SERIF, size=26, color=ACCENT)
    add_text(s, Inches(0.85), Inches(5.6), Inches(7.5), Inches(0.4),
             "A pocket museum, a luxury gift concierge, a traveler's companion.",
             size=14, color=MUTED)
    add_text(s, Inches(0.85), Inches(6.0), Inches(7.5), Inches(0.3),
             "Prepared for the Pineda Covalín team",
             size=11, color=MUTED)

slide_cover()

# 2. THE OPPORTUNITY ---------------------------------------------
def slide_opportunity():
    s = add_slide()
    add_section_header(s, "Why now", "The brand's customer is global. The relationship shouldn't end at the airport.")
    stats = [
        ("40%", "of Mexican sales come from\ntourism — airport, hotel, museum",
         "Most of those buyers are never seen again."),
        ("12+", "airport boutiques and museum\nstores carry your work",
         "Each is a discovery moment in search of a follow-up."),
        ("6", "languages your customers read,\nin five regions",
         "The story behind every piece deserves all of them."),
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

# 3. VISION -------------------------------------------------------
def slide_vision():
    s = add_slide()
    add_section_header(s, "The vision", "Not another store — a cultural companion to a beautiful object.")
    add_text(s, Inches(0.6), Inches(2.3), Inches(12), Inches(2.5),
             ("Pineda Covalín's product is not silk. It is the cultural story "
              "woven into silk — Huichol cosmology, the monarch's migration, "
              "pre-Hispanic codices, the work of Frida and Diego.\n\n"
              "Most international buyers walk away from an airport boutique "
              "with the silk and none of the story. The app gives every piece "
              "a passport, makes the gift a cinematic moment, and turns a "
              "one-time tourist purchase into an ongoing relationship — in the "
              "customer's language, wherever they are."),
             font=SERIF, size=20, color=INK)
    add_text(s, Inches(0.6), Inches(5.8), Inches(12), Inches(0.4),
             "WHY IT MATTERS", size=10, bold=True, color=ACCENT)
    add_text(s, Inches(0.6), Inches(6.1), Inches(12), Inches(1.5),
             ("• Captures the tourist customer who would otherwise vanish after one purchase\n"
              "• Elevates the gift — half the volume — from object to scheduled cultural moment\n"
              "• Gives the brand's existing 40+ retail footprint a digital companion that travels with the customer"),
             size=13, color=INK)
    add_footer(s, 3, slides_total)

slide_vision()

# 4. SIX PILLARS -------------------------------------------------
def slide_pillars():
    s = add_slide()
    add_section_header(s, "Product overview", "Six pillars — five customer-facing, one internal.")
    pillars = [
        ("The Atelier", "Each piece carries its passport — motif, technique, artist, audio guide.",
         GOLD),
        ("Mercado", "Luxury shop curated by collection — Huichol, Frida, Monarcas, Día de Muertos, Codices.",
         ACCENT),
        ("Gift Concierge", "Wrapping, video message, scheduled unboxing — gifting as cinema.",
         PLUM),
        ("Traveler", "Tourist mode: boutiques, appointments, tax-refund, buy-in-city collect-at-airport.",
         TEAL),
        ("Collector's Archive", "Every owned piece registered. Mariposa-cycle tiers reward access, not discounts.",
         ACCENT_DEEP),
        ("El Estudio", "Internal-facing web admin portal — Atelier editor, translations, calendar, concierge.",
         INK),
    ]
    cols = 3; rows = 2
    cw = Inches(4.0); ch = Inches(2.25); gx = Inches(0.15); gy = Inches(0.18)
    x0 = Inches(0.6); y0 = Inches(2.4)
    for i, (title, desc, accent) in enumerate(pillars):
        c = i % cols; r = i // cols
        cx = x0 + (cw + gx) * c
        cy = y0 + (ch + gy) * r
        add_rect(s, cx, cy, cw, ch, fill=WHITE, line=LINE, corner=True)
        # left accent stripe
        add_rect(s, cx, cy, Inches(0.1), ch, fill=accent, corner=True)
        add_text(s, cx + Inches(0.3), cy + Inches(0.2), cw - Inches(0.6),
                 Inches(0.4), str(i + 1), font=SERIF, size=20, bold=True,
                 color=accent)
        add_text(s, cx + Inches(0.3), cy + Inches(0.7), cw - Inches(0.6),
                 Inches(0.5), title, font=SERIF, size=20, color=INK)
        add_text(s, cx + Inches(0.3), cy + Inches(1.25), cw - Inches(0.6),
                 Inches(1.0), desc, size=11, color=MUTED)
    add_footer(s, 4, slides_total)

slide_pillars()

# 5–7. FEATURES BY PHASE -----------------------------------------
def feature_slide(num, total, eyebrow, title, intro, items):
    s = add_slide()
    add_section_header(s, eyebrow, title)
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.6),
             intro, size=14, color=MUTED)
    cols = 2
    cw = Inches(6.0); ch = Inches(0.95); gap = Inches(0.15)
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
              "Foundations: Atelier, Mercado, Gift, Traveler, Archive.",
              "Everything a customer needs in their first 90 days with the app.", [
    ("Multilingual onboarding", "EN/ES at launch — FR/IT/JP/ZH expandable. Apple/Google sign-in."),
    ("Multi-currency, multi-region", "MX/US/EU/Asia-Pacific storefronts. Currency follows the customer."),
    ("The Atelier passport", "Scan QR / NFC tag — motif, artist, technique, artisan community."),
    ("90-second audio guide", "Voiced by curators in the customer's language. Listen on the plane."),
    ("Mercado by collection", "Browse Frida · Huichol · Monarcas · Día de Muertos · Codices."),
    ("Cultural-calendar drops", "Día de Muertos, monarch migration, Frida birthday, Independence Day."),
    ("Gift Concierge", "Signature wrapping, handwritten card, 30-sec video, scheduled unboxing."),
    ("Predictive gift reminders", "Learns each customer's gifting cadence. Mother's Day, anniversaries."),
    ("Travel mode", "Boutiques, museum stores, hotels, studio. Appointment booking, tax-refund."),
    ("Buy-in-city, collect-at-airport", "Purchase in Polanco; pick up at MEX gate on departure."),
    ("Collector's Archive", "Register every piece. Digital certificate of authenticity."),
    ("Mariposa-cycle tiers", "Huevo · Oruga · Crisálida · Mariposa. Access, not discounts."),
    ("Cultural docent (AI)", "Multilingual chat about any motif, technique, collection."),
    ("Visual search (AI)", "Photograph any motif — find related products and their story."),
    ("Scarf-tying studio", "Video library of 30+ techniques. Parisian, ascot, headwrap, bag-handle."),
    ("Atelier services", "Book cleaning, restoration, edge repair. Hotel pickup for tourists."),
])

feature_slide(6, slides_total, "Phase 2 · Depth (months 5–9)",
              "AR, authenticity, gifting at scale.",
              "The features that turn a passport app into a complete cultural platform.", [
    ("AR scarf try-on", "Cloth-drape simulation in your phone's camera mirror."),
    ("AR framing preview", "Scarf as wall art — see the piece scaled to your wall before buying."),
    ("Tour-mode docent", "AI generates a private curatorial essay on YOUR collection."),
    ("Voice-driven shopping", "Speak in any language; results in voice + visuals."),
    ("Image-to-occasion matcher", "Upload an outfit photo; AI suggests the right piece."),
    ("Photo authenticity check", "Vision model flags suspected counterfeits from a tag photo."),
    ("Heritage marketplace", "Brand-curated re-release of vintage and discontinued pieces."),
    ("Gift-narration video", "Auto-generated 60-sec film at the unbox moment."),
    ("Corporate gifting portal", "Bulk orders, dedications, white-glove handler. The diplomatic-gift origin business, modernised."),
    ("Predictive demand sensing", "Wishlists + waitlists + cultural calendar guide reprints."),
])

feature_slide(7, slides_total, "Phase 3 · Cultural authority (months 10+)",
              "From an app to a cultural institution.",
              "Long-form storytelling, community, and operational AI.", [
    ("Editorial / culture engine", "Long-form journal, artisan profiles, museum partner stories."),
    ("Atelier livestreams", "Behind-the-scenes from the Polanco studio. Silk being printed live."),
    ("Limited-edition lottery", "Fair distribution for high-demand collaborations."),
    ("AI bespoke concept", "VIP only. Concept sketch routes to atelier for human design — never AI as final art."),
    ("Multilingual content scaling", "Spanish-first, AI drafts EN/FR/IT/JP/ZH for editor review."),
    ("Counterfeit listing detection", "Scans Mercado Libre, eBay, Amazon, Instagram for fakes."),
    ("VIP signal detection", "Surfaces emerging high-value collectors before they self-identify."),
    ("Cultural-tour itineraries", "App-curated cultural day in Mexico City — studio + Frida house + boutique."),
])

# 8. ONBOARDING FLOW ---------------------------------------------
def slide_onboarding():
    s = add_slide()
    add_section_header(s, "User experience", "Onboarding — under 90 seconds, in any language.")
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.4),
             "The international tourist must feel at home in the first screen. Language is offered before anything else.",
             size=14, color=MUTED)

    steps = [
        ("01", "Bienvenido", "Welcome in six languages.\nTap your language; everything follows."),
        ("02", "Sign in", "Apple, Google, or email.\nNo forms. Tourists never read forms."),
        ("03", "Why we ask", "Plain-language privacy note.\nOpt-in to each data category."),
        ("04", "What do you love?", "Pick three motifs:\nFrida · Huichol · Monarcas · Codices · Día de Muertos."),
        ("05", "First moment", "Scan a piece you own —\nor explore the new drop."),
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
             "DESIGN PRINCIPLE   —   Language is the first form of welcome. Earn permission before asking for data.",
             size=11, bold=True, color=ACCENT)
    add_footer(s, 8, slides_total)

slide_onboarding()

# 9. JOURNEY: TOURIST -------------------------------------------
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
    "The tourist — from airport impulse to ongoing relationship.",
    "40% of Mexican sales come from tourism. Most of those customers are never seen again. This is how we change that.",
    [
        ("AIRPORT", "Buys a Monarca scarf",
         "Sees the piece at MEX boutique on departure. The associate hands her a small card: \"scan to unlock the story.\""),
        ("THE PLANE", "Opens the app",
         "Six-language welcome. Picks Japanese. Scans the tag. The Atelier opens — audio guide in Japanese, voiced by a curator."),
        ("HOME", "Listens to the story",
         "1:32 of a curator narrating the monarch's 4,500-km migration. Saves the piece to her digital archive. Reads about the Hidalgo workshop where it was printed."),
        ("WEEKS LATER", "Returns for the gift",
         "Mother's Day approaching. App suggests a Frida pocket square based on her motif preferences. She uses gift mode — wrapping, card, 30-sec video."),
        ("YEARS LATER", "Crisálida tier",
         "Now has 8 pieces registered. Invitation to the Polanco studio next time she's in Mexico. The relationship that began at a duty-free counter is now a 5-year story."),
    ])

# 10. JOURNEY: GIFT ---------------------------------------------
journey_slide(10, slides_total,
    "User flow · 2 of 3",
    "The gift — half the volume, treated like the moment it is.",
    "Most apps treat gifting as a checkbox. We treat it as cinema.",
    [
        ("CHOOSE", "Asks the AI",
         "\"For my mother-in-law, contemporary Mexican art, $300.\" Three curated picks with reasoning. She picks the Codex Borgia square."),
        ("WRAP", "Customise the parcel",
         "Cempasúchil-paper wrapping, raffia tie, handwritten-style card in Spanish. Adds a 30-second video message recorded in the app."),
        ("SCHEDULE", "Plan the moment",
         "Delivery scheduled for Mother's Day morning. Recipient gets a notification when the parcel ships, another when it's delivered."),
        ("UNBOX", "The recipient app",
         "Mother-in-law installs the app, taps \"I just opened it.\" The video plays. Then the Atelier story unlocks — in Spanish, voiced by the original curator."),
        ("CONTINUE", "A new relationship",
         "The recipient keeps the app. The piece is registered to her now. Her own collector journey begins. One gift becomes two customers."),
    ])

# 11. JOURNEY: COLLECTOR ----------------------------------------
journey_slide(11, slides_total,
    "User flow · 3 of 3",
    "The collector — Huevo to Mariposa.",
    "Recognition replaces discounts. The tier ladder rewards what the brand actually values.",
    [
        ("HUEVO", "First piece",
         "Registers their first scarf. App welcomes them as a collector. Shows the full Monarcas series and what's coming next."),
        ("ORUGA", "Three pieces",
         "Cultural calendar drops are now sent 24 hours before public. Care reminders specific to each piece. Tour-mode docent generates a private essay on their growing collection."),
        ("CRISÁLIDA", "Six pieces",
         "Invited to the Polanco studio next visit. Concierge messaging line opens — direct line to a stylist for the next purchase or gift."),
        ("MARIPOSA", "Twelve pieces",
         "Numbered editions reserved for them in advance. Annual signed piece. Invitation to the atelier livestream when their next-favourite series goes to print."),
        ("FOREVER", "Becomes the story",
         "Collection of 30+ pieces. Featured (with consent) in the brand's editorial. Their lineage of Pineda Covalín pieces becomes part of the brand's institutional record."),
    ])

# 12. SCREEN PREVIEW ---------------------------------------------
def slide_screens():
    s = add_slide()
    add_section_header(s, "Visual reference", "What it looks like in hand.")
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.4),
             "Wireframe-fidelity mockups in the brand palette — warm cream, cochineal carmine, saffron / cempasúchil gold.",
             size=14, color=MUTED)

    screens = [
        ("Onboarding", "6 languages · sign-in"),
        ("Home", "Cultural calendar drop"),
        ("Mercado", "Browse by collection"),
        ("Product", "Numbered edition · ask"),
        ("Atelier", "Audio guide · story"),
        ("Scan", "Authenticity verified"),
        ("El Docente", "Multilingual AI"),
        ("Gift", "Scheduled unboxing"),
        ("Archive", "Crisálida tier"),
        ("Travel", "Boutiques · airport"),
    ]
    cols = 5; rows = 2
    cw = Inches(2.3); ch = Inches(2.0); gx = Inches(0.15); gy = Inches(0.25)
    x0 = Inches(0.6); y0 = Inches(2.7)
    for i, (name, sub) in enumerate(screens):
        c = i % cols; r = i // cols
        x = x0 + (cw + gx) * c
        y = y0 + (ch + gy) * r
        add_rect(s, x, y, cw, ch, fill=INK, corner=True)
        add_rect(s, x + Inches(0.1), y + Inches(0.1),
                 cw - Inches(0.2), ch - Inches(0.2),
                 fill=BG, corner=True)
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
             "Full interactive HTML mockup available — opens in any browser, in the brand palette.",
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
    "AI in service of the cultural story.",
    "Every Tier 1 feature deepens the brand's authority. None replaces human craft.",
    [
        ("Cultural docent (chat)", "Multilingual conversational guide to motifs, techniques, collections. Sources curated by the brand."),
        ("Translation with cultural fidelity", "Keeps Día de Muertos, Huichol, tehuana untranslated; explains concepts for non-Mexican audiences."),
        ("Gift recommender", "Three curated picks with reasoning, in any language, for any occasion and budget."),
        ("Outfit & occasion advisor", "\"A scarf for a wedding in Mexico City in October\" — color theory, motif fit, cultural appropriateness."),
        ("Visual search", "Photograph any motif — find related products in catalog and heritage archive, plus their story."),
        ("Atelier passport summaries", "One-paragraph plain-language origin stories for every SKU, editor-reviewed before publish."),
    ])

# 14. AI TIER 2 + 3 ----------------------------------------------
ai_tier_slide(14, slides_total,
    "Intelligence · Tier 2 & 3",
    "AI that powers the gift, the loop, and the back office.",
    "Phase 2 customer-facing AI plus operational AI the customer never sees.",
    [
        ("AR scarf try-on", "Phone-camera cloth-drape simulation. Match the motif to the outfit before you buy."),
        ("Photo authenticity check", "Vision model trained on real pieces flags suspected counterfeits from a tag photo."),
        ("Tour-mode private essay", "AI writes a personal curatorial essay on YOUR registered collection."),
        ("Voice-driven shopping", "Speak in your native language; results in voice + visuals. For tourists not literate in UI languages."),
        ("Gift-narration video (auto)", "60-second film at the unbox moment, in the recipient's language, voiced by their region's curator."),
        ("Demand sensing", "Wishlists + waitlists + cultural calendar predict which pieces to reprint, in which markets."),
        ("Multilingual content scaling", "Spanish-first; AI drafts EN/FR/IT/JP/ZH; editors review. Lets the brand publish across regions without 5× the team."),
        ("Counterfeit listing detection", "AI scans marketplaces and Instagram for suspected fakes; flags for the legal team."),
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
        ("Language & region", "UI language, country, currency — multi-region brand essential."),
        ("Motif preferences", "Frida / Huichol / Monarcas / Codices / Día de Muertos."),
        ("Buyer mode", "gift vs self — drives the entire experience."),
        ("Travel signals", "\"visiting Mexico in November\" — boutique appointments."),
        ("Collection size & history", "for collector recognition and completion suggestions."),
        ("Occasion patterns", "Mother's Day, anniversaries, holiday gifting cadence."),
        ("Channel of origin", "airport / museum / boutique / hotel / online — attribution."),
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
                     "OTA updates — fast cultural-calendar drops",
                     "Apple / Google sign-in"]),
        ("Commerce", ["Shopify or VTEX storefront API",
                       "Multi-currency · multi-region",
                       "RevenueCat for any digital memberships"]),
        ("Cultural backend", ["Node + TypeScript API",
                               "Postgres + pgvector for motif search",
                               "QR for v1; NFC for premium pieces"]),
        ("Intelligence", ["Claude (Sonnet 4.6 chat, Haiku 4.5 batch)",
                           "Embeddings for collection / motif",
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
    add_section_header(s, "El Estudio · web admin portal",
                       "The internal twin of the mobile app.")
    add_text(s, Inches(0.6), Inches(2.1), Inches(12), Inches(0.8),
             ("The customer uses the mobile app. Your team uses El Estudio. "
              "Same backend, same brand language — different surface for "
              "different users."),
             size=14, color=MUTED)

    # Architecture diagram - three boxes
    # Top: Shopify/VTEX (catalog, orders, payments)
    add_rect(s, Inches(4.5), Inches(3.0), Inches(4.3), Inches(0.85),
             fill=WHITE, line=LINE, corner=True)
    add_text(s, Inches(4.7), Inches(3.05), Inches(3.9), Inches(0.4),
             "SHOPIFY / VTEX", size=10, bold=True, color=ACCENT)
    add_text(s, Inches(4.7), Inches(3.40), Inches(3.9), Inches(0.4),
             "Catalog · orders · payments — unchanged",
             size=11, color=MUTED)

    # Middle - shared API
    add_rect(s, Inches(0.6), Inches(4.2), Inches(12.1), Inches(0.7),
             fill=ACCENT_SOFT, corner=True)
    add_text(s, Inches(0.85), Inches(4.27), Inches(11.6), Inches(0.4),
             "SHARED API · Postgres · Auth · AI gateway · Object storage",
             size=11, bold=True, color=ACCENT,
             anchor=MSO_ANCHOR.MIDDLE)

    # Bottom: two parallel boxes - mobile app | studio
    add_rect(s, Inches(0.6), Inches(5.2), Inches(5.95), Inches(1.6),
             fill=WHITE, line=LINE, corner=True)
    add_rect(s, Inches(0.6), Inches(5.2), Inches(5.95), Inches(0.4),
             fill=ACCENT, corner=True)
    add_text(s, Inches(0.85), Inches(5.22), Inches(5.45), Inches(0.4),
             "MOBILE APP — IOS & ANDROID",
             size=10, bold=True, color=WHITE,
             anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(0.85), Inches(5.7), Inches(5.45), Inches(1.0),
             ("Customer-facing · Atelier · Mercado · Gift Concierge · "
              "Traveler · Collector's Archive · El Docente"),
             size=11, color=INK)

    add_rect(s, Inches(6.75), Inches(5.2), Inches(5.95), Inches(1.6),
             fill=WHITE, line=LINE, corner=True)
    add_rect(s, Inches(6.75), Inches(5.2), Inches(5.95), Inches(0.4),
             fill=INK, corner=True)
    add_text(s, Inches(7.0), Inches(5.22), Inches(5.45), Inches(0.4),
             "EL ESTUDIO — WEB ADMIN PORTAL",
             size=10, bold=True, color=WHITE,
             anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(7.0), Inches(5.7), Inches(5.45), Inches(1.0),
             ("Internal · Atelier editor · translation workflow · cultural "
              "calendar · concierge inbox · VIP admin · authenticity · "
              "analytics"),
             size=11, color=INK)

    # Caption
    add_text(s, Inches(0.6), Inches(7.0), Inches(12), Inches(0.4),
             ("BUILT FOR YOUR TEAM   —   editors, curators, concierge, B2B "
              "managers, analysts. Bilingual ES/EN. Brand-palette UI."),
             size=10, bold=True, color=ACCENT)
    add_footer(s, 17, slides_total)

slide_studio()

# 18. ROADMAP ----------------------------------------------------
def slide_roadmap():
    s = add_slide()
    add_section_header(s, "How we'll deliver", "Roadmap — first nine months.")
    phases = [
        ("Discovery", "Weeks 1–2",
         "Customer interviews (tourist, collector, corporate gifter, EU buyer, US buyer). Audit existing data. Lock Phase 1 scope. Brand language workshop."),
        ("Phase 1 build", "Weeks 3–16",
         "Atelier, Mercado, Gift, Traveler, Archive. EN/ES at launch. Tier 1 AI. Soft launch from Polanco studio."),
        ("Phase 2 build", "Weeks 17–32",
         "AR try-on, photo authenticity, corporate gifting portal, gift-narration video. Add FR/JP/ZH languages."),
        ("Phase 3 build", "Weeks 33–40+",
         "Editorial engine, atelier livestreams, AI bespoke concept, demand sensing."),
    ]
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
                 Inches(2.0), detail, size=11, color=MUTED)
    add_footer(s, 18, slides_total)

slide_roadmap()

# 19. SUCCESS METRICS --------------------------------------------
def slide_metrics():
    s = add_slide()
    add_section_header(s, "How we'll know it's working", "The metrics that matter.")
    metrics = [
        ("Tourist retention", "% of airport / museum buyers who install the app and register their piece within 90 days",
         "Target ≥ 35% by month 9"),
        ("Gift uptake", "% of orders placed through gift-mode with scheduled unboxing",
         "Target ≥ 40% by month 12"),
        ("Recipient activation", "% of gift recipients who install the app and open the Atelier story",
         "Target ≥ 55%"),
        ("Collector depth", "Average pieces registered per active user",
         "Target ≥ 3 by month 9"),
        ("Cross-language reach", "% of sessions in EN, FR, JP, ZH (non-ES)",
         "Target ≥ 50% by month 12"),
        ("Authenticity confidence", "% of pieces verified through the in-app authenticity flow",
         "Target ≥ 70% of new sales"),
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
        ("Calm, never kitsch",
         "The motifs are bold; the interface is restrained. The silk does the talking."),
        ("Language is welcome",
         "Every customer's first language matters. Translation is cultural, not literal."),
        ("Authenticity above all",
         "AI never generates final designs or motifs. The cultural craft is the brand. Guard it."),
        ("Gift as a moment",
         "Half the volume is gifting. We design the moment, not just the checkout."),
        ("Recognition replaces discounts",
         "Luxury earns loyalty through access — studio visits, advance drops, signed pieces. Not coupons."),
        ("Local trust, global voice",
         "Built in México, for the world. The studio is the centre; every region is a guest of honour."),
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

# 21. PARTNERSHIP -------------------------------------------------
def slide_team():
    s = add_slide()
    add_section_header(s, "Working together", "How we'd partner.")
    cards = [
        ("Discovery sprint", "Two weeks. We sit at the Polanco studio. Talk to ten of your customers — tourist, collector, corporate gifter, three regions. Walk away with a signed Phase 1 scope, even if you don't build with us."),
        ("Embedded delivery", "A small team — a lead engineer, a mobile engineer, a designer, a Spanish-language QA — works as an extension of yours. Weekly demos, never a black box."),
        ("Cultural review", "Every customer-facing string of cultural content reviewed by a curator the brand chooses. AI generates; humans approve."),
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

# 22. WHY THIS WORKS ---------------------------------------------
def slide_why():
    s = add_slide()
    add_section_header(s, "Why this works for Pineda Covalín", "The bet behind the build.")
    pts = [
        ("Your story is your moat",
         "No global luxury house can claim authentic Mexican cultural craft. The Atelier passport puts that authority in the customer's hand, in their language."),
        ("The tourist is your hidden customer",
         "40% of your sales walk away never to return. The app makes them collectors. Even a 10% retention shift is the largest growth lever you have."),
        ("The gift is a Trojan horse",
         "Half your volume creates a new customer at every unboxing — your recipient flow is acquisition disguised as service."),
        ("Built to honour, not exploit",
         "AI in service of cultural craft, never replacing it. The brand's reputation grows safer, not riskier, in the building."),
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

# 23. NEXT STEP --------------------------------------------------
def slide_next():
    s = add_slide()
    add_rect(s, 0, 0, SW, SH, fill=ACCENT_DEEP)
    # decorative gold dots
    for cx, cy, r in [(11.0, 1.2, 0.18), (12.4, 2.8, 0.14),
                       (10.4, 4.0, 0.22), (12.0, 5.4, 0.16),
                       (11.2, 6.4, 0.12), (12.7, 4.6, 0.10)]:
        d = s.shapes.add_shape(MSO_SHAPE.OVAL,
                               Inches(cx-r), Inches(cy-r),
                               Inches(2*r), Inches(2*r))
        d.fill.solid(); d.fill.fore_color.rgb = GOLD
        d.line.fill.background(); d.shadow.inherit = False

    add_text(s, Inches(0.6), Inches(0.55), Inches(8), Inches(0.3),
             "NEXT STEP",
             size=11, bold=True, color=GOLD)
    add_text(s, Inches(0.6), Inches(1.1), Inches(11), Inches(2.0),
             "A two-week paid discovery.",
             font=SERIF, size=54, color=WHITE)
    add_text(s, Inches(0.6), Inches(2.7), Inches(10.5), Inches(2.0),
             ("We sit at the Polanco studio. We talk to ten of your "
              "customers — a tourist, a collector, a corporate gifter, "
              "three regions. We audit what you already know about them. "
              "We come back with a lockable Phase 1 scope and a working "
              "interactive prototype of the Atelier, the gift flow, and "
              "the docent in three languages."),
             size=18, color=ACCENT_SOFT)
    add_text(s, Inches(0.6), Inches(5.1), Inches(11), Inches(0.5),
             "WHAT YOU GET",
             size=11, bold=True, color=GOLD)
    add_text(s, Inches(0.6), Inches(5.5), Inches(11), Inches(2.0),
             ("•  A lockable feature scope, costed and timeboxed\n"
              "•  An interactive prototype of three core flows\n"
              "•  A summary of the customer interviews and what we heard\n"
              "•  A go / no-go recommendation. Yours either way."),
             size=14, color=WHITE)
    add_footer(s, 23, slides_total, on_dark=True)

slide_next()

# write -----------------------------------------------------------
out = Path(__file__).parent / "Pineda-Covalin-Pitch.pptx"
prs.save(out)
print(f"wrote {out}  ({len(prs.slides)} slides)")
