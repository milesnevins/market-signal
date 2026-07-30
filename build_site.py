import pathlib

scratch = pathlib.Path(__file__).parent
fonts_css = (scratch / "embedded-fonts.css").read_text()
NEWLINE = chr(10)

# ============================================================== CSS ==============================================================
CSS = """
:root{
  --bg:#f5f3ee;
  --fg:#1a1a18;
  --rule:#d9d4c8;
  --rule-strong:#1a1a18;
  --accent:#BF5700;
  --accent-glow:rgba(191,87,0,.28);
  --accent-wash:rgba(191,87,0,.08);
  --muted:#7a7567;
  --rising:#2a6b3c;
  --stable:#4a5568;
  --font-display:'Playfair Display', Georgia, serif;
  --font-body:'IBM Plex Sans', -apple-system, sans-serif;
  --font-mono:'IBM Plex Mono', 'SFMono-Regular', monospace;
  --font-brand:'Space Grotesk', var(--font-body);
}

@media (prefers-color-scheme: dark){
  :root{
    --bg:#18150f;
    --fg:#ece7db;
    --rule:#39342a;
    --rule-strong:#ece7db;
    --accent:#e3812e;
    --accent-glow:rgba(227,129,46,.30);
    --accent-wash:rgba(227,129,46,.10);
    --muted:#a59c8a;
    --rising:#5aa574;
    --stable:#93a0b3;
  }
}
:root[data-theme="dark"]{
  --bg:#18150f;
  --fg:#ece7db;
  --rule:#39342a;
  --rule-strong:#ece7db;
  --accent:#e3812e;
  --accent-glow:rgba(227,129,46,.30);
  --accent-wash:rgba(227,129,46,.10);
  --muted:#a59c8a;
  --rising:#5aa574;
  --stable:#93a0b3;
}
:root[data-theme="light"]{
  --bg:#f5f3ee;
  --fg:#1a1a18;
  --rule:#d9d4c8;
  --rule-strong:#1a1a18;
  --accent:#BF5700;
  --accent-glow:rgba(191,87,0,.28);
  --accent-wash:rgba(191,87,0,.08);
  --muted:#7a7567;
  --rising:#2a6b3c;
  --stable:#4a5568;
}

*{box-sizing:border-box;}

html, body{
  background:var(--bg);
  -webkit-print-color-adjust:exact;
  print-color-adjust:exact;
}

body{
  color:var(--fg);
  font-family:var(--font-body);
  font-weight:300;
  font-size:16px;
  line-height:1.7;
  margin:0;
  -webkit-font-smoothing:antialiased;
  transition:background .2s ease, color .2s ease;
}

@media (prefers-reduced-motion: reduce){
  body{transition:none;}
  .desk-card, .desk-card-arrow{transition:none !important;}
  .desk-card:hover{transform:none;}
}

a{ color:inherit; }

/* ---------- top nav ---------- */
.topnav{
  position:sticky;
  top:0;
  z-index:900;
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:20px;
  padding:15px 28px;
  background:var(--bg);
  border-bottom:1px solid var(--rule);
}
.topnav-brand{
  font-family:var(--font-display);
  font-size:16px;
  font-weight:600;
  color:var(--fg);
  text-decoration:none;
  flex-shrink:0;
  display:flex;
  align-items:center;
  gap:9px;
}
.brand-mark{flex-shrink:0;overflow:visible;}
.brand-mark .bm-bar{fill:var(--rule-strong);opacity:0.22;}
.brand-mark .bm-line{fill:none;stroke:var(--accent);stroke-width:2.25;stroke-linecap:round;stroke-linejoin:round;}
.brand-mark .bm-dot{fill:var(--accent);animation:bm-pulse 2.6s ease-in-out infinite;filter:drop-shadow(0 0 5px var(--accent-glow));}
@keyframes bm-pulse{
  0%,100%{opacity:1;transform:scale(1);}
  50%{opacity:0.6;transform:scale(1.4);}
}
.brand-mark .bm-dot{transform-origin:19px 3px;}
.topnav-links{
  display:flex;
  gap:20px;
  overflow-x:auto;
  font-family:var(--font-mono);
  font-size:10.5px;
  letter-spacing:0.09em;
  text-transform:uppercase;
  scrollbar-width:none;
  margin:0 4px;
}
.topnav-links::-webkit-scrollbar{display:none;}
.topnav-links a{
  color:var(--muted);
  text-decoration:none;
  white-space:nowrap;
  padding:5px 11px;
  border-radius:999px;
  border:1px solid transparent;
  transition:color .15s ease, border-color .15s ease, background .15s ease;
}
.topnav-links a:hover{color:var(--fg);}
.topnav-links a.active{color:var(--accent);background:var(--accent-wash);border-color:var(--accent-glow);}

/* ---------- theme toggle (now docked in nav) ---------- */
.theme-toggle{
  width:27px;
  height:27px;
  padding:0;
  display:flex;
  align-items:center;
  justify-content:center;
  background:transparent;
  border:1px solid var(--rule);
  border-radius:50%;
  color:var(--muted);
  cursor:pointer;
  flex-shrink:0;
  transition:color .15s ease, border-color .15s ease, background .15s ease;
}
.theme-toggle:hover{color:var(--fg);border-color:var(--muted);}
.theme-toggle:focus-visible{outline:1px solid var(--accent);outline-offset:2px;}
.theme-toggle svg{width:13px;height:13px;display:none;}
.theme-toggle[data-current="dark"] .icon-sun{display:block;}
.theme-toggle[data-current="light"] .icon-moon{display:block;}

/* ---------- pages ---------- */
.page{display:none;}
.page.active{display:block;}
.market{display:none;}
.market.active{display:block;}

/* ---------- market switcher ---------- */
.market-bar{
  display:flex;
  align-items:center;
  gap:12px;
  margin-bottom:8px;
}
.market-label{
  font-family:var(--font-mono);
  font-size:10px;
  text-transform:uppercase;
  letter-spacing:0.1em;
  color:var(--muted);
}
.market-select-wrap{position:relative;display:inline-block;}
.market-select-wrap::after{
  content:"\\25BE";
  position:absolute;
  right:13px;
  top:50%;
  transform:translateY(-50%);
  font-size:9px;
  color:var(--muted);
  pointer-events:none;
}
.market-select{
  appearance:none;
  -webkit-appearance:none;
  -moz-appearance:none;
  font-family:var(--font-mono);
  font-size:11px;
  letter-spacing:0.03em;
  color:var(--fg);
  background:var(--bg);
  border:1px solid var(--rule);
  border-radius:999px;
  padding:7px 30px 7px 14px;
  cursor:pointer;
  transition:border-color .15s ease;
}
.market-select:hover, .market-select:focus-visible{border-color:var(--accent);outline:none;}

.issue{
  max-width:720px;
  margin:0 auto;
  padding:56px 32px 96px;
}
.issue.home{max-width:820px;}

/* ---------- masthead ---------- */
.masthead{
  display:flex;
  justify-content:space-between;
  align-items:flex-end;
  gap:24px;
  flex-wrap:wrap;
  border-top:1px solid var(--rule-strong);
  padding-top:22px;
  padding-bottom:28px;
  border-bottom:1px solid var(--rule);
  margin-bottom:52px;
}
.wordmark{
  font-family:var(--font-display);
  font-size:29px;
  font-weight:600;
  letter-spacing:-0.01em;
  margin:0;
  line-height:1;
}
.wordmark .cre{color:var(--fg);}
.wordmark .signal{color:var(--accent);}
.masthead-meta{
  font-family:var(--font-mono);
  font-size:11px;
  color:var(--muted);
  letter-spacing:0.04em;
  text-align:right;
  line-height:1.8;
  font-variant-numeric:tabular-nums;
}
.masthead-meta .place{color:var(--fg);}

/* ---------- section eyebrow ---------- */
.eyebrow{
  font-family:var(--font-mono);
  font-size:11px;
  text-transform:uppercase;
  letter-spacing:0.14em;
  color:var(--muted);
  margin:0 0 20px;
}

/* ---------- market snapshot ---------- */
.snapshot{
  margin-bottom:14px;
  border:1px solid var(--rule);
  border-radius:20px;
  padding:4px 28px;
}
.snapshot-row{
  display:flex;
  justify-content:space-between;
  align-items:baseline;
  padding:15px 0;
  border-bottom:1px solid var(--rule);
  font-size:15px;
}
.snapshot-row:last-child{border-bottom:none;}
.snapshot-label{color:var(--fg);}
.direction{
  font-family:var(--font-mono);
  font-size:12px;
  letter-spacing:0.06em;
  text-transform:uppercase;
  display:inline-flex;
  align-items:center;
  gap:7px;
}
.direction .glyph{font-size:9px;position:relative;top:-1px;}
.direction.rising{color:var(--rising);}
.direction.stable{color:var(--stable);}
.direction.softening{color:var(--accent);}

.key-line{
  font-size:12.5px;
  font-style:italic;
  color:var(--muted);
  margin:18px 0 0;
  line-height:1.7;
}

/* ---------- category divider ---------- */
.asset-class{
  display:flex;
  align-items:center;
  gap:16px;
  margin:64px 0 30px;
}
.asset-class:first-of-type{margin-top:52px;}
.asset-class .label{
  font-family:var(--font-mono);
  font-size:11px;
  text-transform:uppercase;
  letter-spacing:0.14em;
  color:var(--fg);
  white-space:nowrap;
}
.asset-class .fill{flex:1;border-top:1px solid var(--rule);}

/* ---------- signal ---------- */
.signal-card{
  margin-bottom:26px;
  border:1px solid var(--rule);
  border-radius:20px;
  padding:38px 34px;
}
.signal-title{
  font-family:var(--font-display);
  font-size:22px;
  font-weight:600;
  letter-spacing:-0.005em;
  margin:0 0 6px;
  text-wrap:balance;
  max-width:34ch;
}
.signal-subtitle{
  font-style:italic;
  color:var(--muted);
  font-size:14.5px;
  margin:0 0 26px;
  max-width:46ch;
}
.block{margin-bottom:20px;max-width:58ch;}
.block-label{
  font-family:var(--font-mono);
  font-size:9.5px;
  font-weight:500;
  text-transform:uppercase;
  letter-spacing:0.13em;
  color:var(--accent);
  margin:0 0 9px;
}
.block p{margin:0;}
.implications ul{margin:0;padding:0;list-style:none;}
.implications li{
  padding-left:1.15em;
  text-indent:-1.15em;
  margin-bottom:7px;
  color:var(--fg);
}
.implications li::before{content:"\\2014\\0020";color:var(--muted);}
.watch p{font-style:italic;color:var(--muted);font-size:14.5px;}

.src{
  color:inherit;
  text-decoration:underline;
  text-decoration-color:var(--rule);
  text-decoration-thickness:1px;
  text-underline-offset:3px;
  transition:color .15s ease, text-decoration-color .15s ease;
}
.src:hover{color:var(--accent);text-decoration-color:var(--accent);}

/* ---------- filter bar ---------- */
.filter-bar{
  display:flex;
  flex-wrap:wrap;
  align-items:center;
  justify-content:space-between;
  gap:14px;
  margin:8px 0 40px;
  padding-bottom:20px;
  border-bottom:1px solid var(--rule);
}
.filter-chips{display:flex;flex-wrap:wrap;gap:8px;}
.filter-chip{
  font-family:var(--font-mono);
  font-size:10.5px;
  letter-spacing:0.04em;
  text-transform:uppercase;
  color:var(--muted);
  background:none;
  border:1px solid var(--rule);
  border-radius:999px;
  padding:6px 13px;
  cursor:pointer;
  transition:color .15s ease, border-color .15s ease, background .15s ease;
}
.filter-chip:hover{color:var(--fg);}
.filter-chip.active{color:var(--accent);background:var(--accent-wash);border-color:var(--accent-glow);}
.filter-search-wrap{flex-shrink:0;}
.filter-search{
  font-family:var(--font-body);
  font-size:13px;
  color:var(--fg);
  background:var(--bg);
  border:1px solid var(--rule);
  border-radius:999px;
  padding:8px 16px;
  width:200px;
  transition:border-color .15s ease;
}
.filter-search::placeholder{color:var(--muted);}
.filter-search:focus{outline:none;border-color:var(--accent);}
@media (max-width:560px){
  .filter-search{width:100%;}
  .filter-bar{flex-direction:column;align-items:stretch;}
}

/* ---------- final observation ---------- */
.final-observation{
  border:1px solid var(--rule);
  border-radius:20px;
  margin-top:58px;
  padding:42px 36px;
}
.final-observation .eyebrow{color:var(--muted);}
.final-observation p{margin:0 0 18px;max-width:60ch;}
.final-observation ul{margin:24px 0 0;padding:0;list-style:none;max-width:60ch;}
.final-observation li{padding-left:1.15em;text-indent:-1.15em;margin-bottom:8px;}
.final-observation li::before{content:"\\2014\\0020";color:var(--muted);}

/* ---------- footer ---------- */
footer{
  display:flex;
  justify-content:space-between;
  align-items:center;
  gap:16px;
  flex-wrap:wrap;
  margin-top:64px;
  padding-top:22px;
  border-top:1px solid var(--rule);
}
.footer-wordmark{font-family:var(--font-display);font-size:15px;color:var(--muted);}
.footer-wordmark .signal{color:var(--accent);}
.tagline{
  font-family:var(--font-mono);
  font-size:10.5px;
  color:var(--muted);
  font-style:italic;
  letter-spacing:0.02em;
}

/* ---------- home dashboard ---------- */
.home-hero{margin-bottom:36px;}
.home-title{
  font-family:var(--font-display);
  font-size:38px;
  font-weight:600;
  letter-spacing:-0.01em;
  margin:0 0 14px;
  text-wrap:balance;
}
.accent-rule{
  width:60px;
  height:3px;
  border-radius:3px;
  margin:0 0 18px;
  background:linear-gradient(90deg, var(--accent), transparent);
}
.home-lede{
  font-size:16px;
  color:var(--fg);
  max-width:62ch;
  margin:0 0 16px;
}
.home-lede.muted{color:var(--muted);}

.desk-grid{
  display:flex;
  flex-direction:column;
  gap:10px;
  margin-top:6px;
}
.desk-card{
  background:var(--bg);
  border:1px solid var(--rule);
  border-radius:14px;
  transition:transform .2s cubic-bezier(.2,.7,.3,1), border-color .2s ease, box-shadow .3s ease;
}
.desk-card:hover{
  transform:translateY(-2px);
  border-color:var(--accent);
  box-shadow:0 14px 34px -20px var(--accent-glow), 0 2px 10px -4px var(--accent-glow);
}
.desk-card-link{
  display:block;
  padding:12px 20px;
  text-decoration:none;
  color:inherit;
  cursor:pointer;
}
.desk-card-whatis{
  display:block;
  font-family:var(--font-mono);
  font-size:10.5px;
  letter-spacing:0.03em;
  color:var(--muted);
  text-decoration:none;
  padding:9px 20px;
  border-top:1px solid var(--rule);
  transition:color .15s ease;
}
.desk-card-whatis:hover{color:var(--accent);}
.desk-row-top{
  display:flex;
  align-items:baseline;
  justify-content:space-between;
  gap:16px;
}
.desk-card-name{
  font-family:var(--font-display);
  font-weight:600;
  font-size:18px;
  letter-spacing:-0.005em;
  white-space:nowrap;
}
.desk-card-name .cre{color:var(--fg);}
.desk-card-name .signal{color:var(--accent);}
.desk-card-arrow{
  font-family:var(--font-mono);
  font-size:15px;
  color:var(--muted);
  flex-shrink:0;
  transition:transform .2s ease, color .15s ease;
}
.desk-card:hover .desk-card-arrow{
  color:var(--accent);
  transform:translateX(4px);
}
.desk-row-bottom{
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:16px;
  flex-wrap:wrap;
  margin-top:6px;
}
.desk-card-desc{
  font-size:13.5px;
  line-height:1.5;
  color:var(--fg);
  margin:0;
  flex:1;
  min-width:200px;
}
.desk-card-meta{
  display:inline-block;
  font-family:var(--font-mono);
  font-size:8.5px;
  letter-spacing:0.06em;
  text-transform:uppercase;
  color:var(--muted);
  padding:4px 9px;
  border:1px solid var(--rule);
  border-radius:999px;
  white-space:nowrap;
  flex-shrink:0;
}
.desk-card-link:focus-visible, .desk-card-whatis:focus-visible{outline:2px solid var(--accent);outline-offset:2px;}

/* ---------- responsive ---------- */
@media (max-width:560px){
  .topnav{padding:12px 16px;gap:12px;}
  .issue{padding:40px 20px 72px;}
  .masthead{flex-direction:column;align-items:flex-start;}
  .masthead-meta{text-align:left;}
  .wordmark{font-size:26px;}
  .home-title{font-size:28px;}
  .signal-title{font-size:20px;max-width:none;}
  .asset-class{margin:48px 0 24px;}
  footer{flex-direction:column;align-items:flex-start;}
  .desk-card-link{padding:16px 18px;}
  .desk-card-whatis{padding:10px 18px;}
  .desk-card-desc{min-width:0;}
}

@media print{
  .issue{padding:24px 8px;}
  .topnav{display:none;}
}

/* ---------- about / explainer pages ---------- */
.issue.about{max-width:640px;}
.about-page-title{
  font-family:var(--font-display);
  font-size:26px;
  font-weight:600;
  margin:14px 0 10px;
}
.about-page-lede{
  color:var(--muted);
  font-size:14.5px;
  max-width:56ch;
  margin:0 0 28px;
}
.about-switcher{
  display:flex;
  flex-wrap:wrap;
  gap:8px;
  margin-bottom:8px;
  border-bottom:1px solid var(--rule);
  padding-bottom:20px;
}
.about-switch-link{
  font-family:var(--font-mono);
  font-size:10.5px;
  letter-spacing:0.06em;
  text-transform:uppercase;
  color:var(--muted);
  text-decoration:none;
  padding:6px 13px;
  border-radius:999px;
  border:1px solid var(--rule);
  transition:color .15s ease, border-color .15s ease;
}
.about-switch-link:hover{color:var(--fg);}
.about-switch-link.active{color:var(--accent);border-color:var(--accent);}
.about-title{
  font-family:var(--font-display);
  font-size:28px;
  font-weight:600;
  margin:28px 0 8px;
}
.about-subtitle{
  color:var(--muted);
  font-style:italic;
  font-size:15px;
  margin:0 0 22px;
}
.market .about-title{margin-top:0;}
.about-terms{
  margin-top:26px;
  padding:22px 24px;
  border:1px solid var(--rule);
  border-radius:14px;
}
.about-terms-label{
  font-family:var(--font-mono);
  font-size:10.5px;
  letter-spacing:0.08em;
  text-transform:uppercase;
  color:var(--muted);
  margin:0 0 14px;
}
.about-terms ul{margin:0;padding:0;list-style:none;}
.about-terms li{margin-bottom:10px;font-size:14px;line-height:1.6;}
.about-terms li:last-child{margin-bottom:0;}
.about-term{color:var(--fg);font-weight:600;}
.about-back{
  display:inline-block;
  margin-top:32px;
  font-family:var(--font-mono);
  font-size:11px;
  color:var(--muted);
  text-decoration:none;
}
.about-back:hover{color:var(--accent);}

/* ---------- brand wordmark override (must stay last to win over .wordmark/.footer-wordmark/.desk-card-name) ---------- */
.brand-word{font-family:var(--font-brand);font-weight:700;letter-spacing:-0.015em;}
.brand-word .cre{color:var(--fg);}
.brand-word .signal{color:var(--accent);}
"""

# ============================================================== helpers ==============================================================

def glyph(direction):
    return {"rising": "&#9650;", "stable": "&#9679;", "softening": "&#9660;"}[direction]


def snapshot_html(rows):
    out = []
    for label, direction in rows:
        out.append(
            f'    <div class="snapshot-row"><span class="snapshot-label">{label}</span>'
            f'<span class="direction {direction}"><span class="glyph">{glyph(direction)}</span>{direction.capitalize()}</span></div>'
        )
    return "\n".join(out)


def signals_html(trigger_label, signals, implications_label="Market Implications"):
    out = []
    last_cat = None
    for s in signals:
        if s["category"] != last_cat:
            out.append(f'  <div class="asset-class" data-category="{s["category"]}"><span class="label">{s["category"]}</span><span class="fill"></span></div>')
            last_cat = s["category"]
        impl = "\n".join(f"      <li>{i}</li>" for i in s["implications"])
        out.append(f'''  <div class="signal-card" data-category="{s["category"]}">
    <h3 class="signal-title">{s["title"]}</h3>
    <p class="signal-subtitle">{s["subtitle"]}</p>
    <div class="block"><p class="block-label">{trigger_label}</p><p>{s["trigger"]}</p></div>
    <div class="block"><p class="block-label">Why This Matters</p><p>{s["why"]}</p></div>
    <div class="block implications"><p class="block-label">{implications_label}</p><ul>
{impl}
    </ul></div>
    <div class="block watch"><p class="block-label">What to Watch</p><p>{s["watch"]}</p></div>
  </div>''')
    return "\n".join(out)


def filter_bar_html(signals):
    seen = []
    for s in signals:
        if s["category"] not in seen:
            seen.append(s["category"])
    if not seen:
        return ""
    chips = ['      <button type="button" class="filter-chip active" data-filter-cat="all" onclick="window.__filterSignals(this)">All</button>']
    for cat in seen:
        chips.append(f'      <button type="button" class="filter-chip" data-filter-cat="{cat}" onclick="window.__filterSignals(this)">{cat}</button>')
    return f'''  <div class="filter-bar">
    <div class="filter-chips">
{chr(10).join(chips)}
    </div>
    <div class="filter-search-wrap">
      <input type="text" class="filter-search" placeholder="Search signals&hellip;" oninput="window.__filterSignals(this)">
    </div>
  </div>'''


def final_observation_html(paragraphs, bullets):
    p = "\n".join(f"    <p>{x}</p>" for x in paragraphs)
    b = "\n".join(f"      <li>{x}</li>" for x in bullets)
    return f'''  <div class="final-observation">
    <div class="accent-rule"></div>
    <p class="eyebrow">Final Observation</p>
{p}
    <ul>
{b}
    </ul>
  </div>'''


def masthead_html(name_a, name_b, dateline, drop, coverage):
    return f'''  <div class="masthead">
    <p class="wordmark"><span class="cre">{name_a}</span><span class="signal">{name_b}</span></p>
    <div class="masthead-meta">
      <span class="place">{dateline}</span> &middot; {drop}<br>
      COVERAGE: {coverage}
    </div>
  </div>'''


def footer_html(name_a, name_b, tagline):
    return f'''  <footer>
    <span class="footer-wordmark"><span class="cre">{name_a}</span><span class="signal">{name_b}</span></span>
    <span class="tagline">{tagline}</span>
  </footer>'''


