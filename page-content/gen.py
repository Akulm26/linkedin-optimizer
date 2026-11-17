import subprocess,os,json
F="file:///Users/akulsuhailmalhotra/Content-calendar-automation/assets/fonts/"
SC="/private/tmp/claude-501/-Users-akulsuhailmalhotra-Content-calendar-automation-linkedin-optimizer/3b07b06e-3a99-4b40-a472-8942583399f6/scratchpad/banner/lockup_dark.png"
CSS=f"""@font-face{{font-family:SS4;src:url('{F}SourceSerif4-normal-400.woff2');font-weight:400}}
@font-face{{font-family:SS4;src:url('{F}SourceSerif4-italic-500.woff2');font-weight:500;font-style:italic}}
@font-face{{font-family:FG;src:url('{F}Figtree-normal-400.woff2');font-weight:400}}
@font-face{{font-family:RHM;src:url('{F}RedHatMono-normal-500.woff2');font-weight:500}}
html,body{{margin:0;background:#F4EFE7}}
.s{{display:flex;flex-direction:column;justify-content:center;padding-bottom:190px !important;position:relative;width:1080px;height:1350px;overflow:hidden;box-sizing:border-box;padding:120px 96px;font-family:FG,sans-serif}}
.dk{{background:#751F23;color:#F4EFE7}}.lt{{background:#F4EFE7;color:#240F0F}}
h1,h2{{font-family:SS4,serif;font-weight:400;letter-spacing:-0.03em;margin:0}} h1{{font-size:104px;line-height:1.04}} h2{{font-size:76px;line-height:1.1}}
i{{font-style:italic;font-weight:500}}
p{{font-size:40px;line-height:1.45;margin:36px 0 0;max-width:820px}}
.lab{{font-family:RHM,monospace;font-size:30px;letter-spacing:.1em;text-transform:uppercase;margin-bottom:40px}}
.lt .lab{{color:#751F23}}.dk .lab{{color:#F4EFE7}}

.src{{font-family:RHM,monospace;font-size:30px;margin-top:56px;opacity:.75;color:#240F0F}}
ul{{list-style:none;padding:0;margin:44px 0 0;font-size:42px;line-height:1.35}} li{{padding:20px 0;border-top:2px solid #DCD2CB}} .dk li{{border-color:#9b5a5d}}
li b{{font-family:RHM,monospace;font-weight:500;font-size:30px;color:#751F23;margin-right:24px}}
.ft{{position:absolute;left:96px;right:96px;bottom:72px;display:flex;justify-content:space-between;align-items:center;font-family:RHM,monospace;font-size:30px}}
"""
def mark(sl):
    carve = "#751F23" if sl=="dk" else "#F4EFE7"
    fill = "#240F0F" if sl=="dk" else "#240F0F"
    sight = "#CADC7F" if sl=="dk" else "#751F23"
    return f'<svg width="72" height="72" viewBox="0 0 40 40"><polygon points="2,36 28,10 28,36" fill="{fill}"/><path d="M13 20.4 Q22 19.6 30 19 M5 28.4 Q18 27.2 30 26.4" stroke="{carve}" stroke-width="2.4" fill="none"/><rect x="31" y="10" width="7" height="3.4" fill="{sight}"/></svg>'
def slide(sl,n,total,body,foot=True):
    ftr=f'<div class="ft"><span>{n:02d} / {total:02d}</span>{mark(sl)}</div>' if foot else ''
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="s {sl}"><div>{body}</div>{ftr}</div></body></html>'
def render(html,out):
    open('/tmp/_s.html','w').write(html)
    subprocess.run(['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome','--headless=new','--disable-gpu','--hide-scrollbars','--force-device-scale-factor=2','--window-size=1080,1350','--allow-file-access-from-files','--screenshot='+out,'file:///tmp/_s.html'],capture_output=True)
S=[
("dk","<h1>Brands don't have a content problem.<br><i>They have a go-to-market system problem.</i></h1>"),
("lt","<div class='lab'>The problem</div><h2>Facts live in a few heads. Content gets made by hand.</h2><p>That is a system problem. And systems can be engineered.</p>"),
("lt","<div class='lab'>What GTM engineering is</div><h2>Building <i>automated revenue systems.</i></h2><p>Using AI, data enrichment and workflow automation.</p><div class='src'>Source: Clay, clay.com/blog/gtm-engineering</div>"),
("lt","<div class='lab'>What GTM engineers build</div><ul><li><b>01</b>Integrations between CRM, enrichment and outreach tools</li><li><b>02</b>Scripts that clean and de-duplicate lead data</li><li><b>03</b>Automated outbound playbooks</li><li><b>04</b>Product-usage signals sent to sales reps</li></ul><div class='src'>Source: Topo, topo.io/glossary/gtm-engineer</div>"),
("lt","<div class='lab'>The job in one line</div><h2>Find and fix <i>revenue bottlenecks.</i></h2><p>Clay says it coined the title in 2023. Its GTM engineers act like an internal product team for the go-to-market organization.</p><div class='src'>Source: Clay, clay.com/blog/gtm-engineering</div>"),
("lt","<div class='lab'>Where Clyve fits</div><h2>GTM engineering <i>for brands.</i></h2><p>Audit first: map how your go-to-market runs today. Then build the system.</p>"),
("lt","<div class='lab'>We run it on ourselves</div><h2>Our own posts go through a <i>claims log and a source check.</i></h2><p>Build logs from our own system, every week on this page.</p>"),
("dk",f"<div class='lab'>Next move</div><h1>Want an audit?<br><i>DM us.</i></h1><p>Follow Clyve for weekly build logs.</p><img src='file://{SC}' style='height:64px;margin-top:80px'>"),
]
os.makedirs('start-here',exist_ok=True)
for i,(sl,b) in enumerate(S,1):
    render(slide(sl,i,len(S),b,foot=(i<len(S))),f'start-here/slide-{i:02d}.png')
# build log card
steps=["Read what's working on LinkedIn and Instagram","Plan the next 14 days. Rules are checked in code","Draft each post. Every draft ends with a claims log","Lint the draft","Re-check each claim's source the morning it posts","Render the image. A gate rejects any number not in the draft","A human posts it"]
li=''.join(f"<li><b>{i:02d}</b>{t}</li>" for i,t in enumerate(steps,1))
body=f"<div class='lab'>Build log 01 · How Clyve runs its own content</div><ul style='margin-top:10px;font-size:38px'>{li}</ul>"
render(slide("lt",1,1,body).replace('<span>01 / 01</span>','<span>CLYVE</span>'),'build-log-1/card.png')
