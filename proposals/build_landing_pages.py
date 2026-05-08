"""Generate seysoservices.com/proposals landing pages.

Emits:
  - proposals/index.html  (master index of all brand proposals)
  - proposals/<slug>-mobile-app/landing.html  (per-brand landing)

Each per-brand landing page is self-contained HTML in the brand palette,
with cards linking to the deck, mobile mockup, Studio mockup, and the
client-facing pricing PDF.

The internal pricing PDF is intentionally NOT linked from any landing
page — it's internal-only.

Run from repo root:
    python3 proposals/build_landing_pages.py
"""

from pathlib import Path
from textwrap import dedent

# ---------------------------------------------------------- brands

BRANDS = [
    {
        "slug": "erth-to-erth",
        "folder": "erth-to-erth-mobile-app",
        "name": "Erth to Erth",
        "tagline": "Clothes that come back to the earth — and to the people who wear them.",
        "summary": (
            "A circular-wardrobe companion. The mobile app stewards the "
            "garments your customers already own — passport, repair, "
            "resale, recycle — and turns each piece into a long-life "
            "relationship instead of a one-time sale."
        ),
        "category": "Sustainable apparel · circular fashion",
        "palette": {
            "bg":      "#f3efe7",
            "ink":     "#1f1d18",
            "muted":   "#6b665c",
            "line":    "#d9d2c4",
            "accent":  "#2f4a36",
            "deep":    "#143226",
            "soft":    "#e3ead0",
            "gold":    "#b9914c",
        },
        "deck":     "Erth-to-Erth-Pitch.pptx",
        "mobile":   "mockups.html",
        "studio":   "studio-mockups.html",
        "pricing":  "Erth-to-Erth-Pricing-Client.pdf",
    },
    {
        "slug": "pineda-covalin",
        "folder": "pineda-covalin-mobile-app",
        "name": "Pineda Covalín",
        "tagline": "El alma de México, en el bolsillo de cada cliente.",
        "summary": (
            "A pocket museum, a luxury gift concierge, and a traveler's "
            "companion for the Mexican luxury silk house. Every piece "
            "carries its cultural passport. Every gift becomes a "
            "scheduled cinematic moment."
        ),
        "category": "Luxury silk accessories · cultural craft",
        "palette": {
            "bg":      "#f5ede0",
            "ink":     "#2a1a14",
            "muted":   "#8a7866",
            "line":    "#e6d9c0",
            "accent":  "#a02747",
            "deep":    "#6e1a30",
            "soft":    "#f7e0d8",
            "gold":    "#d89b3d",
        },
        "deck":     "Pineda-Covalin-Pitch.pptx",
        "mobile":   "mockups.html",
        "studio":   "studio-mockups.html",
        "pricing":  "Pineda-Covalin-Pricing-Client.pdf",
    },
    {
        "slug": "titika-active",
        "folder": "titika-active-mobile-app",
        "name": "Titika Active",
        "tagline": "VERSATILE. ACTIVE. LIFE.",
        "summary": (
            "A daily companion to a versatile life — gym, yoga, brunch, "
            "errands. Built around what Titika already does well: the "
            "Closet's three-ways styling, the Practice library, the Fit "
            "Atelier ending the legging-sizing lottery."
        ),
        "category": "Premium athleisure · multi-region",
        "palette": {
            "bg":      "#f6f4f0",
            "ink":     "#1a1a1a",
            "muted":   "#777777",
            "line":    "#e6e3dd",
            "accent":  "#c43e54",
            "deep":    "#8a2236",
            "soft":    "#f8e0e4",
            "gold":    "#d4a85a",
        },
        "deck":     "Titika-Active-Pitch.pptx",
        "mobile":   "mockups.html",
        "studio":   "studio-mockups.html",
        "pricing":  "Titika-Active-Pricing-Client.pdf",
    },
    {
        "slug": "kotn",
        "folder": "kotn-mobile-app",
        "name": "Kotn",
        "tagline": "From the Nile, to your wardrobe.",
        "summary": (
            "A thread between the customer and the people who made what "
            "she wears — the farms in Fayoum, the women's sewing "
            "collective in Cairo, the schools built with last quarter's "
            "profits. Verifiable provenance is the brand's moat. The "
            "app makes it readable."
        ),
        "category": "Direct-trade Egyptian cotton · B Corp essentials",
        "palette": {
            "bg":      "#f4f1ea",
            "ink":     "#1d2a3a",
            "muted":   "#7a7569",
            "line":    "#e2dccd",
            "accent":  "#2f5a78",
            "deep":    "#143247",
            "soft":    "#d6e3ed",
            "gold":    "#c89868",
        },
        "deck":     "Kotn-Pitch.pptx",
        "mobile":   "mockups.html",
        "studio":   "studio-mockups.html",
        "pricing":  "Kotn-Pricing-Client.pdf",
    },
    {
        "slug": "encircled",
        "folder": "encircled-mobile-app",
        "name": "Encircled",
        "tagline": "Fewer pieces. More ways to wear them.",
        "summary": (
            "A transformation engine for a slow-fashion brand. The "
            "Chrysalis Cardi has eight documented styles; most owners "
            "use three. The app teaches the rest, builds capsules from "
            "the closet, and turns the lifetime repair guarantee into a "
            "one-tap workflow."
        ),
        "category": "Multi-way slow-fashion · B Corp · Toronto",
        "palette": {
            "bg":      "#f4efea",
            "ink":     "#2b2a26",
            "muted":   "#888379",
            "line":    "#e6dfd3",
            "accent":  "#5d6e54",
            "deep":    "#36422f",
            "soft":    "#dfe5d6",
            "gold":    "#b89968",
        },
        "deck":     "Encircled-Pitch.pptx",
        "mobile":   "mockups.html",
        "studio":   "studio-mockups.html",
        "pricing":  "Encircled-Pricing-Client.pdf",
    },
    {
        "slug": "moon-juice",
        "folder": "moon-juice-mobile-app",
        "name": "Moon Juice",
        "tagline": "Your daily ritual, guided.",
        "summary": (
            "An adaptogen coach in your customer's pocket. The Apothecary "
            "explains every Moon Dust with sourcing and citations. The "
            "Goals → Stack flow ends the \"which Moon Dust\" guesswork. "
            "The Refill Vault makes subscriptions calm, humane, and "
            "regulator-aware."
        ),
        "category": "Adaptogens · supplements · clean beauty",
        "palette": {
            "bg":      "#f5f0eb",
            "ink":     "#2a1f3d",
            "muted":   "#8b8194",
            "line":    "#e6dfd0",
            "accent":  "#8b6fbf",
            "deep":    "#4a3878",
            "soft":    "#e7defa",
            "gold":    "#c9a85e",
        },
        "deck":     "Moon-Juice-Pitch.pptx",
        "mobile":   "mockups.html",
        "studio":   "studio-mockups.html",
        "pricing":  "Moon-Juice-Pricing-Client.pdf",
    },
    {
        "slug": "cocokind",
        "folder": "cocokind-mobile-app",
        "name": "Cocokind",
        "tagline": "Skincare you can read in full.",
        "summary": (
            "A transparency engine for the brand that pioneered "
            "Sustainability Facts labels. Per-product Facts, citation-"
            "linked ingredients, and routine guidance from the existing "
            "catalog — without invented claims, and without the \"clean\" "
            "language Priscilla retired."
        ),
        "category": "Clean skincare · radical transparency",
        "palette": {
            "bg":      "#f4efe6",
            "ink":     "#2c3a2e",
            "muted":   "#8a9085",
            "line":    "#e0d8c8",
            "accent":  "#6e8b6a",
            "deep":    "#3e4f3b",
            "soft":    "#d8e4d4",
            "gold":    "#c9a85e",
        },
        "deck":     "Cocokind-Pitch.pptx",
        "mobile":   "mockups.html",
        "studio":   "studio-mockups.html",
        "pricing":  "Cocokind-Pricing-Client.pdf",
    },
    {
        "slug": "free-label",
        "folder": "free-label-mobile-app",
        "name": "Free Label",
        "tagline": "The bra that finally fits.",
        "summary": (
            "A fit engine for the Vancouver brand making wire-free, "
            "elastic-free, bamboo bras sized A to L cup and up to 5X. "
            "The Fit Finder ends the under-sizing first try. The Drop "
            "shows real batch counts, no fake urgency. Free size-swap "
            "is the default, not a perk."
        ),
        "category": "Wire-free bras · size-inclusive · slow fashion",
        "palette": {
            "bg":      "#f7f3ed",
            "ink":     "#2a2520",
            "muted":   "#8a7e72",
            "line":    "#e6dcd0",
            "accent":  "#c08f7a",
            "deep":    "#7a4d3d",
            "soft":    "#f0dfd2",
            "gold":    "#c9a85e",
        },
        "deck":     "Free-Label-Pitch.pptx",
        "mobile":   "mockups.html",
        "studio":   "studio-mockups.html",
        "pricing":  "Free-Label-Pricing-Client.pdf",
    },
    {
        "slug": "unika-swim",
        "folder": "unika-swim-mobile-app",
        "name": "Ūnika Swim",
        "tagline": "Made for the body you're in.",
        "summary": (
            "An Atelier-from-couch app for the Toronto custom-swim brand "
            "founded by Betsy Campos. Browse ECONYL® fabrics, draft your "
            "design, book the Yorkville appointment. Cup AAA–H, "
            "mastectomy / ostomy / scar accommodation as service — "
            "with sensitive-fit data in a segregated, audit-logged store."
        ),
        "category": "Custom swimwear · ECONYL® · sensitive-fit aware",
        "palette": {
            "bg":      "#f7f1e8",
            "ink":     "#2a2a26",
            "muted":   "#8a857a",
            "line":    "#e6dccb",
            "accent":  "#d8704a",
            "deep":    "#8a3e22",
            "soft":    "#f5dfd3",
            "gold":    "#d4a85a",
        },
        "deck":     "Unika-Swim-Pitch.pptx",
        "mobile":   "mockups.html",
        "studio":   "studio-mockups.html",
        "pricing":  "Unika-Swim-Pricing-Client.pdf",
    },
]


