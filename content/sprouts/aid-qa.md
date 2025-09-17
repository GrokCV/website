---
title: 新芽专题介绍（8）：AI检测与质量检测
date: 2025-09-17T01:43:00Z
draft: false
math: true
authors: 
- 王雨萌
- 苏奕扬
---

## 一、专题介绍

### 1.1 研究背景

随着大型语言模型（LLMs）的快速发展和广泛应用，其生成文本的质量已达到了令人难以置信的水平，有时**甚至与人类创作的文本几乎无法区分**。这种能力使大模型在多种自然语言处理任务，包括语言翻译、文本摘要、代码生成、故事创作和新闻生成等方面表演出色。然而，LLMs生成高质量文本的能力也带来了潜在的滥用风险和严重的社会问题。因此，对文本进行AI检测变得重要且值得考量。

同时，随着自然语言生成（NLG）技术的迅速发展，如何有效评估生成文本的质量成为关键挑战之一。文本质量评估涉及人工评估和自动化指标两大类方法：前者被视为评价的金标准，能够直接衡量模型输出在语义和语用上的质量，但往往耗时耗力且主观性强；后者则以计算方式快速近似质量，便于大规模实验，但其有效性取决于与人工判断的相关性。

### 1.2 研究意义

1. **AI检测**：防止AI生成内容的滥用，维护学术诚信和内容真实性，为内容审核提供技术支撑。

2. **质量检测**：为自然语言生成系统提供客观、可复现的质量评估与可操作反馈，降低人工评审成本，提升生成内容质量。

3. **技术融合**：将AI检测与质量检测技术相结合，构建更全面的文本评估体系。

### 1.3 当前主要挑战

1. **AI检测挑战**：
   - 检测精度与泛化能力：现有方法在特定模型上表现良好，但跨模型泛化能力有限
   - 对抗性攻击：恶意用户可能通过改写、重述等方式绕过检测
   - 检测速度：实时检测需求与计算复杂度之间的平衡

2. **质量检测挑战**：
   - 评价标准与可解释性：从单一分数走向维度化叙述与可解释评语
   - 多维度指标的定义与标注一致性：如何建立覆盖充分且互不冲突的质量指标
   - 与人工评估的相关性：自动化指标与人工判断的一致性

## 二、学习资料与参考文献

为了引导新芽学子逐步进入研究，本专题结构分为以下四部分：

### 2.1 基础教材与学习材料

在开始探险之前，你需要掌握一些基础的"内功心法"，这些是后续一切学习的基石。以下是你可以使用的一些**书籍/教程**：

