import base64,io,random
from fontTools import subset
from fontTools.ttLib import TTFont
from PIL import Image
O='../'; A=O+'assets/'
D='fonts/'
def wf(fn):
    o=subset.Options(); o.flavor='woff'; f=TTFont(D+fn); s=subset.Subsetter(o)
    s.populate(unicodes=list(range(32,127))+[0x2022,0xB7]); s.subset(f); f.flavor='woff'
    b=io.BytesIO(); f.save(b); return base64.b64encode(b.getvalue()).decode()
FD,FM,FB=wf('BricolageGrotesque-Bold.ttf'),wf('JetBrainsMono-Regular.ttf'),wf('JetBrainsMono-Bold.ttf')
CSS=("@font-face{font-family:UKD;font-weight:700;src:url(data:font/woff;base64,%s) format('woff')}"
"@font-face{font-family:UKM;font-weight:400;src:url(data:font/woff;base64,%s) format('woff')}"
"@font-face{font-family:UKM;font-weight:700;src:url(data:font/woff;base64,%s) format('woff')}"
".d{font-family:UKD,'Space Grotesk',Arial,sans-serif;font-weight:700}"
".m{font-family:UKM,'JetBrains Mono',Consolas,monospace}.b{font-weight:700}")%(FD,FM,FB)
G,GL,W,MU,BD='#FFC700','#FFE8A0','#F5F5F0','#8A8A85','rgba(255,199,0,0.15)'
def b64(im):
    if isinstance(im,str): im=Image.open(im)
    b=io.BytesIO(); im.save(b,'PNG',optimize=True); return 'data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()
ID=b64('id_embed.png'); RP=b64('rp_embed.png')
t=Image.open('id_embed.png'); t=t.resize((int(t.width*340/t.height),340),Image.LANCZOS); IDS=b64(t)
def T(x,y,s,c='m',fill=W,sz=14,extra=''): return f'<text x="{x}" y="{y}" class="{c}" fill="{fill}" font-size="{sz}" {extra}>{s}</text>'
def dot(cx,cy,p,r=4): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{G}"><animate attributeName="opacity" values="1;.2;1" dur="1.6s" repeatCount="indefinite"/></circle>'
def R(x,y,w,h,rx=12,fill='#101010',st=BD,sw=1,extra=''): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{st}" stroke-width="{sw}" {extra}/>'
def svg(p,h,body,defs=''):
    bg=(f'<radialGradient id="{p}glow" cx="85%" cy="40%" r="60%"><stop offset="0" stop-color="{G}" stop-opacity=".13"/><stop offset="1" stop-color="{G}" stop-opacity="0"/></radialGradient>'
        f'<linearGradient id="{p}gold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{GL}"/><stop offset="1" stop-color="{G}"/></linearGradient>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1280" height="{h}" viewBox="0 0 1280 {h}">'
      f'<defs><style>{CSS}</style>{bg}{defs}</defs><rect width="1280" height="{h}" fill="#070707"/><rect width="1280" height="{h}" fill="url(#{p}glow)"/>'
      f'<rect x=".5" y=".5" width="1279" height="{h-1}" fill="none" stroke="{BD}"/>{body}</svg>')
def save(n,s): open(A+n,'w').write(s)
def img(h,x,y,w,hh,par='xMidYMax meet',): return f'<image x="{x}" y="{y}" width="{w}" height="{hh}" preserveAspectRatio="{par}" xlink:href="{h}"/>'
def corners(x,y,w,h,l=22):
    d=f'M{x},{y+l} V{y} H{x+l} M{x+w-l},{y} H{x+w} V{y+l} M{x+w},{y+h-l} V{y+h} H{x+w-l} M{x+l},{y+h} H{x} V{y+h-l}'
    return f'<path d="{d}" fill="none" stroke="{G}" stroke-width="2.5" stroke-linecap="round"/>'
