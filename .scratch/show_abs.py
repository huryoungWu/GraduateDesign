import os, re, sys, glob

D = r"D:\GraduateDesign\.ref_text"
files = sorted(glob.glob(os.path.join(D, "*.txt")))

def clean(s):
    s = re.sub(r'\s+', '', s)
    return s

for f in files:
    t = open(f, encoding='utf-8', errors='ignore').read()
    name = os.path.basename(f)[:-4]
    # abstract cn: first occurrence of 摘要
    m = re.search(r'摘\s*要(.*?)(关键词|關鍵詞)', t, re.S)
    if not m:
        print("="*20, name, "NO ABSTRACT")
        continue
    ab = clean(m.group(1))
    kwm = re.search(r'关键词[：: ]*(.{0,120})', clean(t[m.end():m.end()+400]))
    kw = kwm.group(1) if kwm else ''
    print("="*20, name)
    print("摘要:", ab[:1800])
    print("关键词:", kw[:150])
    print()
