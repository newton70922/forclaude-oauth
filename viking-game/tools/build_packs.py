# 把還沒單獨發布的圖打包成 packs/pNN.bin，並把索引寫進 index.html 的 PACK 區塊。
# 已經打包過的圖不會重打；新圖會放進新的圖包。
import os,json,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ART=os.path.join(ROOT,'art');PK=os.path.join(ROOT,'packs');os.makedirs(PK,exist_ok=True)
pub=set(open(os.path.join(ART,'_published.txt')).read().split())
P=os.path.join(ROOT,'index.html');s=open(P,encoding='utf-8').read()
m=re.search(r'/\*PACK\*/(.*?)/\*PACKEND\*/',s,re.S);pack=json.loads(m.group(1)) if m else {}
keys=sorted(k[:-5] for k in os.listdir(ART) if k.endswith('.webp'))
todo=[k for k in keys if k not in pub and k not in pack]
n=max([int(re.search(r'p(\d+)',v[0]).group(1)) for v in pack.values()]+[0])
LIMIT=1_600_000;cur=[];size=0
def flush():
    global n,cur,size
    if not cur:return
    n+=1;fn=f'packs/p{n:02d}.wasm';off=0;buf=bytearray()
    for k in cur:
        b=open(os.path.join(ART,k+'.webp'),'rb').read();pack[k]=[fn,off,len(b)];buf+=b;off+=len(b)
    open(os.path.join(ROOT,fn),'wb').write(buf);print(fn,len(cur),len(buf));cur=[];size=0
for k in todo:
    sz=os.path.getsize(os.path.join(ART,k+'.webp'))
    if size+sz>LIMIT:flush()
    cur.append(k);size+=sz
flush()
blob='/*PACK*/'+json.dumps(pack,separators=(',',':'))+'/*PACKEND*/'
s=s.replace(m.group(0),blob) if m else s
open(P,'w',encoding='utf-8').write(s);print('packed total',len(pack))
