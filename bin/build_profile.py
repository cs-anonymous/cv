#!/usr/bin/env python3
"""Generate bilingual public pages and fixed Chinese PDFs."""
from pathlib import Path
import argparse, html, json, os
ROOT = Path(__file__).resolve().parents[1]
D = json.loads((ROOT / '_data/profile.json').read_text())
esc = html.escape
LANG = 'zh-CN'
UI = {'教育经历':'Education','研究经历':'Research','工程实践与企业合作':'Engineering & industry collaboration','工程实践':'Engineering','技术与语言':'Technical Skills & Languages','学术交流':'Research visit','荣誉奖励':'Honors & awards','论文列表':'Publications','详细履历':'Full CV','研究方法与实验详情 →':'Research methods and results →','下载简洁版 PDF':'Resume PDF (Chinese)','下载详细版 PDF':'Full CV PDF (Chinese)','阅读详细履历':'Read full CV','微信／手机':'WeChat / Phone','手机':'Phone','邮箱':'Email','学校邮箱':'University email','微信':'WeChat','导师':'Advisor','副导师':'Co-advisor'}
def tr(s): return UI.get(s,s) if LANG=='en' else s
def local(path): return "{{ '" + path + "' | relative_url }}"
def route(path): return ('/en' + path) if LANG=='en' else path

def entry(x, detailed=False):
    meta=' · '.join(filter(None,[x.get('period'),x.get('status',x.get('org',''))]))
    ident=f' id="{esc(x["id"])}"' if x.get('id') else ''
    out=f'<section class="entry"{ident}><h3>{esc(x["title"])}</h3><div class="meta">{esc(meta)}</div>'
    if detailed:
        description_label='Project Description:' if LANG=='en' else '项目描述：'
        contribution_label='Key Contributions:' if LANG=='en' else '主要贡献：'
        out+=f'<ul class="project-points"><li><strong>{description_label}</strong> {esc(x.get("summary",x.get("text","")))}</li>'
        if x.get('details'):
            out+=''.join(f'<li><strong>{contribution_label}</strong> {esc(detail)}</li>' for detail in x['details'])
        out+='</ul>'
    else:
        out+=f'<p>{esc(x.get("summary",x.get("text","")))}</p>'
    if x.get('links'): out+='<div class="entry-links">'+''.join(f'<a href="{esc(u)}">{esc(k)} ↗</a>' for k,u in x['links'].items())+'</div>'
    return out+'</section>\n'
def papers():
    out=''
    for x in D['publications']:
        title=esc(x['title'])
        if x['url']: title=f'<a href="{esc(x["url"])}">{title}</a>'
        out+=f'<section class="entry"><div class="pub-title">{title}</div>'
        if x['authors']: out+=f'<div class="pub-authors">{esc(x["authors"])}</div>'
        out+=f'<div class="meta">{esc(x["venue"])} · {esc(x["role"])}</div></section>'
    return out

def personal():
    c=D['contact'];parts=[]
    for label,value,url in [('微信／手机',c['phone'],'tel:'+c['phone'].replace(' ','')),('邮箱',D['email'],'mailto:'+D['email']),('微信',c['wechat'],None),('学校邮箱',c['university_email'],'mailto:'+c['university_email'])]:
        value=esc(value)
        if url: value=f'<a href="{esc(url)}">{value}</a>'
        parts.append(f'<div><dt>{tr(label)}</dt><dd>{value}</dd></div>')
    supervisors=' · '.join(f'{tr(x["role"])}：<a href="{esc(x["url"])}">{esc(x["name_en"] if LANG=="en" else x["name"])}</a>' for x in D['supervisors'])
    facts=' · '.join(esc(v) for k,v in D['personal'] if k in ('所在城市','预计毕业','Location','Expected graduation'))
    location = c['location'] if LANG == 'zh-CN' else c['location']
    target = c['target'] if LANG == 'zh-CN' else c['target']
    return f'<div class="personal-intro"><img class="portrait" src="{local("/assets/img/ye-sun.jpg")}" width="124" height="180" alt="{esc(D["english_name"] if LANG=="en" else D["name"])}" decoding="async"><div><p class="intro">{esc(D["intro"])}</p><p class="supervisors">{supervisors}</p><p class="meta">{facts}</p><p class="meta">{esc(location)} · {esc(target)}</p><dl class="contact-grid">'+''.join(parts)+'</dl></div></div>'