def issue_page(page_id, active, name_a, name_b, dateline, drop, coverage, snapshot_rows,
               trigger_label, signals, final_paragraphs, final_bullets, tagline, implications_label="Market Implications",
               sample_notice=None):
    active_cls = " active" if active else ""
    notice = ""
    if sample_notice:
        notice = f'<p class="key-line" style="margin:-32px 0 52px;">{sample_notice}</p>'
    return f'''<section id="page-{page_id}" class="page{active_cls}">
<div class="issue">
{masthead_html(name_a, name_b, dateline, drop, coverage)}
{notice}
  <p class="eyebrow">Market Snapshot</p>
  <div class="snapshot">
{snapshot_html(snapshot_rows)}
  </div>
  <p class="key-line">Rising &mdash; positive directional momentum &middot; Stable &mdash; no meaningful directional shift &middot; Softening &mdash; reduced activity or tightening conditions</p>

  <p class="eyebrow" style="margin-top:64px;">Signals</p>
{filter_bar_html(signals)}

{signals_html(trigger_label, signals, implications_label)}

{final_observation_html(final_paragraphs, final_bullets)}

{footer_html(name_a, name_b, tagline)}
</div>
</section>'''


def market_select_html(page_id, markets):
    opts = "\n".join(f'      <option value="{mid}">{label}</option>' for mid, label in markets)
    return f'''  <div class="market-bar">
    <span class="market-label">Market</span>
    <div class="market-select-wrap">
      <select class="market-select" data-desk="{page_id}" onchange="window.__setMarket('{page_id}', this.value)">
{opts}
      </select>
    </div>
  </div>'''


def market_block_html(page_id, market_id, active, name_a, name_b, dateline, drop, coverage, snapshot_rows,
                       trigger_label, signals, final_paragraphs, final_bullets, tagline,
                       implications_label="Market Implications", sample_notice=None, coming_soon=None):
    active_cls = " active" if active else ""
    if coming_soon:
        return f'''<div id="market-{page_id}-{market_id}" class="market{active_cls}">
{masthead_html(name_a, name_b, dateline, drop, coverage)}
  <p class="key-line" style="margin:-32px 0 0;">{coming_soon}</p>
</div>'''
    notice = ""
    if sample_notice:
        notice = f'<p class="key-line" style="margin:-32px 0 52px;">{sample_notice}</p>'
    return f'''<div id="market-{page_id}-{market_id}" class="market{active_cls}">
{masthead_html(name_a, name_b, dateline, drop, coverage)}
{notice}
  <p class="eyebrow">Market Snapshot</p>
  <div class="snapshot">
{snapshot_html(snapshot_rows)}
  </div>
  <p class="key-line">Rising &mdash; positive directional momentum &middot; Stable &mdash; no meaningful directional shift &middot; Softening &mdash; reduced activity or tightening conditions</p>

  <p class="eyebrow" style="margin-top:64px;">Signals</p>
{filter_bar_html(signals)}

{signals_html(trigger_label, signals, implications_label)}

{final_observation_html(final_paragraphs, final_bullets)}

{footer_html(name_a, name_b, tagline)}
</div>'''


def multi_market_page(page_id, active, markets, market_blocks):
    active_cls = " active" if active else ""
    return f'''<section id="page-{page_id}" class="page{active_cls}">
<div class="issue">
{market_select_html(page_id, markets)}
{chr(10).join(market_blocks)}
</div>
</section>'''


# ============================================================== CRE (existing, tested content) ==============================================================

def src(url, text):
    return f'<a class="src" href="{url}" target="_blank" rel="noopener noreferrer">{text}</a>'

CRE_SNAPSHOT = [
    ("Development Activity", "rising"),
    ("Office Pipeline", "stable"),
    ("Industrial Momentum", "rising"),
    ("Mixed-Use Activity", "rising"),
    ("Capital Availability", "stable"),
    ("Infrastructure Relevance", "rising"),
]

CRE_SIGNALS = [
    dict(category="Industrial", title="Amazon Confirmed as Anchor Behind Southeast Austin Mega-Project",
         subtitle="A $5.6 Billion Infrastructure Package Follows the Tenant, Not the Other Way Around",
         trigger=f'''Austin officials confirmed that {src("https://www.kut.org/austin/2026-07-21/secrets-out-amazon-is-the-company-behind-austins-fast-tracked-dogs-head-project", "Amazon's robotics division is the previously unnamed tenant")} behind the roughly 2,600-acre &ldquo;Dog's Head&rdquo; site along the Colorado River in Southeast Austin, and on July 23 {src("https://austincurrent.org/2026/07/23/dogshead-austin-texas-development/", "the Austin City Council voted 7-3 to approve Tax Increment Reinvestment Zone financing")} for the site, with developer Endeavor projecting roughly $3.5 billion in property tax revenue over 30 years to fund infrastructure covering up to 12,000 homes and 4 million square feet of industrial space.''',
         why="A TIRZ vote is a bet the city is willing to make with its own future tax revenue, not just a rezoning approval &mdash; the city is committing to fund infrastructure against tax increment that only materializes if the development actually gets built and leases up as projected. That the anchor tenant turned out to be Amazon's robotics division, rather than a speculative logistics user, changes the credit quality of that bet: a name-brand corporate tenant with disclosed job commitments is a very different anchor than an unnamed spec building. The 1,478-to-645 public sign-up split ahead of the vote also shows this was a genuinely contested approval, not a rubber stamp.",
         implications=[
             "Commits city tax revenue to infrastructure years before the site fully leases up",
             "Establishes Southeast Austin's Colorado River corridor as a new large-scale industrial and mixed-use submarket",
             "Sets a scale precedent for how large a single anchor-tenant deal can move a TIRZ vote",
             "Leaves a pending council vote on the site's regulating plan and development standards still to come",
         ],
         watch="Whether Amazon's disclosed job commitments materialize on the timeline implied by the TIRZ financing, and the outcome of the still-pending council vote on the site's regulating plan."),
    dict(category="Industrial", title="Tesla Signs Major Industrial Lease at Austin Hills Commerce Center",
         subtitle="A Second Big-Box User Confirms the Southeast Corridor Thesis Independently",
         trigger=f'''{src("https://therealdeal.com/texas/2026/07/07/tesla-leases-683k-sf-industrial-building-in-austin-sweep/", "Tesla signed a lease for roughly 682,000 square feet of speculative industrial space")} at 11801 Decker Lake Road, the second phase of Austin Hills Commerce Center &mdash; a 1.4 million-square-foot project from Sansone Group and Principal Asset Management &mdash; with completion targeted for January 2027. Tesla's intended use of the space was not disclosed.''',
         why="Tesla signing for two-thirds of a million square feet of speculative industrial space, without disclosing what it's for, is itself informative &mdash; companies don't pre-lease that much unmarked capacity unless they're confident enough in near-term demand to pay for optionality now rather than wait for a build-to-suit later. Read next to the Dog's Head announcement in the same broad corridor, this is the second large corporate industrial user to commit to Southeast Austin within the same month, from two very different demand drivers, even as reported Austin-metro warehouse vacancy sits near 17%.",
         implications=[
             "Confirms Southeast Austin industrial demand from a second major corporate user independent of the Dog's Head deal",
             "Reduces available large-block speculative industrial inventory in the corridor ahead of the 2027 delivery",
             "Validates developer bets on pre-built speculative big-box space even as metro-wide vacancy runs near 17%",
             "May pressure land pricing for remaining large industrial parcels along the Decker Lake corridor",
         ],
         watch="Whether Tesla discloses its intended use of the space as the January 2027 completion approaches, and whether other large users follow into the same commerce center."),
    dict(category="Office", title="Hines Pays $733/SF for Fully Leased Downtown Austin Tower",
         subtitle="A Full-Price Trophy Trade Is a Different Signal Than the Metro's Vacancy Rate",
         trigger=f'''{src("https://therealdeal.com/texas/2026/07/13/houston-based-hines-snags-405-colorado-for-733-per-sf/", "Hines paid $151 million ($733 per square foot) to buy the 206,000-square-foot tower at 405 Colorado St.")} from Brandywine Realty Trust, a 25-story, Class-A building completed in 2021 and fully leased to tenants including JPMorgan Chase, Bain &amp; Company, and AllianceBernstein; Eastdil Secured advised seller Brandywine, which is executing a plan to sell roughly $300 million of assets from its portfolio.''',
         why="A fully-leased trophy tower trading at $733 per square foot, in a market where office vacancy is running near 25%, is a specific bet on tenant quality and lease term, not a bet on the office sector broadly &mdash; Hines is underwriting JPMorgan, Bain, and AllianceBernstein's credit and renewal likelihood, not downtown Austin office fundamentals as a whole. That Brandywine sold at what appears to be a strong basis, as part of a disclosed disposition program, also suggests the seller found this specific asset easier to monetize than the rest of its portfolio.",
         implications=[
             "Confirms full-price capital remains available for fully-leased, credit-tenant office even as metro vacancy runs near 25%",
             "Signals office pricing is bifurcating sharply by tenant quality and lease term, not moving as one asset class",
             "Advances Brandywine's disclosed $300 million disposition program by one confirmed sale",
             "Provides a $733/SF comp for other fully-leased downtown Austin towers considering a sale",
         ],
         watch="Whether Brandywine's remaining Austin office assets, including One Uptown, trade at comparable pricing, and Hines' plans for the building at lease rollover."),
    dict(category="Multifamily", title="Brandywine Puts Uptown ATX Apartment Tower Up for Sale",
         subtitle="Selling a 93%-Leased Asset Is a Capital-Recycling Decision, Not a Distress Sale",
         trigger=f'''{src("https://therealdeal.com/texas/2026/07/27/brandywine-looks-to-sell-uptown-atx-apartment-complex/", "Brandywine Realty Trust disclosed on its Q2 earnings call that it is marketing Solaris")}, a 341-unit apartment complex at 2800 Solaris St. in the Uptown ATX development that was 93% leased as of the prior month, and is separately seeking a capital partner for the adjacent One Uptown office building, with both transactions expected to close later this year.''',
         why="A REIT selling a 93%-leased, stabilized apartment asset at the same time it sells a fully-leased office trophy nearby is a capital-recycling decision, not a signal that either asset is underperforming &mdash; Brandywine is converting stabilized cash flow into cash to fund its stated $300 million disposition program, which likely goes toward debt paydown or redeployment elsewhere. That the company is simultaneously seeking a partner rather than an outright sale for One Uptown suggests it wants to retain some upside in that asset while still de-risking its balance sheet.",
         implications=[
             "Converts a stabilized, income-producing asset into cash rather than holding for continued yield",
             "Advances the same $300 million disposition program behind the 405 Colorado St. office sale",
             "Signals Brandywine is actively de-levering in Austin even where in-place performance is strong",
             "Tests investor demand for stabilized, 90%-plus-leased Austin multifamily in the current rate environment",
         ],
         watch="The eventual sale price and buyer for Solaris, and whether Brandywine finds a capital partner for One Uptown on the timeline it disclosed."),
    dict(category="Infrastructure", title="Project Connect Light Rail Shrinks to 9.8 Miles, No Subway, No Airport Link",
         subtitle="Six Years After Voter Approval, the Line Voters Funded Isn't the Line Getting Built",
         trigger=f'''{src("https://www.kut.org/transportation/2026-07-24/austin-tx-project-connect-explainer-capmetro-light-rail-bus-train", "Austin's Project Connect light rail has been scaled down from an original 20.2-mile, 31-station plan with a downtown subway to 9.8 miles and 15 stations")} with no subway and no airport connection, nearly six years after 2020 voter approval; the downtown tunnel and airport link, together a $2&ndash;4 billion cost driver, were both eliminated, construction is still not slated to start until 2027, and current light-rail cost estimates exceed $8.2 billion, up from an original $5.8 billion estimate.''',
         why="A rail line's scope and timeline are the single biggest variable in how station-area land actually gets valued, and this is a material downgrade on both dimensions from what voters funded in 2020 &mdash; a shorter route with no downtown subway or airport connection serves fewer trip patterns and touches fewer parcels than the original plan did. That the cost estimate has grown even as scope shrank means the per-mile economics of this project have deteriorated substantially, which matters for how much confidence to place in any future scope restoration.",
         implications=[
             "Narrows the set of parcels that can credibly underwrite against confirmed future rail access",
             "Eliminates the airport connection that would have supported hospitality and office land near the terminal",
             "Signals cost discipline problems that could pressure future extensions or scope restoration",
             "Pushes any land-value effect further out, since construction itself doesn't start until 2027",
         ],
         watch="Whether the 2027 construction start holds, and whether CapMetro identifies funding to restore any of the cut scope in a later phase."),
    dict(category="Mixed-Use", title="Ownership Turns Over on Two Austin-Area Master-Planned Communities",
         subtitle="Horizontal Land Plays Are Still Financeable, Just Through Different Structures",
         trigger=f'''{src("https://www.bisnow.com/austin-san-antonio/news/master-planned-communities/mpc-projects-pose-challenges-texas-developers-135594", "Rockspring closed a $28.2 million loan to begin construction on The Highlands")}, a 254-acre master-planned community in Marble Falls combining houses, apartments, and retail, while The Ridge, a 6,200-home master-planned community south of Austin, was acquired by Wilson Capital in July 2026.''',
         why="Master-planned communities typically take 10 to 20 years to complete and depend on public improvement district bonds and special financing districts, with financing delays historically the biggest bottleneck &mdash; a fresh construction loan on one project and a full ownership change on another, in the same stretch, show capital is still willing to fund multi-decade horizontal land plays in the Austin exurbs despite tighter underwriting conditions elsewhere. Nearly 20 Texas MPCs ranked among the top 50 best-selling nationally in 2025, concentrated in Austin, Houston, Dallas-Fort Worth, and San Antonio.",
         implications=[
             "Confirms construction and acquisition capital remains available for multi-decade MPC land plays",
             "Tests whether new ownership at The Ridge accelerates or slows its 6,200-home build-out",
             "Adds The Highlands' mixed housing-and-retail program to the Austin-exurb supply pipeline",
             "Reinforces Texas MPCs' outsized share of national best-selling master-planned community rankings",
         ],
         watch="Wilson Capital's stated plans for The Ridge's build-out pace, and whether The Highlands secures its next construction draw on schedule."),
]

CRE_FINAL_PARAGRAPHS = [
    "This week's Austin activity splits into two distinct stories: large corporate users continuing to make multi-year commitments to specific corridors, and institutional owners actively recycling capital out of otherwise-healthy assets. Amazon's TIRZ financing, Tesla's industrial lease, and two master-planned-community transactions all reflect long-horizon conviction; Brandywine's back-to-back sale of a fully-leased office tower and a 93%-leased apartment complex reflects the opposite instinct.",
    "The Hines and Brandywine signals are worth reading together. A full-price, $733/SF trophy office trade and a stabilized apartment sale happening at the same company, in the same disposition program, in the same month, show that even sponsors with strong in-place performance are choosing to de-lever in Austin right now &mdash; not because the assets are underperforming, but because converting stabilized cash flow into cash is the priority.",
    "Project Connect's scope reduction is the story with the longest tail. A shorter route, no subway, no airport connection, and a cost estimate that grew even as scope shrank all narrow the set of land that can credibly underwrite against confirmed future rail access &mdash; a material downgrade from what voters approved in 2020, worth remembering every time a station-area land deal cites Project Connect as a value driver.",
]
CRE_FINAL_BULLETS = [
    "Amazon's TIRZ financing and Tesla's industrial lease are both multi-year corridor bets, not short-term demand responses",
    "Brandywine is recycling capital out of a fully-leased office tower and a 93%-leased apartment complex in the same program",
    "A full-price, $733/SF office trade shows quality assets still clear the market even as metro vacancy runs near 25%",
    "Project Connect now delivers less than voters approved in 2020, at a higher cost, with construction still two years out",
]

CRE_MARKETS = [
    ("austin", "Austin, TX"),
    ("usc", "Los Angeles, CA"),
    ("nyu", "New York, NY"),
    ("uga", "Atlanta, GA"),
    ("uf", "Miami, FL"),
]

CRE_AUSTIN_BLOCK = market_block_html(
    "cre", "austin", True, "CRE", "Signal", "AUSTIN, TEXAS", "JULY 29, 2026", "JULY 7&ndash;27, 2026",
    CRE_SNAPSHOT, "What Happened", CRE_SIGNALS, CRE_FINAL_PARAGRAPHS, CRE_FINAL_BULLETS,
    "No predictions. No stock references. Project-anchored interpretation only.",
    implications_label="Local Market Implications",
)
USC_SNAPSHOT = [
    ("Development Activity", "rising"),
    ("Office Pipeline", "stable"),
    ("Industrial Momentum", "stable"),
    ("Mixed-Use Activity", "rising"),
    ("Capital Availability", "stable"),
    ("Infrastructure Relevance", "stable"),
]

USC_SIGNALS = [
    dict(category="Industrial", title="Rexford Industrial Quadruples Planned Asset Sales After $506.9M Loss",
         subtitle="LA's Dominant Industrial Landlord Is Pruning Even Strong-Fundamentals Product",
         trigger=f'''{src("https://www.bisnow.com/los-angeles/news/industrial/rexford-takes-500m-loss-plans-up-to-2b-in-dispositions-this-year-135577", "Rexford Industrial Realty raised its 2026 disposition guidance to $1.5&ndash;2 billion")}, up from $400&ndash;500 million, after posting a $506.9 million net loss in Q2 driven by a noncash impairment; the expanded sell-off covers roughly 8 million square feet, about 16% of Rexford's ~50 million-square-foot LA-basin portfolio, with the company targeting properties it says carry &ldquo;substantially above-market in-place rents&rdquo; from acquisitions &ldquo;at the height of the market.&rdquo;''',
         why="A REIT quadrupling its planned dispositions while eating a half-billion-dollar impairment is a concrete repricing signal, not a portfolio-management footnote &mdash; Rexford is the single largest and most closely-watched industrial landlord in the LA basin, so its own admission that certain assets were bought at peak valuations tells you where the broader market's cost basis stands relative to today's rents. That same-property occupancy still sits at 95.7% even amid this pruning shows the portfolio's operating performance isn't the problem; the entry price is.",
         implications=[
             "Signals that even best-in-class LA industrial product bought at peak pricing no longer pencils at current values",
             "Directs roughly $1 billion of sale proceeds toward paying down $1 billion of debt maturing in 2027",
             "Provides a reference point for how aggressively other LA industrial owners may need to reprice legacy acquisitions",
             "Confirms strong 95.7% same-property occupancy even as the company prunes its highest-basis assets",
         ],
         watch="The pricing Rexford actually achieves on the expanded $1.5&ndash;2 billion disposition slate, and whether other LA-basin industrial REITs follow with similar guidance revisions."),
    dict(category="Industrial", title="Aerospace and Defense Tenants Drive a Two-Speed South Bay Industrial Market",
         subtitle="Longer Leases at Premium Terms Are Reshaping Which Submarket Wins",
         trigger=f'''{src("https://www.bisnow.com/los-angeles/news/industrial/los-angeles-industrial-defense-tech-aerospace-135477", "LA industrial leasing hit 15.7 million square feet in Q2 2026, up 40.4% year-over-year")}, with South Bay accounting for 42% of all leases (up from a 34% historical average) on the strength of aerospace and defense tenants, including a 512,000-square-foot Valar Atomics lease in Torrance and a roughly 400,000-square-foot Divergent Technologies lease in Long Beach; vacancy in the submarket fell to 3.9% and average weighted lease terms stretched from 72 months in 2025 to 83 months today.''',
         why="Aerospace and defense tenants signing 400,000-to-500,000-square-foot leases at terms nearly seven years long is a fundamentally different demand driver than the e-commerce and third-party-logistics leasing that has dominated industrial headlines for years &mdash; these tenants commit to long-duration, mission-specific buildouts tied to government contracts, not seasonal throughput. That South Bay's share of citywide leasing jumped from a 34% historical average to 42% in one quarter shows landlords in that specific submarket now have real pricing power that the rest of the LA industrial market, still facing broader vacancy pressure, does not.",
         implications=[
             "Confirms South Bay is becoming a distinct defense-tech industrial corridor, not just a logistics submarket",
             "Extends average lease duration meaningfully, giving South Bay landlords longer-term income visibility",
             "Reflects roughly $153 billion in defense spending tied to recent federal legislation flowing into real demand",
             "Widens the performance gap between South Bay and the broader, softer LA industrial market",
         ],
         watch="Whether aerospace/defense leasing volume holds through the back half of 2026, and if South Bay vacancy continues falling as landlords test higher asking rents."),
    dict(category="Office", title="Santa Monica Office Building Sells for Conversion to a School",
         subtitle="A 70%-Vacant Building Finds an Exit Outside the Office Category Entirely",
         trigger=f'''{src("https://www.bisnow.com/los-angeles/news/deal-sheet/santa-monica-offices-to-become-school-los-angeles-deal-sheet-135476", "A roughly 100,000-square-foot office and medical building at 2701 Ocean Park Boulevard in Santa Monica, more than 70% vacant, sold to an undisclosed school")} for campus relocation, brokered by Colliers, Industry Partners, and Newmark.''',
         why="A school buying a vacant office building isn't a real estate trade in the traditional sense &mdash; it's an institutional user removing the asset from the office market entirely, with no rent-roll dependency on the office leasing cycle at all. Sellers accept this kind of sale specifically when they've concluded the building can't be re-leased as office at a viable basis, which is itself a data point about the depth of vacancy in this submarket and building type. Unlike a residential or hotel conversion, a school use also permanently removes the building from any future return to commercial use, since institutional buyers rarely resell.",
         implications=[
             "Removes a vacant office building from the leasable office stock permanently, not temporarily",
             "Confirms the seller had concluded re-leasing as office was not viable at this building's basis",
             "Signals institutional users are opportunistically absorbing distressed office product at a discount",
             "May be replicable for other heavily vacant medical-office buildings in the Westside submarket",
         ],
         watch="The sale price once disclosed, and whether other Westside office owners pursue similar institutional-use exits.",
         tldr="A 70%-vacant Santa Monica office building sold to a school, permanently removing it from the office market rather than waiting for a lease-up recovery."),
    dict(category="Multifamily", title="Milhaus Merges With SRG Residential, Agrees to Acquire Broadshore Capital",
         subtitle="Consolidation Is How Mid-Size Multifamily Platforms Are Buying Scale Right Now",
         trigger=f'''{src("https://www.bisnow.com/los-angeles/news/multifamily/milhaus-and-srg-residential-complete-merger-acquire-broadshore-capital-partners-135444", "Indianapolis-based Milhaus completed its merger with Newport Beach's SRG Residential on July 15, 2026")} and separately agreed to acquire LA-based Broadshore Capital Partners, creating a combined platform with $2.5 billion in investment activity and more than 50,000 apartments under third-party management, spanning development, investment management, and lending capabilities across Long Beach, Irvine, Woodland Hills, and Ontario.''',
         why="A mid-size developer merging with an LA-adjacent operator and simultaneously acquiring an investment-and-lending platform is a scale play, not a distressed rescue &mdash; Milhaus is assembling development, third-party management, and capital-markets capabilities under one roof specifically because standalone platforms are finding it harder to compete for institutional capital in a tighter fundraising environment. For USC-market multifamily specifically, this concentrates a meaningful share of LA-area third-party management and lending relationships into one combined platform almost overnight.",
         implications=[
             "Signals mid-size multifamily platforms are consolidating to compete for institutional capital allocations",
             "Adds vertically integrated lending and investment-management capability to a previously development-focused platform",
             "Concentrates LA-area third-party apartment management under a materially larger combined operator",
             "Sets a template other regional multifamily platforms may follow to bulk up ahead of a slower deployment cycle",
         ],
         watch="Whether the combined platform's eight planned development projects break ground on schedule, and if further bolt-on acquisitions follow the Broadshore deal's close this summer."),
    dict(category="Mixed-Use", title="Bankruptcy Court Approves $517M Sale of Stalled Oceanwide Plaza Towers",
         subtitle="A Half-Billion-Dollar Sale Still Leaves an $800 Million Gap to Finish the Job",
         trigger=f'''{src("https://commercialobserver.com/2026/07/oceanwide-plaza-sale-graffiti-towers-los-angeles-kpc/", "A federal bankruptcy judge approved the sale of the stalled, graffiti-covered Oceanwide Plaza towers in downtown LA")} to a partnership led by KPC Development and Lendlease Americas for roughly $517 million in cash and credit, with an estimated $800 million or more still needed to complete the three-tower project; the buyer has six months to close and must begin graffiti removal within 90 days.''',
         why="A $517 million sale price for a project that needs another $800 million-plus to finish is not a valuation of the towers as they stand &mdash; it's a valuation of the entitlements, sunk structural work, and downtown site control, discounted heavily for the enormous execution risk of completing stalled high-rise construction. That a buyer was willing to take this on at all, after years of the site sitting vacant and vandalized, signals a bet that downtown LA's eventual recovery justifies absorbing that risk now, while the entry basis is this depressed. The court-mandated graffiti removal deadline puts a hard, public clock on the buyer's first visible commitment, before the harder work of construction financing even begins.",
         implications=[
             "Establishes a market-clearing basis for stalled, distressed high-rise construction sites downtown",
             "Signals investor willingness to absorb significant completion risk at a steep discount to finish cost",
             "Puts a public 90-day clock on visible progress via mandated graffiti removal",
             "Tests whether an additional $800 million-plus in completion financing is achievable in this rate environment",
         ],
         watch="Whether KPC and Lendlease close within the six-month window, and any construction financing announcements once the sale closes.",
         tldr="A bankruptcy judge approved a $517M sale of the stalled Oceanwide Plaza towers, which still need $800M-plus more before they're finished."),
    dict(category="Retail", title="Sony and Alamo Drafthouse to Reopen Hollywood's ArcLight and Cinerama Dome",
         subtitle="A Six-Year-Dark Landmark Gets a Reopening Date",
         trigger=f'''{src("https://www.bisnow.com/los-angeles/news/retail/hollywood-arclight-and-cinerama-dome-reopening-under-alamo-drafthouse-135526", "Sony Pictures Entertainment struck a lease deal for Alamo Drafthouse to reopen the shuttered Cinerama Dome and former ArcLight Hollywood complex")}, dark since 2020; the Dome keeps its name, the former ArcLight becomes a 14-screen Alamo Drafthouse Hollywood, with construction starting in August 2026 and reopening targeted for 2028.''',
         why="A single-screen landmark like the Cinerama Dome sitting dark for six years is a specific kind of retail vacancy &mdash; the building has cultural cachet that makes it hard to simply repurpose, but that same cachet also makes it hard to find an operator willing to underwrite the renovation cost of a specialty-format theater. Sony's willingness to fund this as the property owner, pairing its content business with Alamo Drafthouse's operating expertise, is a vertically integrated bet that owning both the real estate and a differentiated exhibition brand is worth more than leasing to a generic operator.",
         implications=[
             "Removes a long-vacant landmark retail property from Hollywood's dark-storefront inventory",
             "Signals studio-backed vertical integration between content ownership and specialty exhibition",
             "Sets a multi-year renovation timeline reflecting the deferred capex from six years of vacancy",
             "May reinforce Hollywood Boulevard's entertainment-retail identity ahead of the 2028 reopening",
         ],
         watch="Construction progress toward the 2028 target, and whether Sony pursues similar operator partnerships at other dark venues it controls.",
         tldr="Sony is funding Alamo Drafthouse to reopen Hollywood's Cinerama Dome and ArcLight after six dark years, betting on vertical integration between content and exhibition."),
    dict(category="Hospitality", title="Ian Schrager's PUBLIC West Hollywood Opens on the Sunset Strip",
         subtitle="A New Lifestyle Hotel Bets Against Its Own Industry's Sentiment Survey",
         trigger=f'''{src("https://hospitalitydesign.com/news/public-west-hollywood-california-ian-schrager/185295/", "PUBLIC West Hollywood, a 137-room hotel in the former Standard Hollywood building")}, closed since 2021, opened in July 2026 after a redesign by architect John Pawson, featuring a 16,000-square-foot rooftop park, three food-and-beverage venues, and guestrooms with 11-foot floor-to-ceiling projection surfaces.''',
         why="A high-profile boutique operator committing capital to reopen a shuttered Sunset Strip property runs directly against trade-press sentiment surveys this month finding roughly 80% of hoteliers don't view LA as a viable long-term investment market ahead of the 2028 Olympics &mdash; Schrager's bet is specifically that flight-to-quality, brand-driven capital still finds a market even when broader operator sentiment sours. The extensive amenity buildout (a 16,000-square-foot private rooftop park, in-room projection technology) is also a bet that experiential differentiation, not room count or location alone, is what LA's next hospitality cycle rewards.",
         implications=[
             "Tests whether brand-driven, experience-led hospitality capital still finds LA despite weak broader operator sentiment",
             "Removes a property dark since 2021 from Sunset Strip's vacant hospitality inventory",
             "Sets a high amenity-spend benchmark other Sunset Strip boutique hotels will be compared against",
             "Provides an early read on lifestyle-hotel demand ahead of the 2028 Olympics hospitality buildout",
         ],
         watch="Initial occupancy and rate performance in PUBLIC West Hollywood's first months, and whether other operators follow with reopenings of dark Sunset Strip properties."),
]