# ---------- HERO
p='hr'; roles=['BUILDER','DEVELOPER','FOUNDER','GAMER']; rl=''
for i,r in enumerate(roles):
    s=i/4; pts={0:0,s:0,s+.02:1,s+.23:1,s+.25:0,1:0}; ks=sorted(pts)
    rl+=f'<text x="96" y="282" class="m b" font-size="34" fill="{GL}" opacity="0">{r}<animate attributeName="opacity" keyTimes="{";".join(f"{k:.2f}" for k in ks)}" values="{";".join(str(pts[k]) for k in ks)}" dur="10s" repeatCount="indefinite"/></text>'
b=(R(60,34,300,34,17,)+dot(82,51,p)+T(98,56,'uzairkadher • PUNJAB • LIVE','m',GL,13,'letter-spacing=".6"')
 +f'<clipPath id="{p}ty"><rect x="58" y="96" width="0" height="40"><animate attributeName="width" calcMode="discrete" values="0;17;34;50;67;84;101;118;134;151;168" keyTimes="0;.1;.2;.3;.4;.5;.6;.7;.8;.9;1" dur="1.4s" begin=".3s" fill="freeze"/></rect></clipPath>'
 +f'<g clip-path="url(#{p}ty)">'+T(60,124,"Salam, I'm",'m b',W,28)+'</g>'
 +f'<rect x="60" y="104" width="12" height="26" fill="{G}"><animate attributeName="x" calcMode="discrete" values="60;77;94;110;127;144;161;178;194;211;228" keyTimes="0;.1;.2;.3;.4;.5;.6;.7;.8;.9;1" dur="1.4s" begin=".3s" fill="freeze"/><animate attributeName="opacity" values="1;0;1" dur=".9s" begin="1.7s" repeatCount="indefinite"/></rect>'
 +f'<clipPath id="{p}nm"><rect x="50" y="138" width="760" height="104"/></clipPath><g clip-path="url(#{p}nm)"><text x="56" y="222" class="d" font-size="92" fill="url(#{p}gold)" letter-spacing="1">UZAIR KADHER'
 +'<animate attributeName="y" calcMode="spline" keyTimes="0;.3;1" keySplines="0 0 1 1;.2 .8 .2 1" values="332;332;222" dur="2.2s" fill="freeze"/></text></g>'
 +f'<path d="M60,252 H800" stroke="{BD}"/>'+T(60,282,'&gt;','m b',G,34)+rl
 +T(60,344,'Most Powerful Systems. Built to Dominate.','d',W,31)
 +R(60,386,486,40,20)+dot(84,406,p,5)+T(102,411,'cpmwall.tech • zeecollection.tech • Punjab, PK','m',GL,13)
 +R(820,50,420,380,22,'#101010',BD,1.2)+f'<ellipse cx="1030" cy="250" rx="150" ry="130" fill="{G}" opacity=".08"/>'+img(ID,820,56,420,368)+corners(820,50,420,380))
save('hero.svg',svg(p,480,b))
# ---------- ABOUT / LIFE
p='ab'
b=(T(60,56,'ABOUT / CAPABILITIES','m b',G,13,'letter-spacing="3"')
 +T(60,118,'I ship products,','d',W,46)+T(60,172,'not just code.','d',G,46))