def page(name,title,path,content,nav=False,nav_label=None,nav_order=None):
    pref='en-' if LANG=='en' else ''
    other=path if LANG=='en' else '/en'+path
    if path == '/404.html': other = '/en/'
    fm=['---','layout: page',f'title: "{title}"',f'permalink: {route(path)}',f'lang: {LANG}',f'alternate_url: {other}']
    if nav:
        fm += [f'nav_label: "{nav_label or title}"','nav: true',f'nav_order: {nav_order}']
    else:
        fm += ['nav: false']
    fm+=['---','',f'<link rel="stylesheet" href="{local("/assets/css/profile.css")}">','<div class="profile-content">',content,'</div>','']
    (ROOT/'_pages'/(pref+name)).write_text('\n'.join(fm))

def pages_for_language():
    research_order={'geneticprism':0,'expath':1,'ruledep':2,'inspire':3,'cueir':4}
    experience_order={'materagent':0,'geneticflow':1,'classification':2,'materials':3,'sensetime-aigc':4,'sensetime-tools':5}
    intro=personal();edu=''.join(entry(x) for x in D['education']);research=''.join(entry(x,True) for x in sorted(D['research'],key=lambda x: research_order.get(x.get('id'),99)));engineering=''.join(entry(x,True) for x in sorted(D['experience'],key=lambda x: experience_order.get(x.get('id'),99)));awards='<ul>'+''.join('<li>'+esc(a)+'</li>' for a in D['awards'])+'</ul>'
    def heading(s,ident=''): return f'<h2'+(f' id="{ident}"' if ident else '')+'>'+tr(s)+'</h2>'
    skills='<dl class="skills-list">'+''.join(f'<div><dt>{esc(x["label"])}</dt><dd>{esc(x["text"])}</dd></div>' for x in D['skills'])+'</dl>'
    toc='<nav class="toc" aria-label="'+('CV sections' if LANG=='en' else '履历目录')+'">'+''.join(f'<a href="#{i}">{tr(t)}</a>' for i,t in [('education','教育经历'),('research','研究经历'),('engineering','工程实践'),('skills','技术与语言'),('publications','论文列表')])+'</nav>'
    short=intro+toc+heading('教育经历','education')+edu+heading('研究经历','research')+research
    short+=heading('工程实践与企业合作','engineering')+engineering+heading('技术与语言','skills')+skills+heading('学术交流')+entry(D['visit'])+heading('论文列表','publications')+papers()+heading('荣誉奖励')+awards
    page('about.md','Ye Sun · 孙烨' if LANG=='en' else '孙烨 · Ye Sun','/',short,nav=True,nav_label='Home' if LANG=='en' else '简历',nav_order=0)
    page('research.md',tr('研究经历'),'/research/',research)
    page('experience.md',tr('工程实践'),'/experience/',engineering)
    page('publications.md',tr('论文列表'),'/publications/',papers())
    detail=intro+toc
    detail+=heading('教育经历','education')+edu+heading('研究经历','research')+research+heading('工程实践','engineering')+engineering+heading('技术与语言','skills')+skills+heading('学术交流')+entry(D['visit'])+heading('论文列表','publications')+papers()+heading('荣誉奖励')+awards
    page('cv.md',tr('详细履历'),'/cv/',detail,nav=True,nav_label='Full CV' if LANG=='en' else '详细履历',nav_order=4)

def validate_bilingual():
    zh=json.loads((ROOT/'_data/profile.json').read_text())
    en=json.loads((ROOT/'_data/profile.en.json').read_text())
    def compare_structure(zh_value,en_value,path='profile'):
        if type(zh_value) is not type(en_value):
            raise ValueError(f'Chinese and English {path} values must use the same data type.')
        if isinstance(zh_value,dict):
            if path.endswith('.links'):
                if len(zh_value) != len(en_value) or list(zh_value.values()) != list(en_value.values()):
                    raise ValueError(f'Chinese and English {path} entries must point to the same URLs in the same order.')
                return
            if set(zh_value) != set(en_value):
                raise ValueError(f'Chinese and English {path} fields must match.')
            if zh_value.get('id') != en_value.get('id'):
                raise ValueError(f'Chinese and English {path} entries must preserve the same ID and order.')
            for key in zh_value:
                compare_structure(zh_value[key],en_value[key],f'{path}.{key}')
        elif isinstance(zh_value,list):
            if len(zh_value) != len(en_value):
                raise ValueError(f'Chinese and English {path} lists must have the same length.')
            for index,(zh_item,en_item) in enumerate(zip(zh_value,en_value)):
                compare_structure(zh_item,en_item,f'{path}[{index}]')
    compare_structure(zh,en)

def pages():
    global D,LANG
    validate_bilingual()
    original=D
    for lang,file in [('zh-CN','profile.json'),('en','profile.en.json')]:
        LANG=lang;D=json.loads((ROOT/'_data'/file).read_text());pages_for_language()
    D=original;LANG='zh-CN'
    page('404.md','页面未找到 / Page not found','/404.html',f'<p><a href="{local("/")}">返回首页 / Home</a></p>')
    blog=ROOT/'_pages/blog.md'
    if blog.exists():blog.unlink()

