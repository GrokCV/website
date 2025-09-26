---
title: 新芽专题介绍（45）：多模态医学信息处理——眼底相关多模态融合
date: 2025-09-17T01:06:00Z
draft: false
math: true
---

## 一、专题介绍

### 1.1  研究背景

在现代医学诊断和治疗系统中，多模态医学信息处理是核心技术之一。它涉及融合多种数据源，如超声（Ultrasound , US）、磁共振成像（Magnetic Resonance Imaging, MRI）、光学相干断层扫描（Optical coherence tomography, OCT）、医疗文本报告、患者表格元数据（如年龄、血糖水平等），以提供全面的临床洞察。特别是在眼科领域，眼底相关疾病如糖尿病视网膜病变（diabetic retinopathy, DR）、年龄相关性黄斑变性（age-related macular degeneration, AMD）等，需要多模态数据来实现早期检测和精准诊断。随着人工智能和深度学习的进步，多模态融合已成为提升诊断准确性和效率的关键方向，是各国医疗AI研究的前沿。

### 1.2  研究意义

多模态医学信息处理，特别是眼底相关的融合，能够整合图像的视觉特征、文本的语义信息和表格的结构化数据，从而克服单一模态的局限性。这直接关系到：

1. **临床诊断与筛查**：提升眼底疾病如DR的检测精度，减少误诊，提高公共卫生筛查效率。
2. **个性化医疗**：结合患者元数据实现定制化治疗计划，改善预后。
3. **技术创新**：推动多模态学习算法、跨模态对齐和融合机制的发展，促进AI在医疗领域的应用。

这一主题不仅是医疗AI的典型案例，还适合本科生作为科研入门，培养多学科融合思维。

### 1.3  当前主要挑战

尽管重要，但眼底相关多模态医学信息处理面临多重挑战：

1. **挑战一：模态异质性强，融合难度大**

   * 图像、文本和表格数据类型迥异，特征空间不一致，导致对齐和融合复杂。
   * 眼底图像分辨率高，但文本可能含噪声，表格数据稀疏。

2. **挑战二：数据隐私与标注瓶颈**

   * 医疗数据受隐私法规限制，获取多模态标注数据集困难。
   * 标注需专业医师，成本高，影响模型训练。

3. **挑战三：实时性和可解释性要求高**

   * 临床应用需低延迟处理，但多模态模型计算密集。
   * 模型决策需可解释，以获医师信任。

综上，这一领域仍在快速发展，是学习多模态AI的理想窗口。

***

## 二、学习资料与参考文献

为了引导新芽学子逐步进入研究，本专题结构分为以下四部分：

***

### 2.1  基础教材与学习材料

在开始探险之前，你需要掌握“筑基期”的基础能力和知识，这些是后续一切学习的基石。以下是你可以使用的一些**书籍/教程**：


* [吴恩达《深度学习》视频课程全集_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV16r4y1Y7jv/?spm_id_from=333.788.recommend_more_video.5&vd_source=5bb636547d46db0102d918c90e54da6f)——适合初学者的深度学习教程，了解深度学习各种定义和概念。