for i,s in enumerate(['Full Stack Systems','CPMWall.Tech','ZeeCollection.Tech','Automation']):
    x=60+(i%2)*270; y=226+(i//2)*36
    b+=f'<rect x="{x}" y="{y-10}" width="9" height="9" fill="{G}"><animate attributeName="opacity" values="1;.35;1" dur="3s" begin="{i*.5}s" repeatCount="indefinite"/></rect>'+T(x+20,y,s,'m',W,17)
b+=R(60,316,372,40,20)+dot(84,336,p,5)+T(102,341,'2 LIVE STORES • PUNJAB BUILT • 2026','m b',GL,13)
b+=f'<path d="M650,40 V360" stroke="{BD}"/>'+T(690,56,'LIFE / FLEX','m b',G,13,'letter-spacing="3"')
cards=[('CPM','CPM PUNJABI','GAMING COMMUNITY',['Most Powerful Punjabi','Gaming Community','Platform'],'cpmwall.tech'),('ZEE','ZEE COLLECTION','E-COMMERCE',['Premium Watches','E-Commerce','Storefront'],'zeecollection.tech')]
for i,(ic,ti,tg,ls,u) in enumerate(cards):
    x=690+i*280; b+=R(x,80,262,280,18,'#111111',BD,1.2)+f'<circle cx="{x+46}" cy="130" r="26" fill="#151515" stroke="{G}" stroke-width="1.5"/>'+T(x+46,135,ic,'m b',G,13,'text-anchor="middle"')
    b+=dot(x+228,130,p)+T(x+214,134,'LIVE','m b',GL,10,'text-anchor="end"')+T(x+22,188,ti,'d',W,23)+T(x+22,210,tg,'m b',G,11,'letter-spacing="2"')
    for j,l in enumerate(ls): b+=T(x+22,244+j*22,l,'m',MU,14)
    b+=f'<path d="M{x+22},306 H{x+240}" stroke="{BD}"/>'+T(x+22,336,u,'m b',GL,14)
save('about-life.svg',svg(p,400,b))
# ---------- STACK
p='sk'; cx,cy=640,262; b=T(60,72,'STACK • WEAPONS','d',G,40)+T(60,98,'8 tools. 3 orbits. One empire.','m',MU,14)
orb=[(170,58,22,['Next.js','React']),(285,102,32,['Node.js','MongoDB','TypeScript']),(400,150,44,['Tailwind','JavaScript','Python'])]
for k,(rx,ry,du,ch) in enumerate(orb):
    path=f'M{cx-rx},{cy} a{rx},{ry} 0 1 1 {2*rx},0 a{rx},{ry} 0 1 1 {-2*rx},0'
    b+=f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="{G}" stroke-opacity="{.35-k*.08:.2f}" stroke-dasharray="3 7"/>'
    for i,c in enumerate(ch):
        w=len(c)*8.8+34
        b+=f'<g><animateMotion dur="{du}s" begin="-{du*(i/len(ch)+k*.17):.1f}s" repeatCount="indefinite" path="{path}"/>'+R(-w/2,-17,w,34,17,'#151515',G,1.2)+T(0,5,c,'m b',GL,14,'text-anchor="middle"')+'</g>'
b+=(f'<circle cx="{cx}" cy="{cy}" r="26" fill="none" stroke="{G}" stroke-width="1.5"><animate attributeName="r" values="18;40;18" dur="2.4s" repeatCount="indefinite"/><animate attributeName="opacity" values=".8;0;.8" dur="2.4s" repeatCount="indefinite"/></circle>'
 f'<circle cx="{cx}" cy="{cy}" r="11" fill="{G}"><animate attributeName="r" values="9;13;9" dur="2.4s" repeatCount="indefinite"/></circle>')
save('stack.svg',svg(p,460,b))
# ---------- ID DASHBOARD
p='id'; random.seed(7); bars=''; x=450
while x<826:
    w=random.choice([2,2,3,5]); bars+=f'<rect x="{x}" y="404" width="{w}" height="48" fill="{G if random.random()<.18 else W}"/>'; x+=w+random.choice([2,3,4])
row=lambda y,a,c: R(450,y,380,30,8,'#151515')+T(464,y+20,f'<tspan fill="{G}" font-weight="700">{a}</tspan>  {c}','m',W,12)
card=(f'<path d="M640,80 V112" stroke="{G}" stroke-width="6"/>'+R(622,94,36,26,7,'#151515',G,2)+R(430,110,420,360,20,'#101010',G,1.5)+R(608,124,64,8,4,'#070707',BD)
 +R(450,146,140,160,12,'#151515',BD)+f'<clipPath id="{p}ph"><rect x="450" y="146" width="140" height="160" rx="12"/></clipPath><g clip-path="url(#{p}ph)">'+img(IDS,450,146,140,160)+'</g>'
 +T(610,176,'UZAIR KADHER','d',G,25)+T(610,204,'FOUNDER • BUILDER','m b',W,13)+T(610,226,'PUNJAB, PK','m',MU,13)+T(610,256,'ID: UK-GAME-2026','m b',GL,14)
 +R(610,270,124,28,14,'#151515',G,1.2)+f'<path d="M624,284 l5,5 l9,-10" fill="none" stroke="{G}" stroke-width="2.5" stroke-linecap="round"/>'+T(646,289,'VERIFIED','m b',G,12)
 +row(322,'CPMWALL.TECH','GAMING EMPIRE')+row(360,'ZEECOLLECTION.TECH','WATCHES')+bars)
b=f'<path d="M640,0 V80" stroke="{G}" stroke-width="6"/><ellipse cx="640" cy="300" rx="260" ry="200" fill="{G}" opacity=".05"/>'
b+=f'<g>{card}<animateTransform attributeName="transform" type="rotate" values="-1.5 640 80;1.5 640 80;-1.5 640 80" keyTimes="0;.5;1" calcMode="spline" keySplines=".45 0 .55 1;.45 0 .55 1" dur="3s" repeatCount="indefinite"/></g>'
save('id-dashboard.svg',svg(p,540,b))
# ---------- CONNECT
p='cn'; b=img(RP,40,30,380,340,'xMinYMax meet')+T(470,62,'CONNECT • JOIN THE EMPIRE','d',G,34)
items=[('IG','Instagram','@cpm_punjabi','FOLLOW'),('CPM','CPMWall.Tech','cpmwall.tech','VISIT'),('ZEE','ZeeCollection.Tech','zeecollection.tech','SHOP')]
for i,(ic,ti,u,tg) in enumerate(items):
    y=92+i*92; b+=R(470,y,770,76,16,'#111111',G,1.4)+f'<circle cx="514" cy="{y+38}" r="22" fill="#151515" stroke="{G}"/>'+T(514,y+43,ic,'m b',G,12,'text-anchor="middle"')
    b+=T(552,y+34,ti,'d',W,22)+T(552,y+58,u,'m',MU,14)
    ax=700 if i==0 else 800; an=f'<animate attributeName="x" values="{ax};{ax+10};{ax}" dur="1.1s" begin="{i*.3}s" repeatCount="indefinite"/>'
    b+=f'<svg x="{ax}" y="{y+24}" width="30" height="28" overflow="visible">{an}<path d="M4,3 L16,14 L4,25" fill="none" stroke="{G}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    b+=R(1100,y+22,110,32,16,'#151515',BD)+T(1155,y+43,tg,'m b',GL,12,'text-anchor="middle"')
save('connect.svg',svg(p,400,b))
# ---------- README + PREVIEW
open(O+'README.md','w').write('''![Intro](./assets/hero.svg?v=4)
![About](./assets/about-life.svg?v=4)
![Stack](./assets/stack.svg?v=4)
![ID](./assets/id-dashboard.svg?v=4)
![Connect](./assets/connect.svg?v=4)

## Projects

| Project | What it is | Link |
|---|---|---|
| **CPMWall.Tech** | Most Powerful Punjabi Gaming Community Platform | [cpmwall.tech](https://cpmwall.tech) |
| **ZeeCollection.Tech** | Premium Watches E-Commerce | [zeecollection.tech](https://zeecollection.tech) |

## Connect

[![Instagram](https://img.shields.io/badge/Instagram-@cpm__punjabi-FFC700?style=for-the-badge&logo=instagram&logoColor=black&labelColor=070707)](https://www.instagram.com/cpm_punjabi)

<p align="center"><sub>Black Gold Gaming Boss Edition &bull; Built by UZAIR KADHER &bull; PUNJAB 2026</sub></p>
''')
open(O+'preview.html','w').write('<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Preview</title><style>body{margin:0;background:#0d1117;display:flex;flex-direction:column;align-items:center;gap:12px;padding:20px}img{max-width:100%;width:1280px;display:block}</style>'+''.join(f'<img src="assets/{n}.svg?v=4" alt="{n}">' for n in ['hero','about-life','stack','id-dashboard','connect']))