USC_FINAL_PARAGRAPHS = [
    "This week's Los Angeles signals split into repricing and consolidation on one side, and renewed conviction on the other. Rexford Industrial quadrupling its disposition guidance after a half-billion-dollar loss, and Milhaus assembling scale through merger and acquisition, both describe platforms restructuring how they hold and manage LA real estate right now &mdash; not because performance is weak, but because the current environment rewards scale and lower cost basis over standalone operation.",
    "The two industrial signals are worth reading against each other. Rexford is shedding LA-basin assets it says were bought at peak pricing, while South Bay is simultaneously pulling in its strongest leasing quarter since 2021 on the back of aerospace and defense tenants &mdash; the same broad asset class producing both a repricing story and a demand-surge story, depending on submarket and vintage.",
    "PUBLIC West Hollywood's reopening and Oceanwide Plaza's court-approved sale describe the same underlying dynamic at very different scales: capital willing to absorb real execution risk on Los Angeles hospitality and mixed-use product specifically because the entry basis is now this depressed, not despite it.",
]
USC_FINAL_BULLETS = [
    "Rexford's disposition guidance and Milhaus's merger both describe platforms restructuring for a tighter capital environment",
    "South Bay industrial is posting its strongest leasing quarter since 2021 even as Rexford sheds LA-basin assets elsewhere",
    "A new Sunset Strip hotel opening runs directly against trade-press surveys showing weak LA hospitality investment sentiment",
    "A $517 million sale still requires $800 million-plus more before Oceanwide Plaza is habitable",
]

CRE_USC_BLOCK = market_block_html(
    "cre", "usc", False, "CRE", "Signal", "LOS ANGELES, CA", "JULY 29, 2026", "JULY 15&ndash;28, 2026",
    USC_SNAPSHOT, "What Happened", USC_SIGNALS, USC_FINAL_PARAGRAPHS, USC_FINAL_BULLETS,
    "No predictions. No stock references. Project-anchored interpretation only.",
    implications_label="Local Market Implications",
)
NYC_SNAPSHOT = [
    ("Development Activity", "rising"),
    ("Office Pipeline", "rising"),
    ("Industrial Momentum", "stable"),
    ("Mixed-Use Activity", "rising"),
    ("Capital Availability", "stable"),
    ("Infrastructure Relevance", "stable"),
]

NYC_SIGNALS = [
    dict(category="Office", title="NBCUniversal Renews 244,185 SF at 1221 Avenue of the Americas",
         subtitle="A Legacy Media Tenant Recommits Instead of Shrinking",
         trigger=f'''{src("https://commercialobserver.com/2026/07/nbcuniversal-lease-renewal-office-1221-avenue-of-the-americas/", "NBCUniversal renewed 244,185 square feet at Rockefeller Group's 1221 Avenue of the Americas")} in Midtown, across from its 30 Rockefeller Plaza headquarters, building on a footprint it first established there in 2012 and expanded in 2021; Midtown average asking rents hit $86.18 per square foot in Q2 2026, a quarter Commercial Observer described as having leasing velocity not seen since 2002.''',
         why="A legacy media tenant recommitting to a quarter-million square feet, rather than shrinking or relocating, directly undercuts the narrative that large corporate occupiers are only downsizing their Manhattan footprints. That this renewal lands in a quarter with the strongest Manhattan office leasing velocity since 2002 suggests it's part of a broader pattern of large-tenant conviction, not an isolated holdout renewal driven by relocation costs.",
         implications=[
             "Confirms large legacy tenants are renewing at scale, not uniformly shrinking their Manhattan footprints",
             "Reinforces 1221 Avenue of the Americas and the Rockefeller Center corridor as a durable media-tenant cluster",
             "Adds to a broader Q2 2026 leasing velocity trend described as the strongest since 2002",
             "Supports continued asking-rent growth in Midtown even amid national office-sector caution",
         ],
         watch="Whether other large media or legacy corporate tenants announce comparable renewals in the same submarket this year."),
    dict(category="Mixed-Use", title="Bill Ackman Pays $188M for Lab Building, Plans Brain Research Institute",
         subtitle="A Philanthropic Buyer Converts Office/Lab Stock Into an Institutional Research Campus",
         trigger=f'''{src("https://commercialobserver.com/2026/07/bill-ackman-buys-125-west-end-avenue/", "Bill Ackman's Pershing Square Foundation paid $188 million for the 400,000-square-foot lab building at 125 West End Avenue")} from Taconic Partners, the first piece of a roughly $260 million, two-building, 700,000-square-foot assemblage on the Upper West Side that will become the Ackman Oxman Institute, a brain research center developed with the Mount Sinai Hospital System.''',
         why="A billionaire-funded philanthropic buyer paying a premium to convert existing lab and office stock into a dedicated institutional research campus is a concrete example of life-sciences and &ldquo;eds-and-meds&rdquo; demand becoming a real alternative use case for underused Manhattan office and lab buildings, not just a talking point. Because this is a mission-driven, not yield-driven, acquisition, it's a different kind of demand signal than a REIT or fund buying the same building &mdash; but it still removes real square footage from the conventional office market permanently.",
         implications=[
             "Confirms life-sciences and institutional research demand as a genuine absorption path for older lab/office stock",
             "Removes roughly 700,000 square feet from conventional Manhattan office/lab inventory permanently",
             "Signals continued philanthropic capital willingness to fund large-scale medical research real estate in NYC",
             "May encourage other underused Upper West Side lab buildings to market toward similar institutional buyers",
         ],
         watch="Whether the Foundation closes on the adjacent 320 West 66th Street parcel as planned, and construction/opening timelines for the Ackman Oxman Institute."),
    dict(category="Retail", title="Boutique Fitness Operators Drive Manhattan Retail Vacancy to a 2019 Low",
         subtitle="Experiential Wellness Tenants, Not Apparel Chains, Are Now the Demand Engine",
         trigger=f'''{src("https://www.credaily.com/briefs/boutique-gyms-lead-manhattan-retail-leasing-surge/", "Boutique fitness and wellness operators drove a surge in Manhattan and Brooklyn retail leasing")}, led by Chelsea Piers (76,000 square feet at Seaport) and Life Time (71,000 square feet in North Williamsburg), pushing prime-corridor retail vacancy down to roughly 12% &mdash; the lowest since 2019, with Madison Avenue and SoHo down to about 8%.''',
         why="Wellness and fitness tenants regularly ranking among the largest retail leases in the market, rather than traditional apparel or restaurant chains, is a durable shift in what landlords are underwriting retail rents against &mdash; these operators typically sign long-term leases anchored around expensive buildout (pools, studios, equipment), which makes them stickier tenants than a typical apparel retailer once installed. Vacancy falling to a level not seen since 2019 in the specific corridors these tenants are choosing confirms this demand is broad enough to move real vacancy numbers, not just a handful of headline deals.",
         implications=[
             "Confirms experiential wellness tenants, not apparel or dining, are now the leading edge of large-block retail demand",
             "Pushes prime-corridor Manhattan retail vacancy to its lowest level since 2019",
             "Signals landlords can underwrite rents against sticky, buildout-heavy wellness tenants rather than higher-turnover retail",
             "May pressure remaining large-block retail asking rents higher in the corridors these operators favor",
         ],
         watch="Whether additional large-format wellness operators announce New York leases this year, and rent growth in the specific corridors already tightening."),
    dict(category="Office", title="Brooklyn Medical Office Building Sells for $632/SF, Well Above Conventional Office",
         subtitle="Healthcare-Anchored Real Estate Is Trading at a Premium to Ordinary Office",
         trigger=f'''{src("https://crenews.com/2026/07/28/brooklyn-n-y-medical-office-property-sells-for-89-9mln/", "The 142,249-square-foot East New York Health Hub sold for $89.9 million")}, or roughly $632 per square foot, to Vital Infrastructure Property Trust, with Newmark involved in the brokerage.''',
         why="A $632-per-square-foot price for an outer-borough medical office asset is well above typical Brooklyn office pricing, which confirms healthcare-anchored real estate is trading at a meaningful premium to conventional office right now. That premium reflects the durability of medical tenancies (long leases, high build-out costs, non-discretionary demand) relative to ordinary office space, and reinforces medical and life-science-adjacent property as one of the few office-related categories still attracting strong institutional capital.",
         implications=[
             "Confirms medical office commands a real, quantifiable premium over conventional Brooklyn office pricing",
             "Signals institutional capital (Vital Infrastructure Property Trust) sees durable value in healthcare-anchored real estate",
             "Provides a $632/SF benchmark for other outer-borough medical office sales this cycle",
             "Reinforces healthcare tenancy as a differentiated, still-in-favor office subcategory",
         ],
         watch="Whether comparable outer-borough medical office assets trade at similarly premium pricing, and Vital Infrastructure's disclosed plans for the property."),
]

NYC_FINAL_PARAGRAPHS = [
    "This week's New York signals share a theme: capital is finding conviction in real estate uses that sit adjacent to, or entirely outside of, conventional office and retail &mdash; a legacy media tenant recommitting to Midtown space, a philanthropic buyer converting lab space into an institutional research campus, wellness operators driving retail vacancy to a multi-year low, and a healthcare-anchored asset trading at a steep premium to ordinary office.",
    "The NBCUniversal renewal and the East New York Health Hub sale are worth reading as two data points on the same broader question: which uses is capital willing to pay up for right now. A legacy tenant renewing at scale in a strong leasing quarter, and a medical office property trading at nearly double typical Brooklyn office pricing, both point toward durable, non-discretionary demand commanding real premiums.",
    "The Ackman Oxman Institute purchase and the wellness-driven retail leasing surge describe a similar dynamic from opposite ends of the market: mission-driven and experiential demand, not conventional office or apparel retail, is what's actually absorbing space and moving vacancy right now.",
]
NYC_FINAL_BULLETS = [
    "A legacy media tenant renewed at scale in Manhattan's strongest office leasing quarter since 2002",
    "A philanthropic buyer is converting lab/office stock into a dedicated institutional research campus",
    "Wellness and fitness tenants, not apparel or dining, pushed prime retail vacancy to a 2019 low",
    "A Brooklyn medical office asset traded at nearly double typical conventional office pricing",
]

CRE_NYU_BLOCK = market_block_html(
    "cre", "nyu", False, "CRE", "Signal", "NEW YORK, NY", "JULY 29, 2026", "JULY 15&ndash;28, 2026",
    NYC_SNAPSHOT, "What Happened", NYC_SIGNALS, NYC_FINAL_PARAGRAPHS, NYC_FINAL_BULLETS,
    "No predictions. No stock references. Project-anchored interpretation only.",
    implications_label="Local Market Implications",
)
CRE_UGA_BLOCK = market_block_html(
    "cre", "uga", False, "CRE", "Signal", "ATLANTA, GA", "COMING SOON", "&mdash;",
    [], "What Happened", [], [], [], "No predictions. No stock references. Project-anchored interpretation only.",
    coming_soon="Coming soon &mdash; real research for the Atlanta market is in progress.",
)
CRE_UF_BLOCK = market_block_html(
    "cre", "uf", False, "CRE", "Signal", "MIAMI, FL", "COMING SOON", "&mdash;",
    [], "What Happened", [], [], [], "No predictions. No stock references. Project-anchored interpretation only.",
    coming_soon="Coming soon &mdash; real research for the Miami market is in progress.",
)

CRE_PAGE = multi_market_page("cre", False, CRE_MARKETS,
    [CRE_AUSTIN_BLOCK, CRE_USC_BLOCK, CRE_NYU_BLOCK, CRE_UGA_BLOCK, CRE_UF_BLOCK])

print("CRE page loaded OK", len(CRE_PAGE))

# ============================================================== IB SIGNAL ==============================================================

IB_SNAPSHOT = [
    ("M&amp;A Deal Volume", "rising"),
    ("IPO Pipeline", "rising"),
    ("Leveraged Loan Issuance", "stable"),
    ("Sponsor (PE) Activity", "rising"),
    ("Advisory Fee Pool", "stable"),
    ("Underwriting Conditions", "rising"),
]

