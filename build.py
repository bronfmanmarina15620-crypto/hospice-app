import json,base64,glob
ps=[json.load(open(f)) for f in sorted(glob.glob('data/*.json'))]
ps.sort(key=lambda p:['rs','rm','rk'].index(p['id']) if p['id'] in['rs','rm','rk'] else 9)
t=open('template.html').read().replace('/*DATA*/',json.dumps(ps,ensure_ascii=False)).replace('/*INFO*/',open('info.json').read()).replace('LOGO','data:image/png;base64,'+base64.b64encode(open('logo.png','rb').read()).decode())
open('hospice.html','w').write(t);open('index.html','w').write(t)
