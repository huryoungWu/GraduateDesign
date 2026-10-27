import re,sys,os
D=r"D:\GraduateDesign\.ref_text"
name=sys.argv[1]; terms=sys.argv[2].split("|"); n=int(sys.argv[3]) if len(sys.argv)>3 else 2
t=re.sub(r'\s+','',open(os.path.join(D,name+'.txt'),encoding='utf-8',errors='ignore').read())
for term in terms:
    print("\n---",term)
    c=0
    for m in re.finditer(re.escape(term),t):
        s=max(0,m.start()-350); e=min(len(t),m.start()+650)
        print(t[s:e]); print("...")
        c+=1
        if c>=n: break