IB_SIGNALS = [
    dict(category="M&amp;A", title="Mapfre Buys Safety Insurance for $1.54B in Cash at a 44% Premium",
         subtitle="A Clean All-Cash Deal Is a Useful Baseline for Reading Premium Mechanics",
         trigger=f'''{src("https://www.businesswire.com/news/home/20260723192248/en/Safety-Insurance-Group-Inc.-Enters-Into-Merger-Agreement-With-Mapfre-for-$1.54-Billion", "Spain's Mapfre agreed to acquire Massachusetts-based Safety Insurance Group for $1.54 billion in cash")}, with Safety shareholders receiving $105 per share, a 44% premium to the July 23 closing price; the deal was unanimously approved by both boards and is expected to close in Q1 2027 pending Massachusetts insurance-commissioner approval and HSR clearance.''',
         why="A 44% all-cash premium from a foreign strategic acquirer is about as close to a textbook control premium as this market produces &mdash; no stock-mix complexity, no financing contingency, just a direct statement of how much more Mapfre believes it can extract from Safety's regional agency network once combined with its existing US operations than public markets were pricing standalone. Regulatory approval risk here is real but narrow: a single state insurance commissioner and standard antitrust clearance, not a multi-jurisdiction gauntlet.",
         implications=[
             "Sets a clean 44%-premium reference point for regional insurer take-outs by foreign strategics",
             "Confirms Mapfre is willing to pay full price in cash to combine Safety's agency network with its US platform",
             "Narrows Safety shareholders' outcome to deal certainty rather than integration-dependent stock consideration",
             "Leaves Massachusetts insurance-commissioner approval as the primary closing risk to track",
         ],
         watch="The Massachusetts Commissioner of Insurance's review timeline, and whether any competing bid emerges before the Q1 2027 closing target."),
    dict(category="Sector: Healthcare", title="Tempus AI Buys Cancer-Monitoring Firm Personalis for $1.5B in Stock",
         subtitle="An All-Stock Bolt-On Extends an Existing Commercial Partnership Into Full Ownership",
         trigger=f'''{src("https://finance.yahoo.com/healthcare/articles/tempus-ai-acquires-cancer-monitoring-123048272.html", "Tempus AI agreed to acquire Personalis for $1.5 billion")}, with Personalis shareholders receiving $16.25 per share &mdash; a 28% premium to the unaffected 30-day average &mdash; in a deal structured as 100% stock, though Tempus retains an option to pay up to half in cash; the deal builds on a commercial partnership dating to 2023 and Tempus values the minimal-residual-disease testing market the combined company targets at $20 billion.''',
         why="Funding a bolt-on with stock rather than debt, from a recently public company, is a bet that its own currency is valuable enough to use for M&amp;A without straining its balance sheet &mdash; and acquiring a partner it already had a multi-year commercial relationship with meaningfully de-risks integration relative to a cold acquisition, since both sides already know how the underlying technology and data pipelines work together. That Tempus retains a cash-payment option, without committing to it, preserves flexibility if its stock price moves before closing.",
         implications=[
             "Converts a multi-year commercial partnership into full ownership, lowering integration risk relative to a cold deal",
             "Signals Tempus is comfortable using its post-IPO equity as acquisition currency rather than raising debt",
             "Consolidates minimal-residual-disease testing capability inside one platform in a market Tempus sizes at $20 billion",
             "Preserves optionality to shift up to half the consideration to cash if Tempus's stock price moves before closing",
         ],
         watch="Whether Tempus exercises its cash-payment option before close, and shareholder and regulatory approval timing into late 2026 or early 2027."),
    dict(category="Sponsor Finance", title="EU Clears Record $55B Take-Private of Electronic Arts",
         subtitle="CFIUS, Not Antitrust, Is Now the Last Real Hurdle on the Largest LBO Ever",
         trigger=f'''{src("https://www.engadget.com/2221898/eu-gives-antitrust-approval-to-the-saudi-led-55-billion-takeover-of-ea/", "The European Commission cleared the $55 billion take-private of Electronic Arts")} on July 23, concluding the deal &ldquo;would not raise competition concerns&rdquo;; a consortium led by Saudi Arabia's Public Investment Fund (93.4% ownership), Silver Lake, and Affinity Partners is financing what would be the largest leveraged buyout in history with more than $20 billion in debt, with CFIUS review of Saudi ownership of EA's player data and AI assets now the sole remaining major approval ahead of a September 28 outside date.''',
         why="Clearing EU antitrust on a deal this size confirms competition regulators don't see market-concentration risk in a single publisher's buyout, which shifts the entire remaining risk of the largest LBO ever onto a single, narrower question: whether CFIUS treats sovereign-wealth ownership of a major US data and AI asset as a national-security issue. That distinction matters because antitrust and CFIUS review operate on completely different logic &mdash; one prices market power, the other prices geopolitical risk &mdash; and a deal can clear the first cleanly while still facing real uncertainty on the second.",
         implications=[
             "Confirms more than $20 billion of leverage is placeable on a single mega-cap take-private in today's debt markets",
             "Narrows remaining deal risk to a single national-security review rather than a multi-jurisdiction antitrust gauntlet",
             "Sets a precedent for how CFIUS treats Gulf sovereign-wealth ownership of US data and AI assets specifically",
             "Establishes a financing-structure benchmark other mega-cap sponsor-led take-privates will reference",
         ],
         watch="CFIUS's review outcome ahead of the September 28 outside date, extendable to December 28 if needed."),
    dict(category="Sponsor Finance", title="BlackRock-Led Consortium Closes $40B Acquisition of Aligned Data Centers",
         subtitle="Asset Managers Are Now Both the Equity Sponsor and the Debt Originator on AI Infrastructure",
         trigger=f'''{src("https://www.datacenterfrontier.com/hyperscale/article/55323360/blackrock-led-consortium-to-acquire-aligned-data-centers-in-40-billion-ai-infrastructure-deal", "A BlackRock-led consortium including Global Infrastructure Partners, Abu Dhabi's MGX, Microsoft, and Nvidia closed its roughly $40 billion acquisition of Aligned Data Centers")} from Macquarie Asset Management on July 21, taking 100% of the equity in a platform spanning 50-plus campuses and more than 5 gigawatts of capacity across the Americas, with the consortium committing a further $5 billion toward expansion post-close.''',
         why="This is the infrastructure-fund version of a leveraged buyout, except the sponsor consortium includes strategic technology players (Microsoft, Nvidia) alongside traditional asset managers &mdash; a structure that blends equity sponsorship with guaranteed future customer demand from two of the buyers themselves. BlackRock's dual role here, as both equity sponsor on this deal and, via its separate Meta bond financing this week, as an originator of AI-datacenter debt, shows how far traditional asset managers have moved into building end-to-end AI capital-formation platforms rather than just allocating to them.",
         implications=[
             "Confirms strategic technology buyers are now co-underwriting AI infrastructure equity risk alongside asset managers",
             "Signals continued committed capital (a further $5 billion) beyond the initial acquisition price for expansion",
             "Establishes one of the largest private infrastructure deals ever as a size and structure benchmark",
             "Shows BlackRock building parallel equity-sponsor and debt-originator roles across the AI infrastructure buildout",
         ],
         watch="Deployment pace of the additional $5 billion expansion commitment, and whether Microsoft or Nvidia's involvement translates into disclosed capacity commitments at Aligned's campuses."),
    dict(category="DCM", title="BlackRock Prices ~$12.5B in Bonds at 7.53% to Fund Meta's El Paso Data Center",
         subtitle="A Junk-Like Yield on Nominally Investment-Grade Paper Prices Real AI-Capex Risk",
         trigger=f'''{src("https://finance.yahoo.com/technology/ai/articles/blackrock-raising-12-billion-bonds-121305502.html", "BlackRock priced roughly $12&ndash;12.55 billion of investment-grade-rated bonds at a 7.534% yield")} to fund Meta's roughly 1-gigawatt El Paso, Texas data center, through a BlackRock-controlled entity in which BlackRock holds 80% and Meta 20%, with Meta leasing the facility back and booking it as rent rather than capex; JPMorgan and Morgan Stanley led the deal, which follows the same structure as Meta's $27 billion Louisiana facility financed with Blue Owl.''',
         why="A 7.5%-plus yield on paper rated investment-grade is a meaningfully wide spread for that rating category, which means fixed-income investors are pricing real execution and demand risk into AI-datacenter debt even though the credit rating itself says otherwise &mdash; the rating reflects Meta's ultimate lease obligation, but the yield reflects the market's independent view of the underlying asset and structure. The off-balance-sheet design, where Meta leases rather than owns, is becoming the standard template for how hyperscaler AI capex gets financed without appearing directly on the hyperscaler's own balance sheet.",
         implications=[
             "Confirms fixed-income investors are pricing real risk premium into AI-datacenter debt despite investment-grade ratings",
             "Establishes the 80/20 asset-manager-owned, hyperscaler-leased structure as a repeatable AI-capex financing template",
             "Keeps Meta's data center commitment off its own balance sheet, booked as rent rather than capital expenditure",
             "Extends BlackRock's parallel role as both an equity sponsor (Aligned) and a debt originator on AI infrastructure",
         ],
         watch="Where the bonds trade in secondary markets in their first weeks, and whether other hyperscalers adopt the same 80/20 leaseback structure for their own AI capex."),
    dict(category="Restructuring", title="Republic National Distributing Files Chapter 11 to Wind Down, Not Reorganize",
         subtitle="A 128-Year-Old Distributor Chooses Liquidation Over a Turnaround",
         trigger=f'''{src("https://www.bloomberglaw.com/bankruptcy-law/republic-national-distributing-company-files-for-ch-11-in-texas", "Republic National Distributing Company, once the second-largest US wine-and-spirits distributor, filed for Chapter 11")} in the Southern District of Texas on July 26, reporting $500 million to $1 billion in assets against $1 billion to $10 billion in liabilities and citing more than 100,000 creditors; the company is pursuing going-concern sales and an orderly wind-down rather than a reorganization, with several state joint ventures excluded from the filing and continuing to operate.''',
         why="Choosing a liquidating Chapter 11 over a reorganization is a deliberate signal that management and its advisors concluded no restructured capital structure makes this business viable going forward &mdash; a reorganizing filer keeps operating and re-emerges; a liquidating filer is explicitly selling itself off in pieces. The scale here, over 100,000 creditors and a 128-year operating history, makes this a significant test case for how going-concern sale processes execute inside a wind-down Chapter 11, since most large distribution-company bankruptcies attempt reorganization first.",
         implications=[
             "Signals management concluded no restructured capital stack makes this business viable, not just this quarter's liquidity",
             "Sets a going-concern sale process, not a reorganization, as the resolution path for a major distributor",
             "Preserves the excluded state joint ventures as ongoing, sellable operating businesses within the estate",
             "Provides a rare, large-scale test case for wind-down Chapter 11 execution in a distribution business",
         ],
         watch="Which state joint ventures and business lines attract going-concern buyers first, and the recovery rate creditors ultimately receive."),
    dict(category="ECM", title="Scribe Therapeutics Prices Upsized IPO, Pops 44% on First Day",
         subtitle="A Strategic Co-Investor Alongside a Hot Open Is the Strongest Biotech Demand Signal Available",
         trigger=f'''{src("https://www.stocktitan.net/news/SCTX/scribe-therapeutics-announces-pricing-of-upsized-initial-public-fv1at7xqi0ga.html", "Gene-editing biotech Scribe Therapeutics priced an upsized IPO at $15.00 per share")}, raising roughly $155.5 million including the underwriters' full over-allotment exercise, alongside a concurrent $7.5 million private placement to Sanofi; the stock reportedly jumped as much as 44% on its first day of trading.''',
         why="An upsized deal pricing at the top of its range, with a strategic pharma investor buying into the same round at the IPO price, is about as strong a demand signal as an early-stage biotech offering produces &mdash; underwriters only upsize when order books are genuinely oversubscribed, and Sanofi's concurrent private placement means an industry insider with real diligence capability was willing to co-invest at the retail price, not demand a discount. A 44% first-day pop confirms the upsized pricing still left room on the table, suggesting even more demand existed than the deal ultimately captured.",
         implications=[
             "Confirms genuine oversubscription, not just underwriter optimism, drove the upsized pricing",
             "Signals strategic pharma capital sees enough diligence-backed conviction to co-invest at the retail IPO price",
             "Reopens a biotech IPO window that had been largely shut to early-stage gene-editing companies",
             "May pull forward other drafted biotech S-1s that were waiting for a successful test case like this one",
         ],
         watch="Whether other early-stage biotech companies accelerate IPO filings following this pricing and first-day performance, and Scribe's stock performance beyond the opening pop."),
]

IB_FINAL_PARAGRAPHS = [
    "This week's dealmaking splits into two distinct stories: traditional M&amp;A and sponsor finance running at ordinary scale (Mapfre/Safety, Tempus/Personalis, the EA take-private clearing its last major hurdle), and a genuinely new financing category &mdash; AI infrastructure &mdash; now large enough to move capital markets on its own. The Aligned Data Centers acquisition and the Meta bond financing are two different deals, from the same asset manager, in the same week, both aimed at the same underlying buildout.",
    "BlackRock's dual role is this issue's clearest structural story. On Aligned, BlackRock is the equity sponsor buying the platform outright; on Meta's El Paso facility, BlackRock is the debt originator pricing bonds against a hyperscaler's leaseback obligation. The same asset manager sitting on both sides of the AI capex stack, in the same week, is a preview of how concentrated the financing side of this buildout may become.",
    "The 7.5%-plus yield on nominally investment-grade Meta-backed debt is worth sitting with on its own: fixed-income investors are pricing real execution risk into AI datacenter debt even where the rating says otherwise, which is a more honest signal about how the market actually views this buildout than any rating alone would suggest.",
]
IB_FINAL_BULLETS = [
    "AI infrastructure financing is now large enough to generate its own M&amp;A and DCM signals in the same week",
    "BlackRock is simultaneously the equity sponsor on one AI-infrastructure deal and the debt originator on another",
    "A junk-like 7.5%-plus yield on investment-grade-rated AI-datacenter debt prices real risk the rating doesn't capture",
    "A liquidating, not reorganizing, Chapter 11 at a 128-year-old distributor signals no capital structure fix was viable",
]

IB_PAGE = issue_page(
    "ib", False, "IB", "Signal", "NEW YORK, NY", "JULY 29, 2026", "JULY 19&ndash;27, 2026",
    IB_SNAPSHOT, "What Happened", IB_SIGNALS, IB_FINAL_PARAGRAPHS, IB_FINAL_BULLETS,
    "No predictions. No stock references. Deal-anchored interpretation only.",
)

print("IB page OK", len(IB_PAGE))

# ============================================================== CREDIT SIGNAL ==============================================================

CREDIT_SNAPSHOT = [
    ("Direct Lending Volume", "rising"),
    ("Spread Tightening", "rising"),
    ("Covenant Looseness", "stable"),
    ("Sponsor Demand", "rising"),
    ("Fundraising / Dry Powder", "stable"),
    ("Secondary Market Liquidity", "rising"),
]

CREDIT_SIGNALS = [
    dict(category="Asset-Based Lending", title="Apollo and Blackstone Arrange ~$35B Financing for Anthropic's AI Chip Purchases",
         subtitle="Chip-as-Collateral Lending Is Functionally Asset-Based Credit Against Depreciating Hardware",
         trigger=f'''{src("https://www.benzinga.com/markets/private-markets/26/07/60372922/broadcom-anthropic-just-turned-ais-chip-bet-into-somebody-elses-debt-apollo-and-blackstone-hold-the-keys", "Apollo Global Management and Blackstone arranged a roughly $35 billion financing package")} to fund Anthropic's purchase of custom AI chips from Google and Broadcom, structured through a special-purpose vehicle that buys the chips and leases them back to Anthropic via a delayed-draw facility with roughly 16 separate releases over a bit more than a year; Broadcom is backstopping Anthropic's payment obligations on the largest senior tranches, and roughly $15 billion of the package is expected to migrate to the 144A market by early 2027.''',
         why="Structuring chip purchases as a leased special-purpose vehicle, with a delayed-draw facility that releases capital in roughly 16 tranches, lets private credit underwrite AI infrastructure the same way it underwrites any other depreciating, collateral-backed asset &mdash; except the collateral here is custom silicon whose useful economic life and resale value are far less established than a warehouse or an aircraft. Broadcom's backstop on the senior tranches is doing real work: it converts what would otherwise be pure technology-obsolescence risk into a corporate-credit question about Broadcom's own backstop capacity, which is a very different risk private lenders are much more comfortable pricing.",
         implications=[
             "Confirms private credit can underwrite AI infrastructure at a scale rivaling large syndicated bank deals",
             "Converts chip-obsolescence risk into a corporate-backstop credit question via Broadcom's guarantee",
             "Structures the delayed-draw facility to release capital in step with actual chip delivery, not all at once",
             "Sets a template migrating roughly $15 billion of the package into the 144A market for institutional investors by early 2027",
         ],
         watch="Whether the expected 144A migration proceeds on the early-2027 timeline, and how the chips' resale or residual value holds up as tranches draw down."),
    dict(category="Asset-Based Lending", title="Brookfield and Tor Provide $255M GPU-Backed Note to PaleBlueDot AI",
         subtitle="Asset-Based AI Credit Is Reaching Well Past the Megacap Names",
         trigger=f'''{src("https://www.prnewswire.com/news-releases/palebluedot-ai-closes-us255-million-credit-financing-to-accelerate-agentic-ai-infra-expansion-302831169.html", "PaleBlueDot AI closed a $255 million, three-year, GPU-backed private note")} on July 21, with Brookfield Asset Management and Tor Investment Management as lenders and JPMorgan as placement agent, refinancing an existing credit facility and funding continued buildout of the Silicon Valley agentic-AI infrastructure company's platform.''',
         why="A venture-stage AI infrastructure company, not a household name, tapping private credit directly for GPU-backed debt rather than raising another equity round shows how far down the financing food chain asset-based AI credit has spread in a matter of months &mdash; the same lending logic used on Anthropic's $35 billion package (chips as collateral, asset managers as originator) is now being applied at a fraction of the scale to a much younger, less-established borrower.",
         implications=[
             "Confirms asset-based AI infrastructure lending now extends well below megacap borrowers like Anthropic",
             "Signals GPU collateral is becoming standardized enough for asset managers to underwrite at venture-stage scale",
             "Refinances existing debt rather than funding entirely new capacity, extending runway on established terms",
             "Provides Brookfield and Tor a smaller, earlier-stage comp for pricing future AI infrastructure credit",
         ],
         watch="Whether PaleBlueDot draws on this facility to fund additional infrastructure buildout, and if other venture-stage AI infrastructure platforms follow with similar GPU-backed note issuances."),
    dict(category="Fund Finance", title="Rated NAV Loan Issuance Tops $82B Since 2018 as Initial Ratings Skew Lower",
         subtitle="A Niche GP Liquidity Tool Has Become a Standardized, Ratings-Tracked Asset Class",
         trigger=f'''{src("https://finance.yahoo.com/markets/stocks/articles/kbra-releases-research-private-credit-084600271.html", "KBRA reported cumulative rated NAV loan issuance has topped $82 billion across 157 transactions since 2018")}, after a record $23 billion across 38 deals in 2025; across 279 surveillance reviews from 2020 through the first half of 2026, 95% of rating actions were affirmations, with only two downgrades since early 2025, even as initial 2025 ratings skewed toward BBB rather than the previously typical A-/BBB+ range.''',
         why="NAV lending moving from a niche GP liquidity tool to a standardized, ratings-agency-tracked asset class with $82 billion of cumulative issuance is itself a maturation signal, but the shift toward BBB initial ratings in 2025, alongside increasing use of delayed-draw components and hybrid collateral packages, suggests lenders are underwriting more aggressive advance rates even as the broader market matures &mdash; a combination worth watching for early stress signs, since a 95% affirmation rate reflects performance to date, not necessarily performance through a real portfolio-value downturn.",
         implications=[
             "Confirms NAV lending has scaled into a standardized asset class with real ratings-agency surveillance history",
             "Signals lenders are underwriting more aggressive advance rates via the shift toward BBB initial ratings",
             "Reflects growing structural complexity (delayed-draw components, hybrid collateral, tranching) in new NAV loans",
             "Provides a 95%-affirmation baseline that has not yet been tested through a genuine portfolio-value downturn",
         ],
         watch="Whether the affirmation rate holds if PE portfolio valuations broadly decline, and if initial ratings continue skewing toward BBB on new 2026 issuance."),
    dict(category="Secondary Market", title="Credit Secondaries Market Doubles to $20.4B in H1 2026",
         subtitle="BDC Redemption Pressure Is Becoming a Supply Source for Secondaries",
         trigger=f'''{src("https://alternativecreditinvestor.com/2026/07/23/credit-secondaries-market-doubles-to-20-4bn-in-h1-2026/", "The credit secondaries market more than doubled to $20.4 billion in H1 2026 versus H1 2025")}, already exceeding full-year 2025 volume, per an Evercore report; GP-led transactions made up roughly 83% of H1 2026 volume, drawing primarily on 2018-2021 vintage closed-end funds, with Evercore citing redemption pressure at BDCs and semi-liquid vehicles as an emerging supply driver.''',
         why="A secondaries market doubling in six months, already past last year's full total, means LPs and GPs both need a liquidity release valve faster than the primary market or fund lifecycle normally provides &mdash; and Evercore's explicit link to BDC and semi-liquid-vehicle redemption pressure ties this directly to the same retail-facing private credit vehicles generating governance fights elsewhere this week. GP-led continuation vehicles becoming the dominant format (83% of volume) also means sponsors themselves are driving the liquidity solution, not just LPs seeking an exit.",
         implications=[
             "Confirms private credit LPs and GPs both need liquidity release valves faster than normal fund lifecycles provide",
             "Ties BDC and semi-liquid vehicle redemption pressure directly to rising credit secondaries supply",
             "Signals GP-led continuation vehicles, not LP-driven sales, are the dominant secondaries format this cycle",
             "Sets a volume pace that, if it continues, would roughly quadruple 2025's full-year secondaries total",
         ],
         watch="Whether H2 2026 volume sustains the H1 pace, and if BDC redemption pressure continues rising as a stated driver of secondaries supply."),
    dict(category="Documentation", title="Minority Lenders Escalate Suit Over Trinseo's 2023 Priming Transaction",
         subtitle="A Double-Dip Liability Management Exercise Is Now Years of Bankruptcy Litigation",
         trigger=f'''In Trinseo's Chapter 11 case, minority &ldquo;excluded&rdquo; lenders led by CastleKnight Management are suing to unwind the company's 2023 &ldquo;double-dip&rdquo; liability management exercise and a 2025 exchange offer; Trinseo and the Super HoldCo lenders moved to dismiss on June 9 and again June 22, 2026, and CastleKnight filed a follow-on motion on July 3 seeking derivative standing to pursue breach-of-fiduciary-duty and fraudulent-transfer claims in the US Bankruptcy Court for the Southern District of Texas.''',
         why="CastleKnight alleges the 2023 transaction used a sham intercompany loan and an off-market intercreditor agreement to entrench senior lenders and extract value from excluded minority lenders &mdash; the archetypal creditor-on-creditor violence fact pattern, now generating years of litigation rather than a quick negotiated resolution. This matters beyond Trinseo specifically because research on LME litigation has found lenders who fight priming transactions in court recover roughly 14 cents on the dollar versus 57 cents for senior lenders in clean bankruptcies, which is exactly the bet CastleKnight is making by continuing to litigate instead of settling.",
         implications=[
             "Illustrates how a 2023 priming LME can still generate active bankruptcy litigation three years later",
             "Tests whether minority lenders can win derivative standing to pursue fraudulent-transfer claims directly",
             "Provides a real-world data point on the low historical recovery rate for lenders who litigate against LMEs",
             "Signals continued market appetite for aggressive priming transactions despite the litigation risk they create",
         ],
         watch="The court's ruling on CastleKnight's derivative-standing motion, and whether other minority lender groups in comparable LME disputes cite this case as precedent."),
    dict(category="BDC", title="Prospect Capital Shareholders Renew Below-NAV Share Sale Authority",
         subtitle="Getting Permission to Dilute at a 57% NAV Discount Is a Governance Signal on Its Own",
         trigger=f'''{src("https://www.stocktitan.net/sec-filings/PSEC/8-k-prospect-capital-corp-reports-material-event-e174a28ef8a2.html", "Prospect Capital Corporation shareholders voted on July 7 to renew the company's authority to sell common stock below net asset value")} for the next 12 months, 277.6 million votes for versus 63.9 million against, after the vote was adjourned twice (from June 9 to June 23 to July 7) to solicit sufficient turnout; PSEC has traded around a 57% discount to NAV earlier in 2026, with any single day's sales capped at 25% of shares outstanding.''',
         why="A BDC needing two adjournments to secure shareholder permission to issue equity below NAV, while trading at a 57% discount, tells you the authority itself is contested even though it ultimately passed &mdash; selling new shares below NAV directly dilutes existing holders' per-share value, so management is prioritizing balance-sheet flexibility over near-term shareholder economics. This is precisely the kind of governance dynamic that has drawn activist pressure (including from Saba Capital) at peer BDCs this year.",
         implications=[
             "Confirms management is prioritizing balance-sheet flexibility over near-term shareholder dilution concerns",
             "Signals a steep 57% NAV discount reflects real market skepticism, not just a temporary mispricing",
             "Sets up potential activist scrutiny of a similar kind already targeting peer BDCs this year",
             "Caps daily dilution risk at 25% of shares outstanding, limiting but not eliminating the governance concern",
         ],
         watch="Whether Prospect Capital actually exercises this authority given the steep discount, and if activist investors escalate pressure following the contested vote."),
    dict(category="Direct Lending", title="Lafayette Square Finances RM Capital's Investment in Samaha & Associates",
         subtitle="Lower-Middle-Market Lending Is Clearing Even as Upper-Middle-Market Volume Slows",
         trigger=f'''{src("https://www.prnewswire.com/news-releases/lafayette-square-provides-financing-to-support-rm-capital-partners-investment-in-samaha--associates-302830245.html", "Lafayette Square USA provided a senior secured credit facility backing RM Capital Partners' platform investment in Samaha &amp; Associates")}, a Miami-based technology consulting firm serving credit unions and banks with more than 500 completed engagements for 200-plus clients; facility size and pricing were not disclosed.''',
         why="This deal clearing at all is the signal, not its size &mdash; PitchBook LCD data showed Q2 2026 direct lending volume at $33.6 billion, the lowest since Q2 2023, meaning upper-middle-market deal flow has slowed sharply while smaller, non-sponsor-adjacent lenders like Lafayette Square are still finding and financing lower-middle-market deal flow banks and larger direct lenders are passing on. That bifurcation, not the aggregate volume number alone, is the more useful read on where credit is actually still flowing.",
         implications=[
             "Confirms lower-middle-market direct lending is clearing even as upper-middle-market volume hits a multi-year low",
             "Signals specialty lenders are finding deal flow that larger direct lenders and banks are currently passing on",
             "Provides continued growth capital access for niche vertical-software and services platforms",
             "Reinforces a bifurcating direct lending market by deal size, not a uniform slowdown across the asset class",
         ],
         watch="Whether Q3 2026 direct lending volume data confirms continued softness at the upper-middle-market end while lower-middle-market deal flow holds up."),
]

CREDIT_FINAL_PARAGRAPHS = [
    "This week's signals split into a genuinely new financing frontier and the market's more familiar plumbing. Apollo and Blackstone's $35 billion Anthropic financing and Brookfield/Tor's $255 million PaleBlueDot note describe the same underlying trade &mdash; chips and GPUs as private-credit collateral &mdash; at completely different scales, showing this lending logic now reaches from megacap AI labs down to venture-stage infrastructure platforms in a matter of months.",
    "The NAV loan and secondaries data points are worth reading together. Rated NAV issuance has scaled to $82 billion since 2018 even as initial ratings skew toward BBB, and the credit secondaries market has doubled in six months partly on BDC redemption pressure &mdash; both describe a private credit market that has grown fast enough to need more standardized liquidity tools, faster than it has necessarily proven those tools out through a real downturn.",
    "Trinseo's escalating LME litigation and Prospect Capital's contested below-NAV vote are this week's two governance-risk stories, at different points in the capital structure. One shows how a 2023 priming transaction can still generate active litigation three years later; the other shows a public BDC needing two adjournments to secure authority that directly dilutes its own shareholders.",
]
CREDIT_FINAL_BULLETS = [
    "AI infrastructure financing now spans from a $35 billion megacap deal to a $255 million venture-stage note",
    "NAV loan issuance has scaled past $82 billion since 2018 even as initial ratings skew toward BBB",
    "The credit secondaries market doubled in six months, partly on rising BDC redemption pressure",
    "Lower-middle-market direct lending is clearing even as upper-middle-market volume hits a multi-year low",
]

