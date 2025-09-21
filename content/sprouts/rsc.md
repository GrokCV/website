---
title: 新芽专题介绍（21）：科研成果传播重塑
date: 2025-09-17T01:30:00Z
draft: false
math: true
---

## 一、专题介绍

### 1.1  研究背景

当今，人工智能作为一种快速发展且深刻影响全球产业链与价值链的科学技术，已成为国际科技竞争的战略高地，这一点在AI领域科研文献的年发表量上有明显体现。2022年全球AI领域发表的科研文献数量超过24.2万篇，已是 2015年发文量的两倍之多，如下图所示，且目前科研成果传播的方式仍以PDF为主，这给科研人员带来了很大的文献阅读压力。

回顾信息传播方式的发展史，实际上也是人类认知方式和社会沟通模式不断演进的过程。从早期以文字为核心的传播（如收音机、书信等），到文字与图片相结合的形式（如报纸、期刊），再到如今以视频和短视频为主导的多媒体传播，传播方式的变化深刻影响了知识的生产、分享与接受。然而，在科研领域，成果的传播仍主要依赖文字与图片构成的PDF文档。这一形式在人工智能技术快速发展的当下显然不够优越。

<p align="center">
  <img src="https://i.ibb.co/MksnjNt1/image-20250914160937162.png" alt="AI文献数量" style="zoom:67%;" />
</p>

### 1.2  研究意义

目前虽然已经有了根据文字生成ppt或图片的Agent，但是对于学术论文这一多模态长上下文输入，这些Agent往往取得的效果不佳。本课题基于上述背景，旨在探索科研成果在未来的全新呈现方式，通过使用Agent技术，突破现有的PDF传播模式，逐步探索至最终的传播形式，从而完成科研传播形式的变革。

目前课题已有两个子课题：

- paper2poster：旨在端到端的为学术论文生成美观、信息量足的学术海报。
- paper2ppt：paper2video的前置课题，旨在端到端的为学术论文生成presentation ppt，为最终的video提供内容基础。

### 1.3  当前主要挑战

在科研成果传播方式的重塑过程中，仍面临诸多亟需解决的挑战：

1. **挑战一：大模型性能的限制**
   * 当前生成式大模型的性能仍存在明显瓶颈，直接影响到科研成果传播的呈现效果。
   * 生成复杂内容所需的时间与算力开销较大，在已有工作paper2video中，单篇论文生成视频往往需要超过一小时，并消耗超过 20 万 tokens 。

2. **挑战二：结构未确定**
   - 目前拟确定的最终目标为结构化短视频的方式，如何合理设计短视频的结构与叙事逻辑，以在有限时长内实现科研信息的最优传递，这一结构仍需逐步探讨。
3. **挑战三：没有客观评价指标**
   * 当前对科研成果传播方式的评判多依赖主观感受，没有例如acc这种客观指标进行衡量。

综上，科研成果传播的重塑仍处于探索初期，研究门槛相对较低，且作为新兴领域具有较高的创新潜力。这是一个很好的实践窗口：从实际需求出发，所做即前沿。

***

## 二、学习资料与参考文献

为了引导新芽学子逐步进入研究，本专题结构分为以下四部分：

***

### 2.1  基础教材与学习材料

在开始探险之前，你需要掌握一些基础的“内功心法”，这些是后续一切学习的基石。以下是你可以使用的一些**书籍/教程**：