def pdfs():
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.lib import colors
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.enums import TA_LEFT
    from reportlab.lib.pagesizes import A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether
    font=os.environ.get('CV_FONT','/System/Library/Fonts/Supplemental/Arial Unicode.ttf')
    if not Path(font).exists(): raise SystemExit('Set CV_FONT to a Chinese-capable TrueType font path.')
    pdfmetrics.registerFont(TTFont('CV',font))
    styles={
      'body':ParagraphStyle('body',fontName='CV',fontSize=9.3,leading=14.5,spaceAfter=5,wordWrap='CJK'),
      'small':ParagraphStyle('small',fontName='CV',fontSize=8,leading=12,textColor=colors.HexColor('#586373'),spaceAfter=4,wordWrap='CJK'),
      'title':ParagraphStyle('title',fontName='CV',fontSize=25,leading=32,spaceAfter=8),
      'h2':ParagraphStyle('h2',fontName='CV',fontSize=13.5,leading=20,spaceBefore=11,spaceAfter=6,textColor=colors.HexColor('#6b287f'),keepWithNext=True),
      'h3':ParagraphStyle('h3',fontName='CV',fontSize=10.3,leading=16,spaceBefore=5,spaceAfter=3,keepWithNext=True,wordWrap='CJK')}
    def p(t,kind='body'): return Paragraph(esc(t),styles[kind])
    def section(story,title): story.append(p(title,'h2'))
    def item(story,x,detail=False):
        block=[p(x['title'],'h3'),p(' · '.join(filter(None,[x.get('period'),x.get('status',x.get('org',''))])),'small')]
        if detail:
            block.append(p('• 项目描述：'+x.get('summary',x.get('text',''))))
            block.extend(p('• 主要贡献：'+detail) for detail in x.get('details', []))
        else:
            block.append(p(x.get('summary',x.get('text',''))))
        if x.get('links'):
            block.append(Paragraph(' · '.join(f'<link href="{esc(url)}" color="#6b287f">{esc(label)}</link>' for label,url in x['links'].items()),styles['small']))
        story.append(KeepTogether(block))
    def footer(c,doc):
        c.setFont('CV',8);c.setFillColor(colors.HexColor('#667085'))
        c.drawString(40,24,'孙烨 · Ye Sun | '+D['updated']);c.drawRightString(A4[0]-40,24,str(doc.page))
    dest=ROOT/'assets/pdf';dest.mkdir(exist_ok=True)
    for detailed,name in [(False,'Ye-Sun-Resume-ZH.pdf')]:
        story=[p('孙烨  Ye Sun','title'),p(D['intro']),Paragraph(f'<link href="mailto:{D["email"]}">{D["email"]}</link>',styles['body'])]
        story.append(Paragraph('导师：<link href="https://leishidata.com/">时磊</link> · 副导师：<link href="https://scholar.google.com/citations?user=aeCHfDIAAAAJ&amp;hl=en">童咏昕</link>',styles['small']))
        story.append(p('微信／手机：'+D['contact']['phone'],'small'))
        story.append(Paragraph('学校邮箱：<link href="mailto:sunie@buaa.edu.cn">sunie@buaa.edu.cn</link>',styles['small']))
        section(story,'教育经历')
        for x in D['education']: story.extend([p(x['period']+' · '+x['title'],'h3'),p(x['text'])])
        section(story,'研究经历')
        for x in D['research']: item(story,x,True)
        section(story,'工程实践与企业合作')
        for x in D['experience']: item(story,x,True)
        skills_block=[p('技术与语言','h2')]
        for x in D['skills']:
            skills_block.extend([p(x['label'],'h3'),p(x['text'])])
        story.append(KeepTogether(skills_block))
        section(story,'学术交流');item(story,D['visit'])
        section(story,'荣誉奖励')
        for x in D['awards']: story.append(p(x))
        if detailed:
            section(story,'论文列表')
            for x in D['publications']:
                block=[p(x['title'],'h3')]
                if x['authors']: block.append(p(x['authors'],'small'))
                block.append(p(x['venue']+' · '+x['role'],'small'));story.append(KeepTogether(block))
        doc=SimpleDocTemplate(str(dest/name),pagesize=A4,rightMargin=40,leftMargin=40,topMargin=35,bottomMargin=40,title='孙烨 | '+('详细履历' if detailed else '研究简历'),author='Ye Sun')
        doc.build(story,onFirstPage=footer,onLaterPages=footer)
        print(dest/name)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--pages-only',action='store_true');args=parser.parse_args()
    pages()
    if not args.pages_only: pdfs()