CREDIT_PAGE = issue_page(
    "credit", False, "Credit", "Signal", "NEW YORK, NY", "JULY 29, 2026", "JULY 21&ndash;28, 2026",
    CREDIT_SNAPSHOT, "What Happened", CREDIT_SIGNALS, CREDIT_FINAL_PARAGRAPHS, CREDIT_FINAL_BULLETS,
    "No predictions. No stock references. Facility-anchored interpretation only.",
)

print("Credit page OK", len(CREDIT_PAGE))

# ============================================================== RE DEBT SIGNAL ==============================================================

REDEBT_MARKETS = [
    ("austin", "Austin, TX"),
    ("usc", "Los Angeles, CA"),
    ("nyu", "New York, NY"),
    ("uga", "Atlanta, GA"),
    ("uf", "Miami, FL"),
]

AUSTIN_DEBT_SNAPSHOT = [
    ("CRE Lending Volume", "stable"),
    ("Construction Financing", "rising"),
    ("CMBS Issuance", "stable"),
    ("Agency Multifamily Activity", "stable"),
    ("Credit Availability", "stable"),
    ("Residential Credit (Non-QM / Jumbo)", "stable"),
]

AUSTIN_DEBT_SIGNALS = [
    dict(category="Construction Lending", title="PIMCO and Berkadia Finance 336-Unit Affordable Community Near Austin",
         subtitle="Institutional Credit Meets a Ground Lease Structure for Deeply Affordable Housing",
         trigger=f'''{src("https://rejournals.com/the-nrp-group-breaks-ground-on-336-unit-affordable-housing-community-in-austin-area/", "The NRP Group broke ground on Catalina, a 336-unit affordable multifamily community in Travis County")}, with construction and permanent financing provided by PIMCO and arranged by Berkadia, tax credit equity from Huntington Community Development Corporation, Safehold as ground lessor, and a $2 million contribution from the Housing Authority of Travis County toward units serving households at or below 30% of area median income.''',
         why="Layering this many distinct capital sources &mdash; an institutional bond giant, a specialty tax-credit equity provider, a ground-lease REIT, and a public housing authority &mdash; onto one 336-unit project is a structure built specifically because no single capital source could underwrite the full affordability spectrum this project targets (30% to 70% AMI) alone. PIMCO's participation as construction and permanent lender is notable because institutional fixed-income managers don't typically underwrite ground-up affordable construction directly; doing so here signals confidence in Berkadia's underwriting and in Travis County's affordable housing demand specifically.",
         implications=[
             "Confirms institutional fixed-income capital is willing to underwrite ground-up affordable construction directly",
             "Demonstrates a replicable multi-source capital stack for deeply affordable, mixed-AMI projects",
             "Uses a ground lease structure to reduce the sponsor's land-ownership capital requirement",
             "Adds 336 units, including a deeply affordable tranche, to the Travis County housing pipeline",
         ],
         watch="Construction progress toward the April 2028 completion date, and whether PIMCO participates in additional Berkadia-arranged affordable deals in the Austin metro.",
         tldr="A 336-unit Travis County affordable project is financed by PIMCO directly, alongside tax-credit equity, a ground lease, and a housing authority &mdash; a stack built because no single source could underwrite it alone."),
    dict(category="Bridge Lending", title="Leander Apartment Complex Lands $46.5M Bridge Refinancing",
         subtitle="A Floating-Rate Bridge Loan on a Newly Built Property Is a Read on Where Rents Are Headed",
         trigger=f'''The owner of a 329-unit, built-in-2024 apartment complex on Talon Grasp Trail in Leander {src("https://crenews.com/2026/07/20/bridge-investment-lends-46-5mln-against-leander-texas-apartments/", "secured a $46.5 million floating-rate, interest-only bridge loan from Bridge Investment Group")}, arranged by Walker &amp; Dunlop, against a backdrop of falling rents across the Austin metro.''',
         why="A floating-rate, interest-only bridge loan on a property that's barely two years old is a specific kind of bet: the borrower is choosing short-term, flexible-but-more-expensive debt over locking in long-term fixed financing, which usually means it expects either rents to improve enough to refinance into permanent debt later, or needs the interest-only period to cover debt service while the property finishes lease-up in a softer rent environment. That this is happening against reported Austin-metro rent declines makes the loan structure itself a signal about current lease-up conditions in the northwest suburbs, independent of what any single ownership group says publicly.",
         implications=[
             "Signals lender comfort underwriting new-vintage suburban multifamily despite metro-wide rent softness",
             "Provides an interest-only bridge structure other newly delivered Leander-area properties may seek",
             "Confirms floating-rate bridge debt remains available for stabilized-but-young multifamily assets",
             "Suggests the borrower expects a refinancing window into permanent debt within the loan's term",
         ],
         watch="Lease-up and rent trends at the property over the loan's term, and whether comparable newly delivered Leander complexes pursue similar bridge refinancings."),
    dict(category="Construction Lending", title="$870M Single-Lender Construction Loan Backs Ultra-Luxury Lake Austin Resort",
         subtitle="One Lender Taking the Entire Stack Is a Bet Few Balance Sheets Can Make",
         trigger=f'''Earlier this summer, {src("https://therealdeal.com/texas/2026/06/02/four-seasons-lake-austin-secures-construction-loan/", "TYKO Capital, an affiliate of Elliott Investment Management, provided an $870 million single-lender construction loan")} to Lincoln Property Company and Austin Capital Partners for Four Seasons Private Residences Lake Austin, a 210-acre ultra-luxury resort community with 179 residences, 28 villa lots, and a private marina.''',
         why="A single lender underwriting an $870 million construction loan alone, rather than syndicating it across a club of banks, requires a balance sheet large enough and a risk appetite specific enough that few institutions can make that call &mdash; Elliott's hedge-fund-adjacent capital, deployed through TYKO, is exactly the kind of flexible, patient capital willing to hold that concentration. The scale of this deal is also a specific bet on ultra-high-net-worth demand for branded residential product in Austin, at a price point insulated from the broader multifamily rent softness affecting the rest of the metro this year.",
         implications=[
             "Confirms alternative-capital lenders are willing to hold construction risk at a scale few banks would underwrite alone",
             "Signals continued ultra-high-net-worth demand for branded residential product in the Austin market specifically",
             "Insulates this segment of Austin real estate from the broader multifamily rent softness affecting the metro",
             "Sets a size benchmark for single-lender construction financing on ultra-luxury resort development",
         ],
         watch="Pre-sale activity on the 179 residences and 28 villa lots as construction proceeds, and whether TYKO Capital participates in other ultra-luxury Austin-area developments.",
         tldr="A single hedge-fund-affiliated lender wrote an $870M construction loan alone for an ultra-luxury Lake Austin resort, insulated from the metro's broader rent softness."),
    dict(category="Distress", title="JPMorgan Takes Back The Line Austin at Foreclosure Auction",
         subtitle="A Lender Credit-Bidding to Own a Hotel Says More Than a Discounted Sale Would",
         trigger=f'''{src("https://therealdeal.com/texas/2026/06/03/the-line-hyatt-centric-go-back-to-lenders-at-auction/", "JPMorgan won back The Line Austin, a 428-key downtown hotel, at a Travis County foreclosure auction")} with an unopposed credit bid for the exact $172 million owed on its 2023 loan to an entity tied to Sydell Group before Soho House &amp; Co. acquired the Line brand; it is the third Line-branded hotel to face foreclosure since 2025, following Line DC and Line LA.''',
         why="A lender credit-bidding the full loan balance to take a property back, rather than accepting a discounted third-party bid at auction, signals JPMorgan currently sees more value in owning and repositioning this hotel than in selling into today's soft downtown Austin hospitality buyer pool. That this is the third Line-branded property to hit foreclosure since 2025 also points to trouble at the brand and parent-company level, not just a single asset's local performance.",
         implications=[
             "Signals lenders see more value in owning and repositioning distressed hotel assets than selling at a discount now",
             "Adds downtown Austin's Line hotel to a broader pattern of financial distress at parent company Soho House",
             "Puts a 428-key downtown hotel directly into a bank's real estate-owned portfolio, not a third-party buyer's hands",
             "Signals the brand-level distress at Line hotels is a national pattern, not an Austin-specific problem",
         ],
         watch="Whether JPMorgan re-brands or sells The Line Austin now that it holds the asset directly, and if other Line-branded hotels face similar foreclosure action."),
    dict(category="Agency Multifamily", title="Freddie Mac Sends Vacant Foreclosed Austin Apartments to Auction at an 80% Haircut",
         subtitle="A $50M Loan Writing Down to a $9.5M Opening Bid Is a Hard Basis Reset",
         trigger=f'''{src("https://therealdeal.com/texas/2026/06/08/freddie-mac-sends-foreclosed-austin-apartments-to-auction/", "Freddie Mac listed a fully vacant, 526-unit foreclosed Austin apartment complex")} at 1601 Royal Crest Drive for auction with a $9.5 million opening bid, after previous owner Mia Riverside defaulted on a $50.2 million Freddie Mac loan originated in March 2024 and the agency took the property back at a January 2026 auction with a $50 million credit bid.''',
         why="An agency loan writing down from a $50 million credit bid to a $9.5 million opening bid for resale, on a now-completely-vacant property, is roughly an 80% basis haircut in under six months &mdash; a specific, quantified data point on how far older, non-renovated Austin multifamily stock has actually fallen, not an estimate. That Freddie Mac is willing to publicly reset the ask this aggressively also suggests the agency has concluded holding for a better outcome isn't worth the continued carrying cost on a vacant asset.",
         implications=[
             "Provides a hard, quantified ~80% loss-severity comp for older, non-renovated Austin multifamily stock",
             "Signals the agency prioritized a clean resale over continuing to carry a vacant, non-income-producing asset",
             "Sets a low entry basis that could attract value-add buyers willing to fully reposition the property",
             "Adds to the broader pattern of agency-financed Austin multifamily distress at older vintage properties",
         ],
         watch="The final sale price relative to the $9.5 million opening bid, and the buyer's disclosed renovation or repositioning plans."),
    dict(category="Special Servicing", title="$430M Fairmont Austin Loan Transfers to Special Servicing Over Tax Reserve Dispute",
         subtitle="Tapping a Reserve Fund Without Consent Is What Actually Triggered This, Not Just Soft Performance",
         trigger=f'''Earlier this summer, {src("https://therealdeal.com/texas/2026/06/16/fairmont-austins-cmbs-loan-transferred-to-special-servicing/", "the $430 million CMBS loan on the 1,048-key Fairmont Austin transferred to special servicing")} after owner Manchester Financial Group tapped a reserve fund to pay property taxes without lender consent, with the hotel's cash flow falling to 65% of underwritten levels and occupancy dropping from 72% to 54% since the loan was originated.''',
         why="The trigger event here is a governance violation, not simply a missed payment &mdash; tapping a reserve fund without consent is a covenant breach that gives the lender grounds to act regardless of whether the borrower could otherwise cover debt service. That said, the underlying performance decline (occupancy down 18 points, cash flow at two-thirds of underwriting) is severe enough that the reserve fund dispute reads as a symptom of real distress, not just a technical disagreement between two parties still fundamentally aligned.",
         implications=[
             "Confirms a covenant violation, not just soft performance, triggered this specific special servicing transfer",
             "Signals real underlying performance decline independent of the governance dispute itself",
             "Adds to a broader pattern of Austin hospitality CMBS stress flagged in aggregate portfolio data this year",
             "Puts control of near-term decisions at one of downtown Austin's largest hotels in the servicer's hands",
         ],
         watch="Whether the reserve fund dispute is resolved through a modification or escalates toward a forced sale process, and updated occupancy figures in subsequent servicer reports.",
         tldr="The $430M Fairmont Austin loan hit special servicing over a reserve-fund covenant breach, not just a missed payment &mdash; and occupancy has fallen 18 points since origination."),
    dict(category="Refinancing", title="Barings Refinances Domain Tower 2 Office as JPMorgan Debt Rolls Off",
         subtitle="A Life-Company Lender Backing a Well-Leased Tower Is a Contrast to This Week's Hotel Stress",
         trigger=f'''{src("https://www.commercialsearch.com/news/exclusive-barings-provides-135m-for-austin-office-refi/", "Stonelake Capital Partners closed a $135 million refinancing of Domain Tower 2")}, a 332,265-square-foot, 24-story office tower in Austin's Domain district leased to PayPal, Wise, Samsung, and ShiftKey, with life-company lender Barings retiring 2023-vintage debt originally held by JPMorgan.''',
         why="A life-company asset manager stepping in to refinance a well-leased, tech-tenanted Domain-district tower shows lender risk appetite in Austin office is highly bifurcated by asset quality, not uniformly closed &mdash; the same week a $430 million hotel loan sits in special servicing and a lender is credit-bidding to take back a downtown hotel, a newer, fully-tenanted suburban office tower clears the debt market on ordinary terms. That distinction, quality asset versus distressed asset, matters more right now than property type alone.",
         implications=[
             "Confirms life-company lenders remain active for well-leased, tech-tenanted Austin office product specifically",
             "Retires bank-originated 2023-vintage debt with a longer-duration institutional lender",
             "Signals Domain-district office continues to clear the debt market even as downtown Austin office and hotel debt struggle",
             "Provides a refinancing comp for other newer, well-tenanted suburban Austin office towers",
         ],
         watch="Whether other Domain-district or suburban Austin office towers pursue similar life-company refinancings, and tenant renewal activity as PayPal and Wise's leases approach expiration."),
]

AUSTIN_DEBT_FINAL_PARAGRAPHS = [
    "This week's Austin lending activity is dominated by hospitality distress at multiple scales. JPMorgan credit-bidding to take back The Line Austin, and the Fairmont Austin's ongoing special servicing dispute, are two different downtown hotels now effectively under lender control &mdash; and The Line is the third hotel under its brand nationally to face foreclosure since 2025, meaning at least part of this stress traces back to a brand-level problem, not just Austin-specific softness.",
    "Freddie Mac's roughly 80% basis haircut on the Royal Crest Drive apartment auction is the hardest number in this week's issue &mdash; a $50 million credit bid resetting to a $9.5 million opening ask in under six months is a real, quantified data point on how far older, non-renovated Austin multifamily has actually fallen, not an analyst estimate.",
    "Domain Tower 2's $135 million life-company refinancing is worth reading against all of the above. The same week two hotels landed in lender hands, a well-leased, tech-tenanted suburban office tower cleared the debt market on ordinary terms &mdash; a reminder that Austin lending risk right now tracks asset quality far more than property type or submarket alone.",
]
AUSTIN_DEBT_FINAL_BULLETS = [
    "Two downtown Austin hotels, The Line and the Fairmont, are now effectively under lender control at the same time",
    "The Line Austin's foreclosure is the third at its hotel brand nationally since 2025, pointing to brand-level distress",
    "A Freddie Mac apartment loan reset from a $50M credit bid to a $9.5M opening ask in under six months",
    "A well-leased Domain-district office tower refinanced on ordinary terms the same week two hotels hit distress",
]

REDEBT_NATIONAL_BLOCK_ARCHIVE = market_block_html(
    "redebt", "austin", True, "RE Debt", "Signal", "AUSTIN, TEXAS", "JULY 29, 2026", "JUNE 2&ndash;JULY 28, 2026",
    AUSTIN_DEBT_SNAPSHOT, "What Happened", AUSTIN_DEBT_SIGNALS, AUSTIN_DEBT_FINAL_PARAGRAPHS, AUSTIN_DEBT_FINAL_BULLETS,
    "No predictions. No stock references. Loan-anchored interpretation only.",
)
USC_DEBT_SNAPSHOT = [
    ("CRE Lending Volume", "stable"),
    ("Construction Financing", "stable"),
    ("CMBS Issuance", "stable"),
    ("Agency Multifamily Activity", "rising"),
    ("Credit Availability", "stable"),
    ("Residential Credit (Non-QM / Jumbo)", "stable"),
]

USC_DEBT_SIGNALS = [
    dict(category="CMBS", title="BofA Plaza Sale Triggers $175.87M in CMBS Losses",
         subtitle="A Receivership Sale Finally Prices What Four Bond Trusts Were Actually Owed",
         trigger=f'''{src("https://crenews.com/2026/07/21/sale-of-las-bofa-plaza-causes-175-87mln-of-losses-to-4-cmbs-trusts/", "The receivership sale of the 1.4-million-square-foot Bank of America Plaza in downtown LA to Capital Group for $210 million")} &mdash; after Brookfield Properties defaulted on a $400 million CMBS loan &mdash; resulted in $175.87 million of losses allocated across four CMBS trusts, per Trepp data.''',
         why="A loss allocation only becomes final once a distressed asset actually trades, because until then the loss is an estimate on paper, subject to however optimistic or pessimistic the special servicer's valuation is. A $210 million sale price against a $400 million loan crystallizes the loss at just over 52 cents on the dollar of the original debt, which is a harder, more specific data point for repricing other downtown LA office CMBS exposure than any analyst estimate could be. That the buyer is a real operating company, not another distressed-asset speculator, also suggests the price found a genuine floor rather than another round of extend-and-pretend.",
         implications=[
             "Crystallizes a specific, tradable loss severity for downtown LA office CMBS collateral",
             "Provides a harder valuation benchmark than special-servicer estimates for comparable towers",
             "Confirms a real operating buyer, not just distressed-asset funds, sees value at this basis",
             "May accelerate resolution of other underwater downtown LA office loans across the same trusts",
         ],
         watch="Whether other CMBS trusts holding downtown LA office debt see similar loss allocations following comparable sales, and Capital Group's plans for the building's vacancy.",
         tldr="A $210M sale of Bank of America Plaza crystallized $175.87M in real CMBS losses &mdash; the clearest repricing data point for downtown LA office debt yet."),
    dict(category="Distress", title="Hackman Capital Defaults on Television City Studio Lot Loan",
         subtitle="A Second Hackman-Affiliated Studio Property Hits Distress in the Same Stretch",
         trigger=f'''{src("https://commercialobserver.com/2026/07/la-studios-distress-hackman-television-city-default-sale/", "Hackman Capital Partners defaulted on a $357 million-plus Deutsche Bank-led loan")} against the 25-acre Television City studio lot in the Fairfax District, with a notice of default filed in June 2026; Hackman and partner Affinius Capital had bought the site from CBS in 2019 for $750 million and planned a roughly $1 billion redevelopment, and Rick Caruso and the Gilmore family are named as potential bidders.''',
         why="A second Hackman-affiliated studio property hitting distress in the same stretch &mdash; alongside Manhattan Beach Studios below, and Goldman Sachs having already taken Hackman's Radford Studio Center after a separate $1.1 billion mortgage default &mdash; shows the Hollywood production slowdown is now hitting one sponsor's studio real estate debt directly and repeatedly, not as an isolated event. A single lender's or sponsor's cluster of defaults across a specific collateral type is a more reliable read on that asset class's health than any one default alone.",
         implications=[
             "Confirms Hollywood production softness is translating directly into studio-lot loan defaults, not just anecdotal reports",
             "Puts a third major Hackman-affiliated studio asset into distress or new ownership within a short stretch",
             "Tests whether named potential bidders like Rick Caruso pursue a discounted acquisition of the site",
             "Signals soundstage collateral now carries real credit risk most CRE lenders rarely underwrite",
         ],
         watch="Whether Television City proceeds to a formal sale process, and which of the named potential bidders emerges as the lead buyer."),
    dict(category="Special Servicing", title="$280M Santa Monica Hotel Loan Heads to Special Servicing",
         subtitle="Even Trophy Hospitality Assets Are Tripping on Maturity-Extension Covenants",
         trigger=f'''{src("https://therealdeal.com/la/2026/07/15/edward-thomas-slatkin-280m-loan-to-special-servicing/", "A $280 million CMBS loan against Shutters on the Beach and Casa del Mar")}, the 327-key Santa Monica hotel duo owned by brothers Edward and Thomas Slatkin, was sent to special servicing after the borrowers said they couldn't meet maturity-extension conditions on top of a separate $120 million mezzanine loan; the Slatkins call special servicer LNR's posture &ldquo;unnecessarily aggressive&rdquo; given what they describe as strong hotel performance.''',
         why="A borrower disputing that its hotels are underperforming, while still landing in special servicing over a maturity-extension covenant, shows how a mezzanine tranche stacked on top of CMBS debt can trigger a workout even when the underlying operating story is genuinely contested &mdash; the covenant, not necessarily the cash flow, is what moved this loan. That this is happening to two of Santa Monica's most recognizable beachfront hotels shows maturity risk in this cycle isn't confined to secondary assets.",
         implications=[
             "Shows maturity-extension covenants, not just cash flow, are triggering special servicing transfers this cycle",
             "Signals mezzanine debt stacked on CMBS loans complicates borrower leverage during a workout",
             "Puts two of Santa Monica's most recognizable beachfront hotels under special servicer oversight",
             "Sets up a public dispute between borrower and servicer over whether performance actually justifies this outcome",
         ],
         watch="Whether the Slatkins and LNR reach a modification or the dispute escalates toward a forced process, and any disclosed occupancy or RevPAR data supporting either side's position."),
    dict(category="Distressed Note Sale", title="Lenders Shop $240M Mortgage on Manhattan Beach Studios After Default",
         subtitle="The Marketing Pitch Reveals Who the Lenders Think the Real Buyer Is",
         trigger=f'''{src("https://www.bisnow.com/los-angeles/news/industrial/manhattan-beach-studios-being-shopped-as-possible-defense-tech-site-135465", "Deutsche Bank and Kennedy Wilson are marketing for sale the $240 million mortgage on Hackman Capital Partners' Manhattan Beach Studios")} after filing a notice of default, with marketing materials pitching the 15-soundstage lot to defense-tech and aerospace tenants rather than traditional entertainment production.''',
         why="Selling the note, rather than foreclosing and operating the asset directly, lets the lenders exit at whatever price the market clears without taking on landlord risk themselves &mdash; but the marketing angle is the real signal here. Pitching a legacy film-production lot to defense-tech and aerospace tenants is an explicit bet that Los Angeles soundstage demand from traditional entertainment has softened enough that the highest-value use for this asset has shifted to an entirely different industry. Paired with the Television City default above, this is now a pattern across Hackman's studio portfolio specifically, not a one-off.",
         implications=[
             "Signals lender willingness to exit via note sale rather than foreclosure and direct ownership",
             "Confirms defense-tech and aerospace tenants are actively evaluating legacy studio space in the South Bay",
             "Reflects softening traditional entertainment-production demand for large soundstage assets",
             "Extends a pattern of distress across multiple Hackman-affiliated studio properties in the same stretch",
         ],
         watch="The note's eventual sale price and buyer identity, and whether defense-tech lease commitments materialize at the property."),
    dict(category="Agency Multifamily", title="Freddie Mac Refinances Upland Apartment Complex With 10-Year Interest-Only Loan",
         subtitle="A Full-Term Interest-Only Structure Is the Owner Betting on Appreciation, Not Paydown",
         trigger=f'''{src("https://www.bisnow.com/los-angeles/news/deal-sheet/santa-monica-offices-to-become-school-los-angeles-deal-sheet-135476", "Northmarq arranged a $34 million, 10-year, full-term interest-only loan from Freddie Mac")} to refinance the 324-unit Northwoods Apartments in Upland.''',
         why="A full-term interest-only structure means the owner never pays down principal over the entire 10-year loan term, which only makes sense if the owner is betting that property value appreciation, not amortization, will build equity over the hold period. Freddie Mac agreeing to this structure is itself a statement of confidence in the property's rent-roll durability, since the agency is accepting a loan balance that never shrinks against a property whose value it's implicitly betting will grow or at least hold.",
         implications=[
             "Signals Freddie Mac's confidence in this property's rent-roll durability over a full 10-year term",
             "Reflects an owner strategy built on appreciation rather than debt paydown",
             "Provides a refinancing comp for comparable Inland Empire-adjacent multifamily assets",
             "Confirms agency full-term interest-only structures remain available for well-positioned sponsors",
         ],
         watch="Whether comparable Inland Empire multifamily refinancings secure similar full-term interest-only terms from either agency.",
         tldr="Freddie Mac backed a 10-year, full-term interest-only refinance on an Upland apartment complex &mdash; a structure that bets on appreciation, not paydown."),
    dict(category="Affordable Bond Financing", title="SoLa Impact Closes $105M Bond Financing for 14-Property Affordable Portfolio",
         subtitle="A First-of-Its-Kind Structure Recapitalizes Construction Across a Scattered Site Portfolio",
         trigger=f'''{src("https://therealdeal.com/la/2026/07/22/sola-impact-lands-financing-for-affordable-housing/", "SoLa Impact, one of LA's largest Section 8 landlords, closed roughly $105 million in taxable and tax-exempt municipal bond financing on July 20")} across 14 properties in LA County &mdash; the first publicly rated muni bond of its kind backed by Section 8 housing assets &mdash; recapitalizing ground-up construction of 465 units, more than half restricted to tenants at 60% of area median income or below.''',
         why="Structuring this as a publicly rated municipal bond, rather than a conventional construction loan or agency financing, means SoLa Impact needed a novel capital markets vehicle specifically because the scattered-site, Section 8-heavy nature of this portfolio didn't fit standard multifamily lending boxes cleanly. Getting a public rating on a first-of-its-kind structure requires convincing a rating agency the cash flows across 14 disparate properties are stable and diversified enough to support investment-grade-style scrutiny.",
         implications=[
             "Validates Section 8 rental income as bondable collateral for a scattered-site portfolio at scale",
             "Provides a novel financing template other large-scale affordable housing operators may replicate",
             "Recapitalizes 465 units of construction, more than half deeply income-restricted, onto more permanent capital",
             "Signals rating agencies are willing to rate diversified Section 8 portfolios despite no single strong asset",
         ],
         watch="Whether other affordable housing operators pursue similar public bond structures, and how this bond trades in the municipal secondary market."),
    dict(category="Construction Lending", title="$85M Construction Loan Backs Beverly Hills Mixed-Use Apartments",
         subtitle="65% Loan-to-Cost in a High-Barrier Submarket Shows Selective Lender Appetite Returning",
         trigger=f'''{src("https://crenews.com/2026/06/12/85mln-construction-loan-secured-for-beverly-hills-calif-apartment-project/", "Marcus &amp; Millichap Capital Corp arranged an $85 million, four-year construction loan at 65% loan-to-cost")} for a 140-unit mixed-use apartment development with 13,000 square feet of ground-floor retail at 55 N. La Cienega Blvd in Beverly Hills, for borrower Westland Development Group.''',
         why="A 65% loan-to-cost construction loan in Beverly Hills specifically, rather than in a lower-barrier submarket, signals a national banking institution is willing to underwrite ground-up multifamily risk in one of LA's most supply-constrained, highest-cost-to-build markets &mdash; a bet that high barriers to entry protect the eventual rent basis enough to justify construction risk at today's costs. This stands in contrast to the broader depressed pace of LA multifamily construction starts citywide.",
         implications=[
             "Confirms selective lender appetite for ground-up multifamily construction is returning in high-barrier LA submarkets",
             "Signals confidence that Beverly Hills' supply constraints protect rent basis enough to justify current construction costs",
             "Adds 140 units and 13,000 square feet of ground-floor retail to the Beverly Hills development pipeline",
             "Provides a 65% loan-to-cost benchmark for other high-barrier-submarket construction financing this cycle",
         ],
         watch="Whether the project breaks ground on schedule, and if comparable construction loans follow in other high-barrier Westside submarkets."),
]