# ---------------------------------------------------------- per-brand template

PER_BRAND_TEMPLATE = """\
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{name} — Mobile App Proposal · SEYSO MaaS</title>
<style>
  :root {{
    --bg: {bg};
    --ink: {ink};
    --muted: {muted};
    --line: {line};
    --card: #ffffff;
    --accent: {accent};
    --deep: {deep};
    --soft: {soft};
    --gold: {gold};
  }}
  * {{ box-sizing: border-box; }}
  html, body {{
    margin: 0; padding: 0;
    background: var(--bg); color: var(--ink);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Helvetica Neue", Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    line-height: 1.55;
  }}
  .wrap {{ max-width: 880px; margin: 0 auto; padding: 48px 28px 80px; }}
  header.crumb {{
    display: flex; justify-content: space-between; align-items: center;
    color: var(--muted); font-size: 11px;
    letter-spacing: 2px; text-transform: uppercase; font-weight: 600;
    border-bottom: 1px solid var(--line);
    padding-bottom: 14px; margin-bottom: 36px;
  }}
  header.crumb a {{ color: var(--muted); text-decoration: none; }}
  header.crumb a:hover {{ color: var(--accent); }}

  .eyebrow {{
    color: var(--accent); font-weight: 700;
    font-size: 11px; letter-spacing: 2.5px; text-transform: uppercase;
    margin-bottom: 14px;
  }}
  h1 {{
    font-family: "Times New Roman", Georgia, serif;
    font-weight: 400; font-size: 56px;
    line-height: 1.05; letter-spacing: -1px;
    margin: 0 0 12px; color: var(--ink);
  }}
  .tagline {{
    font-family: "Times New Roman", Georgia, serif;
    color: var(--accent); font-size: 22px; line-height: 1.3;
    margin: 0 0 28px;
  }}
  .summary {{
    color: var(--ink); font-size: 16px; line-height: 1.65;
    margin: 0 0 22px; max-width: 640px;
  }}
  .meta {{
    display: flex; gap: 14px; flex-wrap: wrap;
    color: var(--muted); font-size: 12px;
    border-top: 1px solid var(--line);
    padding-top: 16px; margin-bottom: 40px;
  }}
  .meta .pill {{
    background: var(--soft); color: var(--accent);
    padding: 4px 10px; border-radius: 999px;
    font-size: 11px; font-weight: 700; letter-spacing: 0.5px;
  }}

  h2 {{
    font-family: "Times New Roman", Georgia, serif;
    font-weight: 400; font-size: 22px;
    margin: 0 0 14px; color: var(--ink);
  }}
  .intro {{ color: var(--muted); font-size: 14px; margin: 0 0 22px; }}

  .grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-bottom: 40px;
  }}
  @media (max-width: 640px) {{ .grid {{ grid-template-columns: 1fr; }} }}
  .card {{
    background: var(--card); border: 1px solid var(--line);
    border-radius: 14px; padding: 20px 22px;
    text-decoration: none; color: var(--ink);
    transition: all .15s ease;
    display: flex; flex-direction: column; gap: 6px;
    position: relative;
  }}
  .card:hover {{
    border-color: var(--accent);
    transform: translateY(-1px);
    box-shadow: 0 8px 24px rgba(0,0,0,.06);
  }}
  .card .label {{
    color: var(--muted); font-size: 10px;
    letter-spacing: 2px; text-transform: uppercase; font-weight: 700;
  }}
  .card .name {{
    font-family: "Times New Roman", Georgia, serif;
    font-weight: 400; font-size: 22px;
    color: var(--ink); margin-top: 4px;
  }}
  .card .desc {{
    color: var(--muted); font-size: 12px; line-height: 1.5;
    margin-top: 4px;
  }}
  .card .arrow {{
    position: absolute; top: 18px; right: 22px;
    color: var(--accent); font-size: 18px; font-weight: 700;
  }}

  .closing {{
    background: var(--deep); color: #fff;
    border-radius: 14px; padding: 32px 28px;
    margin-bottom: 40px;
  }}
  .closing .lbl {{
    color: var(--gold); font-size: 11px;
    font-weight: 700; letter-spacing: 2px;
    margin-bottom: 10px;
  }}
  .closing h3 {{
    font-family: "Times New Roman", Georgia, serif;
    font-weight: 400; font-size: 26px;
    margin: 0 0 14px;
  }}
  .closing p {{
    color: var(--soft); margin: 0 0 16px;
    font-size: 14px; line-height: 1.55;
  }}
  .closing a.cta {{
    display: inline-block;
    background: var(--gold); color: var(--deep);
    text-decoration: none;
    padding: 10px 18px; border-radius: 999px;
    font-size: 13px; font-weight: 700; letter-spacing: 0.5px;
  }}

  footer {{
    color: var(--muted); font-size: 11px;
    border-top: 1px solid var(--line);
    padding-top: 18px;
    display: flex; justify-content: space-between; flex-wrap: wrap; gap: 8px;
  }}
  footer a {{ color: var(--muted); text-decoration: none; }}
  footer a:hover {{ color: var(--accent); }}
</style>
</head>
<body>
  <div class="wrap">
    <header class="crumb">
      <a href="../index.html">← seyso · proposals</a>
      <span>{name}</span>
    </header>

    <div class="eyebrow">MOBILE-AS-A-SERVICE · PROPOSAL</div>
    <h1>{name}.</h1>
    <div class="tagline">{tagline}</div>
    <p class="summary">{summary}</p>
    <div class="meta">
      <span class="pill">{category}</span>
      <span>Delivered as MaaS — monthly platform subscription, not a one-time build.</span>
    </div>

    <h2>Five-minute look</h2>
    <p class="intro">Three artifacts and a one-pager. Open in any order.</p>
    <div class="grid">
      <a class="card" href="{deck}">
        <span class="arrow">↗</span>
        <div class="label">23-slide deck · features</div>
        <div class="name">Pitch deck</div>
        <div class="desc">Six product pillars · Phase 1/2/3 features · AI tiers · roadmap · success metrics. Features-only — no costs.</div>
      </a>
      <a class="card" href="{mobile}">
        <span class="arrow">↗</span>
        <div class="label">9 phone screens · interactive HTML</div>
        <div class="name">Mobile app mockup</div>
        <div class="desc">Wireframe-fidelity Phase 1 screens in the brand palette. Opens in any browser; no install.</div>
      </a>
      <a class="card" href="{studio}">
        <span class="arrow">↗</span>
        <div class="label">4 web admin screens · interactive HTML</div>
        <div class="name">The Studio</div>
        <div class="desc">The internal twin of the mobile app. How your team would maintain content, ops, and customer concierge.</div>
      </a>
      <a class="card" href="{pricing}">
        <span class="arrow">↗</span>
        <div class="label">PDF · 4 pages</div>
        <div class="name">Platform investment</div>
        <div class="desc">Right-sized tier recommendation, what's included, year-2 upgrade path, fair terms.</div>
      </a>
    </div>

    <div class="closing">
      <div class="lbl">NEXT STEP</div>
      <h3>A two-week paid discovery.</h3>
      <p>We sit with your team. We talk to ten of your customers. We come back with a lockable Phase 1 scope and a working prototype of two core flows. Either way, you walk away with a signed scope you can use.</p>
      <a class="cta" href="mailto:hello@seysoservices.com?subject=Discovery%20%C2%B7%20{name_url}">Start a discovery</a>
    </div>

    <footer>
      <span>SEYSO · Mobile-as-a-Service</span>
      <a href="https://seysoservices.com">seysoservices.com</a>
    </footer>
  </div>
</body>
</html>
"""


