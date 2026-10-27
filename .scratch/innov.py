import os,re,glob
D=r"D:\GraduateDesign\.ref_text"
pats=["主要创新","创新点","主要贡献","贡献如下","本文的主要工作","研究内容如下","本文工作","工作总结"]
for f in sorted(glob.glob(os.path.join(D,"*.txt"))):
    t=re.sub(r'\s+','',open(f,encoding='utf-8',errors='ignore').read())
    name=os.path.basename(f)[:-4]
    print("="*25,name)
    shown=0
    for p in pats:
        for m in re.finditer(p,t):
            s=max(0,m.start()-80); e=min(len(t),m.start()+700)
            seg=t[s:e]
            # avoid TOC-like segments
            if seg.count('....')>5: continue
            print(f"[{p}]",seg)
            shown+=1
            if shown>=3: break
        if shown>=3: break
    if shown==0:
        # fallback: conclusion
        m=re.search(r'(总结与展望|结论与展望|第六章总结|第七章总结)',t)
        if m: print("[结论]",t[m.start():m.start()+700])
        else: print("[无]")
    print()