USC_DEBT_FINAL_PARAGRAPHS = [
    "This week's Los Angeles lending activity is dominated by studio and hospitality distress clustered around a small number of sponsors. Hackman Capital's Television City default and the Manhattan Beach Studios note sale are both Hackman-affiliated properties in trouble in the same stretch, and Goldman Sachs has already taken a third Hackman studio asset, Radford Studio Center, after a separate default &mdash; a sponsor-level pattern, not three unrelated events.",
    "The Shutters on the Beach and Casa del Mar special servicing transfer adds a different flavor of distress: a maturity-extension covenant, not necessarily weak cash flow, moved this loan, and the borrowers are openly disputing the servicer's characterization. Paired with Bank of America Plaza's now-crystallized $175.87 million CMBS loss, Los Angeles hospitality and office debt are both generating hard numbers this week, not just anecdotal stress.",
    "Against all of that, the Beverly Hills construction loan and the SoLa Impact bond financing show fresh capital is still being extended with real conviction &mdash; one a conventional bank underwriting ground-up risk in a supply-constrained submarket, the other a first-of-its-kind public bond structure built specifically because no conventional loan fit the collateral.",
]
USC_DEBT_FINAL_BULLETS = [
    "Three Hackman-affiliated studio properties have now hit distress or changed hands under duress in the same stretch",
    "A Santa Monica hotel special servicing transfer turned on a maturity covenant, not necessarily weak performance",
    "Los Angeles CMBS distress is being priced and resolved this week, not just extended on paper",
    "Selective construction and public-bond capital is still being extended with real conviction in specific submarkets",
]

REDEBT_USC_BLOCK = market_block_html(
    "redebt", "usc", False, "RE Debt", "Signal", "LOS ANGELES, CA", "JULY 29, 2026", "JULY 15&ndash;28, 2026",
    USC_DEBT_SNAPSHOT, "What Happened", USC_DEBT_SIGNALS, USC_DEBT_FINAL_PARAGRAPHS, USC_DEBT_FINAL_BULLETS,
    "No predictions. No stock references. Loan-anchored interpretation only.",
)
NYC_DEBT_SNAPSHOT = [
    ("CRE Lending Volume", "stable"),
    ("Construction Financing", "rising"),
    ("CMBS Issuance", "stable"),
    ("Agency Multifamily Activity", "rising"),
    ("Credit Availability", "stable"),
    ("Residential Credit (Non-QM / Jumbo)", "stable"),
]

NYC_DEBT_SIGNALS = [
    dict(category="Refinancing", title="SL Green Begins Refinancing $1.77B Mortgage on 245 Park Ave",
         subtitle="A Mega-Loan Refi Attempt Is a Real Test of the Trophy Office Debt Market",
         trigger=f'''{src("https://crenews.com/2026/07/29/sl-green-eyes-refinancing-245-park-office-in-midtown-manhattan/", "SL Green Realty Corp. began efforts to refinance $1.77 billion of existing mortgage debt")} against 245 Park Avenue, its 1.78 million-square-foot Midtown Manhattan office tower.''',
         why="A refinancing attempt at this scale on a large Class A Midtown tower is a direct test of whether debt capital is willing to underwrite mega-loans on trophy office again, rather than just office debt broadly stabilizing on paper. The eventual lender group, pricing, and proceeds relative to the existing $1.77 billion balance will be closely watched as a read on where office lending has actually normalized versus where it merely looks calmer from the outside.",
         implications=[
             "Functions as a live test case for whether $1.77 billion-scale trophy office refinancings can still clear the market",
             "Sets a size benchmark other large Manhattan office sponsors will reference for their own refinancing timelines",
             "Signals SL Green's confidence that lenders remain willing to underwrite its flagship asset at scale",
             "Provides an early read on proceeds and pricing relative to the existing loan balance once terms are disclosed",
         ],
         watch="The identity of the new lender group once disclosed, and whether proceeds come in at, above, or below the existing $1.77 billion balance."),
    dict(category="Distressed Note Sale", title="OceanFirst Sells $1.3B of NYC Rent-Stabilized Apartment Loans to Cerberus",
         subtitle="A Regional Bank De-Risks Its Rent-Regulated Multifamily Exposure in Bulk",
         trigger=f'''{src("https://crenews.com/2026/07/29/oceanfirst-bank-sells-1-3bln-portfolio-of-new-york-apartment-loans/", "OceanFirst Financial Corp. sold a $1.3 billion portfolio of New York City apartment loans to Cerberus Capital Management")}, with most of the underlying properties subject to New York's rent-stabilization regulations.''',
         why="A regional bank offloading $1.3 billion in rent-regulated multifamily paper in bulk, to a distressed-debt buyer rather than another bank, is a concrete data point on how lenders are de-risking exposure to post-HSTPA rent-stabilized buildings &mdash; an asset class many lenders have quietly repriced as structurally impaired collateral since New York's 2019 rent law changes limited owners' ability to raise rents or recoup renovation costs. Cerberus buying at scale suggests distressed-debt investors see a workable basis in this paper that the originating bank no longer wanted to carry.",
         implications=[
             "Confirms regional banks are actively de-risking rent-stabilized NYC multifamily loan exposure in bulk, not loan-by-loan",
             "Signals distressed-debt buyers like Cerberus see a workable basis in rent-regulated paper banks are exiting",
             "Provides a large, real transaction size benchmark for rent-stabilized loan portfolio sales",
             "May prompt other regional banks carrying similar post-HSTPA exposure to pursue comparable bulk sales",
         ],
         watch="Whether other regional or community banks announce similar bulk sales of rent-stabilized NYC multifamily loans."),
    dict(category="Special Servicing", title="$37.5M CMBS Loan on Lower Manhattan Office Building Hits Special Servicing",
         subtitle="Distress Has Moved Well Beyond Trophy Towers Into Small, Older Office Stock",
         trigger=f'''{src("https://crenews.com/2026/07/06/continued-occupancy-cash-flow-issues-prompt-manhattan-office-loans-transfer-to-special-servicing/", "The $37.5 million CMBS loan against the 58,850-square-foot Ditson Building in Lower Manhattan transferred to special servicing")} due to continued occupancy and cash-flow issues; the loan, securitized through the BANK 2018-BN13 trust, carries a fixed rate of 5.43%.''',
         why="A sub-$40 million loan hitting special servicing shows office distress has moved well beyond headline-grabbing trophy towers into small, older Lower Manhattan office stock &mdash; buildings where there's little leasing momentum to justify an extended workout, making straight liquidation a more likely outcome than extend-and-pretend. Aggregating enough of these smaller loan-level events is often a better read on the depth of an office distress cycle than any single large-tower story.",
         implications=[
             "Confirms office distress extends into small, older Lower Manhattan buildings, not just trophy towers",
             "Signals limited leasing momentum makes a negotiated workout less likely than eventual liquidation here",
             "Adds a specific, small-loan data point to the broader Manhattan office CMBS distress narrative",
             "May be more representative of aggregate distress depth than large single-tower special servicing stories",
         ],
         watch="Whether the loan proceeds toward a modification or a forced sale, and comparable special servicing transfers on similarly small, older Manhattan office loans."),
    dict(category="Agency Multifamily", title="Arbor Writes $146.24M Fannie Mae Loan for Lower Manhattan Apartments",
         subtitle="Agency Lenders Remain the Reliable, Lowest-Cost Capital Source for Stabilized NYC Multifamily",
         trigger=f'''{src("https://crenews.com/2026/07/28/arbor-realty-writes-146-24mln-fannie-mae-loan-for-manhattan-apartments/", "Arbor Realty Trust originated a $146.24 million Fannie Mae loan for the 209-unit apartment building at 7 Dey Street")} in Lower Manhattan.''',
         why="Continued heavy GSE appetite for Manhattan multifamily at this scale reinforces that agency lenders remain the reliable, lowest-cost capital source for stabilized NYC apartment assets even while bank and CMBS office lending stays comparatively choppy. That split &mdash; agency capital flowing freely to multifamily while office debt requires much more selective underwriting &mdash; is one of the clearest lender-risk-appetite divides in the current market.",
         implications=[
             "Confirms GSE lenders remain willing to fund large Manhattan multifamily loans at scale",
             "Reinforces the divide between freely-flowing agency multifamily capital and more selective office lending",
             "Provides a $146.24 million comp for comparable Lower Manhattan multifamily agency financings",
             "Signals continued confidence in stabilized NYC apartment collateral specifically",
         ],
         watch="Whether comparable GSE-financed Manhattan multifamily loans price similarly in the coming weeks."),
    dict(category="Construction Lending", title="BXP Closes $1.2B Construction Loan for 343 Madison Ave Office Tower",
         subtitle="A Bank Club Deal Shows Lenders Will Still Fund New Office Supply, With Conditions",
         trigger=f'''{src("https://commercialobserver.com/2026/07/bxp-construction-loan-343-madison-avenue-q2-earnings/", "BXP closed a $1.2 billion construction loan for its 46-story, roughly 930,000-square-foot office tower at 343 Madison Avenue")}, led by Wells Fargo with support from BofA Securities, Bank of New York Mellon, and JPMorgan Chase; the loan carries a four-year initial term plus a one-year extension, an initial rate of Term SOFR plus 2.50% that steps down to plus 2.25% on leasing and construction milestones, and the roughly $2 billion, Grand Central-connected tower is about 50% pre-leased with completion expected in 2029.''',
         why="A major bank club deal financing ground-up trophy office construction, at a moment when office construction lending has been scarce nationally, shows lenders will still underwrite new supply &mdash; but only when it clears a high bar: pre-leased, transit-connected, and built by a top-tier REIT. The rate step-down tied to leasing and construction milestones is itself a signal that lenders are pricing in real execution risk and rewarding de-risking events explicitly, rather than underwriting the project on projected rents alone.",
         implications=[
             "Confirms bank capital will still fund large ground-up office construction when pre-leasing and sponsor quality are strong",
             "Ties borrowing cost directly to leasing and construction milestones, pricing execution risk explicitly into the loan",
             "Sets a $1.2 billion size and multi-bank club structure benchmark for other trophy office construction financings",
             "Reinforces Grand Central-area transit connectivity as a key underwriting factor for new Midtown office supply",
         ],
         watch="Whether 343 Madison's pre-leasing percentage climbs enough to trigger the rate step-down, and construction progress toward the 2029 completion target."),
    dict(category="Affordable Bond Financing", title="Cedarbridge Refinances 1,000-Unit Portfolio With 40-Year Affordability Deal",
         subtitle="A Bank Refinancing Is Being Used to Lock In Affordability, Not Just Provide Subsidy",
         trigger=f'''{src("https://www.bisnow.com/new-york/news/deal-sheet/canadian-reit-brooklyn-medical-office-ny-deal-sheet-135586", "Cedarbridge Management refinanced a 27-building, 1,000-unit multifamily portfolio")} across Brooklyn and Manhattan with a $145.7 million loan from Customers Bank, closing simultaneously with a new 40-year Article 11 affordability agreement negotiated with the NYC Housing Partnership.''',
         why="Tying a private bank refinancing directly to a long-term, 40-year affordability covenant illustrates how lenders and the city are increasingly using debt structuring itself &mdash; not just direct subsidy &mdash; as the mechanism to preserve affordable housing stock at scale. A 27-building portfolio locking in affordability for four decades in exchange for refinancing terms is a much larger and longer-duration commitment than a typical single-building affordable deal.",
         implications=[
             "Demonstrates debt structuring itself, not just subsidy, as a tool for locking in long-term affordability",
             "Locks in affordability across 1,000 units for a full 40-year term, a longer horizon than most comparable deals",
             "Provides a replicable template pairing private bank refinancing with city affordability partnerships",
             "Signals continued private bank appetite to refinance large multifamily portfolios tied to affordability covenants",
         ],
         watch="Whether Customers Bank or other private lenders pursue additional refinancings structured around long-term Article 11 agreements."),
    dict(category="Bridge Lending", title="Ladder Capital Lends $268M to Fund 575 Fifth Ave Office Purchase",
         subtitle="A Non-Bank Lender Underwrites Aggressive Leverage on a Fifth Avenue Trade",
         trigger=f'''{src("https://crenews.com/2026/07/27/ladder-capital-lends-268mln-to-fund-purchase-of-manhattans-575-fifth-ave-office/", "Ladder Capital Corp. lent $268 million to fund the purchase of the 507,031-square-foot office building at 575 Fifth Avenue")}, which traded for $378 million ($745.50 per square foot), implying roughly 71% leverage against the purchase price; Eastdil Secured brokered the sale.''',
         why="A non-bank balance-sheet lender writing a $268 million acquisition loan at roughly 71% loan-to-value on a Fifth Avenue office trade signals real debt capital is still willing to underwrite sizable Manhattan office acquisitions at aggressive leverage. Read alongside this week's special servicing and refinancing-distress signals, it's a useful counterpoint showing the office debt market is bifurcating sharply by asset quality and location, rather than being uniformly frozen.",
         implications=[
             "Confirms non-bank lenders remain willing to underwrite aggressive leverage on quality Manhattan office acquisitions",
             "Provides a 71% loan-to-value benchmark for comparable Fifth Avenue-caliber office acquisition financings",
             "Signals continued bifurcation in office debt markets by asset quality, not a uniform financing freeze",
             "Reinforces Eastdil Secured's role brokering large Manhattan office trades this cycle",
         ],
         watch="The borrower's business plan for 575 Fifth Avenue, and whether comparable non-bank lenders write similarly leveraged acquisition loans on other Manhattan office trades."),
]

NYC_DEBT_FINAL_PARAGRAPHS = [
    "This week's New York lending activity splits cleanly between capital exiting risk and capital extending fresh conviction. OceanFirst's $1.3 billion bulk sale of rent-stabilized loans to Cerberus and the Ditson Building's special servicing transfer both represent lenders recognizing or exiting distress; SL Green's $1.77 billion refinancing attempt, BXP's $1.2 billion construction loan, and Ladder Capital's $268 million acquisition loan all represent fresh capital being extended at real scale.",
    "The SL Green and BXP signals are worth reading together as two different tests of the same question: will debt capital still underwrite Manhattan trophy office at scale? SL Green is asking that question of existing debt on a stabilized asset; BXP already got its answer, in the form of a $1.2 billion bank club construction loan with milestone-based pricing that shows lenders will fund new supply, but only on favorable, pre-leased terms.",
    "Ladder Capital's aggressive 71%-leverage acquisition loan on 575 Fifth Avenue is this week's clearest evidence that office debt isn't frozen uniformly &mdash; it's bifurcating sharply by asset quality, location, and lender type, with non-bank balance-sheet lenders stepping in exactly where the picture otherwise looks most cautious.",
]
NYC_DEBT_FINAL_BULLETS = [
    "A regional bank exited $1.3 billion of rent-stabilized NYC multifamily loan exposure in one bulk sale to Cerberus",
    "SL Green and BXP are both testing whether debt capital still underwrites Manhattan trophy office at billion-dollar scale",
    "A sub-$40 million special servicing transfer shows office distress reaching small, older Lower Manhattan buildings too",
    "A non-bank lender's 71%-leverage acquisition loan shows office debt bifurcating by quality, not freezing uniformly",
]

REDEBT_NYU_BLOCK = market_block_html(
    "redebt", "nyu", False, "RE Debt", "Signal", "NEW YORK, NY", "JULY 29, 2026", "JULY 6&ndash;29, 2026",
    NYC_DEBT_SNAPSHOT, "What Happened", NYC_DEBT_SIGNALS, NYC_DEBT_FINAL_PARAGRAPHS, NYC_DEBT_FINAL_BULLETS,
    "No predictions. No stock references. Loan-anchored interpretation only.",
)
REDEBT_UGA_BLOCK = market_block_html(
    "redebt", "uga", False, "RE Debt", "Signal", "ATLANTA, GA", "COMING SOON", "&mdash;",
    [], "What Happened", [], [], [], "No predictions. No stock references. Loan-anchored interpretation only.",
    coming_soon="Coming soon &mdash; real research for the Atlanta market is in progress.",
)
REDEBT_UF_BLOCK = market_block_html(
    "redebt", "uf", False, "RE Debt", "Signal", "MIAMI, FL", "COMING SOON", "&mdash;",
    [], "What Happened", [], [], [], "No predictions. No stock references. Loan-anchored interpretation only.",
    coming_soon="Coming soon &mdash; real research for the Miami market is in progress.",
)

REDEBT_PAGE = multi_market_page("redebt", False, REDEBT_MARKETS,
    [REDEBT_NATIONAL_BLOCK_ARCHIVE, REDEBT_USC_BLOCK, REDEBT_NYU_BLOCK, REDEBT_UGA_BLOCK, REDEBT_UF_BLOCK])

print("RE Debt page OK", len(REDEBT_PAGE))

# ============================================================== STRUCTURED SIGNAL ==============================================================

STRUCTURED_SNAPSHOT = [
    ("CLO Issuance", "rising"),
    ("Consumer ABS Issuance", "stable"),
    ("Esoteric ABS Issuance", "rising"),
    ("Spread Tightening", "rising"),
    ("Ratings Momentum", "stable"),
    ("Warehouse Financing", "rising"),
]

