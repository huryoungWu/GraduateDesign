import os,re,glob
D=r"D:\GraduateDesign\.ref_text"
pats=[r'1\.3(?:\.\d)?本文主要研究内容',r'1\.3(?:\.\d)?本文主要工作',r'1\.3(?:\.\d)?研究内容',r'1\.4(?:\.\d)?本文主要研究内容',r'本文主要研究内容',r'本文的主要工作',r'主要研究内容如下',r'主要工作如下',r'本文主要贡献',r'主要贡献如下']
for f in sorted(glob.glob(os.path.join(D,"*.txt"))):
    t=re.sub(r'\s+','',open(f,encoding='utf-8',errors='ignore').read())
    name=os.path.basename(f)[:-4]
    print("="*22,name)
    best=None
    for p in pats:
        for m in re.finditer(p,t[:len(t)//3]):  # intro area only
            seg=t[m.start():m.start()+1100]
            if seg.count('....')>3: continue
            best=seg; break
        if best: break
    print(best if best else "（未找到明确贡献段，用摘要/方法代替）")
    print()