* 李沐[《动手学深度学习》](https://zh.d2l.ai/)——适合中文初学者的深度学习教材，以及[课程系列视频](https://space.bilibili.com/1567748478/lists/358497?type=series)

* [《Deep Learning》](https://www.deeplearningbook.org/)（Ian Goodfellow 等）——深度学习入门经典教材

* [PyTorch 官方教程](https://pytorch.org/tutorials)，也可以使用 [PyTorch 中文文档](https://pytorch-cn.readthedocs.io/zh/latest/)

* [《Pattern Recognition and Machine Learning》](https://www.microsoft.com/en-us/research/wp-content/uploads/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf)（Christopher M. Bishop）——机器学习原理入门（难度不小）

此外，你也可以使用一些**入门工具**：

* [Google Colab](https://colab.research.google.com/)：免费云平台，不用安装软件，就能跑PyTorch代码。

* [Kaggle平台](https://www.kaggle.com/)：免费数据集和竞赛

Tips：务必**摆脱所有基础都打好后，再进行下一阶段学习的心态**，在干中学，遇到不明白的再回溯补基础。

***

### 2.2  入门文献

> 学生第一阶段的阅读训练，可帮助理解目标检测/语义分割/关键点检测这一通用方向。**仅用于入门，不可选择此部分文献汇报**。

* **[Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/pdf/2201.11903) (NeurIPS 2022)**
* **[ReAct](https://arxiv.org/pdf/2210.03629): Synergizing Reasoning and Acting in Language Models(ICLR 2023)**
* **[Toolformer](https://arxiv.org/pdf/2302.04761): Language Models Can Teach Themselves to Use Tools(NeurIPS 2023)**
* **[Language Models as Zero-Shot Planners](https://arxiv.org/pdf/2201.07207): Extracting Actionable Knowledge for Embodied Agents(ICML 2022)**
* **[HuggingGPT](https://arxiv.org/pdf/2303.17580): Solving AI Tasks with ChatGPT and its Friends in Hugging Face(NeurIPS 2023)**
* **[Voyager](https://arxiv.org/pdf/2305.16291): An Open-Ended Embodied Agent with Large Language Models(NeurIPS 2023)**
* **[A Comprehensive Review of AI Agents](https://arxiv.org/pdf/2508.11957): Transforming Possibilities**
* **[MetaGPT](https://arxiv.org/pdf/2308.00352): Meta Programming for A Multi-Agent Collaborative Framework(ICLR 2024)**
* **[A Survey on Large Language Model based Autonomous Agents](https://arxiv.org/pdf/2308.11432)**
* **[Agent AI]( https://arxiv.org/pdf/2401.03568): Surveying the Horizons of Multimodal Interaction**

***

### 2.3  进阶文献

> 学生可在此部分选择进阶文献进行专题汇报，或自行查找最新的同类重要文献。
>

* **[The AI Scientist](https://arxiv.org/pdf/2408.06292): Towards Fully Automated Open-Ended Scientific Discovery（github star 11.5k）**

* **[From Words to Worth](https://www.arxiv.org/pdf/2308.11432v1): Newborn Article Impact Prediction with LLM（AAAI 2025）**

* **[MA-RAG](https://arxiv.org/pdf/2505.20096): Multi-Agent Retrieval-Augmented Generation via Collaborative Chain-of-Thought Reasoning**

* **[ResearchAgent](https://www.arxiv.org/pdf/2404.07738v2): Iterative Research Idea Generation over Scientific Literature with Large Language Models(NAACL 2025)**

* **[Chain of Ideas](https://www.arxiv.org/pdf/2410.13185): Revolutionizing Research Via Novel Idea Development with LLM Agents**

* **[Language agents achieve superhuman synthesis of scientific knowledge](https://www.arxiv.org/pdf/2409.13740)**
* **The Budget AI Researcher and the Power of [RAG](https://www.arxiv.org/pdf/2506.12317) Chains**
* **[A Real-World WebAgent with Planning](https://arxiv.org/pdf/2307.12856), Long Context Understanding, and Program Synthesis (ICLR 2024)**
* **[Mobile-Agent](https://www.arxiv.org/pdf/2401.16158): Autonomous Multi-Modal Mobile Device Agent with Visual Perception（ICLR 2024）**

***

### 2.4  科研传播重塑领域相关文献

> 结合本专题的研究背景，逐渐引导学生进入科研传播重塑课题。学生可在此部分选择进阶文献进行专题汇报，或自行查找最新的同类重要文献。
>
> 目前课题直接相关的高质量工作较少

**Paper To Poster**

1. **[Paper2Poster](https://www.arxiv.org/pdf/2505.21497v1): Towards Multimodal Poster Automation from Scientific Papers**

**Paper To Video**

1. **[Preacher](https://www.arxiv.org/abs/2508.09632v6): Paper-to-Video Agentic System（ICCV 2025）**
2. **[PresentAgent](https://www.arxiv.org/pdf/2507.04036): Multimodal Agent for Presentation Video Generation**

**Paper To PPT**

1. **[PPTAgent](https://www.arxiv.org/pdf/2501.03936): Generating and Evaluating Presentations Beyond Text-to-Slides [EMNLP 2025]**

2. **[Talk to Your Slides](https://www.arxiv.org/abs/2505.11604): Language-Driven Agents for Efficient Slide Editing**

## 三、结语与期望

“新芽计划”的初衷是点燃新芽学子对未知探索的热情，并为大家提供一片成长的沃土。科研传播重塑是一个充满挑战与机遇的领域，它既是国家需求的“硬骨头”，也是学术创新的“试金石”。希望通过这个专题，新芽学子不仅能学到前沿的 AI 知识，更能培养出独立思考、动手实践和解决复杂问题的能力。

我们热切期待，在最终的汇报中，能看到大家闪耀着智慧火花的解读与创见！