STRUCTURED_SIGNALS = [
    dict(category="Esoteric ABS", title="Aligned Data Centers Prices $1.183B ABS, Upsized 30% From Target",
         subtitle="An Oversubscribed First-Since-2023 Deal Confirms Investor Appetite Hasn't Faded",
         trigger=f'''{src("https://www.globenewswire.com/news-release/2026/07/28/3334210/0/en/Aligned-Data-Centers-Completes-1-18-Billion-Securitization-Financing.html", "Aligned Data Centers closed a $1.183 billion ABS issuance on July 28")}, its first securitization since 2023, upsized roughly 30% from an initial $905 million target; the Class A-2-I and Class B notes carry a five-year anticipated repayment date, backed by four data center campuses with 14 enterprise customers, more than 90% of annualized base rent from investment-grade counterparties.''',
         why="A 30% upsize on a first-since-2023 deal, in the same week a separate BlackRock-led consortium closed its $40 billion acquisition of the same company, shows institutional capital is underwriting Aligned's cash flows from both the equity and structured-debt side simultaneously &mdash; the ABS market's own appetite here is independent confirmation that the M&amp;A price wasn't disconnected from how bond investors view the same collateral. That over 90% of rent comes from investment-grade counterparties is what let the deal price at this scale despite continued questions about AI-datacenter demand durability broadly.",
         implications=[
             "Confirms institutional ABS investor appetite for data center collateral remains strong despite a three-year gap since Aligned's last deal",
             "Shows equity (the BlackRock acquisition) and structured debt investors reached similar conclusions about the same collateral in the same week",
             "Relies on investment-grade tenant credit quality, not speculative AI demand growth, to support the deal's size",
             "Sets a reference point for how much a data center ABS deal can upsize when tenant credit quality is strong enough",
         ],
         watch="Whether other data center operators follow with new issuance given Aligned's demonstrated demand, and how the notes perform in secondary trading."),
    dict(category="CLO", title="CVC Credit Prices $550M CLO at Near Market-Tight Spreads for Tier-1 Managers",
         subtitle="Top-Shelf Managers Are Pricing Tight Even as Broader New-Issue Volume Slows",
         trigger=f'''{src("https://www.cvc.com/media/news/2026/cvc-credit-prices-third-new-issue-clo-of-2026/", "CVC Credit priced Apidos LVII, a $550 million new-issue CLO, on July 7")}, its third global new-issue CLO of 2026, with a five-year reinvestment period and Scotiabank as lead arranger; CVC described &ldquo;strong demand across the entire debt stack&rdquo; with pricing landing at &ldquo;near market tights for Tier 1 CLO managers.&rdquo;''',
         why="A Tier-1 manager pricing at near-market-tights, even as broader broadly-syndicated-loan CLO volume is reported down roughly 21% year-over-year, shows the CLO primary market is bifurcating by manager quality rather than moving uniformly &mdash; investors are still paying up in spread terms for platforms with CVC's track record while pulling back from less-established shelves. That distinction matters more right now than the aggregate volume figure alone.",
         implications=[
             "Confirms Tier-1 CLO managers can still price at market tights even as aggregate new-issue volume falls",
             "Signals investors are differentiating sharply by manager track record, not treating CLO paper as fungible",
             "Sets a tight pricing reference other Tier-1 platforms will point to on their next new-issue deal",
             "Suggests second-tier CLO shelves face a harder execution environment than the headline volume number implies",
         ],
         watch="Whether CVC's fourth 2026 new-issue CLO, if it prices, matches this spread level, and how second-tier manager pricing compares in the same stretch."),
    dict(category="CLO", title="Macquarie Prices Third U.S. CLO in 18 Months, Draws Ten New Investors",
         subtitle="A Newer Entrant Scaling Fast Shows Investors Backing More Than Just Legacy Platforms",
         trigger=f'''{src("https://www.macquarie.com/us/en/about/news/2026/pricing-marks-continued-growth-for-the-firms-clo-platform.html", "Macquarie Asset Management priced Market Street CLO III, a $409 million CLO, on July 2")}, pushing its total U.S. CLO pricing past $1.6 billion across three deals in 18 months since its inaugural 2025 issuance, and drawing ten new investors to the platform on this print alone.''',
         why="A relatively new entrant scaling to $1.6 billion across three deals in 18 months, with ten new investors on the latest print, is a different story than CVC's tight Tier-1 pricing above &mdash; it shows CLO investors are also willing to back newer platforms building scale quickly, not just consolidating around legacy Tier-1 shops, as Macquarie's Credit &amp; Insurance division (which manages $162 billion) builds out its structured credit franchise following its Spire Management acquisition.",
         implications=[
             "Confirms CLO investors will back scaling newer platforms, not just legacy Tier-1 managers exclusively",
             "Adds ten new investors to Macquarie's CLO platform in a single print, broadening its capital base",
             "Signals Macquarie's Credit &amp; Insurance division is building out structured credit as a core franchise, not a side business",
             "Provides a growth-pace benchmark ($1.6B across three deals in 18 months) for other newer CLO platforms",
         ],
         watch="Whether Macquarie prices a fourth U.S. CLO within the next several months, and if the new-investor count continues growing on subsequent deals."),
    dict(category="Consumer ABS", title="Pagaya Closes Its Largest-Ever Auto ABS at $750M, Upsized",
         subtitle="A New Excess-Spread Tranche Shows Fintech ABS Platforms Getting More Structurally Sophisticated",
         trigger=f'''{src("https://pulse2.com/pagaya-closes-750-million-auto-abs-transaction-its-largest-to-date/", "Pagaya Technologies closed RPM 2026-4 on July 16, a $750 million upsized auto ABS")}, its largest deal ever and fourth fully pre-funded auto ABS of 2026, drawing 41 unique investors including 6 new to Pagaya's platform and 7 new to its auto ABS shelf specifically; the deal included the platform's inaugural excess-spread tranche, bringing total 2026 pre-funded auto ABS issuance to $2.25 billion.''',
         why="Introducing a new excess-spread tranche, designed specifically to let Pagaya monetize residual cash flows separately from traditional note classes, is a structural innovation that broadens the investor base able to buy into the deal &mdash; different investors want different risk-return profiles, and slicing out excess spread as its own tranche lets Pagaya sell to more of them at once, which likely helped this deal both upsize and draw 13 new investors on a single print.",
         implications=[
             "Confirms fintech-adjacent ABS platforms are getting structurally more sophisticated to broaden their investor base",
             "Signals residual cash-flow monetization via excess-spread tranches is becoming a repeatable Pagaya innovation",
             "Extends Pagaya's total 2026 pre-funded auto ABS issuance to $2.25 billion across four deals",
             "Sets a size and structure benchmark ($750M, largest-ever) other fintech-adjacent auto ABS platforms will reference",
         ],
         watch="Whether Pagaya's excess-spread tranche structure appears in other platforms' auto ABS deals, and pricing performance on RPM 2026-4's next servicing reports."),
    dict(category="Synthetic Risk Transfer", title="Santander Prices Its Tenth Auto Credit-Linked Note, First Prime Deal of 2026",
         subtitle="A Tenth Iteration Signals SRT Has Normalized as a Routine Capital Tool for Auto Lenders",
         trigger=f'''{src("https://www.ifre.com/deal/securitisation/2441589/abs-santander-auto-credit-linked-sbcln-2026-a-us279m-priced", "Banco Santander priced SBCLN 2026-A, a $279 million-plus credit-linked note tied to prime U.S. auto loans")}, its debut prime auto CLN of 2026 and tenth auto CLN overall, part of Santander's broader 2026 strategy to shed roughly &euro;40&ndash;45 billion of risk-weighted assets globally via SRT and other capital-relief tools this year.''',
         why="A tenth iteration of the same auto-CLN program shows synthetic risk transfer has become a routine, repeatable capital-management tool for large auto lenders rather than a one-off trade &mdash; evidence the asset class, once dominated by residential mortgage and corporate-loan SRTs, is normalizing for consumer auto risk specifically in the U.S. market, as Santander works through a large, disclosed global risk-weighted-asset reduction target.",
         implications=[
             "Confirms SRT has normalized into a routine, repeatable capital tool for large auto lenders, not a one-off trade",
             "Advances Santander's disclosed &euro;40&ndash;45 billion global risk-weighted-asset reduction target for 2026",
             "Extends the SRT asset class further into consumer auto risk, beyond its historical mortgage and corporate-loan base",
             "Signals other large bank auto lenders may find the same capital-relief tool worth replicating",
         ],
         watch="Whether Santander prices additional prime auto CLNs later in 2026, and if other large bank auto lenders launch comparable SRT programs."),
    dict(category="Rating Action", title="Over 400 CLOs Lined Up for Upgrades After Fitch and Moody's Methodology Changes",
         subtitle="A Methodology-Driven Wave of Upgrades Raises a Real 2008-Adjacent Question",
         trigger=f'''{src("https://www.bloomberg.com/news/articles/2026-07-15/over-400-clos-tabbed-for-upgrade-in-pivot-that-fans-08-fears", "Over 400 CLOs are lined up for ratings upgrades")} after Fitch (June 1) and Moody's (June 5) each proposed CLO ratings-methodology changes reflecting years of actual defaults running below what the agencies' models had predicted &mdash; Fitch's change affecting up to 15% of the CLOs it rates, Moody's affecting roughly a third of the tranches it assesses; the scale and speed of the shift has drawn explicit comparisons to pre-2008 ratings methodology loosening.''',
         why="An upgrade wave driven by a methodology recalibration, rather than by improved underlying collateral credit at each individual deal, decouples the rating itself from loan-level credit quality in a way that's structurally different from a normal rating action &mdash; the loans didn't get safer overnight, the model's assumptions about them changed. That's precisely the mechanism critics are flagging as reminiscent of pre-2008 methodology loosening, and it's a critical distinction for anyone learning to read CLO tranche ratings as a signal rather than accepting them as a fixed technical fact.",
         implications=[
             "Decouples this wave of ratings upgrades from any actual improvement in underlying loan-level collateral credit",
             "Affects up to 15% of Fitch-rated CLOs and roughly a third of Moody's-assessed tranches simultaneously",
             "Draws explicit market comparisons to pre-2008 ratings methodology loosening, a meaningful credibility risk for the agencies",
             "Requires investors to distinguish model-driven upgrades from genuine collateral performance improvements going forward",
         ],
         watch="How quickly the 400-plus flagged upgrades are actually executed, and whether other rating agencies propose similar methodology recalibrations."),
    dict(category="Warehouse Facility", title="Empire Asset Finance Closes First Institutional Warehouse Facility With Bank OZK",
         subtitle="A Textbook Warehouse-to-ABS Pipeline Deal, Even Without a Disclosed Size",
         trigger=f'''{src("https://www.monitordaily.com/empire-asset-finance-secures-senior-warehouse-credit-facility-with-bank-ozk/", "Empire Asset Finance closed its first institutional warehouse credit facility with Bank OZK")} on July 20, funding capital leases, operating leases, loans, and sale-leaseback transactions across equipment types for U.S. and Canadian middle-market borrowers; facility size was not disclosed, but the deal is explicitly framed as building toward future term-out into capital markets and ABS execution.''',
         why="A specialty equipment finance originator lining up bank warehouse funding as the explicit first step toward eventually terming out into a rated securitization is the textbook warehouse-to-ABS pipeline &mdash; this kind of flow deal is a leading indicator of future esoteric ABS supply, since originators only build out warehouse capacity when they're planning to scale origination volume toward a size that eventually justifies a term securitization.",
         implications=[
             "Signals future esoteric equipment-finance ABS supply as Empire scales toward eventual term-out execution",
             "Confirms Bank OZK's continued appetite for warehouse lending to specialty equipment finance originators",
             "Funds a diversified base of capital leases, operating leases, loans, and sale-leasebacks across equipment types",
             "Provides an early-stage leading indicator worth tracking well before any eventual ABS deal actually prices",
         ],
         watch="Empire's origination volume growth against this new warehouse capacity, and any disclosed timeline toward a first term securitization."),
]

STRUCTURED_FINAL_PARAGRAPHS = [
    "This week's signals span from a $1.183 billion data center ABS print to a warehouse facility with an undisclosed size, but they share a theme: this desk covers CLOs and corporate/consumer ABS specifically, a different lane from Securitized Signal, which covers residential and commercial mortgage securitization (RMBS and CMBS) separately. The Aligned Data Centers ABS deal is worth noting alongside IB Signal's coverage of the same company's $40 billion acquisition this week &mdash; equity and structured-debt investors reached similar conclusions about the same collateral independently, in the same stretch.",
    "The two CLO prints this week describe a bifurcating primary market. CVC, a Tier-1 manager, priced near market tights even as broader broadly-syndicated-loan volume is reported down roughly 21% year-over-year; Macquarie, a newer entrant, kept scaling and drew ten new investors on its third deal in 18 months. Both are real demand signals, just from opposite ends of the manager-quality spectrum.",
    "The CLO ratings-methodology story is this issue's most consequential for how to actually read a rating. Over 400 CLOs lined up for upgrades from a model recalibration, not from improved collateral, is a real, current test of whether tranche ratings still track loan-level credit quality &mdash; a distinction with real consequences the last time methodology loosened this broadly.",
]
STRUCTURED_FINAL_BULLETS = [
    "This desk covers CLOs and corporate/consumer ABS specifically, distinct from Securitized Signal's RMBS and CMBS coverage",
    "Aligned Data Centers' $1.183B ABS print and its $40B acquisition (covered in IB Signal) priced the same collateral independently, same week",
    "Tier-1 and newer-entrant CLO managers are both finding real demand, from opposite ends of the manager-quality spectrum",
    "A methodology-driven wave of 400-plus CLO upgrades decouples ratings from loan-level credit quality this cycle",
]

STRUCTURED_PAGE = issue_page(
    "structured", False, "Structured", "Signal", "NEW YORK, NY", "JULY 29, 2026", "JULY 2&ndash;28, 2026",
    STRUCTURED_SNAPSHOT, "What Happened", STRUCTURED_SIGNALS, STRUCTURED_FINAL_PARAGRAPHS, STRUCTURED_FINAL_BULLETS,
    "No predictions. No stock references. Structure-anchored interpretation only.",
)

# ============================================================== SECURITIZED SIGNAL (RMBS / CMBS) ==============================================================

SECURITIZED_SNAPSHOT = [
    ("RMBS Issuance", "rising"),
    ("CMBS Issuance", "stable"),
    ("Collateral Performance", "stable"),
    ("Credit Enhancement Levels", "stable"),
    ("Ratings Momentum", "stable"),
    ("Warehouse Financing", "rising"),
]

SECURITIZED_SIGNALS = [
    dict(category="CMBS Conduit", title="Citi Prices Largest Multifamily-Only CMBS Conduit Since the Financial Crisis",
         subtitle="A Bank's Own Top-Market Rankings Reveal Where Its Origination Pipeline Is Strongest",
         trigger=f'''{src("https://commercialobserver.com/2026/07/citi-conduit-cmbs/", "Citigroup priced the $816.9 million Citigroup Commercial Mortgage Trust 2026-MFAM1")} the week of July 16, the largest single-bank-originated, multifamily-only conduit transaction since the financial crisis, comprising 27 five-year interest-only loans across 27 multifamily properties with New York, Los Angeles, and Florida as the top three markets represented; AAA bonds priced at swaps plus 80 basis points, 8 basis points tighter than a comparable May 2026 deal, with average Fitch loan-to-value at 123.4%.''',
         why="A bank's own top-market rankings in a conduit deal reveal where its origination pipeline actually found qualifying volume, not just where multifamily lending happens broadly &mdash; and pricing 8 basis points tighter than a comparable deal from two months earlier shows AAA investor demand improved in that short window even as single-asset, single-borrower deals now make up roughly three-quarters of private-label CMBS issuance, making this diversified pool a rarer structure investors were evidently glad to see.",
         implications=[
             "Confirms Citi's own multifamily origination pipeline is deepest in New York, Los Angeles, and Florida specifically",
             "Signals AAA CMBS investor demand improved measurably in the eight weeks since a comparable May 2026 print",
             "Provides institutional investors a rare diversified multifamily pool as SASB deals dominate private-label issuance",
             "Sets a tighter spread benchmark for the next large bank-originated multifamily conduit deal"
         ],
         watch="Whether other banks follow with comparable large multifamily-only conduit deals, and loan-level performance disclosures as the pool seasons."),
    dict(category="CMBS SASB", title="Nomura Prices $719M SASB CMBS as Keller Investment Shifts From Agency Debt",
         subtitle="A Sponsor's First-Ever CMBS Execution Is a Real Vote on Where Pricing Sits Right Now",
         trigger=f'''{src("https://commercialobserver.com/2026/07/nomura-sasb-cmbs-keller-newmark/", "Nomura priced the $719 million KELR 2026-MF single-asset, single-borrower CMBS deal")} in early July, its largest sole-bank SASB transaction in nearly two years, backed by 12 multifamily properties and one student-housing asset totaling 3,321 units for borrower Keller Investment Properties &mdash; the sponsor's first-ever CMBS execution after historically relying on agency debt; AAA bonds priced at 135 basis points over SOFR at 77% loan-to-value, multiple times oversubscribed.''',
         why="A sponsor moving from agency financing to a SASB CMBS execution for the first time, and getting oversubscribed at 135 basis points over SOFR, is a direct market vote that CMBS spreads have tightened enough to actually pull borrowers away from their default agency-debt playbook &mdash; sponsors don't switch financing channels for the first time on a $719 million deal unless the pricing genuinely beats their established alternative.",
         implications=[
             "Confirms CMBS pricing has tightened enough to draw sponsors away from agency debt as a default choice",
             "Signals continued strong AAA investor demand for diversified multifamily SASB collateral specifically",
             "Provides Nomura a template sponsor conversion story to pitch other agency-reliant multifamily borrowers",
             "Sets a 135bps-over-SOFR pricing benchmark for comparable multifamily SASB deals",
         ],
         watch="Whether Keller Investment Properties returns to CMBS for future refinancings, and if other agency-reliant sponsors follow with their own first-time SASB executions."),
    dict(category="Non-Agency RMBS", title="AD Mortgage Closes Fifth Non-QM RMBS Deal of 2026, Pace Nearing Quarterly",
         subtitle="Programmatic Quarterly Issuance Signals a Maturing Funding Channel, Not an Opportunistic One",
         trigger=f'''{src("https://www.businesswire.com/news/home/20260708309861/en/KBRA-Assigns-Preliminary-Ratings-to-AD-Mortgage-Trust-2026-NQM5-ADMT-2026-NQM5", "KBRA assigned preliminary ratings on July 8 to ADMT 2026-NQM5, AD Mortgage's fifth non-QM RMBS deal of 2026")}, a $432.4 million transaction backed by 1,008 loans with a 754 weighted-average FICO and 69.1% weighted-average combined LTV, following May's $407 million ADMT 2026-NQM4 and bringing AD Mortgage's year-to-date non-QM issuance to roughly $1.7 billion.''',
         why="Five deals in roughly seven months, at a pace nearing one per quarter, from a single repeat mid-sized shelf issuer indicates the non-QM securitization market has normalized into an established, programmatic funding channel rather than remaining an opportunistic, one-off financing tool &mdash; programmatic issuers plan origination volume around a known securitization cadence, which is a materially more stable funding model than issuers who securitize only when market conditions happen to align.",
         implications=[
             "Confirms non-QM securitization has matured into programmatic, roughly quarterly issuance for repeat shelf issuers",
             "Brings AD Mortgage's 2026 non-QM issuance to roughly $1.7 billion year-to-date across five deals",
             "Signals investor demand deep enough to absorb near-quarterly issuance from a single mid-sized originator",
             "Provides a strong FICO (754) and LTV (69.1%) collateral benchmark for comparable non-QM shelf deals",
         ],
         watch="Whether AD Mortgage maintains this roughly-quarterly pace into Q4 2026, and early delinquency data on ADMT 2026-NQM5 as the pool seasons."),
    dict(category="Non-Agency RMBS", title="KBRA Rates $490.6M Blended Non-Prime RMBS Deal for Aspire Mortgage",
         subtitle="Blending QM-Exempt and Non-QM Collateral Keeps Programmatic Issuance Flowing",
         trigger=f'''{src("https://finance.yahoo.com/real-estate/articles/kbra-assigns-preliminary-ratings-aspire-200300095.html", "KBRA assigned preliminary ratings on July 20 to Aspire Mortgage Trust 2026-4")}, a $490.6 million non-prime RMBS deal backed by 1,070 loans across ten rated certificate classes; the pool is 99% fixed-rate, with 49.1% Safe Harbor QM, 1.9% Rebuttable Presumption QM, 14.5% Non-QM, and 34.5% exempt from the ATR/QM rule.''',
         why="Blending QM-exempt and non-QM loan types within a single non-prime shelf, rather than issuing a pure non-QM pool, is a structural choice that lets issuers keep programmatic issuance flowing even as any single collateral category's origination volume fluctuates &mdash; a mixed pool gives the issuer more loans to draw from each quarter, which matters for maintaining a steady securitization cadence rather than waiting to accumulate enough of one specific loan type.",
         implications=[
             "Shows issuers blending loan types specifically to sustain programmatic issuance cadence",
             "Signals underwriting boxes are widening as issuers combine QM-exempt and non-QM collateral in one pool",
             "Adds a second large non-prime RMBS print in July alongside AD Mortgage's NQM5, deepening market supply",
             "Provides a blended-collateral structural template other non-prime shelf issuers may adopt",
         ],
         watch="How rating agencies price blended QM-exempt/non-QM pools relative to pure non-QM shelves over time, and early performance data on this specific pool."),
    dict(category="CMBS SASB", title="Starwood Prices $482.5M Single-Family Rental Securitization, Its Fifth",
         subtitle="Repeat Institutional SFR Issuance Confirms a Durable, Financeable Asset Class",
         trigger=f'''{src("https://www.businesswire.com/news/home/20260715232837/en/KBRA-Assigns-Preliminary-Ratings-to-STAR-2026-SFR8", "KBRA assigned preliminary ratings on July 15 to Starwood's STAR 2026-SFR8")}, a single-borrower single-family-rental securitization backed by one $482.5 million floating-rate loan secured by 1,749 properties (1,756 units) across ten states, with Atlanta, Phoenix, and Charlotte as the top three markets; aggregate broker price opinion value is $651.7 million, producing a nominal loan-to-value of 74.0% and a KBRA-adjusted LTV of 77.1%.''',
         why="A fifth KBRA-rated SFR securitization from the same institutional sponsor confirms single-family rental has become a durable, repeat-financeable asset class within the SASB market, not a one-time structural experiment &mdash; and that durability matters specifically because it's happening even as more conventional office and retail CMBS collateral faces elevated distress, showing capital markets access for institutional SFR ownership hasn't followed the broader CMBS credit story downward.",
         implications=[
             "Confirms institutional single-family rental ownership remains durably financeable via repeat securitization",
             "Signals SFR capital markets access is holding up even as conventional office and retail CMBS face distress",
             "Concentrates collateral risk in Sunbelt growth markets (Atlanta, Phoenix, Charlotte) specifically",
             "Provides a fifth data point on Starwood's SFR program pricing and structure for comparable sponsors",
         ],
         watch="Whether other institutional SFR operators follow with comparable repeat securitizations, and regional rent performance across the ten states in the collateral pool."),
    dict(category="Rating Action", title="CMBS Delinquency Rate Falls to 7.35%, but Office, Retail, and Multifamily All Worsen",
         subtitle="An Improving Headline Number Driven Entirely by Lodging Masks a Bifurcating Market",
         trigger=f'''{src("https://newslink.mba.org/mba-newslinks/2026/july/trepp-cmbs-delinquency-rate-falls-in-june/", "Trepp reported the overall CMBS delinquency rate fell 20 basis points to 7.35% in June")}, published July 8, versus 7.13% a year earlier; by property type, office delinquency rose 4bps to 11.57%, retail rose 30bps to 6.91%, and multifamily rose 28bps to 7.23%, while lodging fell 79bps to 5.22% &mdash; the primary driver of the headline improvement. Including performing matured balloons, the effective rate would be 9.53%, up 36bps from May.''',
         why="A headline delinquency rate improving almost entirely because of one property type (lodging), while office, retail, and multifamily all simultaneously worsen, means the aggregate number is actively masking a bifurcating credit story rather than describing a broadly healthy market &mdash; anyone pricing or rating a conduit bond needs the property-type breakdown, not the headline figure, since a pool's AAA cushion depends heavily on which property types sit inside it. The 9.53% effective rate including performing matured balloons is also meaningfully worse than the reported 7.35%, since those loans are current on interest but haven't actually repaid principal at maturity.",
         implications=[
             "Shows the headline delinquency improvement is a lodging-specific story, not a broad-based credit recovery",
             "Confirms office, retail, and multifamily CMBS delinquencies all worsened in the same month",
             "Reveals a meaningfully worse 9.53% effective rate once performing matured balloons are included",
             "Requires investors to underwrite pools by property-type composition, not the aggregate headline number",
         ],
         watch="Whether office and retail delinquency trends continue worsening into Q3, and how the performing-matured-balloon share evolves as more loans hit maturity."),
]

