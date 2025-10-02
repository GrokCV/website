---
title: 新芽专题介绍：大模型投毒攻击溯源
date: 2025-09-17T01:08:00Z
draft: false
math: true
---

### 一、专题介绍

#### 1.1 研究背景

大语言模型（LLM）在文本生成方面表现出色，但其知识受限于训练数据，无法获取最新或领域特定的信息。为解决这一问题，检索增强生成（RAG）技术应运而生。RAG系统通过从外部知识库中检索相关文本，为大型语言模型提供额外信息，从而显著提升了生成内容的质量和准确性。

然而，RAG系统在带来便利的同时也引入了新的安全隐患。由于其知识库通常包含来自维基百科等多种来源的文本，攻击者可以通过注入精心设计的“有毒”文本来污染知识库。这种被称为“知识投毒”的攻击方式，可以操控RAG系统，使其针对特定问题生成攻击者预设的误导性或完全错误的答案。尽管学术界已经提出了一些方法，但在面对更具适应性或复杂的攻击时，这些方法往往力不从心。

#### 1.2 研究意义

在这种背景下，仅仅关注如何防御投毒攻击是远远不够的。当一个错误的生成事件发生后，能够准确地追溯并定位到导致该错误生成的“有毒”文本来源，显得尤为重要。这项工作被称为“责任归属”。

这项研究的意义在于：

- **理解错误根源**: 通过定位“有毒”文本，系统设计者可以深入了解模型产生错误行为的根本原因。
- **数据审计**: 能够对数据来源进行有效的审查和清理，移除恶意内容。
- **攻击溯源**: 有助于追踪攻击行为，并为设计更强大的防御机制提供关键信息。

总而言之，对RAG系统中的“毒知识”进行责任归属，是构建更透明、更可信赖的AI系统的关键一步。

#### 1.3 当前主要挑战

在RAG系统中实现准确的责任归属面临着三大挑战：

- **归属范围的规模性**：现代知识库通常包含数百万甚至更多的文档，从中找出极少数被投毒的文本，如同大海捞针，计算成本极高。
- **责任衡量的复杂性**：在RAG的两阶段架构中，“有毒”文本的影响是间接的。它首先影响检索器的检索结果，进而改变提供给大语言模型的上下文，这种复杂的相互作用使得直接衡量单个文本的因果影响力变得非常困难。
- **“有毒”文本的识别难题**：系统在进行责任归属时，通常不知道攻击者注入了多少“有毒”文本，也无法预知其采用的攻击策略。这使得设定一个固定的阈值来区分正常文本和“有毒”文本变得极具挑战性。

## 二、学习资料与参考文献

### 2.1  基础教材与学习材料

以下是你可以使用的一些**书籍/教程**：

* 李沐[《动手学深度学习》](https://zh.d2l.ai/)——适合中文初学者的深度学习教材，以及[课程系列视频](https://space.bilibili.com/1567748478/lists/358497?type=series)
* [《Deep Learning》](https://www.deeplearningbook.org/)（Ian Goodfellow 等）——深度学习入门经典教材
* [PyTorch 官方教程](https://pytorch.org/tutorials)，也可以使用 [PyTorch 中文文档](https://pytorch-cn.readthedocs.io/zh/latest/)
* [Build a Large Language Model (From Scratch)](https://github.com/rasbt/LLMs-from-scratch?tab=readme-ov-file) —— by Sebastian Raschka

此外，你也可以使用一些**入门工具**：

* [Google Colab](https://colab.research.google.com/)：免费云平台，不用安装软件，就能跑PyTorch代码。

* [Kaggle平台](https://www.kaggle.com/)：免费数据集和竞赛

### 2.2 相关文献

**RAG相关文献**

Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (NIPS 2020)

From Local to Global: A GraphRAG Approach to Query-Focused Summarization (2024)

Improving Retrieval Augmented Language Model with Self-Reasoning (AAAI 2025)

Sure: Summarizing retrievals using answer candidates for open-domain QA of LLMs (ICLR 2024)

Flashrag: A modular toolkit for efficient retrieval-augmented generation research (WWW 2025)

**RAG Poisoning Attack相关文献**

PoisonedRAG: Knowledge Corruption Attacks to {Retrieval-Augmented} Generation of Large Language Models (USENIX 2025)

Machine against the rag: Jamming retrieval-augmented generation with blocker documents  (USENIX 2025)

"glue pizza and eat rocks"–exploiting vulnerabilities in retrieval-augmented generative models (EMNLP 2024)

FlippedRAG: Black-Box Opinion Manipulation Adversarial Attacks to Retrieval-Augmented Generation Models (CCS 2025)

AGENTPOISON: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases (NIPS 2024)

**Traceback相关文献**

Poison forensics: Traceback of data poisoning attacks in neural networks (USENIX 2022)

Beagle: Forensics of deep learning backdoor attack for better defense (NDSS 2023)

LAQuer: Localized Attribution Queries in Content-grounded Generation (ACL 2025)

TracLLM: A Generic Framework for Attributing Long Context LLMs (USENIX 2025)

Traceback of poisoning attacks to retrieval-augmented generation (WWW 2025)

Who Taught the Lie? Responsibility Attribution for Poisoned Knowledge in Retrieval-Augmented Generation (IEEE S&P 2026)

## 三、结语与期望

“新芽计划”的初衷是点燃新芽学子对未知探索的热情，并为大家提供一片成长的沃土。希望通过这个专题，新芽学子不仅能学到前沿的 AI 知识，更能培养出独立思考、动手实践和解决复杂问题的能力。

我们热切期待，在最终的汇报中，能看到大家闪耀着智慧火花的解读与创见！