* [《PyTorch深度学习实践》完结合集_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1Y7411d7Ys/?spm_id_from=333.337.search-card.all.click&vd_source=5bb636547d46db0102d918c90e54da6f)——适合初学者的pyotrch实践学习教程，帮助大家了解科研中最常用的深度学习框架pytorch。
*  [卷积操作辅助理解系列视频](https://www.bilibili.com/video/BV16N411y7cV?spm_id_from=333.788.videopod.sections&vd_source=5bb636547d46db0102d918c90e54da6f)-从3D角度理解卷积操作
* [《Deep Learning》](https://www.deeplearningbook.org/)（Ian Goodfellow 等）——深度学习入门经典教材

此外，你也可以使用一些**入门工具**：

* [Google Colab](https://colab.research.google.com/)：免费云平台，不用安装软件，就能跑PyTorch代码。
* [Kaggle平台](https://www.kaggle.com/)：免费数据集和竞赛。
* [医学影像数据集集锦 - 飞桨AI Studio星河社区](https://aistudio.baidu.com/projectdetail/462184)：免费数据集
* [天池数据集_阿里系唯一对外开放数据分享平台-阿里云天池](https://tianchi.aliyun.com/dataset/public?spm=a2c22.12282016.0.0.2b566e12ETIBEO)：免费数据集
* [PyCharm: The only Python IDE you need](https://www.jetbrains.com/pycharm/)：代码集成开发环境


Tips：务必**摆脱所有基础都打好后，再进行下一阶段“结丹期**”的修行，基础不牢，地动山摇~。

***

### 2.2  入门文献（医学信息处理方向经典方法）

> 学生第一阶段的阅读训练，可帮助理解通用技术。**仅用于入门，不可选择此部分文献汇报**。

* ResNet : [Deep Residual Learning for Image Recognition](https://openaccess.thecvf.com/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf)-最经典的图像处理模型
* Bert: [Bert: Pre-training of deep bidirectional transformers for language understanding](https://aclanthology.org/N19-1423/?utm_campaign=The+Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz-_m9bbH_7ECE1h3lZ3D61TYg52rKpifVNjL4fvJ85uqggrXsWDBTB7YooFLJeNXHWqhvOyC): 自然语言处理领域的里程碑式模型
* UNet: [U-Net: Convolutional Networks for Biomedical Image Segmentation](https://arxiv.org/pdf/1505.04597)-医学图像分割领域的里程碑式工作
* SENet:  [**Squeeze**-**and**-**excitation networks**](http://openaccess.thecvf.com/content_cvpr_2018/html/Hu_Squeeze-and-Excitation_Networks_CVPR_2018_paper.html)-注意力机制的代表工作
* ViT:  [An image is worth 16x16 words: Transformers for image recognition at scale](https://arxiv.org/pdf/2010.11929/1000)-Transformer在视觉领域中应用的经典工作
* Swin Transformer: [Swin transformer: Hierarchical vision transformer using shifted windows](https://openaccess.thecvf.com/content/ICCV2021/html/Liu_Swin_Transformer_Hierarchical_Vision_Transformer_Using_Shifted_Windows_ICCV_2021_paper)-ViT系列工作的优秀优化思路 
* MAE: [Masked autoencoders are scalable vision learners](https://openaccess.thecvf.com/content/CVPR2022/html/He_Masked_Autoencoders_Are_Scalable_Vision_Learners_CVPR_2022_paper)-自监督学习、预训练模型经典工作
*CLIP: [Learning transferable visual models from natural language supervision](http://proceedings.mlr.press/v139/radford21a)-图像-文本对比学习经典模型

***

### 2.3  进阶文献（多模态模型前沿方法）

> 学生可在此部分选择进阶文献进行专题汇报，或自行查找最新的同类重要文献。

* MedCLIP: [Medclip: Contrastive learning from unpaired medical images and text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11323634/)
* SAM: [**Segment anything**](http://openaccess.thecvf.com/content/ICCV2023/html/Kirillov_Segment_Anything_ICCV_2023_paper.html)
* MedSAM [Segment anything in medical images](https://www.nature.com/articles/s41467-024-44824-z)
* BLIP系列论文
[Blip: Bootstrapping language-image pre-training for unified vision-language understanding and generation](https://proceedings.mlr.press/v162/li22n.html): BLIP
[Blip-2: Bootstrapping language-image pre-training with frozen image encoders and large language models](https://proceedings.mlr.press/v202/li23q): BLIP2
[Instructblip: Towards general-purpose vision-language models with instruction tuning](https://proceedings.neurips.cc/paper_files/paper/2023/hash/9a6a435e75419a836fe47ab6793623e6-Abstract-Conference.html): InstructBLIP
* LLaVA: [**Visual instruction tuning**](https://proceedings.neurips.cc/paper_files/paper/2023/hash/6dcf277ea32ce3288914faf369fe6de0-Abstract-Conference.html)
* Qwen2.5-VL: [**Qwen2**. **5**-**vl technical report**](https://arxiv.org/abs/2502.13923)




***

### 2.4  多模态医学信息处理领域相关文献（眼底相关）

> 结合本专题的研究背景，逐渐引导学生进入眼底相关多模态处理。学生可在此部分选择进阶文献进行专题汇报，或自行查找最新的同类重要文献。
>
> 
* DeepDR-LLM: [Integrated image-based deep learning and language models for primary diabetes care](https://www.nature.com/articles/s41591-024-03139-8)
* VisionFM: [**Visionfm**: a **multi**-**modal multi**-**task vision foundation model** for **generalist ophthalmic artificial intelligence**](https://arxiv.org/abs/2310.04992)
* MM-Retinal: [MM-retinal: Knowledge-enhanced foundational pretraining with fundus image-text expertise](https://link.springer.com/chapter/10.1007/978-3-031-72378-0_67)
* MedSegX: [A generalist foundation model and database for open-world medical image segmentation](https://www.nature.com/articles/s41551-025-01497-3)
* RetiZero: [Enhancing diagnostic accuracy in rare and common fundus diseases with a knowledge-rich vision-language model](https://www.nature.com/articles/s41467-025-60577-9)
* RCT: [An eyecare foundation model for clinical assistance: a randomized controlled trial](https://www.nature.com/articles/s41591-025-03900-7)
* RETFound: [A foundation model for generalizable disease detection from retinal images](https://www.nature.com/articles/s41586-023-06555-x)
* IDP: [Phenotypic and genetic characteristics of retinal vascular parameters and their association with diseases](https://www.nature.com/articles/s41467-024-52334-1)
* FLAIR: [A foundation language-image model of the retina (flair): Encoding expert knowledge in text supervision](https://www.sciencedirect.com/science/article/pii/S1361841524002822)
* CABNet: [**CABNet**: Category attention block for imbalanced diabetic retinopathy grading](https://ieeexplore.ieee.org/abstract/document/9195035/)
***

## 三、结语与期望

“新芽计划”旨在激发新芽学子探索未知的热情，为广大学子提供成长的沃土。多模态医学信息处理是一个充满挑战与机遇的前沿领域，既是满足医疗需求的“硬核”课题，也是推动学术创新的“试金石”。通过本专题，我们期待新芽学子不仅能掌握前沿医工交叉领域的技术，还能培养独立思考、实践创新以及解决复杂问题的综合能力。

我们热切期待，在最终的汇报中，能看到大家闪耀着智慧火花的解读与创见！
