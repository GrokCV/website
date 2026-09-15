---
title: 新芽专题介绍（25）：汇报多维度质量检测
date: 2025-09-18T01:35:00Z
draft: false
math: true
---

## 研究背景

汇报多维度质量检测肇始于自然语言文本评估、图像质量评估（IQA）、视频质量评估（VQA）等质量评估（QA）领域。由于在当下的工作需求、教育背景，PPT汇报的出现频率越来越高，人们越来越依赖PPT汇报手段进行表达。并且，在当下智能化需求增长的背景下，对汇报的自动化评估的研究蓬勃发展。“汇报多维度质量检测”旨在自动评估PPT/幻灯片质量与口头/视频汇报表现的多维指标，如版式与可读性、信息层次、配色对比、语音清晰度、节奏、肢体与目光、与幻灯片内容的一致性等。相关研究正在从“单模态启发式规则/打分”走向“多模态特征与大模型驱动”的方法，并开始出现专门面向幻灯片质量的数据集与标注体系（如 SlideAudit 等）。

## 研究意义

- 教学/培训/教育：为课堂、MOOC 与企业培训提供客观、可复现的质量评估与可操作反馈，降低人工评审成本。
- 内容生产与辅助创作：为“生成—评估—改进”闭环提供可度量目标（如幻灯片版式缺陷检测、口播节奏与停顿优化）

## 当前挑战

- **数据与可泛化性**：真实课堂/会议场景差异巨大，模型易受领域偏移影响；多模态公开数据仍较有限
- **评价标准与可解释性**：从单一分数走向维度化叙述与可解释评语，到如今大模型作为Judge。但是这些评价标准依然存在显著问题，不是很令人信服。
- **多维指标的定义与标注一致性**：如何建立覆盖充分且互不冲突的幻灯片缺陷分类与口头表现指标，并获得稳定标注

## 基础资料

- [《动手学深度学习》](https://space.bilibili.com/1567748478/lists/358497?type=series) - 适合中文初学者的深度学习教材
- [《Deep Learning》](https://www.deeplearningbook.org/) - 深度学习入门经典教材
- [《Pattern Recognition and Machine Learning》](https://www.microsoft.com/en-us/research/wp-content/uploads/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf) - 机器学习原理入门
- [Google Colab](https://colab.research.google.com/) - 免费云平台，不用安装软件，就能跑PyTorch代码
- [Hugging Face](https://huggingface.co/) - 获取预训练模型、数据集和学习教程的开源社区

## 入门文献

- [Video Quality Assessment: A Comprehensive Survey](https://arxiv.org/abs/2412.04508) (arxiv)
- [LLM-based NLG Evaluation: Current Status and Challenges](https://arxiv.org/abs/2402.01383) (ACL 2025)
- [LLMJ: A Survey on LLM-as-a-Judge](https://www.arxiv.org/abs/2411.15594) (IDEA 2025)
- [HMMs for PQA: Multimodal Assessment of Oral Presentations using HMMs](https://dl.acm.org/doi/10.1145/3382507.3418888) (ICMI 2020)
- [MPSSA: Multimodal Public Speaking Performance Assessment](https://dl.acm.org/doi/10.1145/2818346.2820762) (ICMI 2025)

## 进阶文献

- [PPTC Benchmark: Evaluating Large Language Models for PowerPoint Task Completion](https://huggingface.co/papers/2311.01767) (ACL 2024)
- [PPTAgent: Generating and Evaluating Presentations Beyond Text-to-Slides](https://www.arxiv.org/abs/2501.03936) (EMNLP 2025)
- [AutoPresent: Designing Structured Visuals from Scratch](https://www.arxiv.org/abs/2501.00912) (CVPR 2025)
- [Zoom-VQA : Patches, Frames and Clips Integration for Video Quality Assessment](https://www.arxiv.org/abs/2304.06440) (CVPR 2023)
- [Fast-VQA : Efficient End-to-end Video Quality Assessment with Fragment Sampling](https://arxiv.org/abs/2207.02595v1) (ECCV 2022)
- [NR-VQA : Neighbourhood Representative Sampling for Efficient End-to-end Video Quality Assessment](https://arxiv.org/abs/2210.05357) (TPAMI 2023)

## 相关文献



## 结语

“新芽计划”的初衷是点燃新芽学子对未知探索的热情，并为大家提供一片成长的沃土。希望通过这个专题，新芽学子不仅能学到前沿的 AI 知识，更能培养出独立思考、动手实践和解决复杂问题的能力。

我们热切期待，在最终的汇报中，能看到大家闪耀着智慧火花的解读与创见！
