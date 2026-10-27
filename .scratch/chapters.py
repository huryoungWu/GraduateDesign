import os, re, glob
D = r"D:\GraduateDesign\.ref_text"
for f in sorted(glob.glob(os.path.join(D,"*.txt"))):
    t = re.sub(r'\s+','',open(f,encoding='utf-8',errors='ignore').read())
    name=os.path.basename(f)[:-4]
    print("="*20,name)
    seen=[]
    for m in re.finditer(r'第[一二三四五六七八九十]+章',t):
        s=t[m.start():m.start()+45]
        if s not in seen and len(s)>6:
            seen.append(s)
    # keep plausible chapter headings
    out=[s for s in seen if not s.endswith('第')][:14]
    print(" | ".join(out))