# ---------------------------------------------------------- index template

INDEX_TEMPLATE = """\
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>SEYSO · Proposals</title>
<style>
  :root {
    --bg: #faf7f1;
    --ink: #1a1a1a;
    --muted: #6b665c;
    --line: #e6e0d4;
    --card: #ffffff;
    --accent: #2a3a44;
    --deep: #14202a;
    --soft: #d8e0e4;
    --gold: #c9a85e;
  }
  * { box-sizing: border-box; }
  html, body {
    margin: 0; padding: 0;
    background: var(--bg); color: var(--ink);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Helvetica Neue", Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    line-height: 1.55;
  }
  .wrap { max-width: 1080px; margin: 0 auto; padding: 56px 28px 80px; }

  .eyebrow {
    color: var(--accent); font-weight: 700;
    font-size: 11px; letter-spacing: 2.5px; text-transform: uppercase;
    margin-bottom: 14px;
  }
  h1 {
    font-family: "Times New Roman", Georgia, serif;
    font-weight: 400; font-size: 60px;
    line-height: 1.05; letter-spacing: -1px;
    margin: 0 0 12px;
  }
  .lede {
    font-family: "Times New Roman", Georgia, serif;
    color: var(--accent); font-size: 22px; line-height: 1.35;
    margin: 0 0 28px; max-width: 760px;
  }
  .summary {
    color: var(--ink); font-size: 15px; line-height: 1.65;
    margin: 0 0 38px; max-width: 720px;
  }
  .summary strong { color: var(--accent); }

  h2 {
    font-family: "Times New Roman", Georgia, serif;
    font-weight: 400; font-size: 22px;
    margin: 0 0 6px;
  }
  .intro {
    color: var(--muted); font-size: 14px;
    margin: 0 0 28px;
  }

  .grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-bottom: 56px;
  }
  @media (max-width: 720px) { .grid { grid-template-columns: 1fr; } }

  .brand-card {
    background: var(--card); border: 1px solid var(--line);
    border-radius: 14px;
    overflow: hidden;
    text-decoration: none; color: var(--ink);
    transition: all .15s ease;
    display: grid;
    grid-template-columns: 8px 1fr;
  }
  .brand-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 28px rgba(0,0,0,.06);
  }
  .brand-card .stripe { background: var(--card-accent); }
  .brand-card .body { padding: 22px 24px; }
  .brand-card .label {
    color: var(--muted); font-size: 10px;
    letter-spacing: 2px; text-transform: uppercase; font-weight: 700;
    margin-bottom: 4px;
  }
  .brand-card .name {
    font-family: "Times New Roman", Georgia, serif;
    font-weight: 400; font-size: 24px;
    margin: 0 0 6px;
  }
  .brand-card .tag {
    color: var(--card-accent); font-size: 13px;
    font-style: italic; margin-bottom: 10px;
    line-height: 1.35;
  }
  .brand-card .desc {
    color: var(--muted); font-size: 13px; line-height: 1.5;
  }

  .closing {
    background: var(--deep); color: #fff;
    border-radius: 14px; padding: 36px 32px;
    margin-bottom: 36px;
  }
  .closing .lbl {
    color: var(--gold); font-size: 11px;
    font-weight: 700; letter-spacing: 2px;
    margin-bottom: 10px;
  }
  .closing h3 {
    font-family: "Times New Roman", Georgia, serif;
    font-weight: 400; font-size: 28px;
    margin: 0 0 14px;
  }
  .closing p {
    color: var(--soft); margin: 0 0 16px;
    font-size: 14px; line-height: 1.55;
  }
  .closing a.cta {
    display: inline-block;
    background: var(--gold); color: var(--deep);
    text-decoration: none;
    padding: 10px 18px; border-radius: 999px;
    font-size: 13px; font-weight: 700; letter-spacing: 0.5px;
  }

  footer {
    color: var(--muted); font-size: 11px;
    border-top: 1px solid var(--line);
    padding-top: 18px;
    display: flex; justify-content: space-between; flex-wrap: wrap; gap: 8px;
  }
  footer a { color: var(--muted); text-decoration: none; }
  footer a:hover { color: var(--accent); }
</style>
</head>
<body>
  <div class="wrap">
    <div class="eyebrow">MOBILE-AS-A-SERVICE · PROPOSAL ARCHIVE</div>
    <h1>Proposals.</h1>
    <p class="lede">Brand-tailored mobile + admin Studio proposals,<br/>delivered under the SEYSO MaaS subscription model.</p>
    <p class="summary">
      Each proposal contains a 23-slide pitch deck, an interactive
      mobile-app mockup, an admin Studio mockup, and a platform
      investment one-pager. <strong>Built for the brand</strong> — the
      voice, the palette, the operational reality each one operates
      in. Browse below.
    </p>

    <h2>Brands</h2>
    <p class="intro">Apparel · accessories · activewear · skincare · wellness</p>

    <div class="grid">
__CARDS__
    </div>

    <div class="closing">
      <div class="lbl">NEW PROPOSAL?</div>
      <h3>We tailor a full pack in two weeks.</h3>
      <p>Six pillars, mobile + Studio mockups, pitch deck, pricing, and a deliverability-tuned outreach email — for any brand whose customer relationship is worth deepening.</p>
      <a class="cta" href="mailto:hello@seysoservices.com?subject=New%20MaaS%20proposal">Start a proposal</a>
    </div>

    <footer>
      <span>SEYSO · Mobile-as-a-Service</span>
      <a href="https://seysoservices.com">seysoservices.com</a>
    </footer>
  </div>
</body>
</html>
"""


