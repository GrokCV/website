---
title: 新芽专题介绍（41）：文档智能
date: 2025-09-17T01:10:00Z
draft: false
math: true
authors: 
- admin
---

## 一、专题介绍

### 1.1  研究背景

在信息爆炸的时代，**文档是人类知识最重要的载体之一**。无论是科研论文、法律合同、财务报表，还是日常的办公文档、发票、专利说明书，它们都承载着关键的结构化与非结构化信息。如何让机器能够自动理解这些文档，成为人工智能发展的重要方向。

### 1.2  研究意义

文档通常以**复杂的排版结构、多模态的内容形式**出现，其中包含文字、表格、公式、图表等信息。对于人类来说，阅读与理解这些内容往往轻而易举，但对于机器而言却极具挑战：OCR 错误、格式错乱、跨页内容关联、语义不完整等问题，使得自动解析文档并保证语义准确成为一项艰难任务。

然而，能否让机器真正“读懂”文档，直接关系到：

1.**知识服务与信息检索**：快速、精准地抽取和组织文档信息，使用户能够高效获取有价值的知识，而不是被冗余文本和复杂版式所淹没。

2.**行业应用与安全合规**：在法律、金融、医疗、政务等领域，自动化的合同审阅、财务报表分析、病历解析与政策文件理解，可以显著降低人力成本，减少错误和合规风险。

3.**技术推动与学术创新**：文档智能推动了 多模态学习、结构化信息建模、幻觉抑制与可信 AI 等前沿研究的发展，并反过来为大模型的落地应用提供重要支撑。

因此，这一研究主题不仅具有重大的现实价值，也是深度学习、自然语言处理与计算机视觉交叉融合的典型案例，非常适合作为本科生和研究生进入科研领域的启蒙训练。


### 1.3  当前主要挑战

1. **挑战一：文档格式复杂，结构多样**  

   * 不同文档类型（PDF、Word、扫描件等）结构差异大，文档布局多样。  

   * 子元素（公式、表格、图表）语义解析困难。  

2. **挑战二：信息不完整与噪声干扰**  

   * OCR 错误、排版错乱、扫描伪影等。  

   * 多模态内容（图文混排）带来干扰。  

3. **挑战三：幻觉与可靠性问题**  
   
   * 模型在解析或问答中容易产生“文档幻觉”。  
   
   * 信息可信度与可追溯性不足。  

***

## 二、学习资料与参考文献

为引导新芽学子逐步深入研究并理解文档智能的关键痛点问题，本专题的学习结构设计为五个部分。首先，第一部分提供深度学习相关的入门教材与工具推荐，帮助新芽快速建立必要的算法与编程基础，具备进入该领域研究的基本能力。接下来的四个部分，则聚焦于文档智能的核心研究方向，分别是：

1.**子元素解析** —— 涵盖公式、表格、图表等结构化信息的解析；

2.**文档解析** —— 关注多步骤或端到端的文档解析；

3.**文档矫正** —— 针对 OCR 错误、排版噪声与格式不一致的修复与优化；

4.**文档幻觉** —— 探讨大模型在文档问答与生成中产生虚假内容的问题与应对方法。

新芽学子可以根据自身兴趣，从推荐文献中选择方向进行学习与汇报，在逐步建立对各个任务的初步认知的同时，培养独立分析问题和追踪前沿研究的能力。

***

### 2.1  基础教材与学习材料

在开始探险之前，你需要掌握一些基础的“内功心法”，这些是后续一切学习的基石。以下是你可以使用的一些 书籍/教程：

