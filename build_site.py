import pathlib

scratch = pathlib.Path(__file__).parent
fonts_css = (scratch / "embedded-fonts.css").read_text()
NEWLINE = chr(10)
WHATIS_LABELS = {
    "cre": "CRE",
    "repe": "REPE",
    "redebt": "RE Debt",
    "ib": "IB",
    "credit": "Private Credit",
    "structured": "Structured Finance",
    "securitized": "Securitized Products",
}

# ============================================================== CSS ==============================================================
CSS = """
:root{
  --bg:#f5f3ee;
  --fg:#1a1a18;
  --rule:#d9d4c8;
  --rule-strong:#1a1a18;
  --accent:#1C8FCC;
  --accent-glow:rgba(28,143,204,.28);
  --accent-wash:rgba(28,143,204,.08);
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
    --accent:#6EC6FA;
    --accent-glow:rgba(110,198,250,.30);
    --accent-wash:rgba(110,198,250,.10);
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
  --accent:#6EC6FA;
  --accent-glow:rgba(110,198,250,.30);
  --accent-wash:rgba(110,198,250,.10);
  --muted:#a59c8a;
  --rising:#5aa574;
  --stable:#93a0b3;
}
:root[data-theme="light"]{
  --bg:#f5f3ee;
  --fg:#1a1a18;
  --rule:#d9d4c8;
  --rule-strong:#1a1a18;
  --accent:#1C8FCC;
  --accent-glow:rgba(28,143,204,.28);
  --accent-wash:rgba(28,143,204,.08);
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

/* ---------- settings button + panel ---------- */
.settings-picker{position:relative;flex-shrink:0;}
.settings-btn{
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
  transition:color .15s ease, border-color .15s ease;
}
.settings-btn:hover{color:var(--fg);border-color:var(--muted);}
.settings-btn:focus-visible{outline:1px solid var(--accent);outline-offset:2px;}
.settings-btn svg{width:15px;height:15px;}
.settings-menu{
  position:absolute;
  top:calc(100% + 10px);
  right:0;
  display:none;
  flex-direction:column;
  gap:16px;
  padding:18px;
  min-width:230px;
  background:var(--bg);
  border:1px solid var(--rule);
  border-radius:14px;
  box-shadow:0 14px 34px -14px rgba(0,0,0,.35);
  z-index:950;
}
.settings-menu.open{display:flex;}
.settings-section-label{
  font-family:var(--font-mono);
  font-size:10px;
  letter-spacing:0.08em;
  text-transform:uppercase;
  color:var(--muted);
  margin:0;
}
.settings-row{display:flex;flex-direction:column;gap:9px;}
.settings-row-label{font-size:11.5px;color:var(--muted);}
.theme-segmented{display:flex;border:1px solid var(--rule);border-radius:999px;padding:2px;gap:2px;}
.theme-seg-btn{
  flex:1;
  padding:6px 0;
  font-family:var(--font-mono);
  font-size:10.5px;
  text-transform:uppercase;
  letter-spacing:0.04em;
  background:transparent;
  border:none;
  border-radius:999px;
  color:var(--muted);
  cursor:pointer;
  transition:background .15s ease, color .15s ease;
}
.theme-seg-btn.active{background:var(--accent-wash);color:var(--accent);}

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
.masthead-name{display:flex;flex-direction:column;gap:7px;}
.masthead-whatis{
  font-family:var(--font-mono);
  font-size:10px;
  letter-spacing:0.03em;
  color:var(--muted);
  text-decoration:none;
  transition:color .15s ease;
}
.masthead-whatis:hover{color:var(--accent);}

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
  margin:0 0 10px;
  max-width:46ch;
}
.signal-date{
  font-family:var(--font-mono);
  font-size:10.5px;
  letter-spacing:0.05em;
  text-transform:uppercase;
  color:var(--muted);
  margin:0 0 22px;
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
.subscribe-form{
  display:flex;
  gap:10px;
  max-width:420px;
  margin-top:8px;
}
.subscribe-input{
  flex:1;
  min-width:0;
  padding:11px 16px;
  font-family:var(--font-body);
  font-size:14px;
  color:var(--fg);
  background:var(--bg);
  border:1px solid var(--rule);
  border-radius:999px;
  outline:none;
  transition:border-color .15s ease;
}
.subscribe-input::placeholder{color:var(--muted);}
.subscribe-input:focus{border-color:var(--accent);}
.subscribe-btn{
  flex-shrink:0;
  padding:11px 20px;
  font-family:var(--font-mono);
  font-size:12px;
  letter-spacing:0.03em;
  color:var(--bg);
  background:var(--accent);
  border:none;
  border-radius:999px;
  cursor:pointer;
  transition:opacity .15s ease;
}
.subscribe-btn:hover{opacity:0.85;}
@media (max-width:560px){
  .subscribe-form{flex-direction:column;max-width:none;}
}

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
        date_html = f'<p class="signal-date">{s["date"]}</p>' if s.get("date") else ""
        out.append(f'''  <div class="signal-card" data-category="{s["category"]}">
    <h3 class="signal-title">{s["title"]}</h3>
    <p class="signal-subtitle">{s["subtitle"]}</p>
    {date_html}
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


def masthead_html(name_a, name_b, dateline, drop, coverage, page_id=None):
    whatis = ""
    if page_id and page_id in WHATIS_LABELS:
        whatis = f'<a class="masthead-whatis" href="#/about/{page_id}">What is {WHATIS_LABELS[page_id]}? &rarr;</a>'
    return f'''  <div class="masthead">
    <div class="masthead-name">
      <p class="wordmark"><span class="cre">{name_a}</span><span class="signal">{name_b}</span></p>
      {whatis}
    </div>
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
{masthead_html(name_a, name_b, dateline, drop, coverage, page_id)}
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
{masthead_html(name_a, name_b, dateline, drop, coverage, page_id)}
  <p class="key-line" style="margin:-32px 0 0;">{coming_soon}</p>
</div>'''
    notice = ""
    if sample_notice:
        notice = f'<p class="key-line" style="margin:-32px 0 52px;">{sample_notice}</p>'
    return f'''<div id="market-{page_id}-{market_id}" class="market{active_cls}">
{masthead_html(name_a, name_b, dateline, drop, coverage, page_id)}
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
         date="July 23, 2026",
         trigger=f'''Austin officials confirmed that {src("https://www.kut.org/austin/2026-07-21/secrets-out-amazon-is-the-company-behind-austins-fast-tracked-dogs-head-project", "Amazon's robotics division is the previously unnamed tenant")} behind the roughly 2,600-acre &ldquo;Dog's Head&rdquo; site along the Colorado River in Southeast Austin, and on July 23 {src("https://austincurrent.org/2026/07/23/dogshead-austin-texas-development/", "the Austin City Council voted 7-3 to approve Tax Increment Reinvestment Zone financing")} for the site, with developer Endeavor projecting roughly $3.5 billion in property tax revenue over 30 years to fund infrastructure covering up to 12,000 homes and 4 million square feet of industrial space.''',
         why="A TIRZ vote is a bet the city is willing to make with its own future tax revenue, not just a rezoning approval &mdash; the city is committing to fund infrastructure against tax increment that only materializes if the development actually gets built and leases up as projected. That the anchor tenant turned out to be Amazon's robotics division, rather than a speculative logistics user, changes the credit quality of that bet: a name-brand corporate tenant with disclosed job commitments is a very different anchor than an unnamed spec building. The 1,478-to-645 public sign-up split ahead of the vote also shows this was a genuinely contested approval, not a rubber stamp.",
         implications=[
             "Commits city tax revenue to infrastructure years before the site fully leases up",
             "Establishes Southeast Austin's Colorado River corridor as a new large-scale industrial and mixed-use submarket",
             "Sets a scale precedent for how large a single anchor-tenant deal can move a TIRZ vote",
             "Leaves a pending council vote on the site's regulating plan and development standards still to come",
         ],
         watch="Whether Amazon's disclosed job commitments materialize on the timeline implied by the TIRZ financing, and the outcome of the still-pending council vote on the site's regulating plan."),
    dict(category="Industrial", title="Link Logistics Buys Fully-Leased Round Rock Industrial Building",
         subtitle="A Major Logistics REIT Is Still Buying Small-Bay Austin Industrial, Even With Vacancy Elevated",
         date="July 29, 2026",
         trigger=f'''{src("https://irei.com/news/link-logistics-acquires-fully-leased-texas-industrial-portfolio-in-dallas-and-austin/", "Link Logistics acquired a fully-leased, two-building industrial portfolio spanning Round Rock and Coppell, Texas")}, with the Austin piece a 61,111-square-foot building at 2401 Double Creek Drive in Round Rock; purchase price was not disclosed.''',
         why="A major logistics REIT buying a small-bay, fully-leased infill building in a supply-constrained Austin suburb, even as metro-wide industrial vacancy sits elevated, is a specific bet that submarket-level fundamentals in Round Rock still justify acquisition pricing that the broader Austin industrial market wouldn't support today. That distinction &mdash; buying occupied, infill product rather than speculative big-box space &mdash; is a different industrial thesis than the Amazon or prior Tesla-scale leases this desk has tracked.",
         implications=[
             "Confirms institutional industrial buyers still see value in fully-leased, infill Austin-suburb product",
             "Signals Round Rock specifically remains a supply-constrained submarket despite metro-wide vacancy pressure",
             "Provides a counter-signal to broader \"industrial oversupply\" narratives circulating this cycle",
             "Adds a second major logistics player (alongside Amazon) actively deploying capital in the Austin metro",
         ],
         watch="Whether Link Logistics discloses the purchase price, and if the REIT pursues additional infill acquisitions in the Round Rock or broader Austin-suburb submarkets."),
    dict(category="Office", title="Apollo Global Management Selects Austin as Second U.S. Headquarters",
         subtitle="An $800B Manager Anchoring HQ2 Here Is a Corporate-Relocation Signal Years Ahead of Any Lease",
         date="August 3, 2026",
         trigger=f'''{src("https://finance.yahoo.com/technology/articles/apollo-selects-austin-strategic-hub-131500562.html", "Apollo Global Management announced it has selected Austin as its second U.S. headquarters")}, a hub the roughly $800 billion alternative asset manager says will be built around innovation, emerging technology, and its retirement solutions platform; Apollo said Austin already represents one of its top five capital bases after nearly two decades of existing partnerships in the market. Specific office square footage, address, and headcount were not disclosed.''',
         why="A manager of Apollo's scale anchoring a second U.S. headquarters, rather than simply expanding an existing office, is a corporate-relocation signal that typically precedes real estate absorption by months or years &mdash; the actual lease or build announcement, and the high-wage jobs that come with it, still has to follow. That Apollo frames Austin as already one of its top five capital bases suggests this is a formalization of existing depth in the market, not a speculative bet on an unproven relationship.",
         implications=[
             "Signals a major high-wage corporate anchor is coming to Austin before any specific office real estate is announced",
             "Adds Apollo to the list of large financial and technology firms treating Austin as a genuine second hub, not a satellite office",
             "Creates a specific, named tenant to watch for the eventual real estate follow-through (lease size, submarket, timeline)",
             "Reinforces Austin's positioning for high-wage financial-services job growth alongside its existing tech-sector base",
         ],
         watch="The follow-up real estate announcement disclosing office size, submarket, and headcount, which typically lags a headquarters announcement like this by weeks to months."),
    dict(category="Office", title="Cousins Properties Sells Downtown Austin Tower for $208M",
         subtitle="A Second Trophy Office Trade in the Same Stretch Suggests a Real Repricing Wave, Not an Isolated Deal",
         date="July 31, 2026",
         trigger=f'''{src("https://www.commercialsearch.com/news/cousins-properties-sells-austin-office-asset-for-208m/", "Cousins Properties sold the 518,385-square-foot One Eleven Congress office tower")} at 111 Congress Ave. to Fort Worth-based Canyon Creek Real Estate for $208 million; the 30-story, 1987-built tower was 90.2% leased as of March, and Cousins had invested $66.4 million in capital improvements since acquiring it in 2016. The deal is Canyon Creek's first Austin acquisition since the firm's 2025 formation.''',
         why="A second major downtown Austin office trophy trading in the same stretch as Hines' $151 million purchase of 405 Colorado St. is a meaningfully stronger signal than either sale alone &mdash; one full-price trade could be idiosyncratic, but two in close succession suggests institutional capital is genuinely re-entering downtown Austin office at scale, not just opportunistically picking off a single asset. That a brand-new buyer entity is willing to make this its first Austin acquisition also signals confidence extends beyond incumbent owners.",
         implications=[
             "Confirms a second institutional-scale downtown Austin office trade in the same week as the Hines/405 Colorado deal",
             "Signals a possible broader repricing wave for well-leased Austin office trophies, not an isolated transaction",
             "Introduces a new institutional buyer (Canyon Creek) making downtown Austin its entry point into the market",
             "Provides a second recent full-price comp ($208M) for other downtown Austin office owners considering a sale",
         ],
         watch="Whether additional downtown Austin office towers trade at comparable pricing in the coming weeks, confirming a genuine repricing wave rather than two isolated deals."),
    dict(category="Office", title="Hines Pays $733/SF for Fully Leased Downtown Austin Tower",
         subtitle="A Full-Price Trophy Trade Is a Different Signal Than the Metro's Vacancy Rate",
         date="July 13, 2026",
         trigger=f'''{src("https://therealdeal.com/texas/2026/07/13/houston-based-hines-snags-405-colorado-for-733-per-sf/", "Hines paid $151 million ($733 per square foot) to buy the 206,000-square-foot tower at 405 Colorado St.")} from Brandywine Realty Trust, a 25-story, Class-A building completed in 2021 and fully leased to tenants including JPMorgan Chase, Bain &amp; Company, and AllianceBernstein; Eastdil Secured advised seller Brandywine, which is executing a plan to sell roughly $300 million of assets from its portfolio.''',
         why="A fully-leased trophy tower trading at $733 per square foot, in a market where office vacancy is running near 25%, is a specific bet on tenant quality and lease term, not a bet on the office sector broadly &mdash; Hines is underwriting JPMorgan, Bain, and AllianceBernstein's credit and renewal likelihood, not downtown Austin office fundamentals as a whole. That Brandywine sold at what appears to be a strong basis, as part of a disclosed disposition program, also suggests the seller found this specific asset easier to monetize than the rest of its portfolio.",
         implications=[
             "Confirms full-price capital remains available for fully-leased, credit-tenant office even as metro vacancy runs near 25%",
             "Signals office pricing is bifurcating sharply by tenant quality and lease term, not moving as one asset class",
             "Advances Brandywine's disclosed $300 million disposition program by one confirmed sale",
             "Provides a $733/SF comp for other fully-leased downtown Austin towers considering a sale",
         ],
         watch="Whether Brandywine's remaining Austin office assets, including One Uptown, trade at comparable pricing, and Hines' plans for the building at lease rollover."),
    dict(category="Multifamily", title="Southwest Value Partners Breaks Ground on 372-Unit Aluna Apartments",
         subtitle="Institutional Capital Is Still Deploying Into Ground-Up Austin Multifamily Despite the Cycle",
         date="August 4, 2026",
         trigger=f'''{src("https://therealdeal.com/texas/2026/08/04/texas-top-construction-permits-this-week-2/", "San Diego-based Southwest Value Partners is developing Aluna, a 372-unit, $75 million apartment complex")} at 14335 Tandem Boulevard in Austin, roughly $200,000 per unit; construction is slated to start in September 2026 and wrap by fall 2028.''',
         why="An out-of-state institutional developer committing $75 million to a ground-up, 372-unit Austin apartment project, at a moment when several other local sponsors have been pulling back multifamily starts, is a concrete signal that at least some institutional capital still underwrites new Austin multifamily supply as attractive &mdash; even if the broader development pipeline has slowed. The roughly $200,000-per-unit basis gives other sponsors a fresh, dated construction-cost benchmark to underwrite against.",
         implications=[
             "Confirms institutional capital is still committing to ground-up Austin multifamily despite a broader development slowdown",
             "Provides a fresh, roughly $200,000-per-unit construction-cost benchmark for other Austin multifamily developers",
             "Signals continued confidence in the specific submarket around Tandem Boulevard",
             "Sets a fall 2028 delivery to watch against the metro's broader multifamily supply pipeline",
         ],
         watch="Whether construction actually begins on the September 2026 timeline, and how Aluna's eventual lease-up pace compares to other recent Austin multifamily deliveries."),
    dict(category="Multifamily", title="Cedar Park's Bell District Apartment Component Stalls as Development Slows",
         subtitle="A Missed Groundbreaking Date Is a Real, On-Record Admission of Market Softness",
         date="August 6, 2026",
         trigger=f'''{src("https://communityimpact.com/cedar-park/development/building-bell-district-city-moves-forward-with-art-collective-while-private-development-slows/", "Master developer RedLeaf confirmed the planned 194-unit apartment component of Cedar Park's Bell District mixed-use project has no new groundbreaking date")} after missing its original November target, with RedLeaf partner Rob Shands attributing the delay directly to market conditions: &ldquo;The softness in this market has really been challenging.&rdquo; The city itself is proceeding with a separate, publicly funded $4.5 million arts-collective building on the same site, targeting a fall 2029 opening.''',
         why="A developer publicly attributing a missed groundbreaking date to market softness, on the record, is a rarer and more useful data point than the usual vague disclosure-free delay &mdash; it's a direct admission that current financing and leasing conditions don't yet support breaking ground on this specific multifamily component, even inside an otherwise-active mixed-use district the city is still funding. That the public arts-collective piece is moving forward on schedule while the private apartment piece stalls also shows the slowdown is capital-markets-driven, not a broader loss of confidence in the district itself.",
         implications=[
             "Provides a rare, on-the-record admission that market softness, not entitlement or demand issues, is delaying a specific Austin-metro multifamily start",
             "Shows a mixed-use district can keep moving on its publicly funded components even as the private multifamily piece stalls",
             "Signals suburban Austin-metro apartment starts remain sensitive to financing conditions even in an amenity-rich, city-backed district",
             "Leaves the 194-unit component without a firm delivery timeline to track against the district's fall 2029 arts-building opening",
         ],
         watch="Whether RedLeaf sets a new groundbreaking date for the apartment component, and whether comparable Austin-metro mixed-use developers disclose similar market-driven delays."),
]

CRE_FINAL_PARAGRAPHS = [
    "This week's biggest story for Austin office is that there isn't just one trophy trade &mdash; there are two. Cousins Properties' $208 million sale of One Eleven Congress lands in the same stretch as Hines' $151 million purchase of 405 Colorado St., and a brand-new buyer entity (Canyon Creek) making its Austin debut on the Cousins deal is a stronger signal than either trade alone that institutional capital is genuinely re-entering downtown office, not just opportunistically picking off one asset.",
    "Apollo choosing Austin for a second U.S. headquarters is this week's longest-lead-time signal. It's a corporate-relocation announcement, not a real estate one &mdash; the actual office lease or build, and the jobs that come with it, still has to follow. But an $800 billion manager formalizing what it already calls a top-five capital base is exactly the kind of commitment that shows up in absorption data a year or two from now.",
    "Southwest Value Partners breaking ground on Aluna and RedLeaf's stalled Bell District apartment component tell opposite sides of the same Austin multifamily story this week: some institutional sponsors are still committing fresh capital to ground-up apartments, while others are openly citing market softness to justify delay. Read together with Link Logistics' fully-leased Round Rock acquisition, the throughline is that capital is still moving in Austin, but it's being far more selective about exactly where and what it commits to.",
]
CRE_FINAL_BULLETS = [
    "Two institutional-scale downtown Austin office trophies traded in the same stretch, not just one isolated deal",
    "Apollo's HQ2 announcement is a corporate-relocation signal that precedes any actual real estate by months or years",
    "One institutional sponsor broke ground on new Austin-metro apartments the same week another publicly delayed one, citing market softness",
    "A major logistics REIT is still paying up for fully-leased, infill Austin-suburb industrial despite elevated metro vacancy",
]

CRE_MARKETS = [
    ("austin", "Austin, TX"),
    ("usc", "Los Angeles, CA"),
    ("nyu", "New York, NY"),
    ("uga", "Atlanta, GA"),
    ("uf", "Miami, FL"),
]

CRE_AUSTIN_BLOCK = market_block_html(
    "cre", "austin", True, "CRE", "Signal", "AUSTIN, TEXAS", "AUGUST 10, 2026", "JULY 23&ndash;AUG 10, 2026",
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
         date="July 2026",
         trigger=f'''{src("https://www.bisnow.com/los-angeles/news/industrial/rexford-takes-500m-loss-plans-up-to-2b-in-dispositions-this-year-135577", "Rexford Industrial Realty raised its 2026 disposition guidance to $1.5&ndash;2 billion")}, up from $400&ndash;500 million, after posting a $506.9 million net loss in Q2 driven by a noncash impairment; the expanded sell-off covers roughly 8 million square feet, about 16% of Rexford's ~50 million-square-foot LA-basin portfolio, with the company targeting properties it says carry &ldquo;substantially above-market in-place rents&rdquo; from acquisitions &ldquo;at the height of the market.&rdquo;''',
         why="A REIT quadrupling its planned dispositions while eating a half-billion-dollar impairment is a concrete repricing signal, not a portfolio-management footnote &mdash; Rexford is the single largest and most closely-watched industrial landlord in the LA basin, so its own admission that certain assets were bought at peak valuations tells you where the broader market's cost basis stands relative to today's rents. That same-property occupancy still sits at 95.7% even amid this pruning shows the portfolio's operating performance isn't the problem; the entry price is.",
         implications=[
             "Signals that even best-in-class LA industrial product bought at peak pricing no longer pencils at current values",
             "Directs roughly $1 billion of sale proceeds toward paying down $1 billion of debt maturing in 2027",
             "Provides a reference point for how aggressively other LA industrial owners may need to reprice legacy acquisitions",
             "Confirms strong 95.7% same-property occupancy even as the company prunes its highest-basis assets",
         ],
         watch="The pricing Rexford actually achieves on the expanded $1.5&ndash;2 billion disposition slate, and whether other LA-basin industrial REITs follow with similar guidance revisions."),
    dict(category="Industrial", title="Minority Investors Sue to Delay Industrial Realty Group's $2.9B Reverse Merger",
         subtitle="A Governance Fight Is Playing Out on Top of a Massive LA-Based Industrial Portfolio",
         date="August 3, 2026",
         trigger=f'''{src("https://www.bisnow.com/news/los-angeles/industrial/minority-investors-sue-industrial-realty-group-over-timing-of-reverse-merger", "Seventeen minority investors in IRG Master Holdings sued in LA County Superior Court")} to delay a reverse merger between Industrial Realty Group and mortgage REIT Sachem Capital, arguing the deal would move roughly $3 billion in industrial assets (98 properties valued at $2.9 billion) into a new public entity before an ongoing $350 million-plus arbitration dispute resolves; the merger is slated to close by year-end 2026, with the arbitration trial set for spring 2027.''',
         why="A minority-investor lawsuit specifically over the timing of a reverse merger, rather than its economics, is a governance fight about who controls the outcome of a separate $350 million-plus arbitration once nearly $3 billion of industrial real estate sits inside a new public entity &mdash; if the merger closes first, the minority investors' leverage in that arbitration could change materially. For a portfolio this large concentrated in the LA basin, how this resolves is a real data point on how public-market structures interact with existing LP disputes at scale.",
         implications=[
             "Puts nearly $3 billion of LA-basin industrial real estate at the center of an active governance and timing dispute",
             "Tests whether minority investors can use litigation to control the sequencing of a reverse merger against a pending arbitration",
             "Signals real friction in the run-up to one of the largest industrial-REIT-adjacent public-market transactions in the region",
             "Adds a corporate-structure risk factor for anyone underwriting IRG-affiliated industrial assets ahead of the merger's close",
         ],
         watch="Whether the LA County Superior Court grants a delay, and how the merger's year-end 2026 close interacts with the spring 2027 arbitration trial if it proceeds on schedule."),
    dict(category="Office", title="Innocean USA Doubles HQ Space in Move to Hackman's El Segundo Campus",
         subtitle="A 101,000-SF Lease Shows Creative-Office Repositioning Still Working in the South Bay",
         date="August 7, 2026",
         trigger=f'''{src("https://commercialobserver.com/2026/08/ad-agency-doubles-office-hq-space-in-move-to-hackman-campus-in-l-a/", "Innocean USA, Hyundai Motor Group's ad agency, signed a lease for 101,000 square feet at Hackman Capital Partners' 550,000-square-foot creative office campus")} at 888 Douglas Street in El Segundo, a converted former Northrop Grumman aerospace complex; the agency will relocate roughly 600 employees from Huntington Beach once construction finishes in 2027, with JLL representing the tenant.''',
         why="A name-brand corporate tenant more than doubling its footprint to relocate into a converted aerospace complex is direct evidence that the creative-office repositioning thesis &mdash; taking obsolete industrial or aerospace stock and repackaging it as amenity-rich media/tech campus space &mdash; is still working well enough to win large, real leases, not just attract speculative interest. A 600-employee relocation is also a meaningful, quantifiable jobs commitment to the South Bay submarket specifically.",
         implications=[
             "Confirms large corporate tenants are still committing to converted creative-office product in the South Bay",
             "Validates Hackman Capital's aerospace-to-creative-office repositioning strategy with a real, scaled lease",
             "Brings roughly 600 relocating employees into the El Segundo submarket once construction completes in 2027",
             "Provides a comp for other obsolete aerospace/industrial owners considering a similar creative-office conversion",
         ],
         watch="Whether Hackman signs additional large tenants at the 888 Douglas Street campus ahead of the 2027 completion, and Innocean's actual move-in timeline."),
    dict(category="Office", title="Port of Long Beach Buys Downtown Office Tower for $36M",
         subtitle="A Public Port Authority Becomes an Unlikely Buyer in a Distressed Office Market",
         date="August 5, 2026",
         trigger=f'''{src("https://www.nbclosangeles.com/news/local/port-of-long-beach-purchases-36-million-office-tower/3926199/", "The Port of Long Beach purchased the 13-story, 225,500-square-foot office tower at 100 Oceangate for $36 million")}, aiming to turn it into a hub leasing space to logistics, supply-chain, and customs-brokerage firms under Mayor Rex Richardson's &ldquo;Anchor LB&rdquo; economic-development initiative; it's described as a first-of-its-kind West Coast move by a public port authority into downtown office ownership. Separately, an Avison Young report found downtown Long Beach office vacancy has reached a record 35%, well above the 21.2% Greater LA rate in Q2 2026.''',
         why="A public port authority becoming a downtown office buyer, rather than a private investor stepping in, is an unusual and telling signal about how distressed a specific submarket has become &mdash; at a record 35% vacancy, well above the broader Greater LA rate, private capital apparently wasn't stepping in on terms the city found acceptable, so the port itself is now underwriting the building as an economic-development anchor rather than a pure return play. That's a materially different buyer thesis than anything else on this desk this cycle.",
         implications=[
             "Signals private capital wasn't filling the gap in downtown Long Beach office at an acceptable basis, prompting public intervention",
             "Provides a concrete $36 million/225,500-SF basis for a distressed downtown Long Beach office asset",
             "Establishes a first-of-its-kind West Coast template for a public port authority as a direct downtown office buyer",
             "Confirms downtown Long Beach's 35% vacancy rate is now severe enough to justify an unconventional public-sector response",
         ],
         watch="Which logistics, supply-chain, and customs-brokerage tenants the Port signs under the Anchor LB initiative, and whether other California port authorities consider similar office acquisitions."),
    dict(category="Mixed-Use", title="Bankruptcy Court Approves $517M Sale of Stalled Oceanwide Plaza Towers",
         subtitle="A Half-Billion-Dollar Sale Still Leaves an $800 Million Gap to Finish the Job",
         date="July 2026",
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
    dict(category="Retail", title="University of California Buys 16 Westwood Village Properties for $49.8M",
         subtitle="A University Investor Assembles Land Next to Its Own Campus",
         date="August 3, 2026",
         trigger=f'''{src("https://commercialobserver.com/2026/08/university-of-california-westwood-village-anderson/", "UC Investments, which manages the University of California's $190 billion portfolio, acquired a 16-property, roughly 181,855-square-foot retail and office portfolio in Westwood Village")} along Westwood Boulevard from Anderson Real Estate &mdash; the family behind UCLA Anderson School's naming gift &mdash; for $49.8 million; no development plans were disclosed.''',
         why="A university's own investment arm assembling a meaningful chunk of the retail district immediately adjacent to its campus is a different kind of buyer than a typical institutional fund &mdash; UC Investments doesn't need this to underwrite a market return on the same timeline a private buyer would, which gives it more flexibility to hold, reposition, or redevelop on a longer horizon tied to campus planning rather than fund-life pressure. It's also a useful pattern for USC-market observers: university-adjacent land assembly by the university's own capital is a dynamic that plays out in college-town retail districts well beyond Westwood.",
         implications=[
             "Signals a university endowment-adjacent buyer assembling land specifically next to its own campus, not a typical fund",
             "Gives UC Investments a longer, campus-planning-driven holding horizon than a conventional private buyer would have",
             "Provides a $49.8 million/16-property basis for a Westwood Village retail assemblage",
             "Offers a directly relevant template for how institutional or university-adjacent capital can consolidate college-town retail districts, including near USC",
         ],
         watch="Whether UC Investments discloses redevelopment or long-term planning intentions for the Westwood Village assemblage."),
    dict(category="Retail", title="Caruso's Palisades Village Sets August 15 Reopening, Confirms 99% Leased",
         subtitle="A Concrete Leasing Data Point on Wildfire-Recovery Retail",
         date="August 5, 2026",
         trigger=f'''{src("https://beverlypress.com/2026/08/palisades-village-prepares-for-grand-reopening/", "Caruso confirmed Palisades Village will hold its grand reopening on Saturday, August 15, 2026")}, after a $100 million restoration following the 2025 Palisades Fire; the center will reopen 99% leased, with roughly one-third of tenants being new additions.''',
         why="A 99%-leased reopening after a $100 million wildfire-recovery restoration is a concrete, quantified data point on retail-tenant confidence in fire-affected LA submarkets specifically &mdash; it shows retailers are willing to recommit (and new tenants are willing to enter) once a landlord demonstrates the capital and timeline discipline to actually rebuild, rather than treating fire damage as a reason to walk away from a lease. That roughly a third of the tenant roster is new suggests the reopening is also functioning as a tenant-mix refresh, not just a like-for-like restoration.",
         implications=[
             "Provides a concrete 99%-leased benchmark for retail-tenant confidence in wildfire-affected LA submarkets",
             "Confirms landlords who commit real capital and a firm timeline to fire recovery can retain and attract retail tenants",
             "Uses the reopening to refresh roughly a third of the tenant mix, not just restore the prior roster",
             "Signals continued high-end retail viability in the Palisades trade area post-fire",
         ],
         watch="Opening-week performance and foot traffic at the reopened center, and whether comparable fire-affected LA retail properties pursue similar full restorations."),
]

USC_FINAL_PARAGRAPHS = [
    "This week's Los Angeles signals split between capital still committing to LA real estate and capital fighting over how existing LA real estate gets restructured. Innocean's 101,000-square-foot lease at Hackman's converted aerospace campus and the Port of Long Beach's unconventional purchase of a downtown office tower both show real, if unconventional, demand still finding its way into distressed submarkets, while the IRG/Sachem minority-investor lawsuit shows a nearly $3 billion industrial portfolio caught in a genuine governance fight.",
    "The Port of Long Beach buying its own downtown office tower is this week's clearest distress signal, arguably more telling than a vacancy statistic alone &mdash; a public port authority stepping in as a direct office buyer, in a submarket at a record 35% vacancy, suggests private capital wasn't underwriting that building on terms the city found acceptable.",
    "UC Investments' Westwood Village purchase and Palisades Village's 99%-leased reopening describe two different flavors of patient, confidence-driven capital: a university assembling land next to its own campus on a multi-decade horizon, and a landlord's wildfire-recovery bet paying off in a fully re-leased retail center. Read against Rexford's continued disposition guidance and the IRG/Sachem fight, the throughline this week is that LA capital is moving, but unevenly, and often for reasons beyond a simple cap-rate calculation.",
]
USC_FINAL_BULLETS = [
    "A public port authority buying a downtown office tower is one of the starker distress signals in a submarket now at 35% vacancy",
    "A minority-investor lawsuit is fighting over the timing of a nearly $3 billion industrial-portfolio reverse merger",
    "A 101,000-SF creative-office lease confirms aerospace-to-office conversion demand is still real in the South Bay",
    "Palisades Village reopened 99% leased after a $100M wildfire restoration, a concrete data point on fire-recovery retail confidence",
]

CRE_USC_BLOCK = market_block_html(
    "cre", "usc", False, "CRE", "Signal", "LOS ANGELES, CA", "AUGUST 10, 2026", "JULY 15&ndash;AUG 10, 2026",
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
         date="July 2026",
         trigger=f'''{src("https://commercialobserver.com/2026/07/nbcuniversal-lease-renewal-office-1221-avenue-of-the-americas/", "NBCUniversal renewed 244,185 square feet at Rockefeller Group's 1221 Avenue of the Americas")} in Midtown, across from its 30 Rockefeller Plaza headquarters, building on a footprint it first established there in 2012 and expanded in 2021; Midtown average asking rents hit $86.18 per square foot in Q2 2026, a quarter Commercial Observer described as having leasing velocity not seen since 2002.''',
         why="A legacy media tenant recommitting to a quarter-million square feet, rather than shrinking or relocating, directly undercuts the narrative that large corporate occupiers are only downsizing their Manhattan footprints. That this renewal lands in a quarter with the strongest Manhattan office leasing velocity since 2002 suggests it's part of a broader pattern of large-tenant conviction, not an isolated holdout renewal driven by relocation costs.",
         implications=[
             "Confirms large legacy tenants are renewing at scale, not uniformly shrinking their Manhattan footprints",
             "Reinforces 1221 Avenue of the Americas and the Rockefeller Center corridor as a durable media-tenant cluster",
             "Adds to a broader Q2 2026 leasing velocity trend described as the strongest since 2002",
             "Supports continued asking-rent growth in Midtown even amid national office-sector caution",
         ],
         watch="Whether other large media or legacy corporate tenants announce comparable renewals in the same submarket this year."),
    dict(category="Office", title="Snap Inc. Subleases 199,000 SF at Vornado's Penn 2 From Verizon",
         subtitle="Sublease Supply Is Tightening to a 2019 Low Even as Tech Tenants Keep Absorbing Space",
         date="August 3, 2026",
         trigger=f'''{src("https://www.crainsnewyork.com/real-estate/commercial/cny-snapchat-parent-company-sublease-penn-2-20260803/", "Snap Inc. is taking over three of Verizon's floors (the 8th through 10th) at Vornado Realty Trust's Penn 2")}, a sublease running through 2044 at a premium to Verizon's existing rent; per Colliers' July report, it was the second-largest Manhattan office deal of the month, landing as citywide sublease supply fell to its lowest level since August 2019.''',
         why="A tech tenant taking a nearly two-decade sublease commitment, at a premium to the existing rent, is a strong statement of long-term conviction rather than an opportunistic short-term space grab &mdash; and it's happening at the same moment citywide sublease supply has tightened to a level not seen since 2019. Those two facts together confirm that excess sublease space, one of the clearest post-pandemic overhang indicators for Manhattan office, is genuinely being absorbed, not just quietly extended by existing tenants.",
         implications=[
             "Confirms sublease space, a key post-pandemic office overhang indicator, is genuinely tightening toward 2019 levels",
             "Shows a tech tenant paying a premium to Verizon's existing rent for a near-two-decade sublease commitment",
             "Reinforces Penn District's continued momentum as a leasing destination under Vornado's redevelopment",
             "Adds to the same record-leasing-velocity narrative already visible in the NBCUniversal renewal this cycle",
         ],
         watch="Whether Manhattan sublease supply continues tightening in the back half of 2026, and if other large tech tenants pursue comparable long-term sublease commitments."),
    dict(category="Mixed-Use", title="Bill Ackman Pays $188M for Lab Building, Plans Brain Research Institute",
         subtitle="A Philanthropic Buyer Converts Office/Lab Stock Into an Institutional Research Campus",
         date="July 28, 2026",
         trigger=f'''{src("https://commercialobserver.com/2026/07/bill-ackman-buys-125-west-end-avenue/", "Bill Ackman's Pershing Square Foundation paid $188 million for the 400,000-square-foot lab building at 125 West End Avenue")} from Taconic Partners, the first piece of a roughly $260 million, two-building, 700,000-square-foot assemblage on the Upper West Side that will become the Ackman Oxman Institute, a brain research center developed with the Mount Sinai Hospital System.''',
         why="A billionaire-funded philanthropic buyer paying a premium to convert existing lab and office stock into a dedicated institutional research campus is a concrete example of life-sciences and &ldquo;eds-and-meds&rdquo; demand becoming a real alternative use case for underused Manhattan office and lab buildings, not just a talking point. Because this is a mission-driven, not yield-driven, acquisition, it's a different kind of demand signal than a REIT or fund buying the same building &mdash; but it still removes real square footage from the conventional office market permanently.",
         implications=[
             "Confirms life-sciences and institutional research demand as a genuine absorption path for older lab/office stock",
             "Removes roughly 700,000 square feet from conventional Manhattan office/lab inventory permanently",
             "Signals continued philanthropic capital willingness to fund large-scale medical research real estate in NYC",
             "May encourage other underused Upper West Side lab buildings to market toward similar institutional buyers",
         ],
         watch="Whether the Foundation closes on the adjacent 320 West 66th Street parcel as planned, and construction/opening timelines for the Ackman Oxman Institute."),
    dict(category="Life Sciences", title="Longfellow and Sculptor Sell Long Island City Life Sciences Building for $86.9M",
         subtitle="Another Lab Asset Trades Hands, Echoing the Ackman Thesis From Across the East River",
         date="August 7, 2026",
         trigger=f'''{src("https://therealdeal.com/new-york/2026/08/08/new-york-top-real-estate-deals-friday-august-7-2026/", "An affiliate of Longfellow Real Estate Partners and Sculptor Real Estate sold the 215,000-square-foot Hatch Life Sciences building")} at 43-10 23rd Street in Long Island City &mdash; a century-old former parachute factory converted to lab space &mdash; to a company tied to developer Jack Guttman for $86.9 million.''',
         why="A second life-sciences building trading hands in the same stretch as the Ackman Oxman Institute purchase, this time in Long Island City rather than the Upper West Side, confirms lab-space demand and investor appetite for converted industrial buildings isn't confined to one submarket or one buyer type &mdash; here it's a straightforward institutional sale, not a philanthropic acquisition, which is a useful read on how ordinary investors are pricing the same underlying asset class.",
         implications=[
             "Confirms life-sciences/lab real estate demand extends beyond the Upper West Side into Long Island City",
             "Provides a conventional, yield-driven sale comp to set alongside the mission-driven Ackman lab purchase",
             "Signals converted industrial buildings (a former parachute factory) remain viable lab-conversion candidates",
             "Adds Jack Guttman-affiliated ownership to the roster of active LIC life-sciences investors",
         ],
         watch="The new ownership's leasing and any further conversion or redevelopment plans for the Hatch Life Sciences building."),
    dict(category="Brokerage", title="Barry Gosin to Step Down as Newmark CEO After 47 Years",
         subtitle="Leadership Change at a Top-Tier Brokerage Is a Recruiting-Relevant Data Point in Its Own Right",
         date="August 7, 2026",
         trigger=f'''{src("https://www.crainsnewyork.com/real-estate/commercial/cny-barry-gosin-steps-down-at-newmark-20260807/", "Barry Gosin, one of New York's most prominent commercial real estate executives, is stepping down as CEO of brokerage Newmark & Co.")} after 47 years leading the firm.''',
         why="Leadership succession at a brokerage the scale of Newmark is a different kind of signal than a leasing or sales transaction, but it's directly relevant to anyone tracking the industry's power structure &mdash; nearly five decades under one CEO is an unusually long tenure even by real estate standards, and how Newmark manages this transition will shape client relationships, deal flow, and hiring across the firm for years.",
         implications=[
             "Marks the end of one of commercial real estate's longest-running CEO tenures at a major brokerage",
             "Raises real questions about succession planning and continuity at one of the industry's top-tier firms",
             "Is directly relevant to students and job-seekers targeting Newmark, a firm many CRE recruits target specifically",
             "May prompt broader industry conversation about generational leadership turnover at legacy brokerages",
         ],
         watch="Who Newmark names as Gosin's successor, and whether the transition prompts any senior-level departures or realignment at the firm."),
    dict(category="Multifamily", title="182-Unit Washington Heights Apartment Complex Trades for $80M",
         subtitle="A Large Multifamily Sale Sets a Fresh Uptown Manhattan Per-Unit Comp",
         date="August 6, 2026",
         trigger=f'''{src("https://therealdeal.com/new-york/2026/08/07/new-york-top-real-estate-deals-thursday-august-6/", "The 15-story, 182-unit apartment complex at 1930 Amsterdam Avenue in Washington Heights sold for $80 million")}, or roughly $440,000 per unit; HP Dunwell Housing Development Fund Company remains a partial owner alongside a company tied to Phoenix Realty Group.''',
         why="An $80 million trade for a large, uptown Manhattan apartment complex, at a fresh roughly $440,000-per-unit basis, gives other Washington Heights and upper-Manhattan multifamily owners a real, dated comp to underwrite against &mdash; a useful counterpoint to the discounted Upper West Side stabilized-portfolio pricing this desk has tracked in recent weeks, since it shows large-scale uptown multifamily can still command a healthy per-unit price when the deal structure and location line up.",
         implications=[
             "Provides a fresh, roughly $440,000-per-unit basis for large uptown Manhattan multifamily assets",
             "Signals continued institutional appetite for large-scale Washington Heights apartment complexes",
             "Offers a useful counterpoint to more discounted stabilized-portfolio pricing seen elsewhere in Manhattan recently",
             "Keeps a public-private ownership structure (HP Dunwell alongside Phoenix Realty-affiliated capital) in place post-sale",
         ],
         watch="Whether comparable large uptown Manhattan multifamily assets trade at a similar per-unit basis in the coming weeks."),
    dict(category="Hospitality", title="Korman Communities Buys Out Partners in Three Manhattan AKA-Branded Hotels",
         subtitle="A $220M Gross Valuation, Down From $391M in 2015, Marks Real Hotel Value Erosion",
         date="reported August 4, 2026",
         trigger=f'''{src("https://www.bisnow.com/news/new-york/deal-sheet/snapchat-parent-snags-penn-2-sublease-vornado-verizon", "Korman Communities bought out partners CalSTRS and BlackRock in three AKA-branded hotel properties")} &mdash; 42 West 58th Street, 123 West 44th Street, and 330 East 56th Street &mdash; with the transaction placing the properties' gross value at $220 million, down from a $391 million valuation in 2015.''',
         why="A roughly 44% decline in gross valuation on the same properties since 2015 is a concrete, quantified data point on how much value rising labor, insurance, and debt costs have stripped from extended-stay hospitality assets over the past decade &mdash; Korman buying out its institutional partners at this lower basis suggests the operator sees more upside in owning outright at today's depressed valuation than in continuing a partnership structured around the 2015 pricing.",
         implications=[
             "Provides a concrete, quantified example of NYC hospitality asset values declining over a decade (roughly 44% here)",
             "Signals rising labor, insurance, and debt costs are a real, measurable drag on extended-stay hotel valuations",
             "Lets the operating partner (Korman) consolidate full ownership at a lower basis than its institutional co-investors held",
             "Removes CalSTRS and BlackRock as institutional partners from three Manhattan hospitality assets",
         ],
         watch="Whether Korman pursues renovation or repositioning of the three AKA-branded properties now that it holds full ownership."),
]

NYC_FINAL_PARAGRAPHS = [
    "This week's New York signals split between office-leasing conviction and a broader mix of sales and personnel news. Snap Inc.'s nearly two-decade sublease at Penn 2, alongside the already-strong NBCUniversal renewal, confirms Manhattan sublease supply is genuinely tightening toward 2019 levels, not just being quietly extended by existing tenants.",
    "The Ackman Oxman Institute purchase and the Longfellow/Sculptor life-sciences sale in Long Island City are worth reading together: two different lab-space transactions, on opposite sides of the East River, with two very different buyer types (philanthropic versus conventional institutional). Together they confirm life-sciences demand for converted office and industrial stock is broadening across submarkets, not concentrated in one buyer's thesis.",
    "Barry Gosin's departure after 47 years atop Newmark is this week's reminder that leadership and firm structure are their own category of signal, distinct from any single transaction &mdash; directly relevant to anyone targeting a top-tier brokerage in recruiting. Read alongside the Washington Heights multifamily trade and the Korman AKA hotel buyout, this week's New York desk spans leasing, life sciences, multifamily, hospitality, and now brokerage leadership all at once.",
]
NYC_FINAL_BULLETS = [
    "A nearly two-decade sublease commitment at Penn 2 confirms Manhattan sublease supply is tightening toward a 2019 low",
    "A philanthropic buyer and a conventional institutional seller both traded lab/life-sciences buildings on opposite sides of the East River",
    "One of commercial real estate's longest-running CEO tenures is ending at Newmark after 47 years",
    "A Manhattan hotel operator's buyout of its institutional partners revealed a roughly 44% decline in gross hotel valuation since 2015",
]

CRE_NYU_BLOCK = market_block_html(
    "cre", "nyu", False, "CRE", "Signal", "NEW YORK, NY", "AUGUST 10, 2026", "JULY 28&ndash;AUG 10, 2026",
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

# ============================================================== REPE SIGNAL ==============================================================

REPE_SNAPSHOT = [
    ("Fundraising / Dry Powder", "rising"),
    ("Platform M&amp;A Activity", "rising"),
    ("Portfolio Acquisition Volume", "rising"),
    ("Take-Private Activity", "stable"),
    ("Deployment Pace", "stable"),
    ("GP-Stake / Secondaries Activity", "rising"),
]

REPE_SIGNALS = [
    dict(category="Platform M&amp;A", title="Bridgepoint to Acquire Kayne Anderson Real Estate for ~$1.39B",
         subtitle="A GP-Stake Sale and a Platform Sale Happen in the Same Transaction",
         date="June 29, 2026",
         trigger=f'''{src("https://www.bridgepointgroup.com/about-us/news-and-insights/press-releases/2026/bridgepoint-to-acquire-kayne-anderson-real-estate-strengthening-its-position-as-a-leading-global-middle-market-private-markets-platform", "UK-listed private markets firm Bridgepoint Group agreed to acquire Kayne Anderson Real Estate (KARE), a senior-living- and residential-focused manager, from Kayne Anderson Capital Advisors")} for roughly $1.39 billion in upfront enterprise value; as part of the same transaction, Goldman Sachs Alternatives' Petershill program, which held a minority GP stake in KARE, sold its position.''',
         why="A platform sale and a minority GP-stake exit closing in the same transaction is a clean illustration of how real estate manager ownership itself gets bought and sold at multiple levels simultaneously &mdash; Bridgepoint is buying KARE's full operating business while Petershill, which had only ever owned a slice of KARE's economics, is exiting its own separate position at the same time. Both trades value the same underlying manager, just from different ownership stakes.",
         implications=[
             "Confirms mid-market real estate manager consolidation is active enough to support a $1.39 billion platform sale",
             "Shows a minority GP-stake investor (Petershill) and a full-platform acquirer (Bridgepoint) can exit and enter the same manager simultaneously",
             "Adds senior-living and residential-focused management capability directly to Bridgepoint's private markets platform",
             "Provides a real, dated valuation benchmark for mid-market real estate manager M&amp;A",
         ],
         watch="Deal close timing and whether Bridgepoint retains KARE's existing investment team and strategy post-acquisition."),
    dict(category="Platform M&amp;A", title="Milhaus Merges With SRG Residential, Adds Broadshore Capital's Investment Platform",
         subtitle="An Operator-Developer Buys Its Way Into the Fund-Management Business",
         date="July 14, 2026",
         trigger=f'''{src("https://www.businesswire.com/news/home/20260714343558/en/Milhaus-and-SRG-Residential-Complete-Merger-and-Announce-Acquisition-of-Broadshore-Capital-Partners", "Apartment developer Milhaus completed its merger with Sares Regis Group's multifamily arm, SRG Residential, and simultaneously announced an agreement to acquire Broadshore Capital Partners")}, an SEC-registered investment adviser with roughly $1 billion in AUM; the combined platform's pipeline exceeds $2.5 billion, with more than 50,000 apartment units under third-party management, and Broadshore's principals are joining Milhaus's leadership.''',
         why="An operator-developer acquiring a registered investment adviser, rather than just merging with another developer, is a distinct playbook from the usual story of a large manager buying a smaller one &mdash; Milhaus is specifically buying its way into discretionary fund management and third-party capital relationships it didn't previously have, blending development execution with institutional capital-raising capability under one roof.",
         implications=[
             "Shows an operator-developer acquiring registered investment-adviser capability, not just merging with a peer developer",
             "Creates a combined platform with more than 50,000 apartment units under third-party management",
             "Folds Broadshore's principals directly into Milhaus's leadership, integrating rather than just financing the acquisition",
             "Provides a template for development-focused platforms seeking to add institutional fund-management capability",
         ],
         watch="Whether the combined platform raises a dedicated fund using Broadshore's registered-adviser infrastructure, and integration progress across the merged leadership team."),
    dict(category="Fundraising", title="Starwood Capital Closes $10.2B Opportunistic Fund XIII, Its Largest Ever",
         subtitle="A Flagship Sponsor's Biggest-Ever Raise Doubles as a Strategy Pivot Toward Data Centers",
         date="July 1, 2026",
         trigger=f'''{src("https://www.prnewswire.com/news-releases/starwood-capital-group-raises-10-2-billion-opportunistic-real-estate-fund-302815286.html", "Starwood Capital Group held the final close of SOF XIII, its opportunistic flagship fund, at $10.2 billion in commitments")} from more than 300 investors across roughly 20 countries &mdash; the largest fund in Starwood's history &mdash; already deploying or committing more than $3 billion across 20 deals targeting residential, data center, industrial, and hospitality assets in the US, Europe, and select Asia-Pacific markets.''',
         why="A flagship sponsor's largest-ever raise landing specifically as it pivots toward data centers and Sun Belt exposure is a clear signal of where institutional LP capital wants opportunistic real estate managers deployed right now &mdash; a $10.2 billion vehicle only gets built if hundreds of sophisticated investors across 20 countries buy into both the manager's track record and its stated forward strategy.",
         implications=[
             "Confirms institutional LP appetite for opportunistic real estate remains strong enough to support a record-setting single-manager raise",
             "Signals data centers and Sun Belt exposure as explicit strategic priorities for one of the largest opportunistic platforms",
             "Adds $10.2 billion of fresh dry powder targeting distressed and value-add real estate across three continents",
             "Provides a scale benchmark other flagship opportunistic sponsors will be measured against on their next raise",
         ],
         watch="Deployment pace against the fund's data center and industrial targets, and whether Starwood's next flagship raise references this fund's strategy shift."),
    dict(category="Fundraising", title="Alpaca Real Estate Closes Debut Fund at ~$223M",
         subtitle="A First-Time, AI-Enabled Manager Builds an Institutional LP Base From Scratch",
         date="August 6, 2026",
         trigger=f'''{src("https://www.businesswire.com/news/home/20260806490964/en/Alpaca-Real-Estate-Closes-Debut-Fund-at-Approximately-%24223-Million", "Alpaca Real Estate held the final close of its debut fund at roughly $223 million in commitments")}, plus about $21 million in co-investment to date, targeting infill industrial and high-density residential deals sourced via a proprietary, AI-enabled platform; the firm expects total equity deployed to exceed $300 million, supporting a portfolio approaching $1 billion in AUM, and drew public pensions, RIAs, family offices, and international investors roughly 18 months after first close.''',
         why="A first-time manager successfully building an institutional LP base &mdash; public pensions, RIAs, family offices &mdash; from a standing start is a much harder fundraising path than a flagship sponsor's follow-on close, and this specific debut leaned on a proprietary AI-enabled sourcing platform as its differentiator. It's a useful counterpoint to Starwood's $10.2 billion mega-raise: two very different fundraising stories happening in the same market at the same time.",
         implications=[
             "Confirms institutional LPs will back a genuinely first-time manager when the sourcing thesis is differentiated enough",
             "Provides a real debut-fund benchmark ($223 million, roughly 18 months to close) for other emerging REPE managers",
             "Signals AI-enabled deal sourcing is becoming a credible fundraising differentiator, not just a pitch-deck buzzword",
             "Offers a common career-path data point for REPE professionals considering an eventual spinout into their own platform",
         ],
         watch="Alpaca's initial deployment pace against its infill industrial and high-density residential thesis, and whether it returns to market for a larger Fund II."),
    dict(category="Portfolio Acquisition", title="PCCP and Stonemont Acquire $1B+ Industrial Portfolio From Blackstone's Link Logistics",
         subtitle="A Single Off-Market Transaction Replaces Dozens of One-Off Building Trades",
         date="July 29, 2026",
         trigger=f'''{src("https://commercialobserver.com/2026/07/pccp-stonemount-industrial-portfolio/", "Stonemont and PCCP jointly acquired a 38-building, 5.9 million-square-foot industrial portfolio from Blackstone's Link Logistics platform")} for roughly $1 billion (about $169 per square foot) in an off-market deal spanning 14 markets across 10 states, including Austin, Dallas, Phoenix, and Charlotte, with more than 70 tenants across the assets; the deal was financed with debt from JPMorgan and Wells Fargo, and Eastdil Secured advised.''',
         why="Buying 38 buildings across 14 markets in a single off-market transaction, rather than assembling that footprint building by building, is exactly the kind of platform-scale bet that distinguishes REPE from property-level CRE investing &mdash; the underwriting here is on a diversified, multi-market industrial income stream and a JV capital structure between two sponsors, not on any single asset's local leasing prospects.",
         implications=[
             "Confirms institutional capital is still underwriting large-scale, multi-market industrial portfolios via single transactions",
             "Provides a $169-per-square-foot benchmark for comparable large industrial portfolio trades",
             "Shows how two sponsors (PCCP and Stonemont) structure a joint acquisition and shared debt financing",
             "Signals continued institutional conviction in diversified Sun Belt industrial exposure specifically",
         ],
         watch="Whether PCCP and Stonemont pursue additional joint industrial portfolio acquisitions, and lease-up/renewal activity across the 70-plus existing tenants."),
    dict(category="Portfolio Acquisition", title="TPG AG Real Estate and Redfearn Capital Acquire $628M Industrial Portfolio",
         subtitle="A Second Large-Cap Manager Makes the Same Multi-State Logistics Bet in the Same Window",
         date="August 6, 2026",
         trigger=f'''{src("https://www.tpg.com/news-and-insights/tpg-ag-real-estate-acquires-628m-industrial-portfolio-in-partnership-with-redfearn-capital", "TPG's AG Real Estate unit partnered with Redfearn Capital to acquire a 53-building, roughly 5.4 million-square-foot distribution, logistics, and manufacturing portfolio")} spanning seven states, including Florida, Georgia, North Carolina, Tennessee, Minnesota, Illinois, and Oregon, for $628 million.''',
         why="A second large-cap manager closing a multi-state industrial portfolio acquisition within days of the PCCP/Stonemont deal, rather than an isolated one-off, confirms institutional capital is chasing diversified logistics platforms broadly right now, not just responding to one seller's specific opportunity &mdash; two unrelated buyer groups reaching the same conclusion about the same asset class in the same short window is a stronger signal than either deal alone.",
         implications=[
             "Confirms institutional appetite for multi-state industrial portfolios extends beyond a single buyer or seller",
             "Provides a second, independent basis benchmark ($628 million, 53 buildings) for comparable logistics portfolio trades",
             "Signals large-cap managers are actively competing for diversified industrial platforms across the same target markets",
             "Adds TPG's AG Real Estate unit to the roster of active large-cap industrial portfolio acquirers this cycle",
         ],
         watch="Whether additional large industrial portfolio trades follow in the same states, and how TPG and Redfearn structure asset management across the seven-state footprint."),
    dict(category="Leadership Change", title="Mack Real Estate Group Announces Senior Leadership Promotions and Transitions",
         subtitle="Succession Planning at a Credit-Adjacent Platform Reshuffles Who Runs the Desks Recruits Target",
         date="July 15, 2026",
         trigger=f'''{src("https://finance.yahoo.com/real-estate/articles/mack-real-estate-group-announces-170000594.html", "Mack Real Estate Group named Priyanka Garg, formerly Head of Credit Strategies, as President")}, effective July 1, 2026, while Michael McGillis moved from President to Vice Chairman, retaining his role as President and CFO of NYSE-listed Claros Mortgage Trust; Brett Kaplan and Regina Lubin became Co-Heads of Credit Strategies.''',
         why="Leadership succession at a real estate investment platform with a public-markets-adjacent credit arm is a different kind of signal than a transaction, but it's directly relevant to anyone tracking who actually runs the desks they might recruit into &mdash; a credit-strategies head being promoted to firm president specifically signals where the platform sees its own center of gravity shifting.",
         implications=[
             "Marks a real, dated succession at a major real estate investment platform with a public-markets-adjacent credit arm",
             "Promotes a credit-strategies leader to firm president, a signal of where the platform sees its center of gravity",
             "Keeps continuity at NYSE-listed Claros Mortgage Trust by retaining McGillis in his existing public-company role",
             "Is directly relevant to students and job-seekers tracking leadership at platforms spanning both equity and credit strategies",
         ],
         watch="How the new Co-Heads of Credit Strategies structure splits responsibilities, and whether the leadership transition prompts any further senior-level moves at the platform."),
]

REPE_FINAL_PARAGRAPHS = [
    "Welcome to the first issue of REPE Signal, a new desk covering the fund and ownership layer that sits above any single building &mdash; fund closes, platform M&amp;A, portfolio acquisitions, and sponsor leadership, distinct from CRE Signal's property- and market-level coverage. This inaugural issue spans six weeks of real, dated activity rather than one, since the desk has no prior coverage to build from.",
    "Two platform M&amp;A stories bookend very different playbooks. Bridgepoint's acquisition of Kayne Anderson Real Estate closed alongside a separate GP-stake exit by Goldman Sachs Alternatives' Petershill program, showing how manager ownership trades at multiple levels simultaneously; Milhaus's merger with SRG Residential and acquisition of Broadshore Capital shows an operator-developer buying its way into fund management rather than simply merging with a peer.",
    "Starwood's record $10.2 billion fund close and Alpaca Real Estate's roughly $223 million debut fund describe opposite ends of the same fundraising market &mdash; a flagship sponsor's largest-ever raise, pivoting toward data centers and Sun Belt exposure, alongside a first-time, AI-enabled manager building an institutional LP base from scratch. And two large-cap managers, PCCP/Stonemont and TPG/Redfearn, independently closed multi-state industrial portfolio acquisitions within days of each other, confirming diversified logistics platforms are where institutional capital wants to be deployed right now.",
]
REPE_FINAL_BULLETS = [
    "A platform sale and a separate GP-stake exit closed in the same transaction, showing manager ownership trades at multiple levels at once",
    "Starwood's record $10.2B fund close and Alpaca's ~$223M debut fund show mega-sponsors and first-time managers both raising successfully",
    "Two unrelated large-cap managers closed multi-state industrial portfolio acquisitions within days of each other",
    "An operator-developer (Milhaus) acquired a registered investment adviser to buy its way into fund management, not just merge with a peer",
]

REPE_PAGE = issue_page(
    "repe", False, "REPE", "Signal", "NEW YORK, NY", "AUGUST 10, 2026", "JUNE 29&ndash;AUG 10, 2026",
    REPE_SNAPSHOT, "What Happened", REPE_SIGNALS, REPE_FINAL_PARAGRAPHS, REPE_FINAL_BULLETS,
    "No predictions. No stock references. Platform-anchored interpretation only.",
)

print("REPE page OK", len(REPE_PAGE))

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
    dict(category="M&amp;A", title="Prologis Agrees to Acquire Segro for Roughly &pound;14.0B ($18.8B)",
         subtitle="One of the Largest Cross-Border REIT Combinations of the Year Consolidates European Logistics",
         date="August 3&ndash;4, 2026",
         trigger=f'''{src("https://www.prologis.com/insights-news/press-releases/prologis-announces-recommended-acquisition-segro-plc", "Prologis, the world's largest industrial REIT, struck a recommended acquisition of SEGRO, the UK's largest REIT and a dominant European logistics warehouse owner")}, with Segro shareholders receiving 0.0920 Prologis shares per Segro share (a fixed price of 1,031.7p/share) and a partial cash alternative capped at roughly &pound;3.5 billion; the combined portfolio would span roughly 368 million square feet across Europe.''',
         why="Prologis choosing to combine with, rather than simply compete against, Europe's largest logistics REIT is a statement that scale and pan-European footprint now matter more than organic growth in industrial real estate &mdash; at this size, the deal is also a real test case for how UK takeover code mechanics interact with a US acquirer's all-share-plus-cash structure, a template other cross-border REIT combinations will likely reference.",
         implications=[
             "Creates a combined roughly 368-million-square-foot pan-European logistics portfolio under one owner",
             "Sets a template for UK takeover code mechanics in a US-acquirer, share-plus-cash REIT combination",
             "Signals scale and footprint, not just organic growth, are now the priority in industrial real estate consolidation",
             "Is one of the largest cross-border REIT-to-REIT combinations of the year by deal value",
         ],
         watch="UK regulatory and shareholder approval timelines, and whether a competing bid emerges given SEGRO's scale."),
    dict(category="M&amp;A", title="Curium to Acquire Lantheus in a Deal Worth Up to $8B",
         subtitle="A Cash-Plus-CVR Structure Bridges a Valuation Gap on Milestone-Driven Radiopharma Assets",
         date="August 3, 2026",
         trigger=f'''{src("https://www.bloomberg.com/news/articles/2026-08-03/curium-strikes-deal-to-take-radiopharma-company-lantheus-private", "Radiopharmaceutical giant Curium agreed to take Lantheus Holdings private in a deal worth up to $8 billion")}, paying $102.50 per share in cash upfront plus contingent value rights worth up to $12 per share tied to 2030 sales milestones for Lantheus's prostate cancer and neurology diagnostics and DEFINITY franchise; the deal is expected to close in the first half of 2027.''',
         why="Structuring roughly a fifth of total deal value as contingent value rights, rather than paying it all in cash upfront, lets Curium avoid overpaying if Lantheus's 2030 sales milestones fall short while still giving sellers upside if they're hit &mdash; a textbook example of how acquirers bridge a valuation gap on assets whose value depends heavily on future, binary-ish commercial outcomes rather than current cash flow.",
         implications=[
             "Provides a clean, teachable example of a CVR structure bridging an acquirer/seller valuation gap",
             "Signals continued large-scale consolidation in radiopharmaceuticals and diagnostics",
             "Ties a meaningful share of total deal value directly to 2030 commercial milestones, not paid unconditionally",
             "Sets an up-to-$8 billion benchmark for comparable milestone-driven healthcare M&amp;A this cycle",
         ],
         watch="Whether Lantheus's diagnostics franchises hit the 2030 sales milestones that trigger the full CVR payout, and shareholder/regulatory approval progress toward the H1 2027 close."),
    dict(category="M&amp;A", title="Supernus and Indivior to Combine in All-Stock Merger of Equals",
         subtitle="A Debt-Financed Special Dividend Is Baked Directly Into the Exchange Ratio",
         date="August 3, 2026",
         trigger=f'''{src("https://www.globenewswire.com/news-release/2026/08/03/3337311/0/en/Supernus-Pharmaceuticals-and-Indivior-Pharmaceuticals-to-Merge-Creating-a-Diversified-CNS-Biopharmaceutical-Leader-with-Significant-Scale.html", "Supernus Pharmaceuticals and Indivior agreed to an all-stock merger of equals")}, with each Supernus share converting to 1.5401 Indivior shares and Indivior holders receiving a $1 billion pre-closing special dividend, partly funded via a $650 million Citibank term loan; post-close ownership splits roughly 56.5% Indivior/43.5% Supernus, targeting about $2.2 billion in pro forma revenue and $125 million in cost synergies, with a close expected in Q4 2026.''',
         why="Funding a shareholder dividend with acquired debt before a merger of equals even closes is a specific structural choice that changes the combined company's starting leverage &mdash; it's a way for one side's existing shareholders to extract cash value upfront rather than wait for post-merger synergies to show up in the stock price, and it directly ties M&amp;A structuring to leveraged-finance mechanics in a way straightforward stock-for-stock deals don't.",
         implications=[
             "Demonstrates how a debt-financed special dividend can be built directly into a merger-of-equals exchange ratio",
             "Creates a combined roughly $2.2 billion revenue CNS-focused biopharma platform under a new share structure",
             "Adds real starting leverage to the combined company via the $650 million term loan backing the dividend",
             "Sets a rare-structure precedent (merger of equals plus pre-closing debt-financed dividend) for future pharma combinations",
         ],
         watch="Progress toward the Q4 2026 close and shareholder votes at both companies, and early execution against the $125 million cost-synergy target."),
    dict(category="M&amp;A", title="Nielsen to Acquire DoubleVerify for $2.15B",
         subtitle="A Sponsor-Owned Platform Uses Its Portfolio Company as an Acquisition Vehicle",
         date="August 6&ndash;8, 2026",
         trigger=f'''{src("https://www.nielsen.com/news-center/2026/nielsen-to-acquire-doubleverify-creating-a-leading-independent-media-intelligence/", "Nielsen, itself taken private in 2022 by an Elliott/Brookfield-led consortium, agreed to acquire ad-verification firm DoubleVerify for $13.60 per share in cash")}, a roughly 60% premium to DoubleVerify's 60-day volume-weighted average price, combining audience measurement with ad verification into a business with more than $4 billion in pro forma revenue; the deal is expected to close in Q1 2027.''',
         why="A sponsor-owned platform using its own portfolio company's balance sheet to acquire a public target is a buy-and-build strategy playing out in real time &mdash; Nielsen isn't a strategic acquirer in the traditional sense, it's a private-equity-backed asset being used as the vehicle for further consolidation, which is a useful case study in how sponsors extend a platform's reach beyond the initial take-private.",
         implications=[
             "Illustrates a private-equity-owned platform using its portfolio company as an active acquisition vehicle",
             "Creates a combined media measurement and ad-verification business exceeding $4 billion in pro forma revenue",
             "Sets a roughly 60% premium benchmark for adtech/data-verification take-privates this cycle",
             "Continues Elliott/Brookfield's active build-out of the Nielsen platform since its 2022 take-private",
         ],
         watch="Regulatory review given the combination of two major measurement/verification platforms, and progress toward the Q1 2027 close."),
    dict(category="M&amp;A", title="Eneos to Acquire TPC Group for Roughly $1.3B Enterprise Value",
         subtitle="A Japanese Energy Major Continues Inbound U.S. Petrochemical Consolidation",
         date="August 7, 2026",
         trigger=f'''{src("https://www.bloomberg.com/news/articles/2026-08-07/eneos-acquires-tpc-group-at-1-3-billion-enterprise-value", "Japanese energy major ENEOS Holdings agreed to acquire Houston-based petrochemical processor TPC Group at approximately $1.28 billion enterprise value")}, including debt, gaining Gulf Coast butadiene and C4 hydrocarbon assets and vaulting ENEOS to the world's third-largest butadiene producer; the deal is expected to close in October 2026.''',
         why="A Japanese strategic buyer paying up for U.S. Gulf Coast petrochemical infrastructure, at a moment when much of this cycle's headline M&amp;A has skewed toward tech, healthcare, and financial infrastructure, is a reminder that steady, less headline-grabbing cross-border industrial consolidation keeps happening in the background &mdash; and that Gulf Coast petrochemical assets specifically remain a target for foreign strategics seeking scale in specific feedstock chains.",
         implications=[
             "Continues a pattern of Japanese strategic buyers pursuing inbound U.S. industrial and energy M&amp;A",
             "Vaults ENEOS to the world's third-largest butadiene producer via a single acquisition",
             "Provides a roughly $1.3 billion enterprise-value benchmark for Gulf Coast petrochemical infrastructure",
             "Reinforces that cross-border industrial consolidation continues steadily alongside larger, more headline-driven deals",
         ],
         watch="Regulatory approval progress and integration plans as the deal moves toward its October 2026 close."),
    dict(category="Sponsor Finance", title="EA's $55 Billion Take-Private Buyout Officially Closes",
         subtitle="A Record $20B Single-Bank Debt Commitment Anchors the Largest All-Cash LBO on Record",
         date="August 4, 2026",
         trigger=f'''{src("https://www.ea.com/news/ea-announces-completion-of-acquisition", "Electronic Arts' $55 billion take-private buyout officially closed")}, delisting EA from Nasdaq at $210 per share in cash, funded by roughly $36 billion of equity from Saudi Arabia's Public Investment Fund, Silver Lake, and Affinity Partners, plus $20 billion of debt financing solely committed by JPMorgan Chase; PIF now holds 93.4% of the private entity, Silver Lake 5.5%, and Affinity Partners 1.1%.''',
         why="A single bank committing the entire $20 billion debt tranche, rather than syndicating it across a lending club from the start, is a landmark data point on how much leveraged-finance capacity a top-tier bank is now willing to hold on its own balance sheet for the right sponsor group and asset &mdash; essential context for anyone studying how the largest LBOs in history actually get financed today.",
         implications=[
             "Sets a record for the largest all-cash leveraged buyout on record at $55 billion",
             "Establishes a landmark single-bank debt commitment ($20 billion) as a new reference point for mega-LBO financing capacity",
             "Confirms sovereign wealth capital (PIF) as the dominant equity holder in one of the largest take-privates ever",
             "Provides a real, closed-deal case study in how $50 billion-plus LBO capital structures are actually assembled",
         ],
         watch="How JPMorgan syndicates or retains the $20 billion debt commitment over time, and EA's operating strategy now under private ownership."),
    dict(category="ECM", title="Attovia Therapeutics Prices Upsized $289M IPO, Pops 24% on Debut",
         subtitle="A Strong Biotech IPO Read Signals Reopening Risk Appetite in the ECM Window",
         date="August 5, 2026",
         trigger=f'''{src("https://www.globenewswire.com/news-release/2026/08/05/3338994/0/en/attovia-therapeutics-announces-pricing-of-upsized-initial-public-offering.html", "Clinical-stage immunology biotech Attovia Therapeutics priced an upsized IPO of 17 million shares at $17.00")}, then opened trading around $21.00 on Nasdaq (roughly a $904 million market cap, about a 24% pop); bookrunners were Morgan Stanley, Leerink Partners, Citigroup, and RBC Capital Markets.''',
         why="An upsized biotech IPO that pops roughly 24% on debut, rather than merely holding its offer price, is a materially stronger signal of reopening ECM risk appetite than a deal that simply prices and trades flat &mdash; it tells underwriters and other biotechs waiting in the pipeline that genuine aftermarket demand, not just orderbook padding, is back for clinical-stage names.",
         implications=[
             "Signals genuine aftermarket demand, not just strong bookbuilding, has returned for clinical-stage biotech IPOs",
             "Provides a strong, ~24%-pop comp that other biotechs in the IPO pipeline will reference when timing their own listings",
             "Confirms an upsized deal size (17 million shares) cleared the market without pricing concessions",
             "Adds to a broader 2026 narrative of ECM windows reopening for well-positioned clinical-stage names",
         ],
         watch="Attovia's aftermarket trading performance in the weeks following its debut, and whether other clinical-stage biotechs accelerate IPO timelines in response."),
    dict(category="DCM", title="VICI Properties Prices $1.75B Senior Unsecured Notes Offering",
         subtitle="A Proactive Refinancing Shows Investment-Grade REITs Getting Ahead of Near-Term Maturities",
         date="August 5, 2026",
         trigger=f'''{src("https://investors.viciproperties.com/news-releases/news-release-details/vici-properties-announces-pricing-public-offering-175-billion", "Gaming and experiential REIT VICI Properties priced a two-tranche, $1.75 billion senior unsecured notes offering")} &mdash; $900 million of 5.400% notes due 2031 and $850 million of 5.750% notes due 2036 &mdash; with proceeds refinancing roughly $1.75 billion of 2026 debt maturities; the offering is set to close August 14.''',
         why="Refinancing an entire slate of near-term maturities well ahead of schedule, rather than waiting closer to the due date, is a proactive liability-management move that only investment-grade issuers with reliable bond-market access can execute smoothly &mdash; a clean, teachable example of tranche structuring (splitting a raise across a 2031 and a 2036 maturity) and use-of-proceeds mechanics for anyone learning the DCM side of the business.",
         implications=[
             "Demonstrates proactive liability management, refinancing maturities well ahead of their actual due date",
             "Provides a clean two-tranche structuring example (2031/2036 maturities) for DCM-focused students",
             "Confirms continued reliable investment-grade bond-market access for large experiential/gaming REITs",
             "Sets a fresh IG pricing benchmark (5.400%/5.750%) for comparable REIT unsecured notes issuance",
         ],
         watch="The offering's August 14 close, and whether other IG-rated REITs follow with similarly proactive refinancings of 2026 maturities."),
]

IB_FINAL_PARAGRAPHS = [
    "This week's dealmaking is dominated by large-scale M&amp;A across five very different sectors: Prologis's roughly &pound;14 billion combination with SEGRO in European logistics, Curium's up-to-$8 billion take-private of Lantheus in radiopharma, Supernus and Indivior's merger of equals in CNS biopharma, Nielsen's $2.15 billion acquisition of DoubleVerify in adtech, and ENEOS's roughly $1.3 billion purchase of TPC Group in petrochemicals.",
    "Two of this week's deals are worth studying specifically for their structuring: Curium/Lantheus uses contingent value rights to bridge a valuation gap on milestone-driven diagnostics assets, while Supernus/Indivior bakes a debt-financed special dividend directly into its merger-of-equals exchange ratio. Both are concrete examples of how deal structure, not just headline price, is what actually allocates risk between buyer and seller.",
    "EA's $55 billion take-private officially closing, anchored by a record $20 billion single-bank debt commitment from JPMorgan, is this week's clearest sponsor-finance landmark. Read alongside Attovia's strong biotech IPO debut and VICI's proactive $1.75 billion refinancing, capital markets activity this week spans the full spectrum from the largest LBO on record down to routine, well-executed liability management.",
]
IB_FINAL_BULLETS = [
    "Five separate M&amp;A deals this week span logistics, radiopharma, CNS biopharma, adtech, and petrochemicals",
    "A contingent-value-rights structure and a debt-financed special dividend both show deal structure allocating real risk between buyer and seller",
    "EA's $55 billion take-private closed on a record $20 billion single-bank debt commitment, the largest all-cash LBO on record",
    "A biotech IPO popped roughly 24% on debut, a genuine aftermarket-demand signal beyond just strong bookbuilding",
]

IB_PAGE = issue_page(
    "ib", False, "IB", "Signal", "NEW YORK, NY", "AUGUST 10, 2026", "AUGUST 3&ndash;10, 2026",
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
         date="July 9, 2026",
         trigger=f'''{src("https://www.benzinga.com/markets/private-markets/26/07/60372922/broadcom-anthropic-just-turned-ais-chip-bet-into-somebody-elses-debt-apollo-and-blackstone-hold-the-keys", "Apollo Global Management and Blackstone arranged a roughly $35 billion financing package")} to fund Anthropic's purchase of custom AI chips from Google and Broadcom, structured through a special-purpose vehicle that buys the chips and leases them back to Anthropic via a delayed-draw facility with roughly 16 separate releases over a bit more than a year; Broadcom is backstopping Anthropic's payment obligations on the largest senior tranches, and roughly $15 billion of the package is expected to migrate to the 144A market by early 2027.''',
         why="Structuring chip purchases as a leased special-purpose vehicle, with a delayed-draw facility that releases capital in roughly 16 tranches, lets private credit underwrite AI infrastructure the same way it underwrites any other depreciating, collateral-backed asset &mdash; except the collateral here is custom silicon whose useful economic life and resale value are far less established than a warehouse or an aircraft. Broadcom's backstop on the senior tranches is doing real work: it converts what would otherwise be pure technology-obsolescence risk into a corporate-credit question about Broadcom's own backstop capacity, which is a very different risk private lenders are much more comfortable pricing.",
         implications=[
             "Confirms private credit can underwrite AI infrastructure at a scale rivaling large syndicated bank deals",
             "Converts chip-obsolescence risk into a corporate-backstop credit question via Broadcom's guarantee",
             "Structures the delayed-draw facility to release capital in step with actual chip delivery, not all at once",
             "Sets a template migrating roughly $15 billion of the package into the 144A market for institutional investors by early 2027",
         ],
         watch="Whether the expected 144A migration proceeds on the early-2027 timeline, and how the chips' resale or residual value holds up as tranches draw down."),
    dict(category="Direct Lending", title="BlackRock Arranges $12B+ Private Debt for Meta's AI Data Center via HPS/GIP",
         subtitle="A Traditional Asset Manager's Private-Credit Acquisitions Are Already Originating Megadeals",
         date="July 28&ndash;29, 2026",
         trigger=f'''{src("https://www.bloomberg.com/news/features/2026-07-28", "BlackRock arranged more than $12 billion in private debt financing for one of Meta's AI data centers")}, using its newly-acquired HPS Investment Partners and Global Infrastructure Partners units to originate and structure the facility.''',
         why="BlackRock, a firm best known for public equity and fixed-income index products, originating a $12 billion-plus private-debt megadeal within roughly a year of closing its HPS and GIP acquisitions shows those deals are already generating real origination capability, not just adding AUM on paper. It also confirms hyperscaler AI data center financing has become large and standardized enough that a traditional public-markets giant, not just specialist private credit shops, can compete directly for the biggest deals in the category.",
         implications=[
             "Confirms BlackRock's HPS and GIP acquisitions are already generating megadeal-scale origination capability",
             "Signals hyperscaler AI data center financing is standardized enough to draw traditional asset managers, not just specialists",
             "Sets a $12 billion-plus size benchmark for comparable hyperscaler data center private-debt financings",
             "Reinforces Meta's continued reliance on private credit, alongside bond financing, to fund AI infrastructure buildout",
         ],
         watch="Whether BlackRock's HPS/GIP units originate additional hyperscaler data center financings, and how this facility's terms compare to Meta's other recent bond and private-credit deals."),
    dict(category="Direct Lending", title="Ares Leads $2.2B Second-Lien Loan for MedImpact's Acquisition of Medical Card System",
         subtitle="A Large-Cap Direct Lender Keeps Writing Big Checks Even as Deal Flow Slows Elsewhere",
         date="August 5&ndash;6, 2026",
         trigger=f'''{src("https://www.bloomberg.com/news/articles/2026-08-05/ares-eyes-2-billion-loan-deal-in-slow-year-for-private-credit", "Ares Management is leading a $2.2 billion direct loan, priced roughly 800 basis points over the benchmark rate on a second-lien basis")}, financing pharmacy benefits manager MedImpact Holdings' acquisition of Medical Card System, a Puerto Rico healthcare business Kinderhook Industries has owned since 2022; it's one of the largest private credit deals of 2026 in a roughly $1.8 trillion market.''',
         why="A large-cap direct lender still committing $2.2 billion to a single second-lien healthcare financing, in the same period other data points show industry-wide fundraising and deal-flow deceleration, confirms that private credit activity is concentrating among the biggest platforms rather than slowing uniformly &mdash; scale itself is becoming a competitive advantage in winning the largest available deals.",
         implications=[
             "Confirms large-cap direct lenders are still writing billion-dollar-plus checks even as broader deal flow slows",
             "Signals private credit deal concentration is shifting toward the largest, most scaled platforms",
             "Provides an 800bps second-lien pricing benchmark for comparable healthcare-sector direct loans",
             "Adds to Ares's active 2026 pipeline alongside separately reported financing talks for other large healthcare-adjacent deals",
         ],
         watch="Whether the MedImpact financing closes on the reported terms, and if Ares continues winning similarly large-cap direct lending mandates through the rest of 2026."),
    dict(category="Direct Lending", title="Jane Street Negotiates ~$11B Private Credit Refinancing With PIMCO",
         subtitle="A Non-Sponsor Borrower Turns to Private Credit Specifically to Escape Public Disclosure",
         date="August 6, 2026",
         trigger=f'''{src("https://www.bloomberg.com/news/articles/2026-08-06/jane-street-looks-to-rework-11-billion-debt-into-private-credit", "Market-making giant Jane Street is negotiating with a group of investors including PIMCO to move roughly $11 billion of public debt into a private credit vehicle")}, potentially scaling to $15 billion, to fund further AI infrastructure investment; Jane Street has already committed roughly $6 billion plus a $1 billion equity stake to CoreWeave.''',
         why="A proprietary trading firm, not a private-equity-sponsored company, seeking private credit specifically to sharply limit its disclosure obligations versus quarterly public-market reporting is a genuinely different use case than the sponsor-backed middle-market financings that built the private credit industry &mdash; it shows the asset class's core value proposition (flexibility and confidentiality, not just yield) is now attracting borrowers well outside its traditional base.",
         implications=[
             "Extends private credit's core borrower base beyond sponsor-backed companies to non-sponsor financial firms",
             "Confirms disclosure avoidance, not just pricing or speed, is a standalone reason large borrowers choose private credit",
             "Ties another major AI infrastructure capital commitment (via CoreWeave) directly to a private credit refinancing",
             "Signals PIMCO's continued active role structuring large, non-traditional private credit facilities",
         ],
         watch="Whether the refinancing closes at the reported $11 billion size or scales toward the potential $15 billion, and its final terms once disclosed."),
    dict(category="Documentation", title="Minority Lenders Escalate Suit Over Trinseo's 2023 Priming Transaction",
         subtitle="A Double-Dip Liability Management Exercise Is Now Years of Bankruptcy Litigation",
         date="July 3, 2026",
         trigger=f'''In Trinseo's Chapter 11 case, minority &ldquo;excluded&rdquo; lenders led by CastleKnight Management are suing to unwind the company's 2023 &ldquo;double-dip&rdquo; liability management exercise and a 2025 exchange offer; Trinseo and the Super HoldCo lenders moved to dismiss on June 9 and again June 22, 2026, and CastleKnight filed a follow-on motion on July 3 seeking derivative standing to pursue breach-of-fiduciary-duty and fraudulent-transfer claims in the US Bankruptcy Court for the Southern District of Texas.''',
         why="CastleKnight alleges the 2023 transaction used a sham intercompany loan and an off-market intercreditor agreement to entrench senior lenders and extract value from excluded minority lenders &mdash; the archetypal creditor-on-creditor violence fact pattern, now generating years of litigation rather than a quick negotiated resolution. This matters beyond Trinseo specifically because research on LME litigation has found lenders who fight priming transactions in court recover roughly 14 cents on the dollar versus 57 cents for senior lenders in clean bankruptcies, which is exactly the bet CastleKnight is making by continuing to litigate instead of settling.",
         implications=[
             "Illustrates how a 2023 priming LME can still generate active bankruptcy litigation three years later",
             "Tests whether minority lenders can win derivative standing to pursue fraudulent-transfer claims directly",
             "Provides a real-world data point on the low historical recovery rate for lenders who litigate against LMEs",
             "Signals continued market appetite for aggressive priming transactions despite the litigation risk they create",
         ],
         watch="The court's ruling on CastleKnight's derivative-standing motion, and whether other minority lender groups in comparable LME disputes cite this case as precedent."),
    dict(category="Documentation", title="Private Credit Losing Ground to Bank Refinancings, Bloomberg Reports",
         subtitle="Highly Levered Borrowers Are Now Moving to Syndicated Loans Roughly Three Times More Than the Reverse",
         date="August 8, 2026",
         trigger=f'''{src("https://www.bloomberg.com/news/articles/2026-08-08/private-credit-squeezed-by-bank-refinancings-credit-weekly", "Companies with private-credit loans are refinancing into the syndicated bank loan market roughly three times more often than the reverse flow")}, per Bloomberg's Credit Weekly column, as highly leveraged borrowers chase cheaper capital amid more competitive bank loan pricing.''',
         why="A three-to-one directional flow back toward syndicated bank loans is a real reversal of the &ldquo;private credit is permanently taking share from banks&rdquo; narrative that's underpinned much of the industry's growth pitch &mdash; it doesn't mean private credit is shrinking, but it does mean bank pricing has become competitive enough that borrowers with a real choice are increasingly choosing it, which is a meaningfully different story than one-way disintermediation.",
         implications=[
             "Directly complicates the standard private-credit-taking-share-from-banks recruiting and marketing narrative",
             "Signals bank loan pricing has become competitive enough to win back highly leveraged borrowers with optionality",
             "Suggests private credit's growth may increasingly depend on borrowers without syndicated-market access, not universal share gains",
             "Provides a concrete, directional data point (roughly 3-to-1) rather than a general market-sentiment claim",
         ],
         watch="Whether this refinancing flow direction persists through the rest of 2026, and how private credit managers respond on pricing and terms."),
    dict(category="Secondary Market", title="Bridgepoint Explores &euro;1B+ Private Credit Secondaries Deal",
         subtitle="Even Large, Well-Capitalized Managers Are Seeking Liquidity Through Continuation Vehicles",
         date="August 4, 2026",
         trigger=f'''{src("https://www.bloomberg.com/news/articles/2026-08-04/bridgepoint-explores-1-billion-private-credit-secondaries-deal", "Bridgepoint Group, which manages roughly &euro;17 billion in corporate credit AUM, is exploring selling more than &euro;1 billion of private credit loan positions into a continuation vehicle")}, letting existing LPs cash out while others roll forward; it would rank among the largest private credit secondary sales of the year, coming as Q2 2026 saw record default rates in parts of the private credit market.''',
         why="A well-capitalized, scaled manager seeking a continuation-vehicle exit, rather than holding its positions to maturity, shows that even large private credit managers need liquidity mechanisms for what is structurally an illiquid asset class &mdash; and record Q2 2026 default rates elsewhere in the market are likely pushing secondary buyers to demand steeper discounts, which is a real test of how continuation vehicles price credit risk versus the private equity secondaries market they're modeled on.",
         implications=[
             "Confirms even large, well-capitalized private credit managers need structural liquidity mechanisms",
             "Would rank among the largest private credit secondary sales of the year if completed",
             "Ties rising secondaries activity directly to record Q2 2026 default rates elsewhere in private credit",
             "Tests how continuation-vehicle pricing for credit risk compares to the more established private equity secondaries market",
         ],
         watch="Whether Bridgepoint completes the continuation-vehicle sale and at what discount to par, and if other large corporate-credit managers pursue similar liquidity vehicles."),
    dict(category="Market Structure", title="Dallas and New York Fed to Launch Pilot Survey of Private Credit Market",
         subtitle="Regulators Are Building Their First Systematic Map of a $1.3 Trillion Market",
         date="August 5, 2026",
         trigger=f'''The {src("https://www.newyorkfed.org/newsevents/news/markets/2026/20260805", "Federal Reserve Banks of Dallas and New York announced a voluntary pilot survey of firms with at least $50 million in private-credit AUM lending to U.S. businesses")}, segmenting borrowers into upper-middle, middle, and lower-middle market tiers by EBITDA; the survey follows the Fed's April 2026 request for banks to report private credit exposure, with launch planned after Q3 2026 close and aggregate findings published in Q1 2027.''',
         why="This is the first formal Fed effort to systematically measure the roughly $1.3 trillion direct lending market rather than relying on manager-reported or third-party estimates, and it reflects growing regulatory attention to private credit's size and potential financial-stability implications &mdash; directly relevant context for anyone entering a market regulators are only now beginning to map in a standardized way.",
         implications=[
             "Marks the first systematic Fed effort to measure the private credit market's true scale and composition",
             "Signals growing regulatory attention to private credit's potential financial-stability implications",
             "Segments the market formally by EBITDA tier (upper, middle, lower-middle), a useful standardized framework",
             "Sets up a Q1 2027 published data release that could reshape how the industry's scale is publicly understood",
         ],
         watch="Participation rates once the voluntary survey launches after Q3 2026, and any early signals about what the aggregate findings will show when published in Q1 2027."),
]

CREDIT_FINAL_PARAGRAPHS = [
    "This week's signals show private credit's AI-infrastructure financing wave broadening in borrower type. Apollo/Blackstone's $35 billion Anthropic financing and BlackRock's $12 billion-plus Meta data center loan remain in motion from prior weeks, and now Jane Street &mdash; a proprietary trading firm, not a sponsor-backed company &mdash; is negotiating an $11 billion private credit refinancing specifically to fund further AI infrastructure investment while limiting public disclosure.",
    "Ares's $2.2 billion MedImpact financing is this week's clearest evidence that private credit deal flow is concentrating among the largest platforms rather than slowing uniformly, while the Bloomberg report on borrowers refinancing back into syndicated bank loans roughly three-to-one complicates the standard narrative that private credit is simply taking permanent share from banks.",
    "Bridgepoint's exploration of a &euro;1 billion-plus secondaries sale and the Dallas/New York Fed's new pilot survey both point to a market maturing past its early growth phase: managers now need structural liquidity mechanisms for an illiquid asset class, and regulators are building their first systematic map of a market that's grown too large to track informally.",
]
CREDIT_FINAL_BULLETS = [
    "A proprietary trading firm, not a sponsor-backed company, is negotiating an $11B private credit refinancing to limit public disclosure",
    "A large-cap direct lender committed $2.2B to a single healthcare financing even as broader private credit deal flow slows",
    "Borrowers are refinancing out of private credit into syndicated bank loans roughly three times more than the reverse flow",
    "The Fed is launching its first systematic pilot survey to measure the roughly $1.3 trillion private credit market",
]

CREDIT_PAGE = issue_page(
    "credit", False, "Credit", "Signal", "NEW YORK, NY", "AUGUST 10, 2026", "JULY 28&ndash;AUG 10, 2026",
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
    dict(category="Construction Lending", title="$870M Single-Lender Construction Loan Backs Ultra-Luxury Lake Austin Resort",
         subtitle="One Lender Taking the Entire Stack Is a Bet Few Balance Sheets Can Make",
         date="June 2, 2026",
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
         date="June 3, 2026",
         trigger=f'''{src("https://therealdeal.com/texas/2026/06/03/the-line-hyatt-centric-go-back-to-lenders-at-auction/", "JPMorgan won back The Line Austin, a 428-key downtown hotel, at a Travis County foreclosure auction")} with an unopposed credit bid for the exact $172 million owed on its 2023 loan to an entity tied to Sydell Group before Soho House &amp; Co. acquired the Line brand; it is the third Line-branded hotel to face foreclosure since 2025, following Line DC and Line LA.''',
         why="A lender credit-bidding the full loan balance to take a property back, rather than accepting a discounted third-party bid at auction, signals JPMorgan currently sees more value in owning and repositioning this hotel than in selling into today's soft downtown Austin hospitality buyer pool. That this is the third Line-branded property to hit foreclosure since 2025 also points to trouble at the brand and parent-company level, not just a single asset's local performance.",
         implications=[
             "Signals lenders see more value in owning and repositioning distressed hotel assets than selling at a discount now",
             "Adds downtown Austin's Line hotel to a broader pattern of financial distress at parent company Soho House",
             "Puts a 428-key downtown hotel directly into a bank's real estate-owned portfolio, not a third-party buyer's hands",
             "Signals the brand-level distress at Line hotels is a national pattern, not an Austin-specific problem",
         ],
         watch="Whether JPMorgan re-brands or sells The Line Austin now that it holds the asset directly, and if other Line-branded hotels face similar foreclosure action."),
    dict(category="Distress", title="The Morgan Apartments Heads to Foreclosure After $60.1M Rialto Capital Loan Matures",
         subtitle="A 2021-Vintage Bridge Loan Hits the Maturity Wall Exactly the Way These Loans Were Expected To",
         date="August 3, 2026",
         trigger=f'''{src("https://therealdeal.com/texas/2026/08/03/texas-biggest-loans-head-to-foreclosure-auctions-in-august/", "The Morgan Apartments, a 504-unit complex at 1801 Wells Branch Parkway in Austin, is headed to a Travis County foreclosure auction")} after its owners &mdash; a joint venture of Archway Equities, CAF Capital Partners, and Citymark Capital &mdash; couldn't refinance a 2021-vintage bridge loan at current rates; Rialto Capital Management originated the $60,130,000 loan, which now sits in the FS Rialto 2021-FL3 CRE CLO and is being handled by a special servicer.''',
         why="This is close to a textbook case of the 2021-vintage floating-rate bridge debt maturity wall that CRE debt analysts have been tracking nationally for two years &mdash; a loan originated at the top of the market, structured into a CRE CLO, now unable to refinance at current rates because the sponsor's original business plan and today's cost of capital no longer line up. Watching how the special servicer and CLO structure handle this specific workout is a useful, concrete case study in how that broader maturity-wall story actually plays out loan by loan.",
         implications=[
             "Provides a concrete, dated example of 2021-vintage bridge debt hitting the maturity wall exactly as forecast",
             "Puts the workout decision in the hands of a CRE CLO special servicer rather than a single balance-sheet lender",
             "Adds a 504-unit complex to the pipeline of Austin multifamily assets facing forced ownership change",
             "Signals continued stress specifically among 2021-origination-vintage floating-rate bridge loans in the metro",
         ],
         watch="The foreclosure auction outcome and sale price relative to the $60.1 million loan balance, and how the FS Rialto 2021-FL3 CLO discloses the resulting loss severity."),
    dict(category="Distress", title="Austin Healthcare and Rehabilitation Center Loan Heads to Foreclosure Auction",
         subtitle="Even a Small, Sub-$10M Loan Shows Distress Reaching Non-Multifamily, Non-Hospitality Collateral",
         date="August 3, 2026",
         trigger=f'''{src("https://therealdeal.com/texas/2026/08/03/texas-biggest-loans-head-to-foreclosure-auctions-in-august/", "A $6.5 million loan on the 55-bed Austin Healthcare and Rehabilitation Center at 3509 Rogge Lane")} was named the largest new Travis County loan headed to foreclosure auction this month; the borrower is Houston-based Apollo Healthcare, and the lender is Enclave Equities.''',
         why="A sub-$10 million loan on a small skilled-nursing facility is a very different data point than the mega-loan hotel and multifamily distress stories that usually lead this desk, and that's exactly why it's worth flagging &mdash; it shows real estate credit stress in Austin isn't confined to large, well-covered asset types like hospitality and CMBS-financed multifamily, but is also reaching smaller, specialty-use collateral like healthcare facilities financed by regional private lenders.",
         implications=[
             "Confirms Austin-area loan distress extends to small-balance, specialty-use collateral, not just large multifamily and hotel loans",
             "Shows a regional private lender (Enclave Equities) directly exposed to a skilled-nursing-facility default",
             "Adds healthcare real estate to the list of Austin-metro property types showing credit stress this cycle",
             "Provides a small but real comp for other regional private lenders financing specialty healthcare facilities",
         ],
         watch="The foreclosure auction outcome, and whether other small-balance, specialty-use Austin loans surface with similar distress this month."),
    dict(category="Agency Multifamily", title="Freddie Mac Sends Vacant Foreclosed Austin Apartments to Auction at an 80% Haircut",
         subtitle="A $50M Loan Writing Down to a $9.5M Opening Bid Is a Hard Basis Reset",
         date="June 8, 2026",
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
         date="June 16, 2026",
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
    dict(category="Refinancing", title="Talonvest Arranges $47.6M Loan for Six-Property Texas Self-Storage Portfolio",
         subtitle="A Portfolio Loan With Partial Austin Exposure Shows Self-Storage Still Financeable at Scale",
         date="August 4, 2026",
         trigger=f'''{src("https://www.connectcre.com/stories/talonvest-secures-47-6m-loan-for-6-property-texas-self-storage-portfolio/", "Talonvest Capital arranged a $47.6 million permanent loan for a six-property, more than 600,000-square-foot self-storage portfolio")} spanning five Texas markets including Austin, on behalf of The Jenkins Organization and Clark Investment Group; the financing came from a large bank as a floating-rate structure aligned with the sponsors' long-term hold strategy.''',
         why="A large bank writing a permanent loan across a multi-market self-storage portfolio, rather than financing each asset individually, shows lenders remain comfortable underwriting this property type at a portfolio level &mdash; a meaningfully different risk profile than the single-asset hospitality and multifamily distress dominating this desk, and a reminder that Austin-metro credit conditions vary sharply by property type, not just by submarket.",
         implications=[
             "Confirms self-storage remains a financeable property type at portfolio scale even amid other Austin-metro credit stress",
             "Provides a $47.6 million/six-property benchmark for comparable Texas self-storage portfolio financings",
             "Signals continued large-bank appetite for floating-rate, long-hold self-storage lending specifically",
             "Adds a data point on how sharply Austin-metro lending conditions vary by property type right now",
         ],
         watch="Whether The Jenkins Organization and Clark Investment Group pursue additional self-storage acquisitions financed on a similar portfolio basis."),
]

AUSTIN_DEBT_FINAL_PARAGRAPHS = [
    "This week's Austin lending activity adds two new foreclosure-bound loans to an already-stressed hospitality and multifamily picture. The Morgan Apartments' $60.1 million Rialto Capital loan is close to a textbook case of the 2021-vintage floating-rate bridge debt maturity wall analysts have tracked nationally for two years, while the small, sub-$10 million Austin Healthcare and Rehabilitation Center loan shows that same distress reaching specialty-use collateral well outside the usual multifamily and hospitality headlines.",
    "Read against the Line Austin and Fairmont Austin stories, both still very much in motion from prior weeks, this cycle's Austin debt picture increasingly looks like distress spreading by vintage and structure &mdash; 2021-2023-origination floating-rate loans across multiple property types &mdash; rather than being confined to any single asset class.",
    "Talonvest's $47.6 million self-storage portfolio financing is this week's clearest counter-signal: a large bank underwriting a multi-market portfolio loan at a floating rate shows credit conditions in Austin still vary sharply by property type, with self-storage continuing to clear the debt market on ordinary terms even as hospitality, multifamily bridge debt, and now healthcare collateral show real stress.",
]
AUSTIN_DEBT_FINAL_BULLETS = [
    "Two downtown Austin hotels, The Line and the Fairmont, remain effectively under lender control from prior weeks",
    "A 2021-vintage $60.1M bridge loan on a 504-unit complex hit the maturity wall and is headed to foreclosure",
    "Even a small, sub-$10M skilled-nursing-facility loan is now headed to foreclosure auction in Travis County",
    "A large bank still financed a $47.6M multi-market self-storage portfolio, showing credit conditions vary sharply by property type",
]

REDEBT_NATIONAL_BLOCK_ARCHIVE = market_block_html(
    "redebt", "austin", True, "RE Debt", "Signal", "AUSTIN, TEXAS", "AUGUST 10, 2026", "JUNE 2&ndash;AUG 10, 2026",
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
         date="July 21, 2026",
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
         date="June 2026",
         trigger=f'''{src("https://commercialobserver.com/2026/07/la-studios-distress-hackman-television-city-default-sale/", "Hackman Capital Partners defaulted on a $357 million-plus Deutsche Bank-led loan")} against the 25-acre Television City studio lot in the Fairfax District, with a notice of default filed in June 2026; Hackman and partner Affinius Capital had bought the site from CBS in 2019 for $750 million and planned a roughly $1 billion redevelopment, and Rick Caruso and the Gilmore family are named as potential bidders.''',
         why="A second Hackman-affiliated studio property hitting distress in the same stretch &mdash; alongside Manhattan Beach Studios below, and Goldman Sachs having already taken Hackman's Radford Studio Center after a separate $1.1 billion mortgage default &mdash; shows the Hollywood production slowdown is now hitting one sponsor's studio real estate debt directly and repeatedly, not as an isolated event. A single lender's or sponsor's cluster of defaults across a specific collateral type is a more reliable read on that asset class's health than any one default alone.",
         implications=[
             "Confirms Hollywood production softness is translating directly into studio-lot loan defaults, not just anecdotal reports",
             "Puts a third major Hackman-affiliated studio asset into distress or new ownership within a short stretch",
             "Tests whether named potential bidders like Rick Caruso pursue a discounted acquisition of the site",
             "Signals soundstage collateral now carries real credit risk most CRE lenders rarely underwrite",
         ],
         watch="Whether Television City proceeds to a formal sale process, and which of the named potential bidders emerges as the lead buyer."),
    dict(category="Distress", title="Downtown LA's Metropolitan Building Placed Into Receivership After $32M Default",
         subtitle="A Months-Long Special-Servicer Playbook Reaches Its Next Stage",
         date="July 30, 2026",
         trigger=f'''{src("https://therealdeal.com/la/2026/07/30/downtown-l-a-s-metropolitan-to-receivership-after-default/", "A Los Angeles Superior Court judge granted special servicer LNR Partners' request to place the 88-unit Metropolitan Building")} at 449 South Broadway into receivership, appointing a receiver under a mid-July order; the Fallas family defaulted on roughly $32 million of CMBS debt (originally $31.75 million, a 10-year, interest-only, non-recourse loan originated in 2017), and brokers are now marketing the historic Beaux-Arts building for sale while LNR and the Fallas family continue short-sale talks.''',
         why="This is a clean, real-time illustration of the special-servicer workout playbook students studying CMBS distress should recognize: notice of default, acceleration, judicial foreclosure filing, receivership, and a dual-track sale/foreclosure negotiation running in parallel. That the underlying loan is a decade-old, fixed-structure, interest-only non-recourse deal &mdash; not a floating-rate 2021-2022-vintage loan &mdash; shows even older, conservatively structured CMBS debt isn't immune once a property's operating performance genuinely deteriorates.",
         implications=[
             "Provides a real-time, step-by-step illustration of how CMBS special-servicer workouts actually escalate over months",
             "Shows even decade-old, fixed-rate, interest-only non-recourse loans aren't immune to default and receivership",
             "Puts a historic downtown LA Beaux-Arts building through a dual-track sale and foreclosure process simultaneously",
             "Adds another downtown LA asset to the receivership pipeline alongside Bank of America Plaza",
         ],
         watch="Whether LNR and the Fallas family reach a negotiated short sale before a forced foreclosure sale, and the eventual sale price relative to the $32 million default balance."),
    dict(category="Special Servicing", title="$280M Santa Monica Hotel Loan Heads to Special Servicing",
         subtitle="Even Trophy Hospitality Assets Are Tripping on Maturity-Extension Covenants",
         date="July 15, 2026",
         trigger=f'''{src("https://therealdeal.com/la/2026/07/15/edward-thomas-slatkin-280m-loan-to-special-servicing/", "A $280 million CMBS loan against Shutters on the Beach and Casa del Mar")}, the 327-key Santa Monica hotel duo owned by brothers Edward and Thomas Slatkin, was sent to special servicing after the borrowers said they couldn't meet maturity-extension conditions on top of a separate $120 million mezzanine loan; the Slatkins call special servicer LNR's posture &ldquo;unnecessarily aggressive&rdquo; given what they describe as strong hotel performance.''',
         why="A borrower disputing that its hotels are underperforming, while still landing in special servicing over a maturity-extension covenant, shows how a mezzanine tranche stacked on top of CMBS debt can trigger a workout even when the underlying operating story is genuinely contested &mdash; the covenant, not necessarily the cash flow, is what moved this loan. That this is happening to two of Santa Monica's most recognizable beachfront hotels shows maturity risk in this cycle isn't confined to secondary assets.",
         implications=[
             "Shows maturity-extension covenants, not just cash flow, are triggering special servicing transfers this cycle",
             "Signals mezzanine debt stacked on CMBS loans complicates borrower leverage during a workout",
             "Puts two of Santa Monica's most recognizable beachfront hotels under special servicer oversight",
             "Sets up a public dispute between borrower and servicer over whether performance actually justifies this outcome",
         ],
         watch="Whether the Slatkins and LNR reach a modification or the dispute escalates toward a forced process, and any disclosed occupancy or RevPAR data supporting either side's position."),
    dict(category="Special Servicing", title="$1.1B CMBS Loan on Hudson Pacific/Blackstone's Hollywood Studio Portfolio Hits Special Servicing",
         subtitle="Strong In-Place Cash Flow and a Netflix Anchor Tenant Still Couldn't Beat the Maturity Date",
         date="August 6, 2026",
         trigger=f'''{src("https://crenews.com/2026/08/06/1-1bln-cmbs-loan-on-office-studio-portfolio-in-los-angeles-moves-to-special-servicing/", "A $1.1 billion CMBS loan against Hudson Pacific Properties' and Blackstone's Sunset Studios portfolio")} &mdash; Sunset Gower, Sunset Las Palmas, and Sunset Bronson, plus the Netflix-leased Icon, Cue, and Epic office buildings, roughly 2.23 million square feet total &mdash; transferred to special servicing days ahead of its August 9 maturity; the portfolio is 95.5% leased overall (studio stages 74.6% leased), with HPP holding roughly $566 million of the debt and Blackstone the remainder, and the borrowers have agreed a short-term extension with the special servicer while negotiating a longer-term refinancing.''',
         why="A well-leased portfolio anchored by a credit tenant like Netflix through 2031 still landing in special servicing is a clean illustration that today's refinancing gap is driven by rate and debt-market conditions, not asset quality &mdash; this isn't a story about weak fundamentals, it's a story about a $1.1 billion loan that simply couldn't be refinanced or paid off in time at a workable cost of capital. That distinction matters for how the eventual workout gets priced and negotiated relative to a genuinely distressed asset.",
         implications=[
             "Shows even a Netflix-anchored, 95.5%-leased studio/office portfolio can't outrun a maturity date in this rate environment",
             "Confirms the current wave of large CMBS special servicing transfers is often a refinancing-timing problem, not a fundamentals problem",
             "Puts $1.1 billion of Hudson Pacific/Blackstone Hollywood studio and office debt directly into servicer negotiations",
             "Adds a fourth major Los Angeles studio-adjacent asset to enter distress or special servicing in recent months",
         ],
         watch="Whether Hudson Pacific and Blackstone secure a longer-term refinancing during the extension period, and the eventual terms relative to the original $1.1 billion balance."),
    dict(category="Distressed Note Sale", title="Lenders Shop $240M Mortgage on Manhattan Beach Studios After Default",
         subtitle="The Marketing Pitch Reveals Who the Lenders Think the Real Buyer Is",
         date="July 2026",
         trigger=f'''{src("https://www.bisnow.com/los-angeles/news/industrial/manhattan-beach-studios-being-shopped-as-possible-defense-tech-site-135465", "Deutsche Bank and Kennedy Wilson are marketing for sale the $240 million mortgage on Hackman Capital Partners' Manhattan Beach Studios")} after filing a notice of default, with marketing materials pitching the 15-soundstage lot to defense-tech and aerospace tenants rather than traditional entertainment production.''',
         why="Selling the note, rather than foreclosing and operating the asset directly, lets the lenders exit at whatever price the market clears without taking on landlord risk themselves &mdash; but the marketing angle is the real signal here. Pitching a legacy film-production lot to defense-tech and aerospace tenants is an explicit bet that Los Angeles soundstage demand from traditional entertainment has softened enough that the highest-value use for this asset has shifted to an entirely different industry. Paired with the Television City default above, this is now a pattern across Hackman's studio portfolio specifically, not a one-off.",
         implications=[
             "Signals lender willingness to exit via note sale rather than foreclosure and direct ownership",
             "Confirms defense-tech and aerospace tenants are actively evaluating legacy studio space in the South Bay",
             "Reflects softening traditional entertainment-production demand for large soundstage assets",
             "Extends a pattern of distress across multiple Hackman-affiliated studio properties in the same stretch",
         ],
         watch="The note's eventual sale price and buyer identity, and whether defense-tech lease commitments materialize at the property."),
    dict(category="Construction Lending", title="$85M Construction Loan Backs Beverly Hills Mixed-Use Apartments",
         subtitle="65% Loan-to-Cost in a High-Barrier Submarket Shows Selective Lender Appetite Returning",
         date="June 12, 2026",
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
    "This week's Los Angeles lending activity keeps piling up studio and downtown-office distress. Hackman Capital's Television City default and the Manhattan Beach Studios note sale remain in motion from prior weeks, and now a $1.1 billion CMBS loan on Hudson Pacific and Blackstone's Sunset Studios portfolio has joined them in special servicing &mdash; despite a Netflix anchor tenant and 95.5% overall occupancy, which confirms this wave is largely a refinancing-timing problem, not a fundamentals problem.",
    "Downtown LA office and mixed-use distress is generating harder numbers by the week too. Bank of America Plaza's now-crystallized $175.87 million CMBS loss and the Metropolitan Building's move into receivership are two different downtown assets now working through the special-servicer playbook in real time, one at trophy scale and one at a much smaller, 88-unit scale.",
    "Against all of that, the Beverly Hills construction loan shows fresh capital is still being extended with real conviction in specific, high-barrier submarkets &mdash; a reminder that Los Angeles credit conditions this cycle are tracking asset quality and refinancing timing far more than any single narrative about the market as a whole.",
]
USC_DEBT_FINAL_BULLETS = [
    "A Netflix-anchored, 95.5%-leased $1.1B studio and office portfolio still couldn't outrun its maturity date and hit special servicing",
    "Three Hackman-affiliated studio properties have now hit distress or changed hands under duress in the same stretch",
    "A second downtown LA asset, the Metropolitan Building, is now working through receivership alongside Bank of America Plaza",
    "Selective construction lending is still being extended with real conviction in high-barrier submarkets like Beverly Hills",
]

REDEBT_USC_BLOCK = market_block_html(
    "redebt", "usc", False, "RE Debt", "Signal", "LOS ANGELES, CA", "AUGUST 10, 2026", "JULY 15&ndash;AUG 10, 2026",
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
         date="July 29, 2026",
         trigger=f'''{src("https://crenews.com/2026/07/29/sl-green-eyes-refinancing-245-park-office-in-midtown-manhattan/", "SL Green Realty Corp. began efforts to refinance $1.77 billion of existing mortgage debt")} against 245 Park Avenue, its 1.78 million-square-foot Midtown Manhattan office tower.''',
         why="A refinancing attempt at this scale on a large Class A Midtown tower is a direct test of whether debt capital is willing to underwrite mega-loans on trophy office again, rather than just office debt broadly stabilizing on paper. The eventual lender group, pricing, and proceeds relative to the existing $1.77 billion balance will be closely watched as a read on where office lending has actually normalized versus where it merely looks calmer from the outside.",
         implications=[
             "Functions as a live test case for whether $1.77 billion-scale trophy office refinancings can still clear the market",
             "Sets a size benchmark other large Manhattan office sponsors will reference for their own refinancing timelines",
             "Signals SL Green's confidence that lenders remain willing to underwrite its flagship asset at scale",
             "Provides an early read on proceeds and pricing relative to the existing loan balance once terms are disclosed",
         ],
         watch="The identity of the new lender group once disclosed, and whether proceeds come in at, above, or below the existing $1.77 billion balance."),
    dict(category="Refinancing", title="Blue Owl Capital Provides $106M Refinancing for The Lowell Hotel",
         subtitle="A Major Alternative-Credit Shop Moves Into Trophy NYC Hotel Lending",
         date="August 5, 2026",
         trigger=f'''{src("https://commercialobserver.com/2026/08/blue-owl-capital-106m-refi-lowell-hotel-new-york-city/", "Blue Owl Capital originated a $106 million senior loan to Kensico Properties to refinance existing debt on The Lowell Hotel")}, a 17-story, 74-key luxury boutique hotel at 28 East 63rd Street; CBRE's Matthew Klauer arranged the deal, and the rate was not disclosed.''',
         why="A major alternative-credit shop like Blue Owl writing a senior loan against a trophy Upper East Side boutique hotel, rather than a bank, shows private credit continuing to move into asset classes and geographies that used to be bank-lending territory almost by default. Hospitality lending in particular has stayed selective since the pandemic, so a large, name-brand direct lender underwriting a well-known luxury property is a real data point on where private credit sees opportunity that banks aren't fully filling.",
         implications=[
             "Confirms a major direct lender is willing to underwrite trophy Manhattan hospitality collateral, not just industrial or multifamily",
             "Signals continued private-credit displacement of bank lending in selective real estate categories",
             "Provides a fresh refinancing comp for other trophy Manhattan boutique hotel owners",
             "Adds Blue Owl to the roster of scaled alternative-credit managers actively originating NYC CRE loans this cycle",
         ],
         watch="Whether Blue Owl discloses the loan's rate and term, and if the firm pursues additional Manhattan hospitality financings."),
    dict(category="Refinancing", title="AllianceBernstein Provides $137.5M Refinancing for Bed-Stuy Multifamily",
         subtitle="An Institutional Asset Manager's Floating-Rate Balance-Sheet Loan Backs a Stabilized 421-a Property",
         date="August 3, 2026",
         trigger=f'''{src("https://multifamilyaffordablehousing.com/ejs-hope-street-secure-137-5m-refi-for-brooklyn-development/", "AllianceBernstein provided a three-year, floating-rate $137.5 million refinancing to EJS Group and Hope Street Capital")} for 12 Halsey, a newly completed 240-unit mixed-use multifamily property in Bedford-Stuyvesant, Brooklyn, with 30% of units affordable under the 421-a program; Walker &amp; Dunlop Capital Markets arranged the deal.''',
         why="An institutional asset manager writing a floating-rate balance-sheet loan on a recently delivered, part-affordable Brooklyn multifamily property shows continued institutional lender comfort with 421-a-structured product specifically, at a scale (240 units) large enough to matter for how other outer-borough sponsors underwrite similar mixed-income projects going forward.",
         implications=[
             "Confirms institutional balance-sheet lenders remain active for newly delivered, 421-a-structured Brooklyn multifamily",
             "Provides a $137.5 million refinancing comp for comparable outer-borough mixed-income properties",
             "Signals continued lender comfort with floating-rate structures on recently stabilized assets",
             "Reinforces Walker &amp; Dunlop's continued role arranging institutional multifamily refinancings in Brooklyn",
         ],
         watch="Whether comparable newly delivered, 421-a-structured Brooklyn multifamily properties secure similar institutional refinancing terms."),
    dict(category="Distressed Note Sale", title="OceanFirst Sells $1.3B of NYC Rent-Stabilized Apartment Loans to Cerberus",
         subtitle="A Regional Bank De-Risks Its Rent-Regulated Multifamily Exposure in Bulk",
         date="July 29, 2026",
         trigger=f'''{src("https://crenews.com/2026/07/29/oceanfirst-bank-sells-1-3bln-portfolio-of-new-york-apartment-loans/", "OceanFirst Financial Corp. sold a $1.3 billion portfolio of New York City apartment loans to Cerberus Capital Management")}, with most of the underlying properties subject to New York's rent-stabilization regulations.''',
         why="A regional bank offloading $1.3 billion in rent-regulated multifamily paper in bulk, to a distressed-debt buyer rather than another bank, is a concrete data point on how lenders are de-risking exposure to post-HSTPA rent-stabilized buildings &mdash; an asset class many lenders have quietly repriced as structurally impaired collateral since New York's 2019 rent law changes limited owners' ability to raise rents or recoup renovation costs. Cerberus buying at scale suggests distressed-debt investors see a workable basis in this paper that the originating bank no longer wanted to carry.",
         implications=[
             "Confirms regional banks are actively de-risking rent-stabilized NYC multifamily loan exposure in bulk, not loan-by-loan",
             "Signals distressed-debt buyers like Cerberus see a workable basis in rent-regulated paper banks are exiting",
             "Provides a large, real transaction size benchmark for rent-stabilized loan portfolio sales",
             "May prompt other regional banks carrying similar post-HSTPA exposure to pursue comparable bulk sales",
         ],
         watch="Whether other regional or community banks announce similar bulk sales of rent-stabilized NYC multifamily loans."),
    dict(category="Special Servicing", title="$180M CMBS Loan on Midtown South Office Gets Forbearance",
         subtitle="A Legacy 2015-Vintage Conduit Loan Buys Time Rather Than Heading Straight to a Workout Fight",
         date="August 5, 2026",
         trigger=f'''{src("https://crenews.com/2026/08/05/180mln-cmbs-loan-against-manhattan-office-gets-forbearance/", "The venture that owns the 441,922-square-foot office tower at 261 Fifth Avenue negotiated a forbearance agreement")} with special servicer Midland Loan Services on its $180 million CMBS loan, part of the BACM 2015-UBS7 and MSBAM 2015-C25 deals; the ownership venture is led by BLDG Management and the Feil Organization, with Wells Fargo as master servicer.''',
         why="A forbearance agreement, rather than an immediate escalation toward foreclosure or receivership, shows the borrower and special servicer found enough common ground to buy time on a legacy 2015-vintage conduit loan &mdash; a materially less adversarial outcome than the litigation-heavy or receivership paths other Manhattan and Los Angeles office loans have taken this cycle. It's a useful reminder that not every distressed CMBS office loan ends in a forced sale.",
         implications=[
             "Shows a negotiated forbearance, not litigation or receivership, resolving distress on this legacy conduit loan for now",
             "Adds another Midtown South office asset to the roster of legacy 2015-vintage CMBS loans under active workout",
             "Reinforces Wells Fargo and Midland Loan Services' roles managing distressed legacy conduit exposure",
             "Provides a comparatively borrower-friendly workout comp against the harder-edged distress seen elsewhere this cycle",
         ],
         watch="The forbearance period's length and conditions, and whether the venture secures a permanent refinancing or modification before it expires."),
    dict(category="Construction Lending", title="BXP Closes $1.2B Construction Loan for 343 Madison Ave Office Tower",
         subtitle="A Bank Club Deal Shows Lenders Will Still Fund New Office Supply, With Conditions",
         date="July 28, 2026",
         trigger=f'''{src("https://commercialobserver.com/2026/07/bxp-construction-loan-343-madison-avenue-q2-earnings/", "BXP closed a $1.2 billion construction loan for its 46-story, roughly 930,000-square-foot office tower at 343 Madison Avenue")}, led by Wells Fargo with support from BofA Securities, Bank of New York Mellon, and JPMorgan Chase; the loan carries a four-year initial term plus a one-year extension, an initial rate of Term SOFR plus 2.50% that steps down to plus 2.25% on leasing and construction milestones, and the roughly $2 billion, Grand Central-connected tower is about 50% pre-leased with completion expected in 2029.''',
         why="A major bank club deal financing ground-up trophy office construction, at a moment when office construction lending has been scarce nationally, shows lenders will still underwrite new supply &mdash; but only when it clears a high bar: pre-leased, transit-connected, and built by a top-tier REIT. The rate step-down tied to leasing and construction milestones is itself a signal that lenders are pricing in real execution risk and rewarding de-risking events explicitly, rather than underwriting the project on projected rents alone.",
         implications=[
             "Confirms bank capital will still fund large ground-up office construction when pre-leasing and sponsor quality are strong",
             "Ties borrowing cost directly to leasing and construction milestones, pricing execution risk explicitly into the loan",
             "Sets a $1.2 billion size and multi-bank club structure benchmark for other trophy office construction financings",
             "Reinforces Grand Central-area transit connectivity as a key underwriting factor for new Midtown office supply",
         ],
         watch="Whether 343 Madison's pre-leasing percentage climbs enough to trigger the rate step-down, and construction progress toward the 2029 completion target."),
    dict(category="Construction Lending", title="Vornado, Citadel, and Rudin Land Record $3.3B Construction Loan for 350 Park Avenue",
         subtitle="One of the Largest Construction Loans in NYC History Backs a Supertall Anchored by Its Own Equity Partner",
         date="August 4, 2026",
         trigger=f'''{src("https://therealdeal.com/new-york/2026/08/05/vornado-citadels-350-park-lands-record-financing/", "Ken Griffin (Citadel, 60% stake), Vornado Realty Trust (36%, closing in September), and the Rudin family (4%) locked in a $3.3 billion construction loan")}, among the largest in New York City history, to fund the planned 62-story, roughly 1.9 million-square-foot supertall office tower at 350 Park Avenue, with total project cost around $6 billion; the lender was not disclosed, and Griffin separately extended Vornado a $400 million bridge loan tied to the project.''',
         why="A record-setting construction loan on trophy office, in a market where most office construction lending remains scarce, unlocks specifically because the anchor equity partner is also the anchor tenant's principal &mdash; Ken Griffin's Citadel is both funding and will occupy this building, which removes much of the leasing risk a typical spec office construction loan would carry. That combination of best-in-class collateral and anchor-tenant credit is exactly the kind of deal this cycle's otherwise-cautious construction lenders are still willing to fund at scale.",
         implications=[
             "Sets a record-scale benchmark ($3.3 billion) for trophy office construction lending in this cycle",
             "Shows construction lenders remain willing to fund new office supply when anchor-tenant credit removes leasing risk",
             "Reinforces Park Avenue's continued strength as a location for supertall, anchor-tenant-driven office development",
             "Adds a second major construction loan (alongside BXP's 343 Madison) confirming bank and institutional capital will fund pre-committed new supply",
         ],
         watch="Disclosure of the lender group behind the $3.3 billion loan, and construction milestones as the 62-story tower proceeds."),
    dict(category="Construction Lending", title="LMXD and BedRock Secure $250M Loan for 560-Unit Astoria Housing Development",
         subtitle="A Life Insurer's Balance Sheet Funds Ground-Up Mixed-Income Housing on the Failed Innovation QNS Site",
         date="August 3, 2026",
         trigger=f'''{src("https://commercialobserver.com/2026/08/lmxd-bedrock-250m-loan-35-10-steinway-street-astoria/", "New York Life Investment Management provided a $250 million acquisition and construction loan to LMXD and BedRock Real Estate Partners")} for a 560-unit mixed-income residential project (25% affordable) at 35-10/35-18 Steinway Street in Astoria, Queens &mdash; succeeding the site of the failed Innovation QNS project; JLL arranged the financing, with construction starting this month and completion targeted for 2029.''',
         why="A life-insurance-company balance sheet funding ground-up construction on the site of a previously failed, community-opposed development is a notable vote of confidence in the sponsors' ability to actually deliver where an earlier project couldn't &mdash; and it's a different capital source than the banks and non-bank bridge lenders that dominate this desk's construction-lending coverage, showing life-company capital remains available for large-scale mixed-income multifamily specifically.",
         implications=[
             "Confirms life-insurance-company balance-sheet capital remains available for large-scale mixed-income construction",
             "Succeeds a previously failed development on the same site, a notable underwriting vote of confidence in the new sponsors",
             "Adds 560 units, a quarter affordable, to the Astoria development pipeline with a 2029 completion target",
             "Provides an alternative-capital-source comp distinct from the bank and non-bank bridge lenders dominating recent coverage",
         ],
         watch="Construction progress toward the 2029 completion date, and whether New York Life pursues additional large-scale mixed-income financings in Queens."),
]

NYC_DEBT_FINAL_PARAGRAPHS = [
    "This week's New York lending activity is dominated by construction lending at record scale. Vornado, Citadel, and Rudin's $3.3 billion loan for 350 Park Avenue is among the largest construction loans in city history, and it lands in the same stretch as BXP's $1.2 billion 343 Madison loan and LMXD/BedRock's $250 million Astoria financing &mdash; three very different construction deals, at three very different scales, all confirming lenders will still fund new supply when the underwriting case is strong enough.",
    "SL Green's ongoing $1.77 billion refinancing attempt and the new $180 million 261 Fifth Avenue forbearance are worth reading together as two different points on the same office-debt spectrum: one a live test of whether mega-loans can still clear the market, the other a legacy 2015-vintage loan buying time through negotiation rather than escalating toward a forced sale.",
    "Blue Owl's Lowell Hotel refinancing and AllianceBernstein's 12 Halsey refinancing both show institutional and alternative-credit capital extending fresh refinancing dollars into stabilized assets &mdash; a boutique Manhattan hotel and a newly delivered Brooklyn multifamily property &mdash; even as OceanFirst's $1.3 billion note sale to Cerberus continues the parallel story of banks de-risking rent-regulated exposure in bulk.",
]
NYC_DEBT_FINAL_BULLETS = [
    "A $3.3 billion construction loan for 350 Park Avenue is among the largest in New York City history, anchored by its own equity partner's tenancy",
    "Three separate construction loans, at three very different scales, all confirm lenders will still fund new office and housing supply",
    "A legacy 2015-vintage CMBS loan bought time through forbearance rather than escalating toward foreclosure",
    "A major alternative-credit shop and an institutional asset manager both extended fresh refinancing capital into stabilized NYC assets",
]

REDEBT_NYU_BLOCK = market_block_html(
    "redebt", "nyu", False, "RE Debt", "Signal", "NEW YORK, NY", "AUGUST 10, 2026", "JULY 28&ndash;AUG 10, 2026",
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
         date="July 28, 2026",
         trigger=f'''{src("https://www.globenewswire.com/news-release/2026/07/28/3334210/0/en/Aligned-Data-Centers-Completes-1-18-Billion-Securitization-Financing.html", "Aligned Data Centers closed a $1.183 billion ABS issuance on July 28")}, its first securitization since 2023, upsized roughly 30% from an initial $905 million target; the Class A-2-I and Class B notes carry a five-year anticipated repayment date, backed by four data center campuses with 14 enterprise customers, more than 90% of annualized base rent from investment-grade counterparties.''',
         why="A 30% upsize on a first-since-2023 deal, in the same week a separate BlackRock-led consortium closed its $40 billion acquisition of the same company, shows institutional capital is underwriting Aligned's cash flows from both the equity and structured-debt side simultaneously &mdash; the ABS market's own appetite here is independent confirmation that the M&amp;A price wasn't disconnected from how bond investors view the same collateral. That over 90% of rent comes from investment-grade counterparties is what let the deal price at this scale despite continued questions about AI-datacenter demand durability broadly.",
         implications=[
             "Confirms institutional ABS investor appetite for data center collateral remains strong despite a three-year gap since Aligned's last deal",
             "Shows equity (the BlackRock acquisition) and structured debt investors reached similar conclusions about the same collateral in the same week",
             "Relies on investment-grade tenant credit quality, not speculative AI demand growth, to support the deal's size",
             "Sets a reference point for how much a data center ABS deal can upsize when tenant credit quality is strong enough",
         ],
         watch="Whether other data center operators follow with new issuance given Aligned's demonstrated demand, and how the notes perform in secondary trading."),
    dict(category="Esoteric ABS", title="SEC Guidance Eases Rules for Data Center ABS Securitizations",
         subtitle="A Regulatory Exemption Could Meaningfully Lower Execution Costs for the Next Wave of Deals",
         date="August 3&ndash;4, 2026",
         trigger=f'''{src("https://asreport.americanbanker.com/news/data-center-abs-could-now-see-less-cumbersome-execution-after-sec-guidance", "The SEC concluded, in response to a request from law firm Latham & Watkins, that data center securitizations fall outside the definition of &ldquo;Exchange Act ABS&rdquo;")}, exempting sponsors from the 5% risk-retention requirement, Rule 192 conflict-of-interest restrictions, and the 15Ga-1/15Ga-2 disclosure rules, on the rationale that data center facilities are physical assets that persist beyond note maturity rather than self-liquidating financial collateral.''',
         why="A regulator formally distinguishing data center ABS from conventional self-liquidating collateral, and exempting it from risk-retention and disclosure rules built for mortgage- and auto-style deals, directly lowers the structuring and compliance cost of the next wave of data center securitizations &mdash; a meaningful tailwind for exactly the kind of deal Aligned just priced, and a regulatory precedent other physical-asset ABS categories may eventually seek to invoke.",
         implications=[
             "Directly lowers execution costs for future data center ABS deals by exempting them from risk-retention and disclosure rules",
             "Sets a regulatory precedent distinguishing physical-asset collateral from traditional self-liquidating ABS collateral",
             "Is expected to support desk projections of $30&ndash;40 billion in annual data center ABS supply through 2027",
             "May prompt sponsors in other physical-asset categories to seek similar Exchange Act ABS exemptions",
         ],
         watch="Whether sponsors of upcoming data center ABS deals explicitly structure around this guidance, and if issuance volume accelerates toward the projected $30&ndash;40 billion annual pace."),
    dict(category="Esoteric ABS", title="American Airlines Prices $1.3B Aircraft EETC",
         subtitle="One of the Largest Single Aircraft ABS Prints of the Summer Funds Mostly New Deliveries",
         date="August 5, 2026",
         trigger=f'''{src("https://asreport.americanbanker.com/news/american-airlines-issues-1-3-billion-in-abs-to-finance-mostly-new-aircraft", "American Airlines priced $1.3 billion across two enhanced equipment trust certificate (EETC) trusts")} &mdash; a $1.05 billion Class A tranche rated A- by Fitch and a $273.9 million Class B tranche rated BBB- &mdash; funding 22 new aircraft deliveries through February 2027 plus refinancing of 15 existing aircraft, with roughly 15 joint bookrunners including BNP Paribas, Citigroup, Deutsche Bank, Barclays, BofA, and Goldman Sachs.''',
         why="A large, multi-tranche EETC print with this many joint bookrunners confirms aircraft-backed structured credit remains a deep, liquid execution channel for airline fleet financing even as other transportation-adjacent asset classes see more selective demand &mdash; a useful, dated comp for students studying transportation and equipment-finance ABS as a category distinct from consumer or corporate-loan collateral.",
         implications=[
             "Confirms aircraft EETC issuance remains a deep, liquid financing channel for major airline fleet expansion",
             "Provides fresh A-/BBB- tranche pricing benchmarks for comparable airline EETC issuance",
             "Funds a mix of new deliveries and refinancing of existing aircraft in a single structured transaction",
             "Reinforces transportation/equipment ABS as a distinct esoteric category from consumer or corporate-loan collateral",
         ],
         watch="Whether other major airlines follow with comparable EETC issuance this year, and how the notes perform as the new aircraft are delivered through early 2027."),
    dict(category="Consumer ABS", title="Rocket Prices $513.2M Unsecured Consumer ABS, Its Second CES Deal of the Year",
         subtitle="Closed-End Second AAAs Are Pricing in Line With Non-QM, a Sign of a Maturing Niche",
         date="August 5, 2026",
         trigger=f'''{src("https://asreport.americanbanker.com/news/rockets-unsecured-consumer-loans-support-513-2-million-in-abs", "Rocket priced RKTL 2026-3, a $513.2 million unsecured consumer ABS")} across five KBRA-rated tranches (Class A AAA at 42.72% credit enhancement down to Class E BB at 6.97%), backed by 18,466 unsecured consumer loans with a weighted-average balance of $22,040 and a weighted-average coupon of 12.85%, maturing August 2035.''',
         why="Rocket's fifth unsecured consumer ABS print, in a sector that's been setting issuance records through 2025&ndash;26, is a useful counterpoint to the more esoteric data-center and aircraft ABS above &mdash; it confirms plain-vanilla fintech/marketplace unsecured consumer lending remains a reliably financeable, repeatable ABS category on its own, not just a niche adjacent to the more headline-grabbing esoteric deals.",
         implications=[
             "Confirms unsecured consumer ABS remains a reliably financeable, repeatable issuance category for large originators",
             "Provides a full five-tranche KBRA credit-enhancement ladder (42.72% down to 6.97%) as a fresh pricing comp",
             "Adds to a broader 2025&ndash;26 pattern of record fintech/marketplace unsecured lending ABS issuance",
             "Sets a $22,040 average-balance, 12.85%-coupon benchmark for comparable unsecured consumer loan pools",
         ],
         watch="Rocket's pace of additional unsecured consumer ABS issuance through the rest of 2026, and how RKTL 2026-3 performs in early servicing reports."),
    dict(category="Consumer ABS", title="KBRA Assigns Preliminary Ratings to Lendbuzz's $229.77M Nonprime Auto ABS",
         subtitle="A Fintech Auto Lender Pushes Further Down the Credit Spectrum Than Its Prior Deals",
         date="August 4&ndash;5, 2026",
         trigger=f'''{src("https://finance.yahoo.com/markets/stocks/articles/kbra-assigns-preliminary-ratings-lendbuzz-003700283.html", "KBRA assigned preliminary ratings to Lendbuzz Nonprime Finance Securitization Trust 2026-1")}, a $229.77 million deal across four note classes (Class A credit enhancement 28.50%, Class C 10.00%), backed by retail auto contracts skewing more near-prime/subprime than Lendbuzz's prior securitizations, and including overcollateralization, subordination, a cash reserve account, and excess spread.''',
         why="A fintech auto lender explicitly shifting its collateral pool further down the credit spectrum, disclosed openly in the rating agency's presale materials, is a concrete data point on how far specialty auto lenders are willing to extend credit as they compete for origination volume &mdash; a useful comparison point against Santander's prime-auto CLN activity, showing the auto-lending credit spectrum moving in different directions at different platforms simultaneously.",
         implications=[
             "Confirms Lendbuzz is extending credit further down the risk spectrum than its earlier securitizations",
             "Provides a fresh, transparent credit-quality data point via KBRA's structured overcollateralization and enhancement levels",
             "Adds a near-prime/subprime auto ABS comp distinct from the prime-focused Santander CLN program covered previously",
             "Signals continued fintech auto lender appetite for underserved, harder-to-underwrite borrower segments",
         ],
         watch="How Lendbuzz's nonprime collateral pool performs relative to its prior deals once early servicing data is available."),
    dict(category="Rating Action", title="Over 400 CLOs Lined Up for Upgrades After Fitch and Moody's Methodology Changes",
         subtitle="A Methodology-Driven Wave of Upgrades Raises a Real 2008-Adjacent Question",
         date="July 15, 2026",
         trigger=f'''{src("https://www.bloomberg.com/news/articles/2026-07-15/over-400-clos-tabbed-for-upgrade-in-pivot-that-fans-08-fears", "Over 400 CLOs are lined up for ratings upgrades")} after Fitch (June 1) and Moody's (June 5) each proposed CLO ratings-methodology changes reflecting years of actual defaults running below what the agencies' models had predicted &mdash; Fitch's change affecting up to 15% of the CLOs it rates, Moody's affecting roughly a third of the tranches it assesses; the scale and speed of the shift has drawn explicit comparisons to pre-2008 ratings methodology loosening.''',
         why="An upgrade wave driven by a methodology recalibration, rather than by improved underlying collateral credit at each individual deal, decouples the rating itself from loan-level credit quality in a way that's structurally different from a normal rating action &mdash; the loans didn't get safer overnight, the model's assumptions about them changed. That's precisely the mechanism critics are flagging as reminiscent of pre-2008 methodology loosening, and it's a critical distinction for anyone learning to read CLO tranche ratings as a signal rather than accepting them as a fixed technical fact.",
         implications=[
             "Decouples this wave of ratings upgrades from any actual improvement in underlying loan-level collateral credit",
             "Affects up to 15% of Fitch-rated CLOs and roughly a third of Moody's-assessed tranches simultaneously",
             "Draws explicit market comparisons to pre-2008 ratings methodology loosening, a meaningful credibility risk for the agencies",
             "Requires investors to distinguish model-driven upgrades from genuine collateral performance improvements going forward",
         ],
         watch="How quickly the 400-plus flagged upgrades are actually executed, and whether other rating agencies propose similar methodology recalibrations."),
    dict(category="CLO", title="European CLO Managers Push Back on Aggressive Loan Pricing and Looser Documentation",
         subtitle="Negotiating Leverage Is Shifting Back Toward CLO Managers After a Long Borrower-Friendly Stretch",
         date="August 6, 2026",
         trigger=f'''{src("https://www.bloomberg.com/news/articles/2026-08-06/clos-managers-push-back-on-aggressive-pricing-looser-documents", "European CLO managers are resisting borrower-friendly loan terms")}, per Bloomberg, citing a Spanish waste-management company that dropped a proposed &euro;200 million add-on to its loan in late July after manager pushback, and a Cinven-owned portfolio company that removed a covenant that would have let it blacklist certain law firms in a distress scenario.''',
         why="Specific, named examples of borrowers withdrawing proposed loan add-ons and stripping out borrower-favorable covenants after CLO manager pushback are concrete evidence that negotiating leverage is shifting, at least at the margin, back toward the debt-buyer side after a long stretch of borrower-friendly terms &mdash; the underlying loan documentation quality is exactly what determines a CLO's actual collateral risk, so this kind of pushback matters more to eventual CLO performance than headline spread levels alone.",
         implications=[
             "Provides concrete, named examples of CLO managers successfully resisting borrower-friendly loan terms",
             "Signals negotiating leverage is shifting back toward debt buyers after an extended borrower-friendly stretch",
             "Improves underlying loan documentation quality, which directly affects eventual CLO collateral risk",
             "May extend from Europe to U.S. CLO managers if the same dynamic plays out in domestic leveraged loan markets",
         ],
         watch="Whether U.S. CLO managers show similar documentation pushback in upcoming deals, and if the trend continues through the rest of 2026."),
    dict(category="Warehouse Facility", title="Empire Asset Finance Closes First Institutional Warehouse Facility With Bank OZK",
         subtitle="A Textbook Warehouse-to-ABS Pipeline Deal, Even Without a Disclosed Size",
         date="July 20, 2026",
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
    "This week's signals show data center ABS becoming a genuine, standalone category rather than a one-off. Aligned's $1.183 billion print, still fresh from prior weeks, now has direct regulatory tailwind behind it: the SEC's guidance exempting data center securitizations from Exchange Act ABS risk-retention and disclosure rules should lower execution costs for the next wave of deals, alongside American Airlines' large aircraft EETC as a reminder that esoteric, physical-asset-backed ABS spans well beyond data centers alone.",
    "Rocket's unsecured consumer ABS and Lendbuzz's nonprime auto ABS describe two ends of the same consumer-lending spectrum: one a large, plain-vanilla, repeatable issuance program, the other a fintech auto lender explicitly disclosing a shift further down the credit spectrum. Read together, they're a useful reminder that consumer ABS collateral quality varies as much by issuer strategy as by asset type.",
    "The CLO ratings-methodology story remains this issue's most consequential for how to actually read a rating, and this week's European CLO documentation pushback adds a second, related thread: negotiating leverage over loan terms &mdash; the thing that actually determines a CLO's collateral risk &mdash; may be shifting back toward managers after a long borrower-friendly stretch.",
]
STRUCTURED_FINAL_BULLETS = [
    "SEC guidance easing rules for data center ABS should lower execution costs for the next wave of deals, supporting projected $30-40B in annual issuance",
    "A large aircraft EETC print and two consumer ABS deals show esoteric and consumer ABS both remain deep, active issuance channels",
    "A methodology-driven wave of 400-plus CLO upgrades continues to decouple ratings from loan-level credit quality this cycle",
    "European CLO managers are pushing back on borrower-friendly loan terms, a possible shift in negotiating leverage after a long stretch the other way",
]

STRUCTURED_PAGE = issue_page(
    "structured", False, "Structured", "Signal", "NEW YORK, NY", "AUGUST 10, 2026", "JULY 20&ndash;AUG 10, 2026",
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
         date="Week of July 16, 2026",
         trigger=f'''{src("https://commercialobserver.com/2026/07/citi-conduit-cmbs/", "Citigroup priced the $816.9 million Citigroup Commercial Mortgage Trust 2026-MFAM1")} the week of July 16, the largest single-bank-originated, multifamily-only conduit transaction since the financial crisis, comprising 27 five-year interest-only loans across 27 multifamily properties with New York, Los Angeles, and Florida as the top three markets represented; AAA bonds priced at swaps plus 80 basis points, 8 basis points tighter than a comparable May 2026 deal, with average Fitch loan-to-value at 123.4%.''',
         why="A bank's own top-market rankings in a conduit deal reveal where its origination pipeline actually found qualifying volume, not just where multifamily lending happens broadly &mdash; and pricing 8 basis points tighter than a comparable deal from two months earlier shows AAA investor demand improved in that short window even as single-asset, single-borrower deals now make up roughly three-quarters of private-label CMBS issuance, making this diversified pool a rarer structure investors were evidently glad to see.",
         implications=[
             "Confirms Citi's own multifamily origination pipeline is deepest in New York, Los Angeles, and Florida specifically",
             "Signals AAA CMBS investor demand improved measurably in the eight weeks since a comparable May 2026 print",
             "Provides institutional investors a rare diversified multifamily pool as SASB deals dominate private-label issuance",
             "Sets a tighter spread benchmark for the next large bank-originated multifamily conduit deal"
         ],
         watch="Whether other banks follow with comparable large multifamily-only conduit deals, and loan-level performance disclosures as the pool seasons."),
    dict(category="CMBS SASB", title="Starwood Prices $482.5M Single-Family Rental Securitization, Its Fifth",
         subtitle="Repeat Institutional SFR Issuance Confirms a Durable, Financeable Asset Class",
         date="July 15, 2026",
         trigger=f'''{src("https://www.businesswire.com/news/home/20260715232837/en/KBRA-Assigns-Preliminary-Ratings-to-STAR-2026-SFR8", "KBRA assigned preliminary ratings on July 15 to Starwood's STAR 2026-SFR8")}, a single-borrower single-family-rental securitization backed by one $482.5 million floating-rate loan secured by 1,749 properties (1,756 units) across ten states, with Atlanta, Phoenix, and Charlotte as the top three markets; aggregate broker price opinion value is $651.7 million, producing a nominal loan-to-value of 74.0% and a KBRA-adjusted LTV of 77.1%.''',
         why="A fifth KBRA-rated SFR securitization from the same institutional sponsor confirms single-family rental has become a durable, repeat-financeable asset class within the SASB market, not a one-time structural experiment &mdash; and that durability matters specifically because it's happening even as more conventional office and retail CMBS collateral faces elevated distress, showing capital markets access for institutional SFR ownership hasn't followed the broader CMBS credit story downward.",
         implications=[
             "Confirms institutional single-family rental ownership remains durably financeable via repeat securitization",
             "Signals SFR capital markets access is holding up even as conventional office and retail CMBS face distress",
             "Concentrates collateral risk in Sunbelt growth markets (Atlanta, Phoenix, Charlotte) specifically",
             "Provides a fifth data point on Starwood's SFR program pricing and structure for comparable sponsors",
         ],
         watch="Whether other institutional SFR operators follow with comparable repeat securitizations, and regional rent performance across the ten states in the collateral pool."),
    dict(category="Non-Agency RMBS", title="Lone Star Prices $505M Non-QM RMBS as Spreads Tighten",
         subtitle="A Senior Tranche Tightening From Initial Guidance Signals Continued Strong Investor Demand",
         date="July 29, 2026",
         trigger=f'''{src("https://www.globalcapital.com/securitization/article/2goz6trnx25rv8kgcnta8/securitization/rmbs/lone-star-prices-505m-non-qm-securitization", "Lone Star priced a $505 million non-QM RMBS transaction")}, with the senior Class A tranche tightening to 125 basis points over the benchmark from wider initial price talk.''',
         why="A senior tranche tightening meaningfully from initial guidance, rather than pricing flat to talk, is a direct read on real-time investor demand at the point of sale &mdash; it confirms non-QM RMBS spread compression is continuing into the back half of the summer, not just holding at prior levels, which matters for how the next wave of non-QM issuers time and price their own deals.",
         implications=[
             "Confirms non-QM RMBS spread tightening is continuing into the back half of the summer, not just holding flat",
             "Provides a fresh 125bps senior-tranche pricing benchmark for comparable non-QM RMBS issuance",
             "Signals strong real-time investor demand at the point of sale, not just healthy order books at initial guidance",
             "Adds another distinct non-QM issuer to the roster of active private-label RMBS shelves this cycle",
         ],
         watch="Whether subsequent non-QM RMBS deals continue tightening from initial guidance at a similar pace."),
    dict(category="Non-Agency RMBS", title="Bayview Prices $404M Closed-End Second Securitization, Its Second of 2026",
         subtitle="CES AAA Pricing Is Converging Toward Non-QM Levels as the Niche Matures",
         date="August 3, 2026",
         trigger=f'''{src("https://www.globalcapital.com/securitization/article/2gpqvg3kz2sqxl0pwvrb4/securitization/rmbs/bayview-prices-its-404m-second-ces-securitization-of-the-year", "Bayview priced its second closed-end second-lien (CES) RMBS deal of 2026, a $404 million transaction")}, with AAA tranche pricing converging toward levels typically seen on non-QM deals.''',
         why="AAA pricing on closed-end second-lien RMBS converging toward first-lien non-QM levels is a sign this fast-growing niche is maturing into a more standardized, better-understood asset class in investors' eyes &mdash; when a newer product's top tranche prices in line with an established comparable, that's usually a sign the market has developed enough of a track record to stop demanding a meaningful complexity premium.",
         implications=[
             "Signals the closed-end second RMBS niche is maturing toward pricing parity with established non-QM deals",
             "Confirms Bayview as a repeat, programmatic issuer in the CES space with its second 2026 deal",
             "Provides a $404 million size and AAA-pricing benchmark for comparable second-lien RMBS issuance",
             "Adds evidence that non-agency RMBS product diversification (beyond first-lien non-QM) is gaining real investor acceptance",
         ],
         watch="Whether AAA CES pricing continues converging with non-QM levels on subsequent deals, and if other issuers scale up CES issuance in response."),
    dict(category="Non-Agency RMBS", title="KBRA Rates PennyMac's $348.2M Prime RMBS Deal",
         subtitle="Prime, Agency-Eligible Private-Label Issuance Stays Active Alongside the Non-QM Boom",
         date="August 5, 2026",
         trigger=f'''{src("https://finance.yahoo.com/real-estate/articles/kbra-assigns-preliminary-ratings-pmt-221600847.html", "KBRA rated 44 classes of notes for PennyMac Corp.'s PMT Loan Trust 2026-CNF7")}, a roughly $348.2 million prime, agency-eligible conforming RMBS deal backed by 669 fully-amortizing, mostly 30-year fixed loans, with a weighted-average original LTV of 71.9% and a weighted-average credit score of 776.''',
         why="Continued private-label issuance of prime, agency-eligible conforming loans &mdash; rather than routing them entirely through Fannie Mae or Freddie Mac &mdash; shows large originators like PennyMac still find it economical to securitize this pristine collateral outside the agency system when pricing works, a useful counterpoint to the desk's heavier recent coverage of non-QM and CES issuance specifically.",
         implications=[
             "Confirms prime, agency-eligible private-label RMBS issuance remains active alongside the non-QM boom",
             "Provides a strong 776 weighted-average credit score and 71.9% LTV benchmark for comparable prime shelf deals",
             "Signals PennyMac continues finding private-label execution economical for pristine conforming collateral",
             "Diversifies this desk's recent coverage beyond non-QM and second-lien product into prime issuance",
         ],
         watch="Whether PennyMac maintains a similar pace of prime private-label issuance through the rest of 2026."),
    dict(category="Rating Action", title="Late-Paying CMBS Loans Spike to 8.01% in July, a Leading Stress Indicator",
         subtitle="A Forward-Looking Delinquency Metric Is Flashing Ahead of the Next Formal Print",
         date="August 3, 2026",
         trigger=f'''{src("https://crenews.com/2026/08/03/large-volume-of-late-paying-loans-in-july-causes-spike-in-cmbs-delinquencies/", "Trepp reported that 8.01% of CMBS loans were 30-plus days late in July")}, a sharp jump attributed to a large new wave of late payments during the month, ahead of the next formal, official delinquency-rate release.''',
         why="This 30-day-plus late-payment figure is a different, earlier-stage metric than the headline delinquency rate this desk has tracked previously &mdash; it captures loans just starting to slip before they're formally classified as delinquent, which makes it a genuine leading indicator rather than a restatement of already-known stress, and worth watching specifically for whether it turns into a higher formal delinquency print next cycle.",
         implications=[
             "Provides a leading, earlier-stage stress indicator distinct from the formal monthly CMBS delinquency rate",
             "Signals a meaningful new wave of loans slipping into late-payment status during July specifically",
             "Sets up a real test of whether this spike translates into a higher formal delinquency rate next reporting cycle",
             "Adds a second, complementary Trepp data series worth tracking alongside the headline delinquency figure",
         ],
         watch="Whether the next formal monthly CMBS delinquency print reflects a comparable jump, confirming this leading indicator's signal."),
    dict(category="Rating Action", title="Pre-2016 CMBS Mall Loans Show a Stark Vintage Delinquency Divide",
         subtitle="Legacy Enclosed-Mall Collateral Remains the Sector's Weakest Link by a Wide Margin",
         date="July 30, 2026",
         trigger=f'''{src("https://crenews.com/2026/07/30/older-cmbs-mall-loans-see-greater-delinquency/", "Trepp data shows enclosed-mall CMBS loans originated in 2016 or earlier carry a far higher delinquency rate than 2017-and-later vintages")}, underscoring a stark vintage divide within mall CMBS performance specifically.''',
         why="A vintage-based delinquency split within a single property type isolates origination-era underwriting standards as the driver of distress, independent of the property type's overall health &mdash; it's a reminder that &ldquo;mall CMBS is distressed&rdquo; as a blanket statement obscures a much sharper, more useful fact: it's specifically the oldest-vintage loans dragging down the category's aggregate numbers.",
         implications=[
             "Isolates loan vintage, not just property type, as a key driver of mall CMBS distress specifically",
             "Confirms legacy pre-2016 enclosed-mall collateral remains the CMBS sector's weakest link by a wide margin",
             "Provides investors a vintage-based framework for underwriting remaining mall CMBS exposure more precisely",
             "Adds needed nuance to the broader, often oversimplified narrative that all mall CMBS is uniformly distressed",
         ],
         watch="Whether the vintage-based delinquency gap narrows or widens further as pre-2016 mall loans continue working through maturity."),
    dict(category="Rating Action", title="CMBS Conduit Loan Payoff Rate Hits a Four-Year High of 72.05%",
         subtitle="A Positive-Signal Metric Offers a Genuine Counterpoint to the Delinquency Headlines",
         date="August 7, 2026",
         trigger=f'''{src("https://crenews.com/2026/08/07/cmbs-conduit-loan-payoff-rate-reaches-highest-level-in-4-years/", "Trepp reported the on-time CMBS conduit loan payoff rate rose to 72.05% in July, up from 63.7% in June")}, the highest level in four years.''',
         why="A four-year-high payoff rate, tracked at the same time as this week's rising 30-day delinquency and legacy mall-loan stress, shows CMBS performance data genuinely pulling in different directions depending on which slice you look at &mdash; refinancing conditions are clearly improving enough to let more conduit loans pay off in full at maturity, even as other parts of the market show real, concurrent stress.",
         implications=[
             "Confirms refinancing conditions have improved enough to lift the conduit payoff rate to a four-year high",
             "Provides a genuine positive counterpoint to this week's delinquency and legacy mall-loan distress data",
             "Shows CMBS performance metrics diverging by measure, not moving uniformly in one direction",
             "Sets a fresh 72.05% payoff-rate benchmark to track against future monthly Trepp releases",
         ],
         watch="Whether the payoff rate holds above 70% in subsequent months, and how it interacts with the elevated late-payment figures reported the same week."),
]

SECURITIZED_FINAL_PARAGRAPHS = [
    "This week's non-agency RMBS issuance spans the full credit spectrum at once: Lone Star's tightening non-QM print, Bayview's closed-end second deal pricing toward non-QM levels, and PennyMac's prime, agency-eligible conforming shelf all cleared the market in the same stretch, showing private-label RMBS demand is broad-based right now, not concentrated in any single credit tier.",
    "This week's CMBS performance data pulls in genuinely different directions depending on which metric you look at. A leading 30-day late-payment figure spiked to 8.01% in July, and legacy pre-2016 mall loans continue showing far worse delinquency than newer vintages &mdash; but the conduit loan payoff rate simultaneously hit a four-year high of 72.05%, confirming refinancing conditions are real even as other slices of the market show concurrent stress.",
    "Read together with the Citi conduit deal and Starwood's fifth SFR securitization, both still very much in motion from prior weeks, this issue's throughline is a market where new issuance keeps clearing across nearly every collateral type, even as the underlying performance data on existing loans stays genuinely mixed rather than uniformly improving or worsening.",
]
SECURITIZED_FINAL_BULLETS = [
    "Non-agency RMBS issuance cleared across the full credit spectrum this week, from non-QM to closed-end second to prime conforming",
    "A leading 30-day late-payment metric spiked to 8.01% in July, ahead of the next formal delinquency-rate print",
    "Pre-2016 vintage mall CMBS loans remain far more delinquent than newer vintages, isolating origination era as the key driver of distress",
    "The CMBS conduit loan payoff rate hit a four-year high of 72.05%, a genuine positive counterpoint to this week's delinquency data",
]

SECURITIZED_PAGE = issue_page(
    "securitized", False, "Securitized", "Signal", "NEW YORK, NY", "AUGUST 10, 2026", "JULY 15&ndash;AUG 10, 2026",
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
    ("repe", "REPE"),
    ("redebt", "RE Debt"),
    ("ib", "IB"),
    ("credit", "Credit"),
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

ABOUT_REPE = about_block_html(
    "repe", False,
    "What Is Real Estate Private Equity?",
    "The fund and ownership layer sitting above any single building.",
    [
        "Real estate private equity (REPE) is the business of raising pooled capital &mdash; from pension funds, endowments, and other institutional investors &mdash; into a fund, then deploying it to buy, reposition, or take entire real estate companies private. It's a level up from any single building: REPE Signal covers funds, platforms, and portfolios, while CRE Signal covers individual properties and markets.",
        "A REPE fund typically targets a specific risk-return profile &mdash; core (stabilized, low-risk), value-add (needs repositioning), or opportunistic (development or distress, higher risk and return) &mdash; and raises a fixed pool of capital with a defined life, usually 7 to 10 years, that it must eventually return to its investors.",
        "Recruiting into REPE usually means acquisitions (sourcing and underwriting deals), asset management (executing a fund's business plan once a deal closes), or investor relations/fundraising (raising the next fund). It sits adjacent to, but distinct from, both the property-level work in CRE Signal and the lending work in RE Debt Signal.",
    ],
    [
        ("GP / LP", "&mdash; the general partner runs the fund and makes decisions; limited partners supply the capital and don't."),
        ("Dry powder", "&mdash; capital a fund has raised but not yet deployed into deals."),
        ("Continuation vehicle", "&mdash; a new fund created to let a GP hold an asset longer while giving existing LPs a chance to cash out."),
        ("Take-private", "&mdash; a PE sponsor buying a publicly traded company (like a REIT) and delisting it from the stock market."),
    ],
    "repe", "REPE Signal",
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
{ABOUT_REPE}
{ABOUT_REDEBT}
{ABOUT_IB}
{ABOUT_CREDIT}
{ABOUT_STRUCTURED}
{ABOUT_SECURITIZED}
</div>
</section>'''

print("About page OK", len(ABOUT_PAGE))

# ============================================================== FROZEN ARCHIVE SNAPSHOTS (week of Jul 29, 2026) ==============================================================

CRE_SNAPSHOT_0729 = [
    ("Development Activity", "rising"),
    ("Office Pipeline", "stable"),
    ("Industrial Momentum", "rising"),
    ("Mixed-Use Activity", "rising"),
    ("Capital Availability", "stable"),
    ("Infrastructure Relevance", "rising"),
]

USC_SNAPSHOT_0729 = [
    ("Development Activity", "rising"),
    ("Office Pipeline", "stable"),
    ("Industrial Momentum", "stable"),
    ("Mixed-Use Activity", "rising"),
    ("Capital Availability", "stable"),
    ("Infrastructure Relevance", "stable"),
]

NYC_SNAPSHOT_0729 = [
    ("Development Activity", "rising"),
    ("Office Pipeline", "rising"),
    ("Industrial Momentum", "stable"),
    ("Mixed-Use Activity", "rising"),
    ("Capital Availability", "stable"),
    ("Infrastructure Relevance", "stable"),
]

NYC_DEBT_SNAPSHOT_0729 = [
    ("CRE Lending Volume", "stable"),
    ("Construction Financing", "rising"),
    ("CMBS Issuance", "stable"),
    ("Agency Multifamily Activity", "rising"),
    ("Credit Availability", "stable"),
    ("Residential Credit (Non-QM / Jumbo)", "stable"),
]

IB_SNAPSHOT_0729 = [
    ("M&amp;A Deal Volume", "rising"),
    ("IPO Pipeline", "rising"),
    ("Leveraged Loan Issuance", "stable"),
    ("Sponsor (PE) Activity", "rising"),
    ("Advisory Fee Pool", "stable"),
    ("Underwriting Conditions", "rising"),
]

CREDIT_SNAPSHOT_0729 = [
    ("Direct Lending Volume", "rising"),
    ("Spread Tightening", "rising"),
    ("Covenant Looseness", "stable"),
    ("Sponsor Demand", "rising"),
    ("Fundraising / Dry Powder", "stable"),
    ("Secondary Market Liquidity", "rising"),
]


CRE_SIGNALS_0729 = [
    dict(category="Industrial", title="Amazon Confirmed as Anchor Behind Southeast Austin Mega-Project",
         subtitle="A $5.6 Billion Infrastructure Package Follows the Tenant, Not the Other Way Around",
         date="July 23, 2026",
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
         date="July 7, 2026",
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
         date="July 13, 2026",
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
         date="July 27, 2026",
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
         date="July 24, 2026",
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
         date="July 28, 2026",
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

CRE_FINAL_PARAGRAPHS_0729 = [
    "This week's Austin activity splits into two distinct stories: large corporate users continuing to make multi-year commitments to specific corridors, and institutional owners actively recycling capital out of otherwise-healthy assets. Amazon's TIRZ financing, Tesla's industrial lease, and two master-planned-community transactions all reflect long-horizon conviction; Brandywine's back-to-back sale of a fully-leased office tower and a 93%-leased apartment complex reflects the opposite instinct.",
    "The Hines and Brandywine signals are worth reading together. A full-price, $733/SF trophy office trade and a stabilized apartment sale happening at the same company, in the same disposition program, in the same month, show that even sponsors with strong in-place performance are choosing to de-lever in Austin right now &mdash; not because the assets are underperforming, but because converting stabilized cash flow into cash is the priority.",
    "Project Connect's scope reduction is the story with the longest tail. A shorter route, no subway, no airport connection, and a cost estimate that grew even as scope shrank all narrow the set of land that can credibly underwrite against confirmed future rail access &mdash; a material downgrade from what voters approved in 2020, worth remembering every time a station-area land deal cites Project Connect as a value driver.",
]

CRE_FINAL_BULLETS_0729 = [
    "Amazon's TIRZ financing and Tesla's industrial lease are both multi-year corridor bets, not short-term demand responses",
    "Brandywine is recycling capital out of a fully-leased office tower and a 93%-leased apartment complex in the same program",
    "A full-price, $733/SF office trade shows quality assets still clear the market even as metro vacancy runs near 25%",
    "Project Connect now delivers less than voters approved in 2020, at a higher cost, with construction still two years out",
]

USC_SIGNALS_0729 = [
    dict(category="Industrial", title="Rexford Industrial Quadruples Planned Asset Sales After $506.9M Loss",
         subtitle="LA's Dominant Industrial Landlord Is Pruning Even Strong-Fundamentals Product",
         date="July 2026",
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
         date="Q2 2026",
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
         date="July 17, 2026",
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
         date="July 15, 2026",
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
         date="July 2026",
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
         date="July 2026",
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
         date="July 2026",
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

USC_FINAL_PARAGRAPHS_0729 = [
    "This week's Los Angeles signals split into repricing and consolidation on one side, and renewed conviction on the other. Rexford Industrial quadrupling its disposition guidance after a half-billion-dollar loss, and Milhaus assembling scale through merger and acquisition, both describe platforms restructuring how they hold and manage LA real estate right now &mdash; not because performance is weak, but because the current environment rewards scale and lower cost basis over standalone operation.",
    "The two industrial signals are worth reading against each other. Rexford is shedding LA-basin assets it says were bought at peak pricing, while South Bay is simultaneously pulling in its strongest leasing quarter since 2021 on the back of aerospace and defense tenants &mdash; the same broad asset class producing both a repricing story and a demand-surge story, depending on submarket and vintage.",
    "PUBLIC West Hollywood's reopening and Oceanwide Plaza's court-approved sale describe the same underlying dynamic at very different scales: capital willing to absorb real execution risk on Los Angeles hospitality and mixed-use product specifically because the entry basis is now this depressed, not despite it.",
]

USC_FINAL_BULLETS_0729 = [
    "Rexford's disposition guidance and Milhaus's merger both describe platforms restructuring for a tighter capital environment",
    "South Bay industrial is posting its strongest leasing quarter since 2021 even as Rexford sheds LA-basin assets elsewhere",
    "A new Sunset Strip hotel opening runs directly against trade-press surveys showing weak LA hospitality investment sentiment",
    "A $517 million sale still requires $800 million-plus more before Oceanwide Plaza is habitable",
]

NYC_SIGNALS_0729 = [
    dict(category="Office", title="NBCUniversal Renews 244,185 SF at 1221 Avenue of the Americas",
         subtitle="A Legacy Media Tenant Recommits Instead of Shrinking",
         date="July 2026",
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
         date="July 28, 2026",
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
         date="Mid-July 2026",
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
         date="July 28, 2026",
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

NYC_FINAL_PARAGRAPHS_0729 = [
    "This week's New York signals share a theme: capital is finding conviction in real estate uses that sit adjacent to, or entirely outside of, conventional office and retail &mdash; a legacy media tenant recommitting to Midtown space, a philanthropic buyer converting lab space into an institutional research campus, wellness operators driving retail vacancy to a multi-year low, and a healthcare-anchored asset trading at a steep premium to ordinary office.",
    "The NBCUniversal renewal and the East New York Health Hub sale are worth reading as two data points on the same broader question: which uses is capital willing to pay up for right now. A legacy tenant renewing at scale in a strong leasing quarter, and a medical office property trading at nearly double typical Brooklyn office pricing, both point toward durable, non-discretionary demand commanding real premiums.",
    "The Ackman Oxman Institute purchase and the wellness-driven retail leasing surge describe a similar dynamic from opposite ends of the market: mission-driven and experiential demand, not conventional office or apparel retail, is what's actually absorbing space and moving vacancy right now.",
]

NYC_FINAL_BULLETS_0729 = [
    "A legacy media tenant renewed at scale in Manhattan's strongest office leasing quarter since 2002",
    "A philanthropic buyer is converting lab/office stock into a dedicated institutional research campus",
    "Wellness and fitness tenants, not apparel or dining, pushed prime retail vacancy to a 2019 low",
    "A Brooklyn medical office asset traded at nearly double typical conventional office pricing",
]

NYC_DEBT_SIGNALS_0729 = [
    dict(category="Refinancing", title="SL Green Begins Refinancing $1.77B Mortgage on 245 Park Ave",
         subtitle="A Mega-Loan Refi Attempt Is a Real Test of the Trophy Office Debt Market",
         date="July 29, 2026",
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
         date="July 29, 2026",
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
         date="July 6, 2026",
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
         date="July 28, 2026",
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
         date="July 28, 2026",
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
         date="July 28, 2026",
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
         date="July 27, 2026",
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

NYC_DEBT_FINAL_PARAGRAPHS_0729 = [
    "This week's New York lending activity splits cleanly between capital exiting risk and capital extending fresh conviction. OceanFirst's $1.3 billion bulk sale of rent-stabilized loans to Cerberus and the Ditson Building's special servicing transfer both represent lenders recognizing or exiting distress; SL Green's $1.77 billion refinancing attempt, BXP's $1.2 billion construction loan, and Ladder Capital's $268 million acquisition loan all represent fresh capital being extended at real scale.",
    "The SL Green and BXP signals are worth reading together as two different tests of the same question: will debt capital still underwrite Manhattan trophy office at scale? SL Green is asking that question of existing debt on a stabilized asset; BXP already got its answer, in the form of a $1.2 billion bank club construction loan with milestone-based pricing that shows lenders will fund new supply, but only on favorable, pre-leased terms.",
    "Ladder Capital's aggressive 71%-leverage acquisition loan on 575 Fifth Avenue is this week's clearest evidence that office debt isn't frozen uniformly &mdash; it's bifurcating sharply by asset quality, location, and lender type, with non-bank balance-sheet lenders stepping in exactly where the picture otherwise looks most cautious.",
]

NYC_DEBT_FINAL_BULLETS_0729 = [
    "A regional bank exited $1.3 billion of rent-stabilized NYC multifamily loan exposure in one bulk sale to Cerberus",
    "SL Green and BXP are both testing whether debt capital still underwrites Manhattan trophy office at billion-dollar scale",
    "A sub-$40 million special servicing transfer shows office distress reaching small, older Lower Manhattan buildings too",
    "A non-bank lender's 71%-leverage acquisition loan shows office debt bifurcating by quality, not freezing uniformly",
]

IB_SIGNALS_0729 = [
    dict(category="M&amp;A", title="Mapfre Buys Safety Insurance for $1.54B in Cash at a 44% Premium",
         subtitle="A Clean All-Cash Deal Is a Useful Baseline for Reading Premium Mechanics",
         date="July 23, 2026",
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
         date="July 19, 2026",
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
         date="July 23, 2026",
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
         date="July 21, 2026",
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
         date="July 27, 2026",
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
         date="July 26, 2026",
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
         date="July 23, 2026",
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

IB_FINAL_PARAGRAPHS_0729 = [
    "This week's dealmaking splits into two distinct stories: traditional M&amp;A and sponsor finance running at ordinary scale (Mapfre/Safety, Tempus/Personalis, the EA take-private clearing its last major hurdle), and a genuinely new financing category &mdash; AI infrastructure &mdash; now large enough to move capital markets on its own. The Aligned Data Centers acquisition and the Meta bond financing are two different deals, from the same asset manager, in the same week, both aimed at the same underlying buildout.",
    "BlackRock's dual role is this issue's clearest structural story. On Aligned, BlackRock is the equity sponsor buying the platform outright; on Meta's El Paso facility, BlackRock is the debt originator pricing bonds against a hyperscaler's leaseback obligation. The same asset manager sitting on both sides of the AI capex stack, in the same week, is a preview of how concentrated the financing side of this buildout may become.",
    "The 7.5%-plus yield on nominally investment-grade Meta-backed debt is worth sitting with on its own: fixed-income investors are pricing real execution risk into AI datacenter debt even where the rating says otherwise, which is a more honest signal about how the market actually views this buildout than any rating alone would suggest.",
]

IB_FINAL_BULLETS_0729 = [
    "AI infrastructure financing is now large enough to generate its own M&amp;A and DCM signals in the same week",
    "BlackRock is simultaneously the equity sponsor on one AI-infrastructure deal and the debt originator on another",
    "A junk-like 7.5%-plus yield on investment-grade-rated AI-datacenter debt prices real risk the rating doesn't capture",
    "A liquidating, not reorganizing, Chapter 11 at a 128-year-old distributor signals no capital structure fix was viable",
]

CREDIT_SIGNALS_0729 = [
    dict(category="Asset-Based Lending", title="Apollo and Blackstone Arrange ~$35B Financing for Anthropic's AI Chip Purchases",
         subtitle="Chip-as-Collateral Lending Is Functionally Asset-Based Credit Against Depreciating Hardware",
         date="July 9, 2026",
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
         date="July 21, 2026",
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
         date="July 13, 2026",
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
         date="July 23, 2026",
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
         date="July 3, 2026",
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
         date="July 7, 2026",
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
         date="July 21, 2026",
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

CREDIT_FINAL_PARAGRAPHS_0729 = [
    "This week's signals split into a genuinely new financing frontier and the market's more familiar plumbing. Apollo and Blackstone's $35 billion Anthropic financing and Brookfield/Tor's $255 million PaleBlueDot note describe the same underlying trade &mdash; chips and GPUs as private-credit collateral &mdash; at completely different scales, showing this lending logic now reaches from megacap AI labs down to venture-stage infrastructure platforms in a matter of months.",
    "The NAV loan and secondaries data points are worth reading together. Rated NAV issuance has scaled to $82 billion since 2018 even as initial ratings skew toward BBB, and the credit secondaries market has doubled in six months partly on BDC redemption pressure &mdash; both describe a private credit market that has grown fast enough to need more standardized liquidity tools, faster than it has necessarily proven those tools out through a real downturn.",
    "Trinseo's escalating LME litigation and Prospect Capital's contested below-NAV vote are this week's two governance-risk stories, at different points in the capital structure. One shows how a 2023 priming transaction can still generate active litigation three years later; the other shows a public BDC needing two adjournments to secure authority that directly dilutes its own shareholders.",
]

CREDIT_FINAL_BULLETS_0729 = [
    "AI infrastructure financing now spans from a $35 billion megacap deal to a $255 million venture-stage note",
    "NAV loan issuance has scaled past $82 billion since 2018 even as initial ratings skew toward BBB",
    "The credit secondaries market doubled in six months, partly on rising BDC redemption pressure",
    "Lower-middle-market direct lending is clearing even as upper-middle-market volume hits a multi-year low",
]

# ============================================================== FROZEN SNAPSHOTS (week of Aug 3, 2026) ==============================================================

CRE_SNAPSHOT_0803 = [
    ("Development Activity", "rising"),
    ("Office Pipeline", "stable"),
    ("Industrial Momentum", "rising"),
    ("Mixed-Use Activity", "rising"),
    ("Capital Availability", "stable"),
    ("Infrastructure Relevance", "rising"),
]

CRE_SIGNALS_0803 = [
    dict(category="Industrial", title="Amazon Confirmed as Anchor Behind Southeast Austin Mega-Project",
         subtitle="A $5.6 Billion Infrastructure Package Follows the Tenant, Not the Other Way Around",
         date="July 23, 2026",
         trigger=f'''Austin officials confirmed that {src("https://www.kut.org/austin/2026-07-21/secrets-out-amazon-is-the-company-behind-austins-fast-tracked-dogs-head-project", "Amazon's robotics division is the previously unnamed tenant")} behind the roughly 2,600-acre &ldquo;Dog's Head&rdquo; site along the Colorado River in Southeast Austin, and on July 23 {src("https://austincurrent.org/2026/07/23/dogshead-austin-texas-development/", "the Austin City Council voted 7-3 to approve Tax Increment Reinvestment Zone financing")} for the site, with developer Endeavor projecting roughly $3.5 billion in property tax revenue over 30 years to fund infrastructure covering up to 12,000 homes and 4 million square feet of industrial space.''',
         why="A TIRZ vote is a bet the city is willing to make with its own future tax revenue, not just a rezoning approval &mdash; the city is committing to fund infrastructure against tax increment that only materializes if the development actually gets built and leases up as projected. That the anchor tenant turned out to be Amazon's robotics division, rather than a speculative logistics user, changes the credit quality of that bet: a name-brand corporate tenant with disclosed job commitments is a very different anchor than an unnamed spec building. The 1,478-to-645 public sign-up split ahead of the vote also shows this was a genuinely contested approval, not a rubber stamp.",
         implications=[
             "Commits city tax revenue to infrastructure years before the site fully leases up",
             "Establishes Southeast Austin's Colorado River corridor as a new large-scale industrial and mixed-use submarket",
             "Sets a scale precedent for how large a single anchor-tenant deal can move a TIRZ vote",
             "Leaves a pending council vote on the site's regulating plan and development standards still to come",
         ],
         watch="Whether Amazon's disclosed job commitments materialize on the timeline implied by the TIRZ financing, and the outcome of the still-pending council vote on the site's regulating plan."),
    dict(category="Industrial", title="Link Logistics Buys Fully-Leased Round Rock Industrial Building",
         subtitle="A Major Logistics REIT Is Still Buying Small-Bay Austin Industrial, Even With Vacancy Elevated",
         date="July 29, 2026",
         trigger=f'''{src("https://irei.com/news/link-logistics-acquires-fully-leased-texas-industrial-portfolio-in-dallas-and-austin/", "Link Logistics acquired a fully-leased, two-building industrial portfolio spanning Round Rock and Coppell, Texas")}, with the Austin piece a 61,111-square-foot building at 2401 Double Creek Drive in Round Rock; purchase price was not disclosed.''',
         why="A major logistics REIT buying a small-bay, fully-leased infill building in a supply-constrained Austin suburb, even as metro-wide industrial vacancy sits elevated, is a specific bet that submarket-level fundamentals in Round Rock still justify acquisition pricing that the broader Austin industrial market wouldn't support today. That distinction &mdash; buying occupied, infill product rather than speculative big-box space &mdash; is a different industrial thesis than the Amazon or prior Tesla-scale leases this desk has tracked.",
         implications=[
             "Confirms institutional industrial buyers still see value in fully-leased, infill Austin-suburb product",
             "Signals Round Rock specifically remains a supply-constrained submarket despite metro-wide vacancy pressure",
             "Provides a counter-signal to broader \"industrial oversupply\" narratives circulating this cycle",
             "Adds a second major logistics player (alongside Amazon) actively deploying capital in the Austin metro",
         ],
         watch="Whether Link Logistics discloses the purchase price, and if the REIT pursues additional infill acquisitions in the Round Rock or broader Austin-suburb submarkets."),
    dict(category="Office", title="Apollo Global Management Selects Austin as Second U.S. Headquarters",
         subtitle="An $800B Manager Anchoring HQ2 Here Is a Corporate-Relocation Signal Years Ahead of Any Lease",
         date="August 3, 2026",
         trigger=f'''{src("https://finance.yahoo.com/technology/articles/apollo-selects-austin-strategic-hub-131500562.html", "Apollo Global Management announced it has selected Austin as its second U.S. headquarters")}, a hub the roughly $800 billion alternative asset manager says will be built around innovation, emerging technology, and its retirement solutions platform; Apollo said Austin already represents one of its top five capital bases after nearly two decades of existing partnerships in the market. Specific office square footage, address, and headcount were not disclosed.''',
         why="A manager of Apollo's scale anchoring a second U.S. headquarters, rather than simply expanding an existing office, is a corporate-relocation signal that typically precedes real estate absorption by months or years &mdash; the actual lease or build announcement, and the high-wage jobs that come with it, still has to follow. That Apollo frames Austin as already one of its top five capital bases suggests this is a formalization of existing depth in the market, not a speculative bet on an unproven relationship.",
         implications=[
             "Signals a major high-wage corporate anchor is coming to Austin before any specific office real estate is announced",
             "Adds Apollo to the list of large financial and technology firms treating Austin as a genuine second hub, not a satellite office",
             "Creates a specific, named tenant to watch for the eventual real estate follow-through (lease size, submarket, timeline)",
             "Reinforces Austin's positioning for high-wage financial-services job growth alongside its existing tech-sector base",
         ],
         watch="The follow-up real estate announcement disclosing office size, submarket, and headcount, which typically lags a headquarters announcement like this by weeks to months."),
    dict(category="Office", title="Cousins Properties Sells Downtown Austin Tower for $208M",
         subtitle="A Second Trophy Office Trade in the Same Stretch Suggests a Real Repricing Wave, Not an Isolated Deal",
         date="July 31, 2026",
         trigger=f'''{src("https://www.commercialsearch.com/news/cousins-properties-sells-austin-office-asset-for-208m/", "Cousins Properties sold the 518,385-square-foot One Eleven Congress office tower")} at 111 Congress Ave. to Fort Worth-based Canyon Creek Real Estate for $208 million; the 30-story, 1987-built tower was 90.2% leased as of March, and Cousins had invested $66.4 million in capital improvements since acquiring it in 2016. The deal is Canyon Creek's first Austin acquisition since the firm's 2025 formation.''',
         why="A second major downtown Austin office trophy trading in the same stretch as Hines' $151 million purchase of 405 Colorado St. is a meaningfully stronger signal than either sale alone &mdash; one full-price trade could be idiosyncratic, but two in close succession suggests institutional capital is genuinely re-entering downtown Austin office at scale, not just opportunistically picking off a single asset. That a brand-new buyer entity is willing to make this its first Austin acquisition also signals confidence extends beyond incumbent owners.",
         implications=[
             "Confirms a second institutional-scale downtown Austin office trade in the same week as the Hines/405 Colorado deal",
             "Signals a possible broader repricing wave for well-leased Austin office trophies, not an isolated transaction",
             "Introduces a new institutional buyer (Canyon Creek) making downtown Austin its entry point into the market",
             "Provides a second recent full-price comp ($208M) for other downtown Austin office owners considering a sale",
         ],
         watch="Whether additional downtown Austin office towers trade at comparable pricing in the coming weeks, confirming a genuine repricing wave rather than two isolated deals."),
    dict(category="Office", title="Hines Pays $733/SF for Fully Leased Downtown Austin Tower",
         subtitle="A Full-Price Trophy Trade Is a Different Signal Than the Metro's Vacancy Rate",
         date="July 13, 2026",
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
         date="July 27, 2026",
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
         date="July 24, 2026",
         trigger=f'''{src("https://www.kut.org/transportation/2026-07-24/austin-tx-project-connect-explainer-capmetro-light-rail-bus-train", "Austin's Project Connect light rail has been scaled down from an original 20.2-mile, 31-station plan with a downtown subway to 9.8 miles and 15 stations")} with no subway and no airport connection, nearly six years after 2020 voter approval; the downtown tunnel and airport link, together a $2&ndash;4 billion cost driver, were both eliminated, construction is still not slated to start until 2027, and current light-rail cost estimates exceed $8.2 billion, up from an original $5.8 billion estimate.''',
         why="A rail line's scope and timeline are the single biggest variable in how station-area land actually gets valued, and this is a material downgrade on both dimensions from what voters funded in 2020 &mdash; a shorter route with no downtown subway or airport connection serves fewer trip patterns and touches fewer parcels than the original plan did. That the cost estimate has grown even as scope shrank means the per-mile economics of this project have deteriorated substantially, which matters for how much confidence to place in any future scope restoration.",
         implications=[
             "Narrows the set of parcels that can credibly underwrite against confirmed future rail access",
             "Eliminates the airport connection that would have supported hospitality and office land near the terminal",
             "Signals cost discipline problems that could pressure future extensions or scope restoration",
             "Pushes any land-value effect further out, since construction itself doesn't start until 2027",
         ],
         watch="Whether the 2027 construction start holds, and whether CapMetro identifies funding to restore any of the cut scope in a later phase."),
]

CRE_FINAL_PARAGRAPHS_0803 = [
    "This week's biggest story for Austin office is that there isn't just one trophy trade &mdash; there are two. Cousins Properties' $208 million sale of One Eleven Congress lands in the same stretch as Hines' $151 million purchase of 405 Colorado St., and a brand-new buyer entity (Canyon Creek) making its Austin debut on the Cousins deal is a stronger signal than either trade alone that institutional capital is genuinely re-entering downtown office, not just opportunistically picking off one asset.",
    "Apollo choosing Austin for a second U.S. headquarters is this week's longest-lead-time signal. It's a corporate-relocation announcement, not a real estate one &mdash; the actual office lease or build, and the jobs that come with it, still has to follow. But an $800 billion manager formalizing what it already calls a top-five capital base is exactly the kind of commitment that shows up in absorption data a year or two from now.",
    "Link Logistics' Round Rock acquisition is worth reading against the broader industrial narrative this desk has tracked since Amazon's Dog's Head announcement. A major logistics REIT paying up for fully-leased, infill industrial product, even with metro-wide vacancy elevated, confirms the story here is submarket-specific, not a uniform oversupply picture across all of Austin industrial.",
]

CRE_FINAL_BULLETS_0803 = [
    "Two institutional-scale downtown Austin office trophies traded in the same stretch, not just one isolated deal",
    "Apollo's HQ2 announcement is a corporate-relocation signal that precedes any actual real estate by months or years",
    "A major logistics REIT is still paying up for fully-leased, infill Austin-suburb industrial despite elevated metro vacancy",
    "Amazon's TIRZ financing and Brandywine's ongoing disposition program both remain in motion from prior weeks",
]

USC_SNAPSHOT_0803 = [
    ("Development Activity", "rising"),
    ("Office Pipeline", "stable"),
    ("Industrial Momentum", "stable"),
    ("Mixed-Use Activity", "rising"),
    ("Capital Availability", "stable"),
    ("Infrastructure Relevance", "stable"),
]

USC_SIGNALS_0803 = [
    dict(category="Industrial", title="Rexford Industrial Quadruples Planned Asset Sales After $506.9M Loss",
         subtitle="LA's Dominant Industrial Landlord Is Pruning Even Strong-Fundamentals Product",
         date="July 2026",
         trigger=f'''{src("https://www.bisnow.com/los-angeles/news/industrial/rexford-takes-500m-loss-plans-up-to-2b-in-dispositions-this-year-135577", "Rexford Industrial Realty raised its 2026 disposition guidance to $1.5&ndash;2 billion")}, up from $400&ndash;500 million, after posting a $506.9 million net loss in Q2 driven by a noncash impairment; the expanded sell-off covers roughly 8 million square feet, about 16% of Rexford's ~50 million-square-foot LA-basin portfolio, with the company targeting properties it says carry &ldquo;substantially above-market in-place rents&rdquo; from acquisitions &ldquo;at the height of the market.&rdquo;''',
         why="A REIT quadrupling its planned dispositions while eating a half-billion-dollar impairment is a concrete repricing signal, not a portfolio-management footnote &mdash; Rexford is the single largest and most closely-watched industrial landlord in the LA basin, so its own admission that certain assets were bought at peak valuations tells you where the broader market's cost basis stands relative to today's rents. That same-property occupancy still sits at 95.7% even amid this pruning shows the portfolio's operating performance isn't the problem; the entry price is.",
         implications=[
             "Signals that even best-in-class LA industrial product bought at peak pricing no longer pencils at current values",
             "Directs roughly $1 billion of sale proceeds toward paying down $1 billion of debt maturing in 2027",
             "Provides a reference point for how aggressively other LA industrial owners may need to reprice legacy acquisitions",
             "Confirms strong 95.7% same-property occupancy even as the company prunes its highest-basis assets",
         ],
         watch="The pricing Rexford actually achieves on the expanded $1.5&ndash;2 billion disposition slate, and whether other LA-basin industrial REITs follow with similar guidance revisions."),
    dict(category="Industrial", title="LA County Fines Lineage Logistics Over Fire-Damaged Cold Storage Warehouse",
         subtitle="Cold Storage and Logistics Assets Carry Environmental and Regulatory Exposure Leasing Spreadsheets Don't Capture",
         date="July 30, 2026",
         trigger=f'''{src("https://www.bisnow.com/news/los-angeles/industrial/lineage-cold-storage-rotting-meat-public-health-135596", "LA County Public Health is fining Lineage Logistics $500 per day")} over unsanitary conditions at its fire-damaged 500,000-square-foot cold storage warehouse in Boyle Heights, after a nearly week-long June 2026 fire left hundreds of tons of spoiled meat rotting inside and generated nearly 1,000 resident odor complaints; Mayor Karen Bass set an August 14 deadline for full cleanup, warning the city will pursue legal action if Lineage misses it.''',
         why="Cold storage and logistics real estate carries environmental, regulatory, and community-relations exposure that goes well beyond a typical industrial building's leasing spreadsheet &mdash; a fire at a facility storing perishable goods creates an ongoing public health liability that persists long after the fire itself is out, with real daily financial and legal consequences. That the city set a hard, public deadline with an explicit threat of legal action shows this has moved from a property-management problem into direct regulatory confrontation.",
         implications=[
             "Confirms cold storage industrial assets carry environmental and regulatory risk beyond standard property management",
             "Puts a specific, quantified daily cost ($500/day) on unresolved conditions at a distressed industrial asset",
             "Signals the city is willing to escalate to legal action against a major logistics operator over public health conditions",
             "Adds a real-world case study in industrial-asset risk that goes beyond vacancy and rent, relevant for underwriting this collateral type",
         ],
         watch="Whether Lineage meets the August 14 cleanup deadline, and the status of its permit to rebuild the warehouse to its original condition."),
    dict(category="Office", title="Culver City Advances Plan to Upzone Hayden Tract From Office to Housing",
         subtitle="A 56-to-110-Foot Height Increase Is a Direct Policy Response to a Broken Office Submarket",
         date="July 27, 2026",
         trigger=f'''{src("https://culvercitycrossroads.com/2026/07/27/hayden-tract-specific-plan-to-prioritize-housing-needs-2/", "Culver City's Hayden Tract Specific Plan would raise the district's current 56-foot height cap to 110 feet")} (120 feet for hotels) and increase floor-area ratio to unlock mixed-use residential development, aided by SB 79's transit-density bonus since the district sits between two Metro E Line stations; a Planning Commission review is set for October and a City Council vote for November 2026. Culver City office vacancy sits at 25.7%, with 17 listings in the Hayden Tract alone, versus 20.4% in neighboring Santa Monica.''',
         why="Raising height and density limits specifically to convert a historic office park into housing is a direct, concrete policy mechanism for addressing structural office oversupply &mdash; rather than waiting for the market to resolve elevated vacancy through attrition, the city is changing the zoning itself to make residential redevelopment pencil. That the plan explicitly leverages a state transit-density law (SB 79) shows how new state housing policy is combining with local zoning changes to accelerate office-to-residential conversion economics in specific, well-positioned submarkets.",
         implications=[
             "Provides a concrete zoning mechanism (height and FAR increases) for converting oversupplied office parks to housing",
             "Confirms Culver City office vacancy (25.7%) is severe enough to justify a formal rezoning response, not just individual conversions",
             "Shows SB 79's transit-density bonus directly enabling specific local rezoning plans near Metro stations",
             "Sets a policy template other LA-area cities with similar office oversupply near transit may replicate",
         ],
         watch="The Planning Commission's October review and the City Council's November 2026 vote, and whether specific developers commit to residential redevelopment once the plan is adopted."),
    dict(category="Multifamily", title="Milhaus Merges With SRG Residential, Agrees to Acquire Broadshore Capital",
         subtitle="Consolidation Is How Mid-Size Multifamily Platforms Are Buying Scale Right Now",
         date="July 15, 2026",
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
         date="July 2026",
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
         date="July 2026",
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
    dict(category="Retail", title="Study Ties LA Immigration Enforcement to Over $3M in Lost Fashion District Revenue",
         subtitle="Federal Policy Is Now a Quantifiable Variable in Retail Leasing Fundamentals, Not Just a Headline",
         date="July 2026",
         trigger=f'''{src("https://www.bisnow.com/news/los-angeles/retail/immigration-raids-los-angeles-county-135603", "A UCLA-LAEDC-Placer.ai analysis found LA's June 2025 immigration enforcement crackdown drove over $3 million in lost revenue and roughly 46,000 lost visits")} to nearby businesses in a two-week span, with Fashion District foot traffic in H1 2026 still running 9.9% below 2024 levels; 82% of surveyed businesses reported negative impacts, and ICE arrests in the greater LA area hit 2,581 in Jan-March 2026, a 148% jump year-over-year.''',
         why="A quantified, multi-institution study (UCLA, LAEDC, Placer.ai foot-traffic data) tying a specific federal enforcement action to specific lost revenue and foot-traffic figures turns what's usually a qualitative, headline-driven narrative into an actual variable retail analysts can model. That Fashion District traffic remains meaningfully below 2024 levels more than a year later suggests the effect isn't a short-term disruption but a durable shift in trade-area dynamics for retail-heavy immigrant-serving commercial districts.",
         implications=[
             "Provides a rare, quantified data point connecting federal immigration policy directly to retail leasing fundamentals",
             "Confirms the effect has persisted more than a year, not resolved as a short-term disruption",
             "Signals commercial tenants (57% of respondents) are deferring expansion or consolidating locations in affected districts",
             "Adds a durable, hard-to-model demand risk factor for retail underwriting in immigrant-serving LA trade areas specifically",
         ],
         watch="Whether Fashion District and Little Tokyo foot traffic continues recovering toward 2024 levels, and if commercial vacancy in these districts moves in response."),

    dict(category="Hospitality", title="Ian Schrager's PUBLIC West Hollywood Opens on the Sunset Strip",
         subtitle="A New Lifestyle Hotel Bets Against Its Own Industry's Sentiment Survey",
         date="July 2026",
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

USC_FINAL_PARAGRAPHS_0803 = [
    "This week's Los Angeles signals show real estate risk showing up in less conventional forms than vacancy or cap rates. Lineage's fire-damaged cold storage warehouse is a reminder that industrial and logistics assets carry environmental and regulatory exposure that doesn't show up on a typical rent roll, while the immigration-enforcement study puts a hard number on how federal policy is directly affecting retail foot traffic and revenue in specific LA trade areas.",
    "Culver City's Hayden Tract upzoning plan is this week's clearest policy response to structural office oversupply &mdash; rather than waiting for the market to resolve 25.7% vacancy through attrition, the city is changing height and density limits to make residential redevelopment pencil, aided by a state transit-density law. It's a concrete template other LA-area cities with similar office gluts near transit may follow.",
    "Rexford's disposition guidance and Milhaus's merger, both still very much in motion from prior weeks, continue to describe platforms restructuring how they hold and manage LA real estate right now, while Oceanwide Plaza and PUBLIC West Hollywood remain the desk's clearest examples of capital absorbing real execution risk specifically because entry basis is this depressed.",
]

USC_FINAL_BULLETS_0803 = [
    "Cold storage and logistics real estate carries environmental and regulatory exposure that doesn't show up in a typical rent roll",
    "A quantified study now ties federal immigration enforcement directly to lost Fashion District retail revenue and foot traffic",
    "Culver City is changing zoning itself (height, FAR) to convert oversupplied office into housing, aided by a state transit-density law",
    "Rexford's disposition guidance and Milhaus's merger remain in motion, still describing platforms restructuring for scale",
]

NYC_SNAPSHOT_0803 = [
    ("Development Activity", "rising"),
    ("Office Pipeline", "rising"),
    ("Industrial Momentum", "stable"),
    ("Mixed-Use Activity", "rising"),
    ("Capital Availability", "stable"),
    ("Infrastructure Relevance", "stable"),
]

NYC_SIGNALS_0803 = [
    dict(category="Office", title="NBCUniversal Renews 244,185 SF at 1221 Avenue of the Americas",
         subtitle="A Legacy Media Tenant Recommits Instead of Shrinking",
         date="July 2026",
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
         date="July 28, 2026",
         trigger=f'''{src("https://commercialobserver.com/2026/07/bill-ackman-buys-125-west-end-avenue/", "Bill Ackman's Pershing Square Foundation paid $188 million for the 400,000-square-foot lab building at 125 West End Avenue")} from Taconic Partners, the first piece of a roughly $260 million, two-building, 700,000-square-foot assemblage on the Upper West Side that will become the Ackman Oxman Institute, a brain research center developed with the Mount Sinai Hospital System.''',
         why="A billionaire-funded philanthropic buyer paying a premium to convert existing lab and office stock into a dedicated institutional research campus is a concrete example of life-sciences and &ldquo;eds-and-meds&rdquo; demand becoming a real alternative use case for underused Manhattan office and lab buildings, not just a talking point. Because this is a mission-driven, not yield-driven, acquisition, it's a different kind of demand signal than a REIT or fund buying the same building &mdash; but it still removes real square footage from the conventional office market permanently.",
         implications=[
             "Confirms life-sciences and institutional research demand as a genuine absorption path for older lab/office stock",
             "Removes roughly 700,000 square feet from conventional Manhattan office/lab inventory permanently",
             "Signals continued philanthropic capital willingness to fund large-scale medical research real estate in NYC",
             "May encourage other underused Upper West Side lab buildings to market toward similar institutional buyers",
         ],
         watch="Whether the Foundation closes on the adjacent 320 West 66th Street parcel as planned, and construction/opening timelines for the Ackman Oxman Institute."),
    dict(category="Mixed-Use", title="CW Realty Buys 55 Smith Street in Downtown Brooklyn for $58M",
         subtitle="A Development Site Trades With Room to Build Under the City's New Affordability Program",
         date="July 31, 2026",
         trigger=f'''{src("https://commercialobserver.com/2026/07/cw-realty-buys-55-smith-street-brooklyn/", "CW Realty bought 55 Smith Street in Downtown Brooklyn for $58 million")} from Edison Properties, a site that can support up to roughly 164,000 square feet of development under the city's Universal Affordability Preference program, which allows extra buildable density in exchange for income-restricted units.''',
         why="A development site trading hands in Downtown Brooklyn at a price that only pencils if the buyer can actually use the Universal Affordability Preference density bonus is one of the first real tests of whether that program is unlocking new buildable capacity, rather than sitting unused on paper. If CW Realty is underwriting to the full 164,000 square feet, it's a signal that sponsors are starting to treat the UAP bonus as bankable, not speculative.",
         implications=[
             "Signals sponsors are underwriting real value to the Universal Affordability Preference density bonus",
             "Confirms continued investment appetite for Downtown Brooklyn development sites despite broader office caution",
             "Provides a per-buildable-square-foot benchmark for other UAP-eligible sites in the borough",
             "May encourage additional site owners near transit-rich Brooklyn corridors to test the program",
         ],
         watch="Whether CW Realty files development plans and what unit mix/affordability split it pursues under the UAP framework."),
    dict(category="Retail", title="Boutique Fitness Operators Drive Manhattan Retail Vacancy to a 2019 Low",
         subtitle="Experiential Wellness Tenants, Not Apparel Chains, Are Now the Demand Engine",
         date="Mid-July 2026",
         trigger=f'''{src("https://www.credaily.com/briefs/boutique-gyms-lead-manhattan-retail-leasing-surge/", "Boutique fitness and wellness operators drove a surge in Manhattan and Brooklyn retail leasing")}, led by Chelsea Piers (76,000 square feet at Seaport) and Life Time (71,000 square feet in North Williamsburg), pushing prime-corridor retail vacancy down to roughly 12% &mdash; the lowest since 2019, with Madison Avenue and SoHo down to about 8%.''',
         why="Wellness and fitness tenants regularly ranking among the largest retail leases in the market, rather than traditional apparel or restaurant chains, is a durable shift in what landlords are underwriting retail rents against &mdash; these operators typically sign long-term leases anchored around expensive buildout (pools, studios, equipment), which makes them stickier tenants than a typical apparel retailer once installed. Vacancy falling to a level not seen since 2019 in the specific corridors these tenants are choosing confirms this demand is broad enough to move real vacancy numbers, not just a handful of headline deals.",
         implications=[
             "Confirms experiential wellness tenants, not apparel or dining, are now the leading edge of large-block retail demand",
             "Pushes prime-corridor Manhattan retail vacancy to its lowest level since 2019",
             "Signals landlords can underwrite rents against sticky, buildout-heavy wellness tenants rather than higher-turnover retail",
             "May pressure remaining large-block retail asking rents higher in the corridors these operators favor",
         ],
         watch="Whether additional large-format wellness operators announce New York leases this year, and rent growth in the specific corridors already tightening."),
    dict(category="Retail", title="BTF Capital Fund Buys Key Food-Anchored Whitestone Shopping Center for $56M",
         subtitle="A Grocery-Anchored Queens Center Draws Fresh Institutional Capital and New Financing",
         date="July 31, 2026",
         trigger=f'''{src("https://commercialobserver.com/2026/07/schuckman-realty-buys-153-15-cross-island-parkway-queens/", "BTF Capital Fund bought the Key Food-anchored Whitestone Shopping Center in Queens for $56 million")}, with Acadia Realty providing roughly $48.5 million in financing on the deal.''',
         why="A grocery-anchored Queens shopping center trading at a healthy basis, with a name-brand institutional lender like Acadia Realty willing to finance a majority of the purchase price, confirms that necessity-based retail anchored by a durable grocery tenant remains one of the most financeable property types in the outer boroughs right now, even as financing for other retail formats stays selective.",
         implications=[
             "Confirms grocery-anchored retail remains highly financeable even in a selective lending environment",
             "Signals institutional lenders like Acadia Realty see durable value in necessity-based outer-borough retail",
             "Provides a fresh basis benchmark for Key Food and similar grocery-anchored Queens centers",
             "Reinforces continued investor appetite for stabilized, cash-flowing retail over speculative retail plays",
         ],
         watch="Whether BTF Capital Fund pursues similar grocery-anchored acquisitions elsewhere in Queens or the outer boroughs."),
    dict(category="Multifamily", title="Delshah Capital Buys Five Upper West Side Apartment Buildings for $36.9M",
         subtitle="A 147-Unit Portfolio Trades More Than $20 Million Below Its 2018 Price",
         date="July 30, 2026",
         trigger=f'''{src("https://commercialobserver.com/2026/07/delshah-upper-west-side-sale-quality-capital-37m/", "Delshah Capital bought five Upper West Side apartment buildings totaling 147 units for $36.9 million")} from Quality Capital USA, more than $20 million below the portfolio's 2018 purchase price.''',
         why="A rent-stabilized-heavy Upper West Side multifamily portfolio trading more than $20 million below its 2018 basis is a concrete data point on how much value New York's 2019 rent law changes have stripped from older stabilized buildings &mdash; and on the kind of discount a well-capitalized buyer like Delshah now needs to see before stepping in. That the buyer is a repeat, experienced New York multifamily operator, not a distressed or forced seller, suggests this discount is becoming the market clearing price, not a one-off.",
         implications=[
             "Confirms rent-stabilized Manhattan multifamily is trading well below pre-2019 rent-law pricing",
             "Provides a concrete basis benchmark for other stabilized Upper West Side portfolios coming to market",
             "Signals experienced operators like Delshah see enough value at the new basis to keep acquiring",
             "May encourage other long-held stabilized portfolios to test a sale at similarly discounted pricing",
         ],
         watch="Whether Delshah announces capital improvement or repositioning plans for the portfolio, and whether comparable stabilized portfolios trade at similar discounts."),
    dict(category="Hospitality", title="Eurostars Buys Midtown's Chemists' Club Hotel for $95M",
         subtitle="A Spanish Hotel Group Pays Roughly $888,000 Per Key for a Boutique Midtown Asset",
         date="July 30, 2026",
         trigger=f'''{src("https://therealdeal.com/new-york/2026/07/30/eurostars-buys-chemists-club-hotel-in-midtown/", "Eurostars, the hotel arm of Spain's Hotusa Group, bought the 107-key Chemists' Club Hotel at 52 East 41st Street for $95 million")}, or roughly $888,000 per key, from Azora.''',
         why="A per-key price approaching $900,000 for a boutique Midtown hotel, paid by a foreign operator entering or expanding in the New York market, signals continued conviction in Manhattan hospitality fundamentals even as some other office-adjacent asset classes stay under pressure. A cross-border buyer choosing to deploy capital into a single boutique asset, rather than a larger branded portfolio, also suggests confidence in this specific submarket and price point rather than pure portfolio diversification.",
         implications=[
             "Confirms continued foreign capital appetite for boutique Manhattan hospitality assets",
             "Provides a roughly $888,000-per-key benchmark for comparable boutique Midtown hotel trades",
             "Signals Eurostars/Hotusa's entry or expansion into the New York hospitality market",
             "Reinforces hospitality as a relatively resilient office-adjacent asset class in the current cycle",
         ],
         watch="Whether Eurostars pursues additional New York hotel acquisitions and any rebranding or renovation plans for the property."),
]

NYC_FINAL_PARAGRAPHS_0803 = [
    "This week's New York signals share a theme: capital is finding conviction across a wide range of uses at once &mdash; a legacy media tenant recommitting to Midtown office space, a philanthropic buyer converting lab space into an institutional research campus, and a run of investment sales spanning a Brooklyn development site, a Queens grocery-anchored center, an Upper West Side multifamily portfolio, and a Midtown boutique hotel.",
    "The NBCUniversal renewal and the Ackman Oxman Institute purchase are worth reading as two data points on the same broader question: which office and lab uses is capital willing to commit to right now. A legacy tenant renewing at scale in a record leasing quarter, alongside a philanthropic buyer permanently converting adjacent lab stock, both point toward durable, mission-anchored demand absorbing space that might otherwise sit vacant.",
    "The week's investment sales &mdash; 55 Smith Street, Whitestone Shopping Center, the Upper West Side multifamily portfolio, and the Chemists' Club Hotel &mdash; span nearly every property type and price point, and together suggest transaction volume across the city is broadening rather than concentrating in any single asset class.",
]

NYC_FINAL_BULLETS_0803 = [
    "A legacy media tenant renewed at scale in Manhattan's strongest office leasing quarter since 2002",
    "A philanthropic buyer is converting lab/office stock into a dedicated institutional research campus",
    "A Downtown Brooklyn development site traded on the strength of the city's new density bonus program",
    "Investment sales activity broadened across retail, multifamily, and hospitality this week",
]

NYC_DEBT_SNAPSHOT_0803 = [
    ("CRE Lending Volume", "stable"),
    ("Construction Financing", "rising"),
    ("CMBS Issuance", "stable"),
    ("Agency Multifamily Activity", "rising"),
    ("Credit Availability", "stable"),
    ("Residential Credit (Non-QM / Jumbo)", "stable"),
]

NYC_DEBT_SIGNALS_0803 = [
    dict(category="Refinancing", title="SL Green Begins Refinancing $1.77B Mortgage on 245 Park Ave",
         subtitle="A Mega-Loan Refi Attempt Is a Real Test of the Trophy Office Debt Market",
         date="July 29, 2026",
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
         date="July 29, 2026",
         trigger=f'''{src("https://crenews.com/2026/07/29/oceanfirst-bank-sells-1-3bln-portfolio-of-new-york-apartment-loans/", "OceanFirst Financial Corp. sold a $1.3 billion portfolio of New York City apartment loans to Cerberus Capital Management")}, with most of the underlying properties subject to New York's rent-stabilization regulations.''',
         why="A regional bank offloading $1.3 billion in rent-regulated multifamily paper in bulk, to a distressed-debt buyer rather than another bank, is a concrete data point on how lenders are de-risking exposure to post-HSTPA rent-stabilized buildings &mdash; an asset class many lenders have quietly repriced as structurally impaired collateral since New York's 2019 rent law changes limited owners' ability to raise rents or recoup renovation costs. Cerberus buying at scale suggests distressed-debt investors see a workable basis in this paper that the originating bank no longer wanted to carry.",
         implications=[
             "Confirms regional banks are actively de-risking rent-stabilized NYC multifamily loan exposure in bulk, not loan-by-loan",
             "Signals distressed-debt buyers like Cerberus see a workable basis in rent-regulated paper banks are exiting",
             "Provides a large, real transaction size benchmark for rent-stabilized loan portfolio sales",
             "May prompt other regional banks carrying similar post-HSTPA exposure to pursue comparable bulk sales",
         ],
         watch="Whether other regional or community banks announce similar bulk sales of rent-stabilized NYC multifamily loans."),
    dict(category="Distressed Note Sale", title="Hilco Real Estate Markets 12 Nonperforming NYC-Area Bank Notes",
         subtitle="A Batch Note Sale Signals Banks Are Still Working Through Distressed Small-Balance Loans",
         date="July 30, 2026",
         trigger=f'''{src("https://www.e-a-a.com/nyc-distressed-bank-notes-hit-market-for-sale/", "Hilco Real Estate began marketing 12 nonperforming bank notes secured by NYC-area multifamily and retail properties")}, carrying more than $14 million in combined unpaid principal balance, with bids due August 13.''',
         why="A batch of a dozen small-balance nonperforming notes hitting the market at once, rather than trickling out individually, suggests originating banks are actively clearing distressed small-balance NYC multifamily and retail exposure off their books rather than waiting for individual workouts to resolve. Bundling into a single Hilco-marketed sale also signals the originating lender wants speed and finality over maximizing recovery on any single loan.",
         implications=[
             "Confirms banks are still working through a pipeline of distressed small-balance NYC multifamily and retail loans",
             "Signals a preference for batch note sales over slower loan-by-loan workouts among some originating lenders",
             "Provides a fresh benchmark for pricing on sub-$14 million nonperforming NYC-area note pools",
             "May prompt other lenders carrying similar small-balance distress to pursue comparable batch sales",
         ],
         watch="The August 13 bid deadline results and which buyer types (special servicers, distressed-debt funds, local investors) are active on the pool."),
    dict(category="Special Servicing", title="$37.5M CMBS Loan on Lower Manhattan Office Building Hits Special Servicing",
         subtitle="Distress Has Moved Well Beyond Trophy Towers Into Small, Older Office Stock",
         date="July 6, 2026",
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
         date="July 28, 2026",
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
         date="July 28, 2026",
         trigger=f'''{src("https://commercialobserver.com/2026/07/bxp-construction-loan-343-madison-avenue-q2-earnings/", "BXP closed a $1.2 billion construction loan for its 46-story, roughly 930,000-square-foot office tower at 343 Madison Avenue")}, led by Wells Fargo with support from BofA Securities, Bank of New York Mellon, and JPMorgan Chase; the loan carries a four-year initial term plus a one-year extension, an initial rate of Term SOFR plus 2.50% that steps down to plus 2.25% on leasing and construction milestones, and the roughly $2 billion, Grand Central-connected tower is about 50% pre-leased with completion expected in 2029.''',
         why="A major bank club deal financing ground-up trophy office construction, at a moment when office construction lending has been scarce nationally, shows lenders will still underwrite new supply &mdash; but only when it clears a high bar: pre-leased, transit-connected, and built by a top-tier REIT. The rate step-down tied to leasing and construction milestones is itself a signal that lenders are pricing in real execution risk and rewarding de-risking events explicitly, rather than underwriting the project on projected rents alone.",
         implications=[
             "Confirms bank capital will still fund large ground-up office construction when pre-leasing and sponsor quality are strong",
             "Ties borrowing cost directly to leasing and construction milestones, pricing execution risk explicitly into the loan",
             "Sets a $1.2 billion size and multi-bank club structure benchmark for other trophy office construction financings",
             "Reinforces Grand Central-area transit connectivity as a key underwriting factor for new Midtown office supply",
         ],
         watch="Whether 343 Madison's pre-leasing percentage climbs enough to trigger the rate step-down, and construction progress toward the 2029 completion target."),
    dict(category="Construction Lending", title="Slate Property Group Raises $1B Fund for Apartment Construction and Bridge Loans",
         subtitle="A Sponsor-Turned-Lender Commits Fresh Capital to Transit-Oriented Multifamily",
         date="July 31, 2026",
         trigger=f'''{src("https://crenews.com/2026/07/31/slate-property-raises-1bln-for-low-leverage-lending-strategy/", "Slate Property Group closed a $1 billion separately managed account dedicated to senior construction and bridge loans on apartment properties")}, targeting transit-oriented East Coast multifamily and funding an inaugural $45 million construction loan.''',
         why="An experienced multifamily sponsor raising a dedicated $1 billion vehicle to lend, rather than only develop, on transit-oriented apartments signals real conviction that senior, low-leverage construction and bridge debt on multifamily is an attractive risk-adjusted return right now &mdash; and that a sponsor's own underwriting experience is seen as an edge in originating that paper. A fresh $1 billion of dedicated capital is also a meaningful addition to the pool of lenders willing to fund ground-up apartment construction.",
         implications=[
             "Adds a meaningful new $1 billion source of construction and bridge capital for transit-oriented multifamily",
             "Signals experienced sponsors see an edge underwriting senior apartment debt using their own development experience",
             "Reinforces transit-oriented East Coast multifamily as a favored target for fresh construction lending capital",
             "May pressure pricing on comparable apartment construction loans as a new dedicated lender enters the market",
         ],
         watch="Deployment pace out of the fund and the terms/location of its next construction loans after the inaugural $45 million deal."),
    dict(category="Bridge Lending", title="Fortress Provides ~70% LTC Loan for $240M Purchase of 1441 Broadway",
         subtitle="A Below-Market-Rent Trophy Tower Trade Gets Aggressive Acquisition Leverage",
         date="July 28, 2026",
         trigger=f'''{src("https://commercialobserver.com/2026/07/60-guilders-sentry-realty-1441-broadway-sale/", "Fortress Investment Group provided a floating-rate acquisition loan covering roughly 70% of project cost")} for 60 Guilders and Sentry Realty's $240 million purchase of 1441 Broadway, a 550,000-square-foot Times Square tower that is about 90% leased at below-market rents, from the estate of LH Charney.''',
         why="A non-bank lender underwriting roughly 70% loan-to-cost on a heavily-leased but below-market-rent trophy tower is a bet that the buyer can mark rents up to current market as leases roll, not just a bet on the building's current cash flow. Fortress's willingness to lend at that leverage against a mark-to-market thesis, rather than in-place income alone, signals real lender conviction in near-term Times Square office rent growth.",
         implications=[
             "Confirms non-bank lenders will underwrite acquisition leverage against a rent mark-to-market thesis, not just in-place income",
             "Signals continued lender conviction in near-term Times Square office rent growth as leases roll to market",
             "Provides a roughly 70% loan-to-cost benchmark for comparable below-market-rent trophy office acquisitions",
             "Reinforces Fortress's active role financing large Manhattan office trades this cycle",
         ],
         watch="The pace at which 60 Guilders/Sentry Realty mark expiring leases to market at 1441 Broadway, and Fortress's appetite for similar mark-to-market acquisition loans elsewhere in Midtown."),
]

NYC_DEBT_FINAL_PARAGRAPHS_0803 = [
    "This week's New York lending activity again splits between capital exiting risk and capital extending fresh conviction. OceanFirst's $1.3 billion bulk sale of rent-stabilized loans to Cerberus, Hilco's batch sale of a dozen nonperforming NYC-area notes, and the Ditson Building's special servicing transfer all represent lenders recognizing or exiting distress; SL Green's $1.77 billion refinancing attempt, BXP's $1.2 billion construction loan, Slate's new $1 billion lending vehicle, and Fortress's acquisition loan on 1441 Broadway all represent fresh capital being extended at real scale.",
    "The SL Green and BXP signals are worth reading together as two different tests of the same question: will debt capital still underwrite Manhattan trophy office at scale? SL Green is asking that question of existing debt on a stabilized asset; BXP already got its answer, in the form of a $1.2 billion bank club construction loan with milestone-based pricing that shows lenders will fund new supply, but only on favorable, pre-leased terms.",
    "Fortress's acquisition loan on 1441 Broadway and Slate's new construction and bridge lending vehicle are this week's clearest evidence that non-bank lenders are stepping in with real conviction &mdash; one betting on rent mark-to-market at a below-market-rent trophy tower, the other committing a full $1 billion to transit-oriented multifamily construction debt.",
]

NYC_DEBT_FINAL_BULLETS_0803 = [
    "A regional bank exited $1.3 billion of rent-stabilized NYC multifamily loan exposure in one bulk sale to Cerberus",
    "SL Green and BXP are both testing whether debt capital still underwrites Manhattan trophy office at billion-dollar scale",
    "A batch sale of 12 nonperforming notes and a sub-$40 million special servicing transfer show distress still working through the system",
    "Non-bank lenders committed nearly $1.5 billion combined to a below-market-rent office trade and a new multifamily construction fund",
]

IB_SNAPSHOT_0803 = [
    ("M&amp;A Deal Volume", "rising"),
    ("IPO Pipeline", "rising"),
    ("Leveraged Loan Issuance", "stable"),
    ("Sponsor (PE) Activity", "rising"),
    ("Advisory Fee Pool", "stable"),
    ("Underwriting Conditions", "rising"),
]

IB_SIGNALS_0803 = [
    dict(category="M&amp;A", title="ICE Agrees to Acquire MarketAxess for Roughly $6.0B in Cash",
         subtitle="An Exchange Operator Buys Its Way Into Bond-Trading Infrastructure",
         date="July 30, 2026",
         trigger=f'''{src("https://ir.theice.com/", "Intercontinental Exchange agreed to acquire MarketAxess Holdings for approximately $6.0 billion in cash")}, at $167 per share, a roughly 33% premium to MarketAxess's undisturbed share price.''',
         why="ICE paying a 33% premium in cash, rather than stock, for the leading electronic bond-trading platform signals real conviction that owning fixed-income trading infrastructure outright is worth a full-price acquisition, not a partnership or minority stake. Folding MarketAxess into an exchange operator that already runs equities, derivatives, and data businesses continues a broader consolidation of trading infrastructure into a small number of vertically integrated operators.",
         implications=[
             "Confirms exchange operators see full ownership of fixed-income trading infrastructure as worth a premium cash bid",
             "Continues the consolidation of market infrastructure into a small number of vertically integrated operators",
             "Sets a scarcity precedent for remaining independent electronic bond-trading platforms",
             "Signals continued M&amp;A appetite even at large, ~$6 billion transaction sizes",
         ],
         watch="Regulatory review timing given the tie-up of two major market-infrastructure operators, and any competing or higher bids before the deal closes."),
    dict(category="Sponsor Finance", title="Grant Thornton Advisors to Acquire CBIZ for $5B, Backed by New Mountain Capital",
         subtitle="Private Capital Keeps Consolidating Professional Services Platforms",
         date="July 29, 2026",
         trigger=f'''{src("https://www.globenewswire.com/news-release/2026/07/29/", "Grant Thornton Advisors agreed to acquire CBIZ for approximately $5 billion")}, at $55 per share in cash, with the deal backed by New Mountain Capital.''',
         why="A private-equity-backed accounting and advisory platform paying $5 billion to acquire another public professional-services firm shows sponsor capital continuing to roll up fragmented advisory and accounting platforms into larger, PE-owned national players. The scale of this deal, on the heels of other recent accounting-sector consolidation, suggests the professional-services roll-up thesis still has real runway.",
         implications=[
             "Confirms sponsor-backed professional-services platforms are still willing to pay full price for public-company scale",
             "Extends the multi-year accounting and advisory consolidation trend to a $5 billion transaction size",
             "Reinforces New Mountain Capital's active role building out professional-services platforms",
             "May prompt other mid-cap public accounting or advisory firms to explore a similar sale process",
         ],
         watch="Deal financing terms once disclosed, and whether the combined platform pursues further bolt-on acquisitions post-close."),
    dict(category="Sponsor Finance", title="Ares Management in Talks to Acquire Leonard Green &amp; Partners",
         subtitle="Alternative Asset Manager Consolidation Reaches the Sponsor Level Itself",
         date="July 28, 2026",
         trigger=f'''{src("https://www.axios.com/2026/07/28/ares-leonard-green", "Ares Management is in talks to acquire private equity firm Leonard Green &amp; Partners")}, according to Axios.''',
         why="Large alternative asset managers acquiring other established private equity sponsors, rather than just raising new funds organically, shows the consolidation wave that has swept private credit and infrastructure now reaching the buyout sponsor tier itself. If completed, it would add Leonard Green's consumer and retail buyout expertise and existing fund relationships directly onto Ares's platform rather than Ares building that capability from scratch.",
         implications=[
             "Signals alternative asset manager consolidation is reaching the buyout sponsor level, not just credit and infrastructure",
             "Would add Leonard Green's consumer/retail buyout expertise directly onto Ares's existing platform",
             "Continues a broader trend of scaled managers acquiring rather than organically building new strategy verticals",
             "May prompt other mid-sized independent buyout sponsors to explore similar strategic combinations",
         ],
         watch="Whether the talks result in a signed deal, and how Leonard Green's existing fund LPs and carry structures would be treated in any combination."),
    dict(category="ECM", title="Jersey Mike's IPO Raises ~$1B, Then Falls 6% on Its Debut",
         subtitle="A 10x-Oversubscribed Book Still Wasn't Enough to Hold the Open",
         date="July 29&ndash;30, 2026",
         trigger=f'''{src("https://www.cnbc.com/2026/07/30/", "Blackstone-backed Jersey Mike's priced its IPO at $23 per share, raising roughly $1 billion")}, with the offering reported to be around 10 times oversubscribed; the stock nonetheless fell approximately 6% on its trading debut.''',
         why="A heavily oversubscribed book failing to prevent a first-day decline is a useful reminder that strong demand at pricing doesn't guarantee aftermarket support once a stock is actually trading &mdash; institutional allocations and retail follow-through are different things, and this gap between the two is exactly what sponsors and underwriters watch most closely when timing the next IPO in the pipeline.",
         implications=[
             "Shows strong IPO order books don't guarantee first-day aftermarket performance",
             "Provides Blackstone and underwriters a real data point on retail follow-through versus institutional demand",
             "May make other sponsors in the IPO pipeline more cautious on pricing relative to indicated demand",
             "Reinforces that a large raise (~$1 billion) and a weak debut can coexist in the same deal",
         ],
         watch="Whether the stock stabilizes or continues declining in the weeks after listing, and how the debut affects pricing on the next consumer IPO in the pipeline."),
    dict(category="Restructuring", title="Alkegen Files Prepackaged Chapter 11 to Eliminate ~$3.1B of Debt",
         subtitle="A Sponsor-Backed Industrial Manufacturer Uses Bankruptcy as a Balance-Sheet Reset",
         date="July 26, 2026",
         trigger=f'''{src("https://news.bloomberglaw.com/", "Clearlake Capital-sponsored Alkegen filed for prepackaged Chapter 11 bankruptcy, eliminating approximately $3.1 billion of debt")} under a plan negotiated with creditors in advance of the filing.''',
         why="A prepackaged, rather than contested, Chapter 11 shows the sponsor and creditors reached agreement on the balance-sheet fix before the filing, which is typically the faster, lower-cost path through court for both sides. Eliminating roughly $3.1 billion of debt at a single industrial manufacturer is a large enough deleveraging that it will likely be referenced as a comp for other over-levered, sponsor-backed industrial credits still negotiating with lenders.",
         implications=[
             "Confirms sponsors and creditors are increasingly negotiating balance-sheet fixes before filing, not during a contested case",
             "Removes roughly $3.1 billion of debt from a single sponsor-backed industrial manufacturer's balance sheet",
             "Provides a large deleveraging comp for other over-levered sponsor-backed industrial credits",
             "Signals Clearlake's willingness to use a prepackaged filing to preserve the underlying operating business",
         ],
         watch="Alkegen's post-emergence capital structure and ownership, and whether other Clearlake-sponsored credits pursue similar prepackaged processes."),
    dict(category="Sector: Healthcare", title="argenx to Acquire Forte Biosciences for ~$2.2B at an 86% Premium",
         subtitle="A Steep Premium for a Single Antibody Asset Shows Aggressive Bidding for Late-Stage Pipeline",
         date="July 27, 2026",
         trigger=f'''{src("https://www.bloomberg.com/news/articles/2026-07-27", "argenx agreed to acquire Forte Biosciences for approximately $2.2 billion in cash")}, a premium of roughly 86% to Forte's undisturbed share price, primarily to obtain Forte's FB102 antibody candidate.''',
         why="An 86% premium for a single clinical-stage antibody asset is an unusually steep price even by biotech M&amp;A standards, and signals argenx sees enough strategic value in FB102 specifically to pay well above where the market had it priced. Premiums at this level tend to reset how other bidders think about the going-in price for comparable late-stage immunology or antibody assets still in play.",
         implications=[
             "Sets an unusually high, roughly 86%, premium benchmark for single-asset clinical-stage biotech acquisitions",
             "Signals argenx's specific strategic conviction in the FB102 antibody candidate",
             "May reset pricing expectations for other late-stage immunology or antibody assets still seeking buyers",
             "Confirms large biotech acquirers remain willing to pay up for de-risked, clinically advanced pipeline",
         ],
         watch="FB102's subsequent trial readouts and regulatory path once under argenx's ownership, and whether the premium prompts competing bids for comparable assets."),
    dict(category="Sector: Industrials", title="TransDigm to Acquire Prince &amp; Izant for ~$1.066B From Industrial Growth Partners",
         subtitle="A Serial Acquirer Keeps Bolting Niche Aerospace Suppliers Onto Its Platform",
         date="July 27, 2026",
         trigger=f'''{src("https://www.prnewswire.com/", "TransDigm Group agreed to acquire Prince &amp; Izant Company for approximately $1.066 billion in cash")} from Industrial Growth Partners.''',
         why="TransDigm's playbook of acquiring niche, highly-engineered aerospace component suppliers at premium multiples and running them for cash flow has been consistent for years, and this deal is a straightforward continuation of that strategy at a scale ($1.066 billion) large enough to matter to Industrial Growth Partners' fund returns. It's a useful reminder that steady, programmatic sector M&amp;A is still happening even in weeks dominated by larger, more headline-grabbing deals.",
         implications=[
             "Continues TransDigm's established strategy of acquiring niche, highly-engineered aerospace suppliers",
             "Provides Industrial Growth Partners a full-cycle exit at a meaningful, roughly $1.066 billion valuation",
             "Reinforces aerospace component supply as a sector where premium strategic multiples remain available",
             "Signals continued steady sector M&amp;A activity alongside the week's larger headline deals",
         ],
         watch="Integration of Prince &amp; Izant into TransDigm's platform and whether TransDigm signals further near-term bolt-on acquisitions."),
]

IB_FINAL_PARAGRAPHS_0803 = [
    "This week's dealmaking spans market infrastructure, professional services, and the sponsor tier itself: ICE's ~$6.0 billion cash acquisition of MarketAxess, Grant Thornton Advisors' $5 billion purchase of CBIZ backed by New Mountain Capital, and Ares Management's reported talks to acquire Leonard Green &amp; Partners are three different flavors of the same underlying story &mdash; consolidation moving up the value chain from operating companies to the platforms and sponsors that own them.",
    "Jersey Mike's IPO is this week's clearest reminder that strong indicated demand and aftermarket performance are different things: a book reported around 10 times oversubscribed still wasn't enough to hold the stock above its offer price on debut, a gap other sponsors with IPOs in the pipeline will be watching closely.",
    "Alkegen's prepackaged Chapter 11, argenx's premium-priced acquisition of Forte Biosciences, and TransDigm's bolt-on purchase of Prince &amp; Izant round out a week where restructuring and sector M&amp;A both moved at a steady, programmatic pace alongside the larger headline transactions.",
]

IB_FINAL_BULLETS_0803 = [
    "Consolidation moved up the value chain this week, reaching market infrastructure, professional services, and sponsors themselves",
    "A 10x-oversubscribed IPO book still wasn't enough to prevent a 6% first-day decline for Jersey Mike's",
    "A prepackaged Chapter 11 eliminated ~$3.1B of debt at a sponsor-backed industrial manufacturer with creditor agreement already in hand",
    "An 86% takeover premium for a single antibody asset shows how aggressively biotech acquirers are bidding for late-stage pipeline",
]

CREDIT_SNAPSHOT_0803 = [
    ("Direct Lending Volume", "rising"),
    ("Spread Tightening", "rising"),
    ("Covenant Looseness", "stable"),
    ("Sponsor Demand", "rising"),
    ("Fundraising / Dry Powder", "stable"),
    ("Secondary Market Liquidity", "rising"),
]

CREDIT_SIGNALS_0803 = [
    dict(category="Asset-Based Lending", title="Apollo and Blackstone Arrange ~$35B Financing for Anthropic's AI Chip Purchases",
         subtitle="Chip-as-Collateral Lending Is Functionally Asset-Based Credit Against Depreciating Hardware",
         date="July 9, 2026",
         trigger=f'''{src("https://www.benzinga.com/markets/private-markets/26/07/60372922/broadcom-anthropic-just-turned-ais-chip-bet-into-somebody-elses-debt-apollo-and-blackstone-hold-the-keys", "Apollo Global Management and Blackstone arranged a roughly $35 billion financing package")} to fund Anthropic's purchase of custom AI chips from Google and Broadcom, structured through a special-purpose vehicle that buys the chips and leases them back to Anthropic via a delayed-draw facility with roughly 16 separate releases over a bit more than a year; Broadcom is backstopping Anthropic's payment obligations on the largest senior tranches, and roughly $15 billion of the package is expected to migrate to the 144A market by early 2027.''',
         why="Structuring chip purchases as a leased special-purpose vehicle, with a delayed-draw facility that releases capital in roughly 16 tranches, lets private credit underwrite AI infrastructure the same way it underwrites any other depreciating, collateral-backed asset &mdash; except the collateral here is custom silicon whose useful economic life and resale value are far less established than a warehouse or an aircraft. Broadcom's backstop on the senior tranches is doing real work: it converts what would otherwise be pure technology-obsolescence risk into a corporate-credit question about Broadcom's own backstop capacity, which is a very different risk private lenders are much more comfortable pricing.",
         implications=[
             "Confirms private credit can underwrite AI infrastructure at a scale rivaling large syndicated bank deals",
             "Converts chip-obsolescence risk into a corporate-backstop credit question via Broadcom's guarantee",
             "Structures the delayed-draw facility to release capital in step with actual chip delivery, not all at once",
             "Sets a template migrating roughly $15 billion of the package into the 144A market for institutional investors by early 2027",
         ],
         watch="Whether the expected 144A migration proceeds on the early-2027 timeline, and how the chips' resale or residual value holds up as tranches draw down."),
    dict(category="Asset-Based Lending", title="Fortress Agrees to $1.5B Forward-Flow Deal to Buy Wayflyer's SMB Loans",
         subtitle="A Forward-Flow Structure Lets an E-Commerce Lender Originate Without Holding the Risk",
         date="July 29&ndash;30, 2026",
         trigger=f'''{src("https://www.bloomberg.com/news/articles/2026-07-29", "Fortress Investment Group agreed to a $1.5 billion forward-flow deal to purchase small-business loans originated by Wayflyer")}, an e-commerce lender, according to Bloomberg and FF News.''',
         why="A forward-flow structure lets Wayflyer keep originating small-business loans off its own balance sheet by pre-selling them to Fortress as they're made, which is functionally the same asset-based lending logic used on Anthropic's chip financing, just applied to SMB receivables instead of GPUs &mdash; private credit is increasingly comfortable committing capital in advance against a pipeline of future originations, not just existing collateral pools.",
         implications=[
             "Confirms forward-flow structures are spreading from consumer and specialty finance into e-commerce SMB lending",
             "Lets Wayflyer scale origination volume without retaining the credit risk on its own balance sheet",
             "Signals continued private credit appetite for SMB receivables as an asset-based lending category",
             "Provides Fortress a committed pipeline of future originations rather than a one-time portfolio purchase",
         ],
         watch="Wayflyer's origination volume growth under the new forward-flow commitment, and whether comparable e-commerce lenders pursue similar forward-flow deals."),
    dict(category="Documentation", title="CoreWeave Forced to Sweeten Pricing and Add Covenants on $2.6B Loan",
         subtitle="Investor Pushback Shows Real Documentation Discipline Returning to AI-Adjacent Credit",
         date="July 29&ndash;Aug 3, 2026",
         trigger=f'''{src("https://www.bloomberg.com/news/articles/2026-07-29", "CoreWeave was forced to raise pricing by 100 to 125 basis points and add maintenance covenants on a $2.6 billion loan")} after investor pushback, according to Bloomberg, with follow-on coverage confirming the repricing held through early August.''',
         why="Lenders successfully pushing back on price and documentation, rather than accepting whatever terms an in-demand AI-infrastructure borrower initially offers, is a concrete sign that real underwriting discipline persists even in the hottest corner of private credit right now. Maintenance covenants specifically give lenders an ongoing check on performance, not just a one-time credit approval, which is exactly the kind of documentation term that tends to disappear first when a borrower has excess leverage in a negotiation.",
         implications=[
             "Confirms lenders retain real negotiating leverage on pricing and documentation even for in-demand AI borrowers",
             "Adds maintenance covenants that give lenders an ongoing performance check, not just a point-in-time approval",
             "Sets a 100-125bps repricing benchmark other AI-infrastructure borrowers may face in future syndications",
             "Signals documentation discipline persisting in AI-adjacent credit even amid heavy capital demand",
         ],
         watch="Whether other AI-infrastructure borrowers face similar repricing or covenant additions in upcoming syndications."),
    dict(category="Documentation", title="Minority Lenders Escalate Suit Over Trinseo's 2023 Priming Transaction",
         subtitle="A Double-Dip Liability Management Exercise Is Now Years of Bankruptcy Litigation",
         date="July 3, 2026",
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
         date="July 7, 2026",
         trigger=f'''{src("https://www.stocktitan.net/sec-filings/PSEC/8-k-prospect-capital-corp-reports-material-event-e174a28ef8a2.html", "Prospect Capital Corporation shareholders voted on July 7 to renew the company's authority to sell common stock below net asset value")} for the next 12 months, 277.6 million votes for versus 63.9 million against, after the vote was adjourned twice (from June 9 to June 23 to July 7) to solicit sufficient turnout; PSEC has traded around a 57% discount to NAV earlier in 2026, with any single day's sales capped at 25% of shares outstanding.''',
         why="A BDC needing two adjournments to secure shareholder permission to issue equity below NAV, while trading at a 57% discount, tells you the authority itself is contested even though it ultimately passed &mdash; selling new shares below NAV directly dilutes existing holders' per-share value, so management is prioritizing balance-sheet flexibility over near-term shareholder economics. This is precisely the kind of governance dynamic that has drawn activist pressure (including from Saba Capital) at peer BDCs this year.",
         implications=[
             "Confirms management is prioritizing balance-sheet flexibility over near-term shareholder dilution concerns",
             "Signals a steep 57% NAV discount reflects real market skepticism, not just a temporary mispricing",
             "Sets up potential activist scrutiny of a similar kind already targeting peer BDCs this year",
             "Caps daily dilution risk at 25% of shares outstanding, limiting but not eliminating the governance concern",
         ],
         watch="Whether Prospect Capital actually exercises this authority given the steep discount, and if activist investors escalate pressure following the contested vote."),
    dict(category="BDC", title="Blue Owl's AUM Hits $319B, But Fundraising Slows to ~$7.6-7.8B in Q2",
         subtitle="A Scaled Manager's Growth Is Decelerating Even as Its Balance Sheet Keeps Expanding",
         date="July 30, 2026",
         trigger=f'''{src("https://privatemarketsinsights.com/", "Blue Owl Capital reported Q2 2026 assets under management of $319 billion, but quarterly fundraising fell to roughly $7.6 to $7.8 billion")}, with direct lending down to approximately 35% of total AUM as the firm's other strategies grow as a share of the platform.''',
         why="A manager still growing total AUM while its quarterly fundraising pace slows is a sign that net new commitments, not just asset appreciation or reinvestment, are decelerating even at one of the largest scaled direct lending platforms &mdash; and direct lending shrinking as a share of Blue Owl's own mix suggests the firm itself is diversifying away from the strategy that built it, which is a different signal than a simple industry-wide slowdown.",
         implications=[
             "Confirms fundraising deceleration is reaching even the largest scaled direct lending platforms",
             "Signals Blue Owl is diversifying its own mix away from direct lending as a share of total AUM",
             "Provides a $7.6-7.8 billion quarterly fundraising benchmark against which peer BDC/manager raises will be compared",
             "Distinguishes AUM growth from net new fundraising, two metrics that are moving in different directions here",
         ],
         watch="Whether Blue Owl's fundraising pace recovers in Q3, and whether direct lending's shrinking AUM share continues as other strategies scale."),
    dict(category="Direct Lending", title="Lafayette Square Finances RM Capital's Investment in Samaha &amp; Associates",
         subtitle="Lower-Middle-Market Lending Is Clearing Even as Upper-Middle-Market Volume Slows",
         date="July 21, 2026",
         trigger=f'''{src("https://www.prnewswire.com/news-releases/lafayette-square-provides-financing-to-support-rm-capital-partners-investment-in-samaha--associates-302830245.html", "Lafayette Square USA provided a senior secured credit facility backing RM Capital Partners' platform investment in Samaha &amp; Associates")}, a Miami-based technology consulting firm serving credit unions and banks with more than 500 completed engagements for 200-plus clients; facility size and pricing were not disclosed.''',
         why="This deal clearing at all is the signal, not its size &mdash; PitchBook LCD data showed Q2 2026 direct lending volume at $33.6 billion, the lowest since Q2 2023, meaning upper-middle-market deal flow has slowed sharply while smaller, non-sponsor-adjacent lenders like Lafayette Square are still finding and financing lower-middle-market deal flow banks and larger direct lenders are passing on. That bifurcation, not the aggregate volume number alone, is the more useful read on where credit is actually still flowing.",
         implications=[
             "Confirms lower-middle-market direct lending is clearing even as upper-middle-market volume hits a multi-year low",
             "Signals specialty lenders are finding deal flow that larger direct lenders and banks are currently passing on",
             "Provides continued growth capital access for niche vertical-software and services platforms",
             "Reinforces a bifurcating direct lending market by deal size, not a uniform slowdown across the asset class",
         ],
         watch="Whether Q3 2026 direct lending volume data confirms continued softness at the upper-middle-market end while lower-middle-market deal flow holds up."),
    dict(category="Direct Lending", title="BlackRock Arranges $12B+ Private Debt for Meta's AI Data Center via HPS/GIP",
         subtitle="A Traditional Asset Manager's Private-Credit Acquisitions Are Already Originating Megadeals",
         date="July 28&ndash;29, 2026",
         trigger=f'''{src("https://www.bloomberg.com/news/features/2026-07-28", "BlackRock arranged more than $12 billion in private debt financing for one of Meta's AI data centers")}, using its newly-acquired HPS Investment Partners and Global Infrastructure Partners units to originate and structure the facility.''',
         why="BlackRock, a firm best known for public equity and fixed-income index products, originating a $12 billion-plus private-debt megadeal within roughly a year of closing its HPS and GIP acquisitions shows those deals are already generating real origination capability, not just adding AUM on paper. It also confirms hyperscaler AI data center financing has become large and standardized enough that a traditional public-markets giant, not just specialist private credit shops, can compete directly for the biggest deals in the category.",
         implications=[
             "Confirms BlackRock's HPS and GIP acquisitions are already generating megadeal-scale origination capability",
             "Signals hyperscaler AI data center financing is standardized enough to draw traditional asset managers, not just specialists",
             "Sets a $12 billion-plus size benchmark for comparable hyperscaler data center private-debt financings",
             "Reinforces Meta's continued reliance on private credit, alongside bond financing, to fund AI infrastructure buildout",
         ],
         watch="Whether BlackRock's HPS/GIP units originate additional hyperscaler data center financings, and how this facility's terms compare to Meta's other recent bond and private-credit deals."),
]

CREDIT_FINAL_PARAGRAPHS_0803 = [
    "This week's signals split into a genuinely new financing frontier and the market's more familiar plumbing. Apollo/Blackstone's $35 billion Anthropic financing, Fortress's $1.5 billion Wayflyer forward-flow deal, and BlackRock's $12 billion-plus Meta data center financing describe the same underlying trade at very different scales and structures &mdash; private credit underwriting AI infrastructure and AI-adjacent receivables as collateral, with even a traditional asset manager like BlackRock now originating megadeals through its newly-acquired HPS and GIP units.",
    "CoreWeave's forced repricing is worth reading against that backdrop: even as capital keeps flowing into AI-infrastructure credit at record scale, lenders on this specific $2.6 billion loan still won 100-125 basis points of additional pricing and new maintenance covenants, which is real evidence that documentation discipline hasn't been fully competed away by demand.",
    "Trinseo's escalating LME litigation and the two BDC stories &mdash; Prospect Capital's contested below-NAV vote and Blue Owl's AUM growth alongside slowing fundraising &mdash; round out a week where governance and growth-quality questions surfaced at very different points in the private credit ecosystem.",
]

CREDIT_FINAL_BULLETS_0803 = [
    "AI infrastructure and AI-adjacent private credit now spans a $35B chip financing, a $12B+ hyperscaler data center loan, and a $1.5B SMB forward-flow deal",
    "Lender pushback forced CoreWeave to raise pricing and add covenants on a $2.6B loan, even amid heavy AI-credit demand",
    "Blue Owl's AUM kept growing to $319B even as its own quarterly fundraising pace slowed to roughly $7.6-7.8B",
    "Lower-middle-market direct lending is clearing even as upper-middle-market volume hits a multi-year low",
]

AUSTIN_DEBT_SNAPSHOT_0729 = [
    ("CRE Lending Volume", "stable"),
    ("Construction Financing", "rising"),
    ("CMBS Issuance", "stable"),
    ("Agency Multifamily Activity", "stable"),
    ("Credit Availability", "stable"),
    ("Residential Credit (Non-QM / Jumbo)", "stable"),
]

AUSTIN_DEBT_SIGNALS_0729 = [
    dict(category="Construction Lending", title="PIMCO and Berkadia Finance 336-Unit Affordable Community Near Austin",
         subtitle="Institutional Credit Meets a Ground Lease Structure for Deeply Affordable Housing",
         date="July 15, 2026",
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
         date="July 20, 2026",
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
         date="June 2, 2026",
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
         date="June 3, 2026",
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
         date="June 8, 2026",
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
         date="June 16, 2026",
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
         date="June 30, 2026",
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

AUSTIN_DEBT_FINAL_PARAGRAPHS_0729 = [
    "This week's Austin lending activity is dominated by hospitality distress at multiple scales. JPMorgan credit-bidding to take back The Line Austin, and the Fairmont Austin's ongoing special servicing dispute, are two different downtown hotels now effectively under lender control &mdash; and The Line is the third hotel under its brand nationally to face foreclosure since 2025, meaning at least part of this stress traces back to a brand-level problem, not just Austin-specific softness.",
    "Freddie Mac's roughly 80% basis haircut on the Royal Crest Drive apartment auction is the hardest number in this week's issue &mdash; a $50 million credit bid resetting to a $9.5 million opening ask in under six months is a real, quantified data point on how far older, non-renovated Austin multifamily has actually fallen, not an analyst estimate.",
    "Domain Tower 2's $135 million life-company refinancing is worth reading against all of the above. The same week two hotels landed in lender hands, a well-leased, tech-tenanted suburban office tower cleared the debt market on ordinary terms &mdash; a reminder that Austin lending risk right now tracks asset quality far more than property type or submarket alone.",
]

AUSTIN_DEBT_FINAL_BULLETS_0729 = [
    "Two downtown Austin hotels, The Line and the Fairmont, are now effectively under lender control at the same time",
    "The Line Austin's foreclosure is the third at its hotel brand nationally since 2025, pointing to brand-level distress",
    "A Freddie Mac apartment loan reset from a $50M credit bid to a $9.5M opening ask in under six months",
    "A well-leased Domain-district office tower refinanced on ordinary terms the same week two hotels hit distress",
]

USC_DEBT_SNAPSHOT_0729 = [
    ("CRE Lending Volume", "stable"),
    ("Construction Financing", "stable"),
    ("CMBS Issuance", "stable"),
    ("Agency Multifamily Activity", "rising"),
    ("Credit Availability", "stable"),
    ("Residential Credit (Non-QM / Jumbo)", "stable"),
]

USC_DEBT_SIGNALS_0729 = [
    dict(category="CMBS", title="BofA Plaza Sale Triggers $175.87M in CMBS Losses",
         subtitle="A Receivership Sale Finally Prices What Four Bond Trusts Were Actually Owed",
         date="July 21, 2026",
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
         date="June 2026",
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
         date="July 15, 2026",
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
         date="July 2026",
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
         date="July 17, 2026",
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
         date="July 20, 2026",
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
         date="June 12, 2026",
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

USC_DEBT_FINAL_PARAGRAPHS_0729 = [
    "This week's Los Angeles lending activity is dominated by studio and hospitality distress clustered around a small number of sponsors. Hackman Capital's Television City default and the Manhattan Beach Studios note sale are both Hackman-affiliated properties in trouble in the same stretch, and Goldman Sachs has already taken a third Hackman studio asset, Radford Studio Center, after a separate default &mdash; a sponsor-level pattern, not three unrelated events.",
    "The Shutters on the Beach and Casa del Mar special servicing transfer adds a different flavor of distress: a maturity-extension covenant, not necessarily weak cash flow, moved this loan, and the borrowers are openly disputing the servicer's characterization. Paired with Bank of America Plaza's now-crystallized $175.87 million CMBS loss, Los Angeles hospitality and office debt are both generating hard numbers this week, not just anecdotal stress.",
    "Against all of that, the Beverly Hills construction loan and the SoLa Impact bond financing show fresh capital is still being extended with real conviction &mdash; one a conventional bank underwriting ground-up risk in a supply-constrained submarket, the other a first-of-its-kind public bond structure built specifically because no conventional loan fit the collateral.",
]

USC_DEBT_FINAL_BULLETS_0729 = [
    "Three Hackman-affiliated studio properties have now hit distress or changed hands under duress in the same stretch",
    "A Santa Monica hotel special servicing transfer turned on a maturity covenant, not necessarily weak performance",
    "Los Angeles CMBS distress is being priced and resolved this week, not just extended on paper",
    "Selective construction and public-bond capital is still being extended with real conviction in specific submarkets",
]

STRUCTURED_SNAPSHOT_0729 = [
    ("CLO Issuance", "rising"),
    ("Consumer ABS Issuance", "stable"),
    ("Esoteric ABS Issuance", "rising"),
    ("Spread Tightening", "rising"),
    ("Ratings Momentum", "stable"),
    ("Warehouse Financing", "rising"),
]

STRUCTURED_SIGNALS_0729 = [
    dict(category="Esoteric ABS", title="Aligned Data Centers Prices $1.183B ABS, Upsized 30% From Target",
         subtitle="An Oversubscribed First-Since-2023 Deal Confirms Investor Appetite Hasn't Faded",
         date="July 28, 2026",
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
         date="July 7, 2026",
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
         date="July 2, 2026",
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
         date="July 16, 2026",
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
         date="July 2026",
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
         date="July 15, 2026",
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
         date="July 20, 2026",
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

STRUCTURED_FINAL_PARAGRAPHS_0729 = [
    "This week's signals span from a $1.183 billion data center ABS print to a warehouse facility with an undisclosed size, but they share a theme: this desk covers CLOs and corporate/consumer ABS specifically, a different lane from Securitized Signal, which covers residential and commercial mortgage securitization (RMBS and CMBS) separately. The Aligned Data Centers ABS deal is worth noting alongside IB Signal's coverage of the same company's $40 billion acquisition this week &mdash; equity and structured-debt investors reached similar conclusions about the same collateral independently, in the same stretch.",
    "The two CLO prints this week describe a bifurcating primary market. CVC, a Tier-1 manager, priced near market tights even as broader broadly-syndicated-loan volume is reported down roughly 21% year-over-year; Macquarie, a newer entrant, kept scaling and drew ten new investors on its third deal in 18 months. Both are real demand signals, just from opposite ends of the manager-quality spectrum.",
    "The CLO ratings-methodology story is this issue's most consequential for how to actually read a rating. Over 400 CLOs lined up for upgrades from a model recalibration, not from improved collateral, is a real, current test of whether tranche ratings still track loan-level credit quality &mdash; a distinction with real consequences the last time methodology loosened this broadly.",
]

STRUCTURED_FINAL_BULLETS_0729 = [
    "This desk covers CLOs and corporate/consumer ABS specifically, distinct from Securitized Signal's RMBS and CMBS coverage",
    "Aligned Data Centers' $1.183B ABS print and its $40B acquisition (covered in IB Signal) priced the same collateral independently, same week",
    "Tier-1 and newer-entrant CLO managers are both finding real demand, from opposite ends of the manager-quality spectrum",
    "A methodology-driven wave of 400-plus CLO upgrades decouples ratings from loan-level credit quality this cycle",
]

SECURITIZED_SNAPSHOT_0729 = [
    ("RMBS Issuance", "rising"),
    ("CMBS Issuance", "stable"),
    ("Collateral Performance", "stable"),
    ("Credit Enhancement Levels", "stable"),
    ("Ratings Momentum", "stable"),
    ("Warehouse Financing", "rising"),
]

SECURITIZED_SIGNALS_0729 = [
    dict(category="CMBS Conduit", title="Citi Prices Largest Multifamily-Only CMBS Conduit Since the Financial Crisis",
         subtitle="A Bank's Own Top-Market Rankings Reveal Where Its Origination Pipeline Is Strongest",
         date="Week of July 16, 2026",
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
         date="Early July 2026",
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
         date="July 8, 2026",
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
         date="July 20, 2026",
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
         date="July 15, 2026",
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
         date="July 8, 2026",
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

SECURITIZED_FINAL_PARAGRAPHS_0729 = [
    "This is the first real issue of Securitized Signal, carved out specifically to cover non-agency RMBS and CMBS as their own vertical, distinct from Structured Signal's focus on CLOs and consumer ABS. The Citi conduit deal is a useful example of why that split matters: it's a genuinely national capital-markets pricing story, not a market-specific lending story, which is exactly the kind of signal this desk exists to carry instead of forcing it into a location-specific RE Debt Signal market.",
    "The Nomura and Citi deals this week describe CMBS pricing from two different angles &mdash; a sponsor switching away from agency debt for the first time, and a bank's own top-market rankings revealing where its origination pipeline is deepest. Both are real, capital-backed reads on where CMBS demand currently sits, at a moment when SASB deals dominate private-label issuance.",
    "The Trepp delinquency data is this issue's most important structural point: a headline number improving almost entirely because of lodging, while office, retail, and multifamily all worsen in the same month, is a bifurcating credit story hiding inside an aggregate figure. That distinction matters more than the headline every time a conduit pool's property-type mix gets underwritten.",
]

SECURITIZED_FINAL_BULLETS_0729 = [
    "This desk covers RMBS and CMBS specifically, distinct from Structured Signal's CLO and consumer ABS coverage",
    "A sponsor's first-ever CMBS execution and a bank's record conduit deal both show real capital-backed CMBS demand",
    "Institutional single-family rental securitization keeps clearing the market even as conventional CMBS faces distress",
    "A falling headline CMBS delinquency rate is masking worsening office, retail, and multifamily credit underneath it",
]

# ============================================================== ARCHIVE ==============================================================
# Each week, before overwriting a desk/market's live content with fresh research,
# snapshot the outgoing week here so past issues remain readable. Append new
# entries to ARCHIVE_ENTRIES going forward -- never remove old ones.

ARCHIVE_ENTRIES = [
    # (entry_id, label, name_a, name_b, dateline, drop, coverage, snapshot, signals, final_paragraphs, final_bullets, tagline, implications_label)
    ("cre-austin-20260729", "CRE &middot; Austin, TX &middot; Jul 29, 2026", "CRE", "Signal", "AUSTIN, TEXAS", "JULY 29, 2026", "JULY 7&ndash;27, 2026", CRE_SNAPSHOT_0729, CRE_SIGNALS_0729, CRE_FINAL_PARAGRAPHS_0729, CRE_FINAL_BULLETS_0729, "No predictions. No stock references. Project-anchored interpretation only.", "Local Market Implications"),
    ("cre-usc-20260729", "CRE &middot; Los Angeles, CA &middot; Jul 29, 2026", "CRE", "Signal", "LOS ANGELES, CA", "JULY 29, 2026", "JULY 15&ndash;28, 2026", USC_SNAPSHOT_0729, USC_SIGNALS_0729, USC_FINAL_PARAGRAPHS_0729, USC_FINAL_BULLETS_0729, "No predictions. No stock references. Project-anchored interpretation only.", "Local Market Implications"),
    ("cre-nyu-20260729", "CRE &middot; New York, NY &middot; Jul 29, 2026", "CRE", "Signal", "NEW YORK, NY", "JULY 29, 2026", "JULY 15&ndash;28, 2026", NYC_SNAPSHOT_0729, NYC_SIGNALS_0729, NYC_FINAL_PARAGRAPHS_0729, NYC_FINAL_BULLETS_0729, "No predictions. No stock references. Project-anchored interpretation only.", "Local Market Implications"),
    ("redebt-austin-20260729", "RE Debt &middot; Austin, TX &middot; Jul 29, 2026", "RE Debt", "Signal", "AUSTIN, TEXAS", "JULY 29, 2026", "JUNE 2&ndash;JULY 28, 2026", AUSTIN_DEBT_SNAPSHOT_0729, AUSTIN_DEBT_SIGNALS_0729, AUSTIN_DEBT_FINAL_PARAGRAPHS_0729, AUSTIN_DEBT_FINAL_BULLETS_0729, "No predictions. No stock references. Loan-anchored interpretation only.", "Market Implications"),
    ("redebt-usc-20260729", "RE Debt &middot; Los Angeles, CA &middot; Jul 29, 2026", "RE Debt", "Signal", "LOS ANGELES, CA", "JULY 29, 2026", "JULY 15&ndash;28, 2026", USC_DEBT_SNAPSHOT_0729, USC_DEBT_SIGNALS_0729, USC_DEBT_FINAL_PARAGRAPHS_0729, USC_DEBT_FINAL_BULLETS_0729, "No predictions. No stock references. Loan-anchored interpretation only.", "Market Implications"),
    ("redebt-nyu-20260729", "RE Debt &middot; New York, NY &middot; Jul 29, 2026", "RE Debt", "Signal", "NEW YORK, NY", "JULY 29, 2026", "JULY 6&ndash;29, 2026", NYC_DEBT_SNAPSHOT_0729, NYC_DEBT_SIGNALS_0729, NYC_DEBT_FINAL_PARAGRAPHS_0729, NYC_DEBT_FINAL_BULLETS_0729, "No predictions. No stock references. Loan-anchored interpretation only.", "Market Implications"),
    ("ib-20260729", "IB Signal &middot; Jul 29, 2026", "IB", "Signal", "NEW YORK, NY", "JULY 29, 2026", "JULY 19&ndash;27, 2026", IB_SNAPSHOT_0729, IB_SIGNALS_0729, IB_FINAL_PARAGRAPHS_0729, IB_FINAL_BULLETS_0729, "No predictions. No stock references. Deal-anchored interpretation only.", "Market Implications"),
    ("credit-20260729", "Credit Signal &middot; Jul 29, 2026", "Credit", "Signal", "NEW YORK, NY", "JULY 29, 2026", "JULY 21&ndash;28, 2026", CREDIT_SNAPSHOT_0729, CREDIT_SIGNALS_0729, CREDIT_FINAL_PARAGRAPHS_0729, CREDIT_FINAL_BULLETS_0729, "No predictions. No stock references. Facility-anchored interpretation only.", "Market Implications"),
    ("structured-20260729", "Structured Signal &middot; Jul 29, 2026", "Structured", "Signal", "NEW YORK, NY", "JULY 29, 2026", "JULY 2&ndash;28, 2026", STRUCTURED_SNAPSHOT_0729, STRUCTURED_SIGNALS_0729, STRUCTURED_FINAL_PARAGRAPHS_0729, STRUCTURED_FINAL_BULLETS_0729, "No predictions. No stock references. Structure-anchored interpretation only.", "Market Implications"),
    ("securitized-20260729", "Securitized Signal &middot; Jul 29, 2026", "Securitized", "Signal", "NEW YORK, NY", "JULY 29, 2026", "JULY 7&ndash;28, 2026", SECURITIZED_SNAPSHOT_0729, SECURITIZED_SIGNALS_0729, SECURITIZED_FINAL_PARAGRAPHS_0729, SECURITIZED_FINAL_BULLETS_0729, "No predictions. No stock references. Pool-anchored interpretation only.", "Market Implications"),
    ("cre-austin-20260803", "CRE &middot; Austin, TX &middot; Aug 3, 2026", "CRE", "Signal", "AUSTIN, TEXAS", "AUGUST 3, 2026", "JULY 23&ndash;AUG 3, 2026", CRE_SNAPSHOT_0803, CRE_SIGNALS_0803, CRE_FINAL_PARAGRAPHS_0803, CRE_FINAL_BULLETS_0803, "No predictions. No stock references. Project-anchored interpretation only.", "Local Market Implications"),
    ("cre-usc-20260803", "CRE &middot; Los Angeles, CA &middot; Aug 3, 2026", "CRE", "Signal", "LOS ANGELES, CA", "AUGUST 3, 2026", "JULY 15&ndash;AUG 3, 2026", USC_SNAPSHOT_0803, USC_SIGNALS_0803, USC_FINAL_PARAGRAPHS_0803, USC_FINAL_BULLETS_0803, "No predictions. No stock references. Project-anchored interpretation only.", "Local Market Implications"),
    ("cre-nyu-20260803", "CRE &middot; New York, NY &middot; Aug 3, 2026", "CRE", "Signal", "NEW YORK, NY", "AUGUST 3, 2026", "JULY 28&ndash;AUG 3, 2026", NYC_SNAPSHOT_0803, NYC_SIGNALS_0803, NYC_FINAL_PARAGRAPHS_0803, NYC_FINAL_BULLETS_0803, "No predictions. No stock references. Project-anchored interpretation only.", "Local Market Implications"),
    ("redebt-nyu-20260803", "RE Debt &middot; New York, NY &middot; Aug 3, 2026", "RE Debt", "Signal", "NEW YORK, NY", "AUGUST 3, 2026", "JULY 28&ndash;AUG 3, 2026", NYC_DEBT_SNAPSHOT_0803, NYC_DEBT_SIGNALS_0803, NYC_DEBT_FINAL_PARAGRAPHS_0803, NYC_DEBT_FINAL_BULLETS_0803, "No predictions. No stock references. Loan-anchored interpretation only.", "Market Implications"),
    ("ib-20260803", "IB Signal &middot; Aug 3, 2026", "IB", "Signal", "NEW YORK, NY", "AUGUST 3, 2026", "JULY 26&ndash;AUG 3, 2026", IB_SNAPSHOT_0803, IB_SIGNALS_0803, IB_FINAL_PARAGRAPHS_0803, IB_FINAL_BULLETS_0803, "No predictions. No stock references. Deal-anchored interpretation only.", "Market Implications"),
    ("credit-20260803", "Credit Signal &middot; Aug 3, 2026", "Credit", "Signal", "NEW YORK, NY", "AUGUST 3, 2026", "JULY 21&ndash;AUG 3, 2026", CREDIT_SNAPSHOT_0803, CREDIT_SIGNALS_0803, CREDIT_FINAL_PARAGRAPHS_0803, CREDIT_FINAL_BULLETS_0803, "No predictions. No stock references. Facility-anchored interpretation only.", "Market Implications"),
]

ARCHIVE_MARKETS = [(entry_id, label) for entry_id, label, *_ in ARCHIVE_ENTRIES]

ARCHIVE_BLOCKS = []
for i, (entry_id, label, name_a, name_b, dateline, drop, coverage, snapshot, signals, final_paragraphs, final_bullets, tagline, implications_label) in enumerate(ARCHIVE_ENTRIES):
    ARCHIVE_BLOCKS.append(market_block_html(
        "archive", entry_id, i == 0, name_a, name_b, dateline, drop, coverage,
        snapshot, "What Happened", signals, final_paragraphs, final_bullets, tagline,
        implications_label=implications_label,
    ))

ARCHIVE_PAGE = multi_market_page("archive", False, ARCHIVE_MARKETS, ARCHIVE_BLOCKS)

print("Archive page OK", len(ARCHIVE_PAGE))

HOME_PAGE = f'''<section id="page-home" class="page active">
<div class="issue home">
  <div class="home-hero">
    <p class="eyebrow">Weekly Intelligence, By Desk</p>
    <h1 class="home-title brand-word"><span class="cre">Market</span><span class="signal">Signal</span></h1>
    <div class="accent-rule"></div>
    <p class="home-lede">Market Signal is weekly market intelligence for students recruiting into finance &mdash; seven desks, each read closely enough to explain why a deal matters, not just that it happened. Follow your target desk for real fluency in interviews; follow the rest so no adjacent-industry question catches you flat-footed. No predictions. No stock references. Every signal is anchored to something that actually happened &mdash; never commentary floating free of one.</p>
    <form action="https://buttondown.com/api/emails/embed-subscribe/milesnevins" method="post" target="popupwindow" onsubmit="window.open('https://buttondown.com/api/emails/embed-subscribe/milesnevins', 'popupwindow', 'width=600,height=800')" class="subscribe-form">
      <input type="email" name="email" placeholder="Enter email" required class="subscribe-input" aria-label="Email address">
      <button type="submit" class="subscribe-btn">Get it weekly &rarr;</button>
    </form>
  </div>

  <p class="eyebrow">The Desks</p>
  <div class="desk-grid">
{desk_card("cre", "CRE", "Signal",
           "Commercial real estate signals across multiple university markets nationwide.",
           "Latest: Aug 10, 2026", "CRE")}
{desk_card("repe", "REPE", "Signal",
           "Fund closes, platform M&amp;A, take-privates, and sponsor capital strategy signals.",
           "Latest: Aug 10, 2026", "REPE")}
{desk_card("redebt", "RE Debt", "Signal",
           "Construction, bridge, agency, and CMBS lending signals.",
           "Latest: Aug 10, 2026", "RE Debt")}
{desk_card("ib", "IB", "Signal",
           "M&amp;A, capital markets, sponsor finance, and restructuring signals.",
           "Latest: Aug 10, 2026", "IB")}
{desk_card("credit", "Credit", "Signal",
           "Direct lending, BDCs, and private credit signals.",
           "Latest: Aug 10, 2026", "Private Credit")}
{desk_card("structured", "Structured", "Signal",
           "CLOs, ABS, and securitized credit signals.",
           "Latest: Aug 10, 2026", "Structured Finance")}
{desk_card("securitized", "Securitized", "Signal",
           "Non-agency RMBS and CMBS signals.",
           "Latest: Aug 10, 2026", "Securitized Products")}
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
    <a href="#/repe" data-nav="repe">REPE</a>
    <a href="#/redebt" data-nav="redebt">RE Debt</a>
    <a href="#/ib" data-nav="ib">IB</a>
    <a href="#/credit" data-nav="credit">Credit</a>
    <a href="#/structured" data-nav="structured">Structured</a>
    <a href="#/securitized" data-nav="securitized">Securitized</a>
    <a href="#/archive" data-nav="archive">Archive</a>
  </div>
  <div class="settings-picker">
    <button type="button" class="settings-btn" onclick="window.__toggleSettingsMenu()" aria-label="Settings" title="Settings">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>
    </button>
    <div class="settings-menu" id="settings-menu">
      <p class="settings-section-label">Display</p>
      <div class="settings-row">
        <span class="settings-row-label">Theme</span>
        <div class="theme-segmented">
          <button type="button" class="theme-seg-btn" data-theme-choice="light" onclick="window.__setTheme('light')">Light</button>
          <button type="button" class="theme-seg-btn" data-theme-choice="dark" onclick="window.__setTheme('dark')">Dark</button>
        </div>
      </div>
    </div>
  </div>
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
    var segBtns = document.querySelectorAll(".theme-seg-btn");
    for (var i = 0; i < segBtns.length; i++){
      segBtns[i].classList.toggle("active", segBtns[i].getAttribute("data-theme-choice") === theme);
    }
  }
  window.__setTheme = function(theme){
    try { localStorage.setItem(KEY, theme); } catch(e){}
    reflect(theme);
  };
  reflect(current());
})();
</script>'''

SETTINGS_SCRIPT = '''<script>
(function(){
  window.__toggleSettingsMenu = function(){
    var menu = document.getElementById("settings-menu");
    if (menu) menu.classList.toggle("open");
  };
  document.addEventListener("click", function(e){
    var picker = document.querySelector(".settings-picker");
    var menu = document.getElementById("settings-menu");
    if (menu && picker && !picker.contains(e.target)) menu.classList.remove("open");
  });
})();
</script>'''

ROUTER_SCRIPT = '''<script>
(function(){
  var PAGES = ["home","cre","repe","redebt","ib","credit","structured","securitized","about","archive"];
  var MARKETS = {
    cre: ["austin","usc","nyu","uga","uf"],
    redebt: ["austin","usc","nyu","uga","uf"],
    about: ["cre","repe","redebt","ib","credit","structured","securitized"],
    archive: __ARCHIVE_ENTRY_IDS__
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

ARCHIVE_ENTRY_IDS_JSON = "[" + ",".join(f'"{eid}"' for eid, _ in ARCHIVE_MARKETS) + "]"
ROUTER_SCRIPT = ROUTER_SCRIPT.replace("__ARCHIVE_ENTRY_IDS__", ARCHIVE_ENTRY_IDS_JSON)

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
    SETTINGS_SCRIPT,
    HOME_PAGE,
    CRE_PAGE,
    REPE_PAGE,
    REDEBT_PAGE,
    IB_PAGE,
    CREDIT_PAGE,
    STRUCTURED_PAGE,
    SECURITIZED_PAGE,
    ABOUT_PAGE,
    ARCHIVE_PAGE,
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
    "<meta name=\"description\" content=\"Weekly market intelligence for students recruiting into finance — CRE, IB, Private Credit, RE Debt, Structured Finance, and Securitized Products, each read closely enough to explain why a deal matters.\">",
    "<meta property=\"og:type\" content=\"website\">",
    "<meta property=\"og:title\" content=\"Market Signal\">",
    "<meta property=\"og:description\" content=\"Weekly market intelligence for students recruiting into finance — CRE, IB, Private Credit, RE Debt, Structured Finance, and Securitized Products, each read closely enough to explain why a deal matters.\">",
    "<meta property=\"og:url\" content=\"https://market-signal-au3.pages.dev/\">",
    "<meta name=\"twitter:card\" content=\"summary\">",
    "<meta name=\"twitter:title\" content=\"Market Signal\">",
    "<meta name=\"twitter:description\" content=\"Weekly market intelligence for students recruiting into finance.\">",
    "</head>",
    "<body>",
    FRAGMENT,
    "</body>",
    "</html>",
])

out_path = pathlib.Path("/Users/milesnevins/Downloads/files/signal-site.html")
out_path.write_text(html)
print("wrote", out_path, len(html), "bytes")