* 李沐[《动手学深度学习》](https://zh.d2l.ai/)适合中文初学者的深度学习教材，以及[课程系列视频](https://space.bilibili.com/1567748478/lists/358497?type=series)

* 吴恩达，DeepLearning.AI课程[LLM微调大模型](https://www.bilibili.com/video/BV1c4i9YQEX8/?spm_id_from=333.337.search-card.all.click&vd_source=88ed50b385f354ed4e0a1345a135f69d)

* [《Deep Learning》](https://www.deeplearningbook.org/)（Ian Goodfellow 等）深度学习入门经典教材

* [PyTorch 官方教程](https://pytorch.org/tutorials)，也可以使用 [PyTorch 中文文档](https://pytorch-cn.readthedocs.io/zh/latest/)

* [《Pattern Recognition and Machine Learning》](https://www.microsoft.com/en-us/research/wp-content/uploads/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf)（Christopher M. Bishop）机器学习原理入门（难度不小）

此外，你也可以使用一些**入门工具**：

* [Google Colab](https://colab.research.google.com/)：免费云平台，不用安装软件，就能跑PyTorch代码。

* [Kaggle平台](https://www.kaggle.com/)：免费数据集和竞赛

Tips：务必**摆脱所有基础都打好后，再进行下一阶段学习的心态**，在干中学，遇到不明白的再回溯补基础。

***

### 2.2 入门文献（经典方法）

> 学生第一阶段的阅读训练，可帮助理解AI检测与质量检测这一通用方向,具象化去了解"文本检测与评估"。**仅用于入门，不可选择此部分文献汇报**。

**AI检测综述**：

1. [A Survey on LLM-Generated Text Detection](https://arxiv.org/abs/2310.14724): Necessity, Methods, and Future Directions (2023, 综述)

**文本质量评估综述**：

1. [Best practices for the human evaluation of automatically generated text](https://aclanthology.org/W19-8643/) (2019, 综述)
2. [A Survey on Evaluation of Large Language Models](https://arxiv.org/abs/2307.03109) (2023, 综述)
3. [From Generation to Judgment: Opportunities and Challenges of LLM-as-a-judge](https://arxiv.org/abs/2411.16594) (2024, 综述)

**经典AI检测方法**：

1. [Detecting Fake Content with Relative Entropy Scoring](https://ceur-ws.org/Vol-377/paper4.pdf) (2019)
2. [Gltr](https://arxiv.org/abs/1906.04043): Statistical detection and visualization of generated text (ACL 2019)

**经典质量评估方法**：

1. [BLEU](https://aclanthology.org/P02-1040/): a method for automatic evaluation of machine translation (ACL 2002)
2. [ROUGE](https://aclanthology.org/W04-1013/): A Package for Automatic Evaluation of Summaries (2004)

***

### 2.3 进阶文献（前沿方法）

> 学生可在此部分选择进阶文献进行专题汇报，或自行查找最新的同类重要文献。在此，我们将正式接触AI检测与质量检测的前沿方法。

**AI检测前沿方法：**

**基于统计特征的方法**：

1. [DetectGPT](https://arxiv.org/abs/2301.11305): Zero-Shot Machine-Generated Text Detection using Probability Curvature (ICML 2023)
2. [DetectLLM](https://arxiv.org/abs/2306.05540): Leveraging Log Rank Information for Zero-Shot Detection of Machine-Generated Text (EMNLP 2023)
3. [Fast-DetectGPT](https://arxiv.org/abs/2310.05130): Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature (ICLR 2024)

**基于监督和对比学习的方法**：

4. [CoCo](https://arxiv.org/abs/2212.10341): Coherence-Enhanced Machine-Generated Text Detection Under Data Limitation With Contrastive Learning (EMNLP 2023)
5. [ConDA](https://arxiv.org/abs/2309.03992): Contrastive Domain Adaptation for AI-generated Text Detection (IJCNLP-AACL 2023)
6. [Deepfake Text Detection in the Wild](https://arxiv.org/abs/2305.13242v2) (ACL 2024)
7. [OUTFOX](https://arxiv.org/abs/2307.11729): LLM-Generated Essay Detection Through In-Context Learning with Adversarially Generated Examples (AAAI 2024)
8. [DNA-GPT](https://arxiv.org/abs/2305.17359): Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text (ICLR 2024)
9. [Who Wrote This?](https://arxiv.org/abs/2405.04286) The Key to Zero-Shot LLM-Generated Text Detection Is GECScore (COLING 2025)
10. [Spotting LLMs With Binoculars](https://arxiv.org/abs/2401.12070): Zero-Shot Detection of Machine-Generated Text (ICML 2024)
11. [RepreGuard](https://arxiv.org/abs/2508.13152): Detecting LLM-Generated Text by Revealing Hidden Representation Patterns (TACL 2025)
12. [DetectAnyLLM](https://fjc2005.github.io/detectanyllm): Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models (ACMMM 2025)

**基于水印的方法**：

13. [A Watermark for Large Language Models](https://arxiv.org/abs/2301.10226) (ICML 2023)
14. [On the Reliability of Watermarks for Large Language Models](https://arxiv.org/abs/2306.04634) (ICLR 2024)

**文本质量评估前沿方法**：

**人工评估方法**：

1. [Re-Examining Summarization Evaluation across Multiple Quality Criteria](https://aclanthology.org/2023.findings-emnlp.924/) (EMNLP 2023)
2. [SummEval](https://arxiv.org/abs/2007.12626): Re-evaluating Summarization Evaluation (TACL 2021)
3. [Experts, Errors, and Context](https://arxiv.org/abs/2104.14478): A Large-Scale Study of Human Evaluation for Machine Translation (TACL 2021)
4. [Best-Worst Scaling More Reliable than Rating Scales](https://arxiv.org/abs/1712.01765): A Case Study on Sentiment Intensity Annotation (ACL 2017)

**自动化指标方法**：

5. [MoverScore](https://arxiv.org/abs/1909.02622): Text Generation Evaluating with Contextualized Embeddings and Earth Mover Distance (EMNLP 2019)
6. [BERTScore](https://arxiv.org/abs/1904.09675): Evaluating Text Generation with BERT (ICLR 2020)
7. [G-Eval](https://arxiv.org/abs/2303.16634): NLG Evaluation using Gpt-4 with Better Human Alignment (EMNLP 2023)

***

## 三、结语与期望

"新芽计划"的初衷是点燃新芽学子对未知探索的热情，并为大家提供一片成长的沃土。希望通过这个专题，新芽学子不仅能学到前沿的 AI 知识，更能培养出独立思考、动手实践和解决复杂问题的能力。

我们热切期待，在最终的汇报中，能看到大家闪耀着智慧火花的解读与创见！