* 李沐[ 《动手学深度学习》](https://zh.d2l.ai/)  ——适合中文初学者的深度学习教材，以及(https://space.bilibili.com/1567748478/lists/358497?type=series) 

* [《Deep Learning》](https://www.deeplearningbook.org/) （Ian Goodfellow 等）——深度学习入门经典教材

* [PyTorch 官方教程](https://pytorch.org/tutorials)，也可以使用 [PyTorch 中文文档](https://pytorch-cn.readthedocs.io/zh/latest/)

* [《Pattern Recognition and Machine Learning》](https://www.microsoft.com/en-us/research/wp-content/uploads/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf)（Christopher M. Bishop）——机器学习原理入门

此外，你还可以借助一些**入门工具**：

* [Google Colab](https://colab.research.google.com/)：免费云平台，不用安装软件，就能跑PyTorch代码。

* [Kaggle平台](https://www.kaggle.com/)：免费数据集和竞赛，适合边学边练。

**Tips**：务必避免“所有基础都打好后再开始”的心态。建议在实践中学习，遇到不明白的概念再回溯补基础，这样效率更高，也更贴近科研训练的真实过程。

***

### 2.2  子元素解析任务相关研究

> 本专题重点关注以下几个方向：

- 公式解析  

随着智能教育、学术资料数字化和人机交互技术的快速发展，如何实现手写数学公式的自动识别与理解成为计算机视觉与自然语言处理交叉领域的重要课题。与普通文本识别相比，数学公式不仅是科学研究和工程应用中的核心表达工具，更承载着高度抽象的知识与推理逻辑。大量纸质档案、课堂板书和科研笔记中仍存在海量未结构化的手写公式信息，其高效数字化和机器可读化对于知识传播、智能检索以及学术资源共享具有重要意义。

**手写公式识别（Handwritten Mathematical Expression Recognition）**的难点主要体现在三个方面：书写风格多样性：不同作者的笔迹差异明显，笔画粗细、连写习惯和个体化符号变化使字符识别极具挑战。二维空间结构复杂性：公式包含分数、上下标、根号、括号、多层嵌套等结构，需要同时解析字符身份与空间布局关系，突破传统线性序列建模的局限。符号与语义耦合：公式不仅是符号堆叠，还蕴含逻辑与语义约束，识别系统必须兼顾字符精度与结构完整性，才能实现从“图像—符号序列—语义表达”的可靠映射。

**公式解析相关文献**:

* [DenseNet](https://ieeexplore.ieee.org/document/8099726 ) DenseNet ： Densely Connected Convolutional Networks  （2017-CVPR）
* [CAN](https://arxiv.org/abs/2207.11463) CAN ：When Counting Meets HMER: Counting-Aware Network for Handwritten Mathematical Expression Recognition （2022-ECCV）
* [SAN](https://arxiv.org/abs/2203.01601) SAN : Syntax-Aware Network for Handwritten Mathematical Expression Recognition  (2022-CVPR)
* [CoMER](https://arxiv.org/abs/2207.04410) CoMER : Modeling Coverage for Transformer-based Handwritten Mathematical Expression Recognition  (2022-ECCV)
* [NAMER] (https://arxiv.org/abs/2407.11380)  NAMER :  Non-Autoregressive Modeling for Handwritten Mathematical Expression Recognition  （2024-ECCV）
* [PosFormer] ( https://arxiv.org/abs/2407.07764) PosFormer: Recognizing Complex Handwritten Mathematical Expression with Position Forest Transformer (2024-ECCV)
* [ICAL] (https://arxiv.org/abs/2405.09032) ICAL : Implicit Character-Aided Learning forEnhanced Handwritten MathematicalExpression Recognition (2024-ICDAR)  

-表格解析

**表格（Tables）是承载结构化信息最高频、最密集**的载体之一。发票、论文、年报、财报、医疗记录、试验日志等大量关键数据都被组织在表格中。对机器而言，想要真正“读懂文档”，就必须先读懂表格。表格解析目标是把表格从“像素”还原为“结构化数据与语义”。典型子任务包括：

**表格检测（Table Detection）**：从整页文档/图像中定位表格区域，输出表格的外接框或分割掩码，为后续步骤裁剪出“表格片”。

**表格结构识别（Table Structure Recognition, TSR）**：在表格片内解析行、列、单元格的网格骨架，恢复**跨行/跨列（row/col span）**与单元格拓扑关系，得到结构化表示（如 HTML/Matrix/JSON）。

**表格内容识别（Table Content Recognition）**：结合 OCR/版面信息，将文本、数值、符号等正确对齐到对应单元格；处理空单元、噪声与对齐误差，输出可直接用于分析或导出的 CSV/HTML/JSON。

简言之：**先找表格（检测）→ 搭骨架（结构）→ 填内容（对齐/识别）**

**表格解析相关文献**：

* [EDD](https://arxiv.org/pdf/1911.10683.pdf) ：Image-based Table Recognition: Data, Model, and Evaluation

* [LGPMA](https://arxiv.org/abs/2105.06224) ：LGPMA: Complicated Table Structure Recognition with Local and Global Pyramid Mask Alignment

* [Cascade TabNet](https://arxiv.org/abs/2004.12629) ：CascadeTabNet: An Approach for End-to-End Table Detection and Structure Recognition from Image-based Documents

* [TGRNet](https://openaccess.thecvf.com/content/ICCV2021/papers/Xue_TGRNet_A_Table_Graph_Reconstruction_Network_for_Table_Structure_Recognition_ICCV_2021_paper.pdf) ：TGRNet: A Table Graph Reconstruction Network for Table Structure Recognition

* [GraphTSR](https://arxiv.org/abs/1908.04729) ：Complicated Table Structure Recognition

* [TableFormer](https://arxiv.org/abs/2203.01017) ：Table Structure Understanding with Transformers

* [UniTable](https://arxiv.org/abs/2403.04822) ：UniTable: Towards a Unified Framework for Table Recognition via Self-Supervised Pretraining

* [UniTabNet](https://arxiv.org/abs/2409.13148) ：Bridging Vision and Language Models for Enhanced Table Structure Recognition (UniTabNet)

* [TableNet](https://www.researchgate.net/publication/338420921_TableNet_Deep_Learning_model_for_end-to-end_Table_detection_and_Tabular_data_extraction_from_Scanned_Document_Images) ：TableNet: Deep Learning Model for End-to-end Table Detection and Tabular Data Extraction from Scanned Document Images

* [DeepDeSRT](https://www.semanticscholar.org/paper/DeepDeSRT%3A-Deep-Learning-for-Detection-and-of-in-Schreiber-Agne/f8bead3ae810cd3f7427d3004e45b4158da9b744) ：DeepDeSRT: Deep Learning for Detection and Structure Recognition of Tables in Document Images

* [TSRNet](https://www.sciencedirect.com/science/article/abs/pii/S0031320322004265) ：Table Structure Recognition and Form Parsing by End-to-End Graph Neural Network (TSRNet)

* [TableCenterNet](https://arxiv.org/abs/2504.17522) ：Towards One-Stage End-to-End Table Structure Parsing with TableCenterNet

* [TableStructureFormer](https://link.springer.com/article/10.1007/s40747-025-01975-w) ：TableStructureFormer: An Improved Masked-Attention Framework for Table Structure Recognition

- 图表解析  

在当今信息社会中，**图表是传达数据与知识的最常用方式之一**。折线图、柱状图、饼图等数据可视化图表，帮助人们直观理解复杂的统计信息；流程图、思维导图等结构类图表，则能清晰展示层级关系与逻辑结构。

然而，如何让人工智能模型像人类一样“读懂图表”，一直是学术界的重要研究方向。这类任务统称为图表解析与理解（Chart Parsing/Understanding），通常包含：

1.**结构图表解析**：解析流程图、思维导图等，重建其中的结构与关系。

2.**图表摘要生成**：自动生成图表描述或总结。

3.**图表问答**：让模型回答图表相关问题。

这一领域正迅速发展，成为视觉与语言多模态研究的重要分支。

**图表解析相关文献**：

* [FigureQA](https://arxiv.org/abs/1710.07300): FigureQA: An Annotated Figure Dataset for Visual Reasoning (ArXiv 2017)

* [DVQA](https://arxiv.org/abs/1801.08163): DVQA: Understanding Data Visualizations via Question Answering (CVPR 2018)

* [LEAF-QA](https://arxiv.org/abs/2001.02356): LEAF-QA: Locating and Editing in Automatic Figure Question Answering (WACV 2020)

* [PlotQA](https://arxiv.org/abs/1909.00977): PlotQA: Reasoning over Scientific Plots (AAAI 2020)

* [ChartOCR](https://arxiv.org/abs/2103.14642): ChartOCR: Data Extraction from Charts via Hybrid Deep Models (WACV 2021)

* [ChartQA](https://arxiv.org/abs/2203.10244): ChartQA: A Benchmark for Question Answering about Charts with Natural Language (ACL Findings 2022)

* [OpenCQA](https://arxiv.org/abs/2210.16477): OpenCQA: Open-ended Question Answering on Charts (EMNLP 2022)

* [MatCha](https://arxiv.org/abs/2205.12558): MatCha: Enhancing Math Reasoning in Chart Understanding via Pre-training (ArXiv 2022)

* [Pix2Struct](https://arxiv.org/abs/2210.03347): Pix2Struct: Screenshot Parsing as Pretraining for Visual Language Understanding (ICLR 2023)

* [ChartReader](https://arxiv.org/abs/2302.09618): ChartReader: A Unified Framework for Chart Derendering and Understanding (ArXiv 2023)

* [LineFormer](https://arxiv.org/abs/2303.15144): LineFormer: Line Chart Data Extraction with Transformers (ArXiv 2023)

* [Scientific Chart Summarization](https://arxiv.org/abs/2112.13068): Summarizing Charts in Scientific Documents (AAAI 2022)

* [Chart-to-Text](https://arxiv.org/abs/2202.10772): Chart-to-Text: A Large-scale Benchmark for Chart Summarization (ACL 2022)

* [VisText](https://arxiv.org/abs/2301.02282): VisText: A Benchmark for Semantically Rich Chart Captioning (ArXiv 2023)

* [GenChaR](https://arxiv.org/abs/2306.00965): GenChaR: Generating Chart Reports for Stock Market Data (ArXiv 2023)

* [Arrow R-CNN](https://arxiv.org/abs/1905.13580): Arrow R-CNN for Flowchart Object Detection (ICDAR 2019 / IJDAR 2021)

* [FLODIAL](https://arxiv.org/abs/2106.14800): FLODIAL: Dialogue-based Flowchart Understanding (ArXiv 2021)

* [GenFlowchart](https://arxiv.org/abs/2402.12917): GenFlowchart: Generative Flowchart Parsing with SAM and GPT (ArXiv 2024)

* [FlowLearn](https://arxiv.org/abs/2407.01350): FlowLearn: Evaluating LVLMs on Flowchart Understanding (ArXiv 2024)

* [MindBench](https://arxiv.org/abs/2407.02057): MindBench: A Benchmark for Mind Map Understanding (ArXiv 2024)

* [ChartQAPro](https://arxiv.org/abs/2503.02417): ChartQAPro: A More Challenging Benchmark for Chart Question Answering (ArXiv 2025)

* [ChartQA-X](https://arxiv.org/abs/2502.09329): ChartQA-X: Explainable Question Answering on Charts (ArXiv 2025)

### 2.3  文档解析任务相关研究

在日常办公、科研和信息传播中，PDF、Word、扫描件等文档是最主要的载体。然而，这些文档往往包含**多样化的排版结构与多模态内容**：文字、标题、页眉页脚、图表、公式、表格混杂在一起，甚至还可能伴随扫描噪声、OCR 错误和版面错乱。如何让人工智能系统能够自动识别并重建文档中的 层次结构与语义逻辑，即所谓的文档解析（Document Parsing），成为学术界和工业界的重要研究方向。
目前，文档解析的研究范式主要可以分为以下两类：

1.**Pipeline 级联方法**：通过多个专家模型的级联与组合来完成文档解析任务。例如，先使用 OCR 模型完成文字识别，再调用版面分析模型确定区域边界，最后结合表格/图表解析模型实现结构化抽取。这种方法具有可控性强、可解释性好的优势，但存在整体性能依赖单点模型、流程复杂、误差易级联放大的问题。

2.**基于多模态大模型（MLLM）的文档解析方法**： 近年来，多模态大模型的发展为文档解析带来新的思路，大体可以分为两种路线：a.**模块化方式**：先通过 MLLM 进行布局分析与子元素划分，再由专门模块分别处理文本、表格、图像等内容，最后融合结果。b.**端到端方式**：直接将整份文档输入 MLLM，输出结构化结果或语义理解结果，避免中间环节的繁琐步骤。这类方法具有统一性和鲁棒性，但在可解释性和对细节的精确把控方面仍需进一步探索。

文档解析不仅是信息抽取与检索的基础环节，也是智能问答、知识图谱构建、自动摘要生成等高层任务的前提。随着深度学习与大模型的发展，文档解析正逐渐从 传统 pipeline 模式 向 端到端、多模态统一建模 转变，成为文档智能领域的核心研究课题之一。

**文档解析相关文献**:

-级联方法

* [MinerU](https://github.com/opendatalab/MinerU/blob/master/README_zh-CN.md) 

-MLLM相关（模块化）

* [MonkeyOCR](https://arxiv.org/abs/2506.05218)Document Parsing with a Structure-Recognition-Relation Triplet Paradigm（2025 arxiv）

* [Dolphin](https://arxiv.org/abs/2505.14059):(2025 arxiv):Document Image Parsing via Heterogeneous Anchor Prompting（2025 arxiv）

-MLLM相关（端到端）

* [GOT-OCR](https://arxiv.org/abs/2409.01704):Towards OCR-2.0 via a Unified End-to-end Model 

* [Nougat](https://arxiv.org/abs/2308.13418):Neural Optical Understanding for Academic Documents

* [MistralOCR](https://mistral.ai/news/mistral-ocr) :tech report

* [OLMOC](https://github.com/allenai/olmocr):tech report

* [dots.ocr](https://github.com/rednote-hilab/dots.ocr):Multilingual Document Layout Parsing in a Single Vision-Language Model 

-通用MLLM

* [InternVL3](https://huggingface.co/papers/2504.10479) :tech report**

* [Qwen3VL](https://qwen.ai/blog?id=99f0335c4ad9ff6153e517418d48535ab6d8afef&from=research.latest-advancements-list) :tech report

-测评相关

* [OmniDocBench](https://arxiv.org/abs/2412.07626):Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations (2024 CVPR)

* [CC-OCR](https://arxiv.org/abs/2412.02210):A Comprehensive and Challenging OCR Benchmark for Evaluating Large Multimodal Models in Literacy(2024 arxiv)

* [OCRBench](https://arxiv.org/abs/2305.07895): On the Hidden Mystery of OCR in Large Multimodal Models (2023 arxiv)

### 2.4  文档矫正任务相关研究

> 学生可在此部分选择进阶文献进行专题汇报，或自行查找最新的同类重要文献。

> 文档图像矫正可以分为有先验辅助与无先验辅助两类。

**有先验辅助**

* [DocUNet](https://openaccess.thecvf.com/content_cvpr_2018/papers/Ma_DocUNet_Document_Image_CVPR_2018_paper.pdf)：DocUNet: Document Image Unwarping via A Stacked U-Net（CVPR 2018）

* [DewarpNet](https://openaccess.thecvf.com/content_ICCV_2019/papers/Das_DewarpNet_Single-Image_Document_Unwarping_With_Stacked_3D_and_2D_Regression_ICCV_2019_paper.pdf)：DewarpNet: Single-Image Document Unwarping With Stacked 3D and 2D Regression Networks（ICCV 2019）

* [DocTr](https://arxiv.org/pdf/2110.12942.pdf)：DocTr: Document Image Transformer for Geometric Unwarping and Illumination Correction（ACMMM 2021）

* [Marior](https://arxiv.org/pdf/2207.11515.pdf)：Marior: Margin Removal and Iterative Content Rectification for Document Dewarping in the Wild（ACMMM 2022）

* [PaperEdge](https://dl.acm.org/doi/pdf/10.1145/3528233.3530756)：Learning From Documents in the Wild to Improve Document Unwarping（SIGGRAPH 2022）

* [DocGeoNet](https://arxiv.org/pdf/2210.08161.pdf)：Geometric Representation Learning for Document Image Rectification（ECCV 202）

* [FTADR](https://openaccess.thecvf.com/content/ICCV2023/papers/Li_Foreground_and_Text-lines_Aware_Document_Image_Rectification_ICCV_2023_paper.pdf)：Foreground and Text-lines Aware Document Image Rectification（ICCV 2023）

* [Layout-DocFlattn](https://dl.acm.org/doi/pdf/10.1145/3627818)：Layout-Aware Single-Image Document Flatening（TOG 2023）

* [UVDoc](https://dl.acm.org/doi/fullHtml/10.1145/3610548.3618174)：	UVDoc: Neural Grid-based Document Unwarping（SIGGRAPH 2023）

* [DocRes](https://arxiv.org/abs/2405.04408)：	DocRes: A Generalist Model Toward Unifying Document Image Restoration Tasks（CVPR 2024）

* [Iso-UVField](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136970568.pdf)：Learning an Isometric Surface Parameterization for Texture Unwrapping（ECCV 2022）

* [Grid Regularization] (https://openaccess.thecvf.com/content/CVPR2022/papers/Jiang_Revisiting_Document_Image_Dewarping_by_Grid_Regularization_CVPR_2022_paper.pdf):Revisiting Document Image Dewarping by Grid Regularization（CVPR 2022）

* [DocTr plus](https://arxiv.org/abs/2304.08796)：Deep Unrestricted Document Image Rectification（TMM 2023）

* [ForCenNet](https://arxiv.org/abs/2507.19804)：ForCenNet: Foreground-Centric Network for Document Image Rectification（ICCV 2025）

**无先验辅助**

* [DDCP](https://arxiv.org/pdf/2203.10543.pdf)：Document Dewarping with Control Points（ICDAR 2021）

* [FDRNet](https://openaccess.thecvf.com/content/CVPR2022/papers/Xue_Fourier_Document_Restoration_for_Robust_Document_Dewarping_and_Recognition_CVPR_2022_paper.pdf)：Fourier Document Restoration for Robust Document Dewarping and Recognition（CVPR 2022）

* [DocReal](https://openaccess.thecvf.com/content/WACV2024/papers/Yu_DocReal_Robust_Document_Dewarping_of_Real-Life_Images_via_Attention-Enhanced_Control_WACV_2024_paper.pdf)：DocReal: Robust Document Dewarping of Real-Life Images via Attention-Enhanced Control Point Prediction（WACV 2023）

* [TADoc](https://arxiv.org/abs/2508.06988)：TADoc: Robust Time-Aware Document Image Dewarping（ECAI 2024）

### 2.5  文档幻觉任务相关研究

随着视觉语言模型和文档理解系统的发展，OCR在各种应用中扮演了核心角色，例如：文档数字化、票据处理、自动表单识别以及多模态问答（VQA）。然而，现代OCR系统，尤其是集成于大型视觉语言模型中的OCR模块，仍然存在视觉文字幻觉问题：模型在缺乏明确视觉证据的情况下生成不存在或错误的文本信息。

**来源**：幻觉通常来自多方面，包括图像质量差、字体复杂、噪声干扰、模型的语言偏置以及多模态生成模型的过度自信输出。

**影响**：在实际应用中，这类幻觉可能导致关键业务决策错误，如错误票据识别、金融报表处理错误，甚至医疗文档理解失误。

**OCR幻觉相关文献**:

学生第一阶段的阅读训练，可帮助理解目标检测/语义分割/关键点检测这一通用方向。仅用于入门，不可选择此部分文献汇报。

* [LLAVA](https://arxiv.org/abs/2304.08485) : Visual Instruction Tuning （NeurIPS 2023 Oral）

* [Qwen-VL](https://arxiv.org/abs/2308.12966) : Qwen-VL: A Versatile Vision-Language Model for Understanding, Localization, Text Reading, and Beyond）

* [InternVL](https://arxiv.org/abs/2312.14238) : InternVL: Scaling up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks

* [MiniCPM-V](https://arxiv.org/abs/2408.01800) : MiniCPM-V: A GPT-4V Level MLLM on Your Phone

* [Monkey](https://arxiv.org/abs/2311.06607)  Monkey: Image Resolution and Text Label Are Important Things for Large Multi-modal Models (CVPR 2024)

* [Kim-VL](https://arxiv.org/abs/2504.07491) : Kimi-VL Technical Report

* [DBNet](https://arxiv.org/abs/1911.08947) :Real-time Scene Text Detection with Differentiable Binarization (AAAI2020) 目前主流OCR检测模型

* [CRAFT](https://arxiv.org/abs/1904.01941)  Character Region Awareness for Text Detection （CVPR2019）经典OCR检测模型

* [CRNN](https://arxiv.org/abs/1507.05717) : n End-to-End Trainable Neural Network for Image-based Sequence Recognition and Its Application to Scene Text Recognition 目前主流OCR识别模型 (TPAMI 2016)

* [SVTR](https://arxiv.org/abs/2205.00159) : SVTR: Scene Text Recognition with a Single Visual Model (IJCAI2022) 目前主流OCR识别模型

* [ABCNet](https://arxiv.org/abs/2002.10200) : ABCNet: Real-time Scene Text Spotting with Adaptive Bezier-Curve Network  (CVPR 2020) 经典端到端识别模型

* [TESTR](https://arxiv.org/abs/2204.01918) : Text Spotting Transformers (CVPR 2022)

**进阶文献（幻觉抑制经典方法）**

学生可在此部分选择进阶文献进行专题汇报，或自行查找最新的同类重要文献。

分为三种方法：基于视觉注意增强；基于对比解码；基于强化学习

- 对比解码

* [VCD](https://arxiv.org/abs/2311.16922) : Mitigating Object Hallucinations in Large Vision-Language Models through Visual Contrastive Decoding (CVPR 2024)

* [ICD](https://arxiv.org/abs/2403.18715) : Mitigating Hallucinations in Large Vision-Language Models with Instruction Contrastive Decoding （Findings of ACL 2024）

* [VDGD](https://arxiv.org/abs/2405.15683v3) : VDGD: Mitigating LVLM Hallucinations in Cognitive Prompts by Bridging the Visual Perception Gap (ICLR2025)

* [ICT](https://arxiv.org/abs/2411.15268) : Image-Object Cross-Level Trusted Intervention for Mitigating Object Hallucination in Large Vision-Language Models   (CVPR2025)

- 视觉注意增强

* [OPERA](https://arxiv.org/abs/2311.17911) : OPERA: Alleviating Hallucination in Multi-Modal Large Language Models via Over-Trust Penalty and Retrospection-Allocation (CVPR 2024)

* [ClearSight](https://arxiv.org/abs/2503.13107) :  learSight: Visual Signal Enhancement for Object Hallucination Mitigation in Multimodal Large language Models (CVPR 2025)

* [MemVR](https://arxiv.org/pdf/2410.03577) : Look Twice Before You Answer: Memory-Space Visual Retracing for Hallucination Mitigation in MLLMs (ICML 2025)

* [CCA](https://arxiv.org/abs/2410.15926) : Mitigating Object Hallucination via Concentric Causal Attention  (NeurIPS 2024)

* [Deco](https://arxiv.org/abs/2405.20985) :  DeCo: Decoupling Token Compression from Semantic Abstraction in Multimodal Large Language Models (ICLR 2025)

* [AGLA](https://arxiv.org/abs/2406.12718) : Mitigating Object Hallucinations in Large Vision-Language Models with Assembly of Global and Local Attention (CVPR 2025)

- 强化学习

* [OPA-DPO](https://arxiv.org/abs/2501.09695)  Mitigating Hallucinations in Large Vision-Language Models via DPO: On-Policy Data Hold the Key  (CVPR 2025)

* [TL-DPO](https://arxiv.org/abs/2506.11417v1)  Stop learning it all to mitigate visual hallucination, Focus on the hallucination target  (CVPR 2025)

- Benchmark

* [HallusionBench](https://arxiv.org/abs/2310.14566) : HallusionBench: An Advanced Diagnostic Suite for Entangled Language Hallucination and Visual Illusion in Large Vision-Language Models (CVPR 2024)

* [CHAIR](https://arxiv.org/abs/1809.02156)   Object Hallucination in Image Captioning (EMNLP 2018)

* [POPE](https://arxiv.org/abs/2305.10355)   Evaluating Object Hallucination in Large Vision-Language Models(EMNLP 2023)

* [PhD](https://arxiv.org/abs/2403.11116)  A ChatGPT-Prompted Visual hallucination Evaluation Dataset  (CVPR 2025)

## 三、结语与期望

“新芽计划”的初心在于为青年学子打开通向科研的大门，让大家在探索未知的过程中积累勇气与自信。文档智能作为连接人工智能与人类知识的重要桥梁，既是国家产业发展的关键需求，也是学术前沿的挑战高地。

从子元素解析到文档解析，从文档矫正到幻觉抑制，每一个任务都对应着真实世界中的痛点与应用需求。如何让机器像人类一样可靠地“读懂”文档，不仅关系到信息服务的效率与安全，更决定着人工智能能否真正融入科研、金融、法律、医疗等核心行业。

我们希望通过本专题，新芽学子能够：

1.**在实践中学习** —— 不拘泥于“打好基础再开始”，而是在动手中发现问题、解决问题。

2.**在探索中成长** —— 通过阅读文献与小型实验，建立科研思维，培养对前沿问题的敏锐洞察。

3.**在交流中创新** —— 在汇报与讨论中碰撞思想，勇敢提出独立见解，敢于质疑已有方法。

未来，文档智能必将伴随大模型与多模态技术的突破而不断进化，成为推动知识社会和智能产业发展的重要支点。我们期待新芽学子能够抓住这一研究窗口，用好推荐的学习资源和研究路线，勇敢迈出第一步，在科研旅程中留下属于自己的足迹。