SECURITIZED_FINAL_PARAGRAPHS = [
    "This is the first real issue of Securitized Signal, carved out specifically to cover non-agency RMBS and CMBS as their own vertical, distinct from Structured Signal's focus on CLOs and consumer ABS. The Citi conduit deal is a useful example of why that split matters: it's a genuinely national capital-markets pricing story, not a market-specific lending story, which is exactly the kind of signal this desk exists to carry instead of forcing it into a location-specific RE Debt Signal market.",
    "The Nomura and Citi deals this week describe CMBS pricing from two different angles &mdash; a sponsor switching away from agency debt for the first time, and a bank's own top-market rankings revealing where its origination pipeline is deepest. Both are real, capital-backed reads on where CMBS demand currently sits, at a moment when SASB deals dominate private-label issuance.",
    "The Trepp delinquency data is this issue's most important structural point: a headline number improving almost entirely because of lodging, while office, retail, and multifamily all worsen in the same month, is a bifurcating credit story hiding inside an aggregate figure. That distinction matters more than the headline every time a conduit pool's property-type mix gets underwritten.",
]
SECURITIZED_FINAL_BULLETS = [
    "This desk covers RMBS and CMBS specifically, distinct from Structured Signal's CLO and consumer ABS coverage",
    "A sponsor's first-ever CMBS execution and a bank's record conduit deal both show real capital-backed CMBS demand",
    "Institutional single-family rental securitization keeps clearing the market even as conventional CMBS faces distress",
    "A falling headline CMBS delinquency rate is masking worsening office, retail, and multifamily credit underneath it",
]

SECURITIZED_PAGE = issue_page(
    "securitized", False, "Securitized", "Signal", "NEW YORK, NY", "JULY 29, 2026", "JULY 7&ndash;28, 2026",
    SECURITIZED_SNAPSHOT, "What Happened", SECURITIZED_SIGNALS, SECURITIZED_FINAL_PARAGRAPHS, SECURITIZED_FINAL_BULLETS,
    "No predictions. No stock references. Pool-anchored interpretation only.",
)


print("Structured page OK", len(STRUCTURED_PAGE))

# ============================================================== HOME PAGE ==============================================================

def desk_card(page_id, name_a, name_b, desc, meta, whatis_label):
    return f'''  <div class="desk-card">
    <a class="desk-card-link" href="#/{page_id}">
      <div class="desk-row-top">
        <p class="desk-card-name"><span class="cre">{name_a}</span><span class="signal">{name_b}</span></p>
        <span class="desk-card-arrow">&rarr;</span>
      </div>
      <div class="desk-row-bottom">
        <p class="desk-card-desc">{desc}</p>
        <span class="desk-card-meta">{meta}</span>
      </div>
    </a>
    <a class="desk-card-whatis" href="#/about/{page_id}">What is {whatis_label}? &rarr;</a>
  </div>'''

# ============================================================== ABOUT / EXPLAINER PAGES ==============================================================

ABOUT_SWITCHER_ITEMS = [
    ("cre", "CRE"),
    ("ib", "IB"),
    ("credit", "Credit"),
    ("redebt", "RE Debt"),
    ("structured", "Structured"),
    ("securitized", "Securitized"),
]

def about_switcher_html(active_id):
    links = []
    for aid, label in ABOUT_SWITCHER_ITEMS:
        cls = " active" if aid == active_id else ""
        links.append(f'      <a class="about-switch-link{cls}" data-about-id="{aid}" href="#/about/{aid}">{label}</a>')
    return NEWLINE.join(links)

def about_block_html(desk_id, active, title, subtitle, paragraphs, terms, back_href, back_label):
    active_cls = " active" if active else ""
    paras = NEWLINE.join(f"    <p>{p}</p>" for p in paragraphs)
    term_items = NEWLINE.join(f"      <li><span class=\"about-term\">{t}</span> {d}</li>" for t, d in terms)
    return f'''<div id="market-about-{desk_id}" class="market{active_cls}">
  <p class="eyebrow">What Is It?</p>
  <h1 class="about-title">{title}</h1>
  <p class="about-subtitle">{subtitle}</p>
{paras}
  <div class="about-terms">
    <p class="about-terms-label">Key terms to know</p>
    <ul>
{term_items}
    </ul>
  </div>
  <a class="about-back" href="#/{back_href}">&larr; Back to {back_label}</a>
</div>'''

ABOUT_CRE = about_block_html(
    "cre", True,
    "What Is Commercial Real Estate?",
    "The business of property that isn't a single family's home.",
    [
        "Commercial real estate (CRE) covers property used for business purposes rather than housing one family &mdash; office towers, apartment complexes, warehouses, retail centers, and hotels. Even apartment buildings count as \"commercial\" once they're owned as an income-producing asset rather than a single home.",
        "The core idea: a piece of land can be worth wildly different amounts depending on what's built on it and who wants to occupy it. CRE is the business of finding that gap &mdash; buying, developing, leasing, or repositioning a property for more than it cost, or advising someone else through that process.",
        "Recruiting into CRE usually means one of three paths: development (building new projects), brokerage (finding tenants or buyers), or asset/property management (running buildings day to day). The debt and capital-markets side of the same industry is covered separately in RE Debt Signal.",
    ],
    [
        ("Cap rate", "&mdash; a property's annual income divided by its price; the quick way investors compare deals."),
        ("NOI", "&mdash; net operating income, a property's income after operating expenses but before debt payments."),
        ("Submarket", "&mdash; a specific neighborhood or corridor within a larger metro, since pricing and demand vary block by block."),
        ("Entitlement", "&mdash; the government approvals a developer needs before construction can legally begin."),
    ],
    "cre", "CRE Signal",
)

ABOUT_IB = about_block_html(
    "ib", False,
    "What Is Investment Banking?",
    "Advising companies on their biggest, highest-stakes financial decisions.",
    [
        "Investment banks advise companies on major financial decisions: buying another company (M&amp;A), raising money by selling stock (equity capital markets) or bonds (debt capital markets), or restructuring debt when a company is in financial trouble.",
        "These decisions are high-stakes and infrequent for any single company, so companies pay banks a fee to run the process, find the right counterparties or investors, and negotiate the best terms &mdash; expertise most companies don't need often enough to build in-house.",
        "Analysts and associates build the financial models and prep the pitch materials; managing directors run the client relationships and win the mandates that bring in the work.",
    ],
    [
        ("M&amp;A", "&mdash; mergers and acquisitions; one company buying, merging with, or selling to another."),
        ("ECM / DCM", "&mdash; equity and debt capital markets; the teams that help companies raise money by selling stock or bonds."),
        ("Sell-side / buy-side", "&mdash; sell-side advises the company doing a deal; buy-side represents the investors putting up capital."),
        ("Mandate", "&mdash; the formal engagement where a company hires a specific bank to run a specific deal."),
    ],
    "ib", "IB Signal",
)

ABOUT_CREDIT = about_block_html(
    "credit", False,
    "What Is Private Credit?",
    "Lending directly to companies, outside the banking system.",
    [
        "Instead of a company borrowing from a bank or issuing public bonds, private credit funds lend directly to companies &mdash; often ones owned by private equity firms &mdash; using money raised from institutional investors like pension funds and insurers.",
        "It's one of the fastest-growing corners of finance because banks pulled back from riskier corporate lending after tighter regulation following the 2008 financial crisis, and private credit funds stepped in to fill that gap with more flexible, custom-negotiated loans.",
        "Credit analysts underwrite a borrower's ability to repay, similar to a bank loan officer, but usually for larger, more complex deals with fewer regulatory constraints than a traditional bank loan.",
    ],
    [
        ("BDC", "&mdash; business development company; a publicly traded vehicle that pools capital to make these loans."),
        ("Direct lending", "&mdash; a fund lending straight to a borrower, without a bank arranging or syndicating the loan."),
        ("Unitranche", "&mdash; a single blended loan that combines what would otherwise be separate senior and subordinated debt."),
        ("Covenant", "&mdash; a condition in a loan agreement the borrower must maintain, like a minimum cash flow level."),
    ],
    "credit", "Credit Signal",
)

ABOUT_REDEBT = about_block_html(
    "redebt", False,
    "What Is Commercial Real Estate Debt?",
    "Every property needs a loan behind it &mdash; this is that loan, examined closely.",
    [
        "Every CRE project needs a loan behind it, just like a house needs a mortgage. RE Debt Signal covers that loan side specifically: who's lending, on what terms, and what happens when a loan runs into trouble.",
        "A property's owner and its lender have very different risk exposure &mdash; the lender gets paid first but doesn't share in the upside if the property does well, so lenders underwrite a deal completely differently than an equity investor does. That difference is what makes CRE debt its own specialized career path, distinct from the development or brokerage side covered in CRE Signal.",
        "Loan originators at banks and debt funds underwrite and price new loans; special servicers step in specifically when an existing loan is in distress and needs a workout.",
    ],
    [
        ("LTV", "&mdash; loan-to-value; the loan amount as a percentage of the property's value, a core risk measure."),
        ("Debt yield", "&mdash; a property's income divided by the loan amount, used to judge how much cushion a lender has."),
        ("Special servicing", "&mdash; the process a troubled loan enters so a specialist can manage a workout, sale, or foreclosure."),
        ("Mezzanine debt", "&mdash; a second layer of debt that sits between the senior loan and the equity, higher risk and higher rate."),
    ],
    "redebt", "RE Debt Signal",
)

ABOUT_STRUCTURED = about_block_html(
    "structured", False,
    "What Is Structured Finance?",
    "Pooling loans together, then slicing that pool into new securities.",
    [
        "Structured finance takes a pool of loans &mdash; corporate loans, auto loans, credit card debt &mdash; and repackages them into new securities that get sold off in slices, called tranches, each with a different risk and return level.",
        "Pooling and slicing risk lets a lender turn loans it's already made into cash it can lend out again, and lets investors buy exactly the risk level they want, instead of owning any single underlying loan outright.",
        "Structuring bankers design these deals and negotiate the tranche terms; portfolio managers at CLO managers select which loans actually go into the pool and manage it over time.",
    ],
    [
        ("CLO", "&mdash; collateralized loan obligation; a pool of corporate loans repackaged into tranches of bonds."),
        ("Tranche", "&mdash; one slice of a structured deal's capital stack, ranked by which slice absorbs losses first."),
        ("ABS", "&mdash; asset-backed security; a bond backed by a pool of loans other than mortgages, like auto or credit card debt."),
        ("Equity tranche", "&mdash; the riskiest, first-loss slice of a deal, which also captures the most upside if it performs well."),
    ],
    "structured", "Structured Signal",
)

ABOUT_SECURITIZED = about_block_html(
    "securitized", False,
    "What Is Mortgage Securitization?",
    "The same pooling-and-slicing idea as Structured Signal, but for mortgages specifically.",
    [
        "Securitized Signal covers the same pooling-and-slicing idea as structured finance, but applied specifically to mortgages: RMBS bundles residential mortgages, CMBS bundles commercial mortgages, and both get sold to bond investors in tranches.",
        "It's treated as its own specialty rather than folded into CLOs and corporate ABS because mortgage securitization has its own collateral type, investor base, and risk drivers &mdash; property values and occupancy, not corporate credit quality.",
        "Conduit lenders originate mortgages specifically to sell into these pools; rating agencies and investors analyze the underlying loan-level data on every property in the pool to price each tranche.",
    ],
    [
        ("CMBS conduit", "&mdash; a pool of many commercial mortgages from different properties, bundled into one deal."),
        ("SASB", "&mdash; single-asset, single-borrower; a CMBS deal backed by just one property instead of a diversified pool."),
        ("Credit enhancement", "&mdash; the cushion of subordinate bonds that absorbs losses before a senior tranche takes a hit."),
        ("Re-REMIC", "&mdash; a re-securitization that repackages existing mortgage bonds into a new set of tranches."),
    ],
    "securitized", "Securitized Signal",
)

ABOUT_PAGE = f'''<section id="page-about" class="page">
<div class="issue about">
  <p class="eyebrow">What Is It?</p>
  <h1 class="about-page-title brand-word"><span class="cre">Market</span><span class="signal">Signal</span> Explainers</h1>
  <p class="about-page-lede">Short, plain-English primers on each industry this newsletter covers &mdash; read one before diving into that desk's signals if the vocabulary is new to you.</p>
  <div class="about-switcher">
{about_switcher_html("cre")}
  </div>
{ABOUT_CRE}
{ABOUT_IB}
{ABOUT_CREDIT}
{ABOUT_REDEBT}
{ABOUT_STRUCTURED}
{ABOUT_SECURITIZED}
</div>
</section>'''

print("About page OK", len(ABOUT_PAGE))

HOME_PAGE = f'''<section id="page-home" class="page active">
<div class="issue home">
  <div class="home-hero">
    <p class="eyebrow">Weekly Intelligence, By Desk</p>
    <h1 class="home-title brand-word"><span class="cre">Market</span><span class="signal">Signal</span></h1>
    <div class="accent-rule"></div>
    <p class="home-lede">Market Signal is weekly market intelligence for students recruiting into finance &mdash; six desks, each read closely enough to explain why a deal matters, not just that it happened. Follow your target desk for real fluency in interviews; follow the rest so no adjacent-industry question catches you flat-footed. No predictions. No stock references. Every signal is anchored to something that actually happened &mdash; never commentary floating free of one.</p>
  </div>

  <p class="eyebrow">The Desks</p>
  <div class="desk-grid">
{desk_card("cre", "CRE", "Signal",
           "Commercial real estate signals across multiple university markets nationwide.",
           "Latest: Jul 29, 2026", "CRE")}
{desk_card("ib", "IB", "Signal",
           "M&amp;A, capital markets, sponsor finance, and restructuring signals.",
           "Latest: Jul 29, 2026", "IB")}
{desk_card("credit", "Credit", "Signal",
           "Direct lending, BDCs, and private credit signals.",
           "Latest: Jul 29, 2026", "Private Credit")}
{desk_card("redebt", "RE Debt", "Signal",
           "Construction, bridge, agency, and CMBS lending signals.",
           "Latest: Jul 29, 2026", "RE Debt")}
{desk_card("structured", "Structured", "Signal",
           "CLOs, ABS, and securitized credit signals.",
           "Latest: Jul 29, 2026", "Structured Finance")}
{desk_card("securitized", "Securitized", "Signal",
           "Non-agency RMBS and CMBS signals.",
           "Latest: Jul 29, 2026", "Securitized Products")}
  </div>

  <footer>
    <span class="footer-wordmark brand-word"><span class="cre">Market</span><span class="signal">Signal</span></span>
    <span class="tagline">No predictions. No stock references. Anchored interpretation only.</span>
  </footer>
</div>
</section>'''

print("Home page OK", len(HOME_PAGE))

# ============================================================== NAV + SCRIPTS ==============================================================

NAV = '''<nav class="topnav">
  <a class="topnav-brand" href="#/home">
    <svg class="brand-mark" viewBox="0 0 22 22" width="26" height="26" xmlns="http://www.w3.org/2000/svg">
      <rect class="bm-bar" x="0.5" y="14" width="3.2" height="7" rx="1"></rect>
      <rect class="bm-bar" x="6.2" y="10" width="3.2" height="11" rx="1"></rect>
      <rect class="bm-bar" x="11.9" y="6" width="3.2" height="15" rx="1"></rect>
      <rect class="bm-bar" x="17.6" y="2" width="3.2" height="19" rx="1"></rect>
      <path class="bm-line" d="M2 16.5 L7.8 11.5 L13.5 7.5 L19 3.2"></path>
      <circle class="bm-dot" cx="19" cy="3.2" r="2.1"></circle>
    </svg>
    <span class="brand-word"><span class="cre">Market</span><span class="signal">Signal</span></span>
  </a>
  <div class="topnav-links">
    <a href="#/home" data-nav="home">Home</a>
    <a href="#/cre" data-nav="cre">CRE</a>
    <a href="#/ib" data-nav="ib">IB</a>
    <a href="#/credit" data-nav="credit">Credit</a>
    <a href="#/redebt" data-nav="redebt">RE Debt</a>
    <a href="#/structured" data-nav="structured">Structured</a>
    <a href="#/securitized" data-nav="securitized">Securitized</a>
  </div>
  <button type="button" id="theme-toggle" class="theme-toggle" onclick="window.__toggleCreSignalTheme()" aria-label="Switch color theme" title="Switch color theme">
    <svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><circle cx="12" cy="12" r="4"></circle><path d="M12 2.5v2.5M12 19v2.5M4.6 4.6l1.8 1.8M17.6 17.6l1.8 1.8M2 12h2.5M19.5 12H22M4.6 19.4l1.8-1.8M17.6 6.4l1.8-1.8"></path></svg>
    <svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M20 14.3A8.2 8.2 0 1 1 9.7 4a6.8 6.8 0 0 0 10.3 10.3Z"></path></svg>
  </button>
</nav>'''

THEME_SCRIPT = '''<script>
(function(){
  var KEY = "cre-signal-theme";
  var root = document.documentElement;
  function stored(){ try { return localStorage.getItem(KEY); } catch(e){ return null; } }
  function systemPref(){ return (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches) ? "dark" : "light"; }
  function current(){ var s = stored(); return (s === "light" || s === "dark") ? s : systemPref(); }
  function reflect(theme){
    root.setAttribute("data-theme", theme);
    var btn = document.getElementById("theme-toggle");
    if (btn) btn.setAttribute("data-current", theme);
  }
  window.__toggleCreSignalTheme = function(){
    var next = current() === "dark" ? "light" : "dark";
    try { localStorage.setItem(KEY, next); } catch(e){}
    reflect(next);
  };
  reflect(current());
})();
</script>'''

ROUTER_SCRIPT = '''<script>
(function(){
  var PAGES = ["home","cre","ib","credit","redebt","structured","securitized","about"];
  var MARKETS = {
    cre: ["austin","usc","nyu","uga","uf"],
    redebt: ["austin","usc","nyu","uga","uf"],
    about: ["cre","ib","credit","redebt","structured","securitized"]
  };
  function parseHash(){
    var h = location.hash.replace(/^#\\/?/, "");
    var parts = h.split("/");
    var page = PAGES.indexOf(parts[0]) !== -1 ? parts[0] : "home";
    var market = parts[1] || null;
    return {page: page, market: market};
  }
  function render(){
    var state = parseHash();
    for (var i = 0; i < PAGES.length; i++){
      var el = document.getElementById("page-" + PAGES[i]);
      if (el) el.classList.toggle("active", PAGES[i] === state.page);
    }
    var links = document.querySelectorAll(".topnav-links a");
    for (var j = 0; j < links.length; j++){
      links[j].classList.toggle("active", links[j].getAttribute("data-nav") === state.page);
    }
    var markets = MARKETS[state.page];
    if (markets){
      var market = (state.market && markets.indexOf(state.market) !== -1) ? state.market : markets[0];
      for (var k = 0; k < markets.length; k++){
        var mel = document.getElementById("market-" + state.page + "-" + markets[k]);
        if (mel) mel.classList.toggle("active", markets[k] === market);
      }
      var select = document.querySelector('.market-select[data-desk="' + state.page + '"]');
      if (select) select.value = market;
      var subLinks = document.querySelectorAll('[data-about-id]');
      for (var s = 0; s < subLinks.length; s++){
        subLinks[s].classList.toggle("active", subLinks[s].getAttribute("data-about-id") === market);
      }
    }
    window.scrollTo(0, 0);
  }
  window.__setMarket = function(desk, market){
    location.hash = "#/" + desk + "/" + market;
  };
  window.addEventListener("hashchange", render);
  render();
})();
</script>'''

FILTER_SCRIPT = '''<script>
window.__filterSignals = function(el){
  var bar = el.closest(".filter-bar");
  if (!bar) return;
  var scope = bar.closest(".market") || bar.closest(".issue");
  if (!scope) return;
  if (el.classList && el.classList.contains("filter-chip")){
    var chips = bar.querySelectorAll(".filter-chip");
    for (var i = 0; i < chips.length; i++){ chips[i].classList.remove("active"); }
    el.classList.add("active");
  }
  var activeChip = bar.querySelector(".filter-chip.active");
  var category = activeChip ? activeChip.getAttribute("data-filter-cat") : "all";
  var searchInput = bar.querySelector(".filter-search");
  var keyword = searchInput ? searchInput.value.trim().toLowerCase() : "";

  var cards = scope.querySelectorAll(".signal-card");
  for (var j = 0; j < cards.length; j++){
    var card = cards[j];
    var cat = card.getAttribute("data-category");
    var matchCat = (category === "all") || (cat === category);
    var text = card.textContent.toLowerCase();
    var matchKw = !keyword || text.indexOf(keyword) !== -1;
    card.style.display = (matchCat && matchKw) ? "" : "none";
  }
  var dividers = scope.querySelectorAll(".asset-class");
  for (var k = 0; k < dividers.length; k++){
    var div = dividers[k];
    var sib = div.nextElementSibling;
    var anyVisible = false;
    while (sib && !sib.classList.contains("asset-class")){
      if (sib.classList.contains("signal-card") && sib.style.display !== "none"){ anyVisible = true; break; }
      sib = sib.nextElementSibling;
    }
    div.style.display = anyVisible ? "" : "none";
  }
};
</script>'''

# ============================================================== ASSEMBLE ==============================================================

BODY = NEWLINE.join([
    NAV,
    THEME_SCRIPT,
    HOME_PAGE,
    CRE_PAGE,
    IB_PAGE,
    CREDIT_PAGE,
    REDEBT_PAGE,
    STRUCTURED_PAGE,
    SECURITIZED_PAGE,
    ABOUT_PAGE,
    FILTER_SCRIPT,
    ROUTER_SCRIPT,
])

FRAGMENT = "<style>" + NEWLINE + fonts_css + NEWLINE + CSS + NEWLINE + "</style>" + NEWLINE + BODY

html = NEWLINE.join([
    "<!DOCTYPE html>",
    "<html lang=\"en\">",
    "<head>",
    "<meta charset=\"UTF-8\">",
    "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">",
    "<title>Market Signal</title>",
    "</head>",
    "<body>",
    FRAGMENT,
    "</body>",
    "</html>",
])

out_path = pathlib.Path("/Users/milesnevins/Downloads/files/signal-site.html")
out_path.write_text(html)
print("wrote", out_path, len(html), "bytes")
