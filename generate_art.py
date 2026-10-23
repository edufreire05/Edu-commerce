"""Builds local, self-contained editorial SVG assets for the fictional demo catalog."""
from pathlib import Path
import html
O=Path(__file__).parent/'public/assets';O.mkdir(parents=True,exist_ok=True)
def wrap(bg,content,number,accent='#ff6105'):
 return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 820" width="720" height="820"><defs>
 <radialGradient id="bg" cx="58%" cy="38%" r="72%"><stop stop-color="#fff4e9"/><stop offset=".57" stop-color="{bg}"/><stop offset="1" stop-color="{bg}" stop-opacity=".85"/></radialGradient>
 <linearGradient id="metal" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#fff9e9"/><stop offset=".54" stop-color="#d4cbba"/><stop offset="1" stop-color="#aaa49c"/></linearGradient>
 <linearGradient id="purple" x1="0" y1="0" x2=".95" y2="1"><stop stop-color="#dfc8f9"/><stop offset=".5" stop-color="#9985db"/><stop offset="1" stop-color="#5148a7"/></linearGradient>
 <linearGradient id="console" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#d9d8d8"/><stop offset=".58" stop-color="#a4a6a8"/><stop offset="1" stop-color="#717681"/></linearGradient>
 <linearGradient id="orange" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#ffe59b"/><stop offset=".45" stop-color="#ff8b38"/><stop offset="1" stop-color="#ed4b52"/></linearGradient>
 <linearGradient id="dark" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#52505d"/><stop offset=".45" stop-color="#242434"/><stop offset="1" stop-color="#10101b"/></linearGradient>
 <linearGradient id="horizon" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#39265d"/><stop offset=".5" stop-color="#e46685"/><stop offset="1" stop-color="#ffb769"/></linearGradient>
 <filter id="shadow" x="-50%" y="-50%" width="200%" height="210%"><feGaussianBlur stdDeviation="24"/></filter>
 <filter id="subtle" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="2" dy="12" stdDeviation="12" flood-color="#282334" flood-opacity=".25"/></filter>
 <pattern id="dots" width="21" height="21" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.2" fill="#000" opacity=".08"/></pattern>
 </defs>
 <rect width="720" height="820" fill="url(#bg)"/><rect width="720" height="820" fill="url(#dots)"/>
 <circle cx="550" cy="154" r="240" fill="#fff" opacity=".16"/>
 <path d="M0 670L720 560V820H0Z" fill="#fff" opacity=".11"/>
 <ellipse cx="360" cy="664" rx="244" ry="50" fill="#27192f" opacity=".23" filter="url(#shadow)"/>
 {content}
 <g font-family="Arial,sans-serif" letter-spacing="5" font-size="13" fill="#29252b" opacity=".42"><text x="45" y="60">REWIND® / ARCHIVE</text><text x="45" y="775">OBJECT NO. {number}</text><text x="607" y="775">© 26</text></g>
 <path d="M45 80H675" stroke="#333" opacity=".16" stroke-width="1"/>
 </svg>'''
def text(x,y,s,size=22,fill='#fff',weight=800,ls=1,anchor='middle'):
 return f'<text x="{x}" y="{y}" fill="{fill}" text-anchor="{anchor}" font-family="Arial,sans-serif" font-size="{size}" font-weight="{weight}" letter-spacing="{ls}">{html.escape(s)}</text>'
def buttons(cx,cy):
 return f'<rect x="{cx-52}" y="{cy-10}" width="104" height="20" rx="5" fill="#323035"/>'+f'<rect x="{cx-10}" y="{cy-52}" width="20" height="104" rx="5" fill="#323035"/>'

def pocket(color=False):
 shell='url(#purple)' if color else 'url(#metal)'
 scr='#4a7656' if not color else '#f6b3e5'
 return f'''<g transform="translate(32 22) rotate(-11 340 380)" filter="url(#subtle)"><rect x="189" y="154" width="300" height="502" rx="38" fill="{shell}" stroke="#fff" stroke-opacity=".5" stroke-width="8"/><rect x="204" y="170" width="270" height="466" rx="30" fill="none" stroke="#615c61" stroke-opacity=".12" stroke-width="3"/><rect x="219" y="198" width="242" height="223" rx="13" fill="#43454c"/><rect x="232" y="215" width="216" height="185" rx="5" fill="#2c3034"/><rect x="265" y="235" width="149" height="145" rx="5" fill="{scr}"/><rect x="278" y="249" width="123" height="115" fill="#536e5c" opacity=".65"/>'''+ (f'<circle cx="340" cy="307" r="30" fill="#ffb15e"/><path d="M289 332L340 272L393 332" fill="none" stroke="#ff77a0" stroke-width="9"/>' if color else '<path d="M290 328h22v-22h20v-20h20v-22h20" stroke="#243d2f" stroke-width="9" fill="none"/>') + f'''{text(340,394,'DOT MATRIX' if not color else 'COLOR DISPLAY',10,'#bbc2bc',500,2)}{buttons(275,498)}<g transform="rotate(-22 407 501)"><ellipse cx="385" cy="500" rx="17" ry="13" fill="#8e2852"/><ellipse cx="427" cy="500" rx="17" ry="13" fill="#8e2852"/></g><rect x="301" y="580" width="30" height="7" rx="3.5" fill="#58525a"/><rect x="345" y="580" width="30" height="7" rx="3.5" fill="#58525a"/>{text(340,613,'REWIND • POCKET',12,'#50495a',700,2)}</g>'''

def console(version=1):
 if version==1:
  return '''<g filter="url(#subtle)" transform="rotate(-7 355 400)"><path d="M103 400L248 291H563L642 427L512 583H160Z" fill="#786b86"/><path d="M110 388L248 289H560L632 410L515 548H162Z" fill="url(#console)" stroke="#e2dee8" stroke-width="7"/><path d="M245 337h300l55 85H178Z" fill="#777086"/><path d="M255 348h280l37 60H215Z" fill="#423f50"/><path d="M165 440h436l-78 94H175Z" fill="#a5a5ad"/><rect x="248" y="476" width="150" height="17" rx="8" fill="#484356"/><rect x="427" y="475" width="34" height="21" rx="7" fill="#49434e"/><circle cx="538" cy="479" r="13" fill="#65606d"/>'''+text(390,385,'SUPER 16',39,'#e8e2ec',900,1)+text(339,527,'REWIND  /  1991',15,'#54505c',700,3)+'''</g>'''
 return '''<g filter="url(#subtle)" transform="rotate(5 360 395)"><path d="M121 382L210 305H579L634 437L552 550H141Z" fill="#27292e"/><path d="M130 365L210 294H566L625 420L549 524H150Z" fill="url(#dark)" stroke="#777883" stroke-width="5"/><path d="M230 323H541L589 412H178Z" fill="#14151e"/><path d="M241 339h280l35 60H205Z" fill="#4b4d57"/><circle cx="370" cy="373" r="57" fill="#252630" stroke="#81818e" stroke-width="7"/><circle cx="370" cy="373" r="33" fill="#151821"/><path d="M181 464h395" stroke="#82838c" stroke-width="4"/><rect x="216" y="475" width="187" height="17" rx="8" fill="#111318"/><circle cx="523" cy="476" r="11" fill="#ff6105"/>'''+text(370,534,'RETRO DRIVE / 32',18,'#b9bbbf',900,2)+'''</g>'''

def cartridge(title,number,scheme):
 c1,c2=scheme
 return f'''<g transform="translate(27 7) rotate(-8 360 370)" filter="url(#subtle)"><path d="M190 180h323v54h42v408H145V234h45Z" fill="#2e2e39"/><path d="M198 194h309v50h34v382H159V245h39Z" fill="#555261"/><rect x="186" y="267" width="327" height="267" rx="8" fill="{c1}"/><rect x="197" y="278" width="305" height="245" rx="3" fill="url(#horizon)"/><circle cx="409" cy="354" r="74" fill="{c2}" opacity=".94"/><path d="M196 484L267 401L310 446L394 362L508 488v34H196Z" fill="#241d4d"/><path d="M196 493L260 447L310 470L369 420L508 493v29H196Z" fill="#ff7658" opacity=".76"/><path d="M222 512h267M230 488h251M243 466h229" stroke="#ffeeb6" opacity=".28" stroke-width="2"/>{text(350,317,title,33,'#ffffff',900,1)}{text(351,344,number,18,'#ffe89d',800,4)}<rect x="182" y="554" width="341" height="50" rx="7" fill="#393746"/>{text(353,584,'REWIND ENTERTAINMENT SYSTEM',13,'#c4c1cf',700,1)}<path d="M211 638h255" stroke="#211e2c" stroke-width="9"/></g>'''

def stick():
 return '''<g transform="rotate(-7 350 400)" filter="url(#subtle)"><path d="M104 467L243 382H539L640 499L553 586H148Z" fill="#151a2d"/><path d="M117 454L248 369H536L628 485L546 561H155Z" fill="url(#dark)" stroke="#56607a" stroke-width="6"/><path d="M238 406H521L584 481H163Z" fill="#262e49"/><ellipse cx="274" cy="453" rx="66" ry="33" fill="#101220"/><path d="M269 437L257 246" stroke="#222330" stroke-width="24" stroke-linecap="round"/><circle cx="256" cy="239" r="51" fill="url(#orange)" stroke="#ffbb65" stroke-width="9"/>'''+''.join(f'<circle cx="{x}" cy="{y}" r="22" fill="{c}" stroke="#0e1523" stroke-width="6"/>' for x,y,c in [(406,430,'#ff6105'),(474,425,'#ffbe5e'),(441,480,'#ef4661'),(516,473,'#68d3d8'),(532,422,'#a993e3'),(374,473,'#ee9d9d')])+text(345,540,'ARCADE / ZERO',17,'#e6c58d',800,4)+'''</g>'''

def controller():
 return '''<g filter="url(#subtle)" transform="rotate(-8 365 450)"><path d="M205 353Q266 308 360 341Q480 306 525 365L601 529Q609 594 549 601Q519 596 473 536H251Q200 609 151 600Q104 591 129 517Z" fill="#49434e"/><path d="M216 355Q265 318 360 354Q468 314 513 367L585 520Q592 580 550 580Q513 578 467 516H255Q200 592 159 580Q132 575 151 522Z" fill="url(#metal)" stroke="#f0dfc9" stroke-width="6"/>{buttons(244,436)}<circle cx="481" cy="405" r="17" fill="#e49a52"/><circle cx="522" cy="440" r="17" fill="#b359a4"/><circle cx="442" cy="449" r="17" fill="#478fce"/><circle cx="485" cy="483" r="17" fill="#6ba774"/><rect x="322" y="423" width="37" height="11" rx="5" fill="#77717a"/><rect x="371" y="423" width="37" height="11" rx="5" fill="#77717a"/>'''+text(367,489,'64',18,'#5a5664',900,1)+'''</g>'''

def arcade():
 return '''<g filter="url(#subtle)" transform="rotate(-6 350 410)"><path d="M266 120H487L545 255L527 666H207L219 265Z" fill="#161927"/><path d="M279 134H471L529 262L515 646H223L234 266Z" fill="url(#dark)" stroke="#7a547e" stroke-width="8"/><path d="M279 147H472L508 214H245Z" fill="url(#orange)"/>'''+text(376,193,'PIXEL',39,'#241b3b',900,2)+'''<path d="M273 245H477L482 421H258Z" fill="#080a17" stroke="#ec7a8c" stroke-width="9"/><rect x="283" y="264" width="174" height="137" fill="url(#horizon)"/><circle cx="386" cy="321" r="45" fill="#ffba76"/><path d="M290 381l40-45 34 26 32-61 59 79" fill="#262356"/><path d="M234 433H495L523 505H217Z" fill="#de77a1"/><circle cx="311" cy="461" r="18" fill="#ffce61"/><path d="M313 448v-36" stroke="#35203d" stroke-width="12"/><circle cx="405" cy="464" r="12" fill="#f6e5b1"/><circle cx="444" cy="464" r="12" fill="#59499b"/><rect x="254" y="541" width="217" height="79" rx="8" fill="#20213c"/>'''+text(361,590,'REWIND ARCADE',20,'#ffb967',800,2)+'''</g>'''

def figure():
 pix='''<path d="M222 239h52v-43h52v44h54v-44h55v44h54v165h-54v55h-54v-55h-52v55h-55v-55h-52Z" fill="#82bba1" stroke="#347b6e" stroke-width="9"/><rect x="275" y="310" width="43" height="43" fill="#182e2d"/><rect x="392" y="310" width="43" height="43" fill="#182e2d"/><rect x="258" y="385" width="42" height="43" fill="#347b6e"/><rect x="411" y="385" width="42" height="43" fill="#347b6e"/>'''
 return f'''<g filter="url(#subtle)" transform="rotate(-3 345 390)">{pix}<path d="M248 470L234 518H483L463 470Z" fill="#343d44"/><rect x="225" y="519" width="272" height="59" rx="11" fill="url(#dark)"/>{text(362,556,'8 BIT LEGEND',20,'#f9f0cc',800,3)}</g>'''

def vhs():
 return '''<g filter="url(#subtle)" transform="rotate(-9 350 400)"><rect x="115" y="257" width="505" height="311" rx="18" fill="#1f1e29"/><rect x="128" y="273" width="478" height="274" rx="12" fill="#292a34" stroke="#79747b" stroke-width="5"/><rect x="150" y="298" width="436" height="168" rx="5" fill="url(#horizon)"/><path d="M150 458L280 340L354 398L466 300L586 428V466H150Z" fill="#322250"/>'''+text(368,352,'GAME NIGHT',45,'#fff1c9',900,2)+text(365,389,'PLAY • REWIND • REPEAT',13,'#fff1c9',700,2)+'''<rect x="149" y="482" width="438" height="51" rx="8" fill="#15161c"/><circle cx="234" cy="508" r="22" fill="#74747b"/><circle cx="503" cy="508" r="22" fill="#74747b"/><rect x="304" y="496" width="137" height="23" rx="5" fill="#444550"/></g>'''
items={
 'pixel-pocket':('#eadcb7',pocket(False),'01'),
 'super-station':('#e3d8e9',console(1),'02'),
 'neon-runner':('#ffa88e',cartridge('NEON RUNNER','DX',('#eb6677','#ff9d72')),'03'),
 'arcade-stick':('#c0d8e9',stick(),'04'),
 'pocket-color':('#d7c2e6',pocket(True),'05'),
 'galactic-quest':('#b3d7cb',cartridge('GALACTIC','QUEST IV',('#6daaba','#b0e1df')),'06'),
 'dual-pad':('#ffd4bd',controller(),'07'),
 'mini-arcade':('#f4c16e',arcade(),'08'),
 'space-figure':('#bddecd',figure(),'09'),
 'vhs-night':('#f2b8cb',vhs(),'10'),
 'retro-drive':('#cfd2d9',console(2),'11'),
 'moonlight-racer':('#c3c6f5',cartridge('MOONLIGHT','RACER',('#7b6caf','#f1c3b9')),'12')
}
for name,(bg,art,number) in items.items():
 full=wrap(bg,art,number)
 (O/(name+'.svg')).write_text(full,encoding='utf-8')
 # transparent product-only composition for hero and collection highlights
 import re
 inner=re.search(r'(<defs>.*?</defs>)',full,re.S).group(1)
 cutout=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 820">{inner}{art}</svg>'
 (O/(name+'-cutout.svg')).write_text(cutout,encoding='utf-8')
print(f'Generated {len(items)} distinct product illustrations')