# ---------------------------------------------------------- generate

ROOT = Path(__file__).parent

def url_encode_brand(name):
    return name.replace(" ", "%20").replace("ó", "%C3%B3")


def generate_per_brand():
    for b in BRANDS:
        p = b["palette"]
        html = PER_BRAND_TEMPLATE.format(
            name=b["name"],
            name_url=url_encode_brand(b["name"]),
            tagline=b["tagline"],
            summary=b["summary"],
            category=b["category"],
            deck=b["deck"],
            mobile=b["mobile"],
            studio=b["studio"],
            pricing=b["pricing"],
            **p,
        )
        out = ROOT / b["folder"] / "landing.html"
        out.write_text(html)
        print(f"  wrote {out.relative_to(ROOT.parent)}")


def generate_index():
    cards = []
    for b in BRANDS:
        accent = b["palette"]["accent"]
        muted = b["palette"]["muted"]
        cards.append(
            f'      <a class="brand-card" href="{b["folder"]}/landing.html" '
            f'style="--card-accent: {accent}; --card-muted: {muted};">\n'
            f'        <div class="stripe"></div>\n'
            f'        <div class="body">\n'
            f'          <div class="label">{b["category"]}</div>\n'
            f'          <div class="name">{b["name"]}</div>\n'
            f'          <div class="tag">{b["tagline"]}</div>\n'
            f'          <div class="desc">{b["summary"][:160]}…</div>\n'
            f'        </div>\n'
            f'      </a>'
        )
    html = INDEX_TEMPLATE.replace("__CARDS__", "\n".join(cards))
    out = ROOT / "index.html"
    out.write_text(html)
    print(f"  wrote {out.relative_to(ROOT.parent)}")


if __name__ == "__main__":
    print(f"generating per-brand landings ({len(BRANDS)})...")
    generate_per_brand()
    print("generating master index...")
    generate_index()
    print("done.")
