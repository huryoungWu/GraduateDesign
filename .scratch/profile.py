import os, re, glob, collections

D = r"D:\GraduateDesign\.ref_text"
files = sorted(glob.glob(os.path.join(D, "*.txt")))

KEYS = {
 "传统统计/ML": ["ARIMA","SARIMA","指数平滑","EWMA","Prophet","STL","XGBoost","LightGBM","随机森林","支持向量机","SVM","LOF","孤立森林","Isolation Forest","K-Means","DBSCAN","卡尔曼","3-Sigma","IQR","GARCH","VAR","Hawkes","时间点过程","马尔可夫","causal","因果"],
 "经典DL": ["LSTM","GRU","RNN","CNN","TCN","自编码器","Autoencoder","VAE","GAN","扩散模型","Diffusion","GNN","图卷积","GCN","GAT","MLP","Mamba","状态空间","SSM"],
 "Transformer": ["Transformer","Informer","Autoformer","FEDformer","PatchTST","iTransformer","TimesNet","TFT","Temporal Fusion","DLinear","注意力机制","Attention","Dynaformer","Monarchformer","BGMformer"],
 "LLM": ["大语言模型","大模型","LLM","GPT","Llama","BERT","RoBERTa","T5","Time-LLM","GLM","Qwen","提示","Prompt","LoRA","语义"],
 "TSFM": ["时序基础模型","基础模型","Foundation Model","预训练","MOMENT","TimesFM","Chronos","Moirai","TimeGPT","UniTS","Timer","TimesNet基础","零样本","少样本","zero-shot","few-shot"],
}

for f in files:
    t = open(f, encoding='utf-8', errors='ignore').read()
    t = re.sub(r'\s+', '', t)
    name = os.path.basename(f)[:-4]
    print("="*25, name)
    # TOC: between 目录 and 第一章 (or 第1章)
    m = re.search(r'目录(.{0,4000}?)(第一章|第1章)', t)
    if m:
        toc = m.group(1)
        # get chapter/section headings roughly
        heads = re.findall(r'(第[一二三四五六七八九十]+章[^\.．]{0,40})', toc)
        subs = re.findall(r'(\d+\.\d+(?:\.\d+)?[^\.．]{0,30})', toc)
        print("章节:", " | ".join(heads[:12]))
        print("小节:", " ; ".join(subs[:28]))
    else:
        print("目录: 未找到")
    counts = {}
    for cat, kws in KEYS.items():
        c = sum(t.count(k) for k in kws)
        present = [k for k in kws if t.count(k) > 0]
        counts[cat] = (c, present[:18])
    for cat,(c,p) in counts.items():
        print(f"{cat}: {c} | {','.join(p)}")
    print()
