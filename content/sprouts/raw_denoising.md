---
title: 新芽专题介绍（34）：图像Raw域去噪
date: 2025-09-17T01:17:00Z
draft: false
math: true
---

## 一、专题介绍

### 1.1  研究背景

随着智能手机、无人机、安防摄像头等便携式成像设备的广泛应用，图像质量提升成为核心需求。然而，由于传感器尺寸小、像素密度高，拍摄条件受光线、曝光时间和传感器噪声等因素影响，得到的图像往往**信噪比低、噪声明显**。传统的图像去噪方法通常在经过ISP（Image Signal Processing，图像信号处理）后的RGB域中处理图像，但ISP处理会引入非线性映射、色彩失真以及噪声空间复杂化，使去噪变得更加困难。因此，越来越多研究开始关注在**Raw域直接去噪**，即在图像信号未经过完整ISP处理前，对原始传感器采集的图像进行噪声抑制，以最大程度**保留细节和真实信号**。

### 1.2  研究意义

Raw域图像去噪不仅是图像处理领域的基础研究问题，也具有实际工程应用价值：

1. **提升图像质量**：在拍摄暗光环境、夜景或高速运动场景下，Raw域去噪能够有效提高图像清晰度，降低颗粒感和噪点。
2. **推动计算摄影技术**：Raw域去噪是高端摄影算法链条中的关键环节，可为HDR成像、超分辨率重建、多帧融合等后续处理提供干净信号。
3. **优化移动端成像系统**：轻量化、实时的Raw域去噪算法能够兼顾移动设备有限的计算资源和功耗要求，为智能手机、无人机等提供更好的成像体验。

因此，这一研究主题不仅意义重大，而且Raw域去噪涉及噪声建模、深度学习网络设计、非均匀噪声处理等前沿技术，是低级视觉任务的典型研究案例，适合作为本科生或研究生的科研启蒙项目。

![](https://imgtu.com/uploads/1o5hktap/denoise.png)

▲一个典型的夜间带噪场景：噪声强度大，场景存在色彩偏移。

### 1.3  当前主要挑战

Raw域图像去噪虽然理论上优势明显，但在实际应用中仍面临多重挑战：

1. **挑战一：噪声复杂且非均匀**
   - Raw域噪声通常由**光子噪声、读出噪声、热噪声**等多种类型叠加而成。
   - 噪声具有空间非均匀性（随着像素强度和ISO变化而变化），使得简单的均值滤波或卷积难以有效处理。
2. **挑战二：数据标注困难**
   - 高质量的Raw域去噪训练需要**干净的Ground Truth图像**，而真实环境中获取零噪声Raw图像非常困难。
   - 合成噪声的方法虽然可行，但噪声分布可能与真实场景不完全匹配，影响模型泛化能力。
3. **挑战三：算法与硬件资源限制**
   - Raw图像通常为高位深度（如12bit或14bit），分辨率高，处理数据量大。
   - 实时去噪要求算法既高效又准确，尤其在移动设备和嵌入式系统上，计算资源和功耗有限。
4. **挑战四：与ISP链的协同问题**
   - Raw域去噪需与后续ISP处理协同，否则可能出现颜色偏移、伽马失真等问题。
   - 如何设计与ISP解耦或协同优化的去噪算法，是当前研究的重要方向。

综上所述，Raw域图像去噪是低级视觉与计算摄影领域的核心问题，既有理论价值，又有实际应用需求。通过研究Raw域去噪，不仅能够提升图像质量，还能深入理解噪声建模、信号增强与深度学习算法设计的关键技术。

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

### 2.2  噪声建模文献

> 学生第一阶段的阅读训练，可帮助理解**噪声建模/噪声参数估计**的方法，为后续去噪方法的学习打基础

*  [LR-MoG](https://openaccess.thecvf.com/content_cvpr_2016/papers/Zhu_From_Noise_Modeling_CVPR_2016_paper.pdf): From noise modeling to blind image denoising (CVPR 2016)
*  [Noise flow](https://openaccess.thecvf.com/content_ICCV_2019/papers/Abdelhamed_Noise_Flow_Noise_Modeling_With_Conditional_Normalizing_Flows_ICCV_2019_paper.pdf): Noise modeling with conditional normalizing flows (ICCV 2019)
*  [Normalizing Flows](https://openaccess.thecvf.com/content/CVPR2022/papers/Kousha_Modeling_sRGB_Camera_Noise_With_Normalizing_Flows_CVPR_2022_paper.pdf): Modeling sRGB Camera Noise with Normalizing Flows (CVPR 2022)
*  [Gan-based noise model for denoising real images](https://openaccess.thecvf.com/content/ACCV2020/papers/Tran_GAN-based_Noise_Model_for_Denoising_Real_Images_ACCV_2020_paper.pdf) (ACCV 2020)
*  [CA-NoiseGAN](https://arxiv.org/pdf/2008.09370): Learning camera-aware noise models (ECCV 2020)
*  [Physics-based noise modeling for extreme low-light photography](https://arxiv.org/pdf/2108.02158) (TPAMI 2021)
*  [ELD]([2108.02158](https://arxiv.org/pdf/2108.02158)): Physics-based noise modeling for extreme low-light photography (TPAMI 2021)
*  [LLD](https://openaccess.thecvf.com/content/CVPR2023/papers/Cao_Physics-Guided_ISO-Dependent_Sensor_Noise_Modeling_for_Extreme_Low-Light_Photography_CVPR_2023_paper.pdf): Physics guided iso-dependent sensor noise modeling for extreme low light photography (CVPR 2023)
*  [SCUNet](https://link.springer.com/content/pdf/10.1007/s11633-023-1466-0.pdf): Practical Blind Image Denoising via Swin-Conv-UNet and Data Synthesis (MIR 2023)
*  [Non-parametric sensor noise modeling and synthesis](https://link.springer.com/chapter/10.1007/978-3-031-72691-0_5) (ECCV 2024)

### 2.3 去噪入门文献（图像去噪经典方法）

> 学生了解去噪方法的入门阅读训练，可帮助理解**图像去噪中的经典方法**。

*  [Image denoising using scale mixtures of Gaussians in the wavelet domain](https://www.cns.nyu.edu/pub/eero/portilla03-preprint.pdf) (TIP 2003)
*  [Image denoising via sparse and redundant representations over learned dictionaries](https://www.egr.msu.edu/~aviyente/elad06.pdf) (TIP 2006)
*  [Non-local sparse models for image restoration](https://ora.ox.ac.uk/objects/uuid:cbb65689-27c6-4fd2-ba84-e953e61c0510/files/scz30pv50d) (ICCV 2009)
*  [BM3D](https://web.eecs.utk.edu/~hqi/ece692/references/noise-BM3D-tip07.pdf): Image denoising by sparse 3-D transform-domain collaborative filtering (TIP 2007)
*  [NL-means](https://audio.rightmark.org/lukin/msu/NonLocal.pdf): A non-local algorithm for image denoising (CVPR 2005)
*  [CSR]([0697.pdf](https://see.xidian.edu.cn/faculty/wsdong/Papers/Conference/0697.pdf)): Sparsity-based image denoising via dictionary learning and structural clustering (CVPR 2011)
*  [WNNM](https://openaccess.thecvf.com/content_cvpr_2014/papers/Gu_Weighted_Nuclear_Norm_2014_CVPR_paper.pdf): Weighted nuclear norm minimization with application to image denoising (CVPR 2014)
*  [MC-WNNM](https://openaccess.thecvf.com/content_ICCV_2017/papers/Xu_Multi-Channel_Weighted_Nuclear_ICCV_2017_paper.pdf): Multi-channel weighted nuclear norm minimization for real color image denoising (ICCV 2017)

### 2.4 去噪进阶文献（图像去噪前沿方法）

> 帮助同学了解图像去噪的前沿算法，学生可在此部分选择进阶文献进行专题汇报。

*  [Trainable nonlinear reaction diffusion](https://arxiv.org/pdf/1508.02848): A flexible framework for fast and effective image restoration (TPAMI 2016)
*  [DnCNN](https://arxiv.org/pdf/1608.03981): Beyond a gaussian denoiser: Residual learning of deep cnn for image denoising (TIP 2017)
*  [FFDNet](https://arxiv.org/pdf/1710.04026): Toward a fast and flexible solution for cnn-based image denoising (TIP 2018)
*  [RIDNet](https://openaccess.thecvf.com/content_ICCV_2019/papers/Anwar_Real_Image_Denoising_With_Feature_Attention_ICCV_2019_paper.pdf): Real image denoising with feature attention (CVPR 2019)
*  [SAD-Net](https://arxiv.org/pdf/2001.10291): Spatial adaptive network for single image denoising (ECCV 2020)
*  [CBDNet](https://openaccess.thecvf.com/content_CVPR_2019/papers/Guo_Toward_Convolutional_Blind_Denoising_of_Real_Photographs_CVPR_2019_paper.pdf): Toward convolutional blind denoising of real photographs (CVPR 2019)
*  [DANNet](https://arxiv.org/pdf/2007.05946): Dual adversarial network: Toward real-world noise removal and noise generation (ECCV 2020)
*  [Swinir](https://openaccess.thecvf.com/content/ICCV2021W/AIM/papers/Liang_SwinIR_Image_Restoration_Using_Swin_Transformer_ICCVW_2021_paper.pdf): Image restoration using swin transformer (ICCV 2021)
*  [DPIR](https://arxiv.org/pdf/2008.13751): Plug-and-play image restoration with deep denoiser prior (TPAMI 2021)
*  [GRL](https://openaccess.thecvf.com/content/CVPR2023/papers/Li_Efficient_and_Explicit_Modelling_of_Image_Hierarchies_for_Image_Restoration_CVPR_2023_paper.pdf): Efficient and explicit modelling of image hierarchies for image restoration (CVPR 2023)
*  [Restormer](https://openaccess.thecvf.com/content/CVPR2022/papers/Zamir_Restormer_Efficient_Transformer_for_High-Resolution_Image_Restoration_CVPR_2022_paper.pdf): Efficient transformer for high-resolution image restoration (CVPR 2022)
*  [Lg-bpn](https://openaccess.thecvf.com/content/CVPR2023/html/Wang_LG-BPN_Local_and_Global_Blind-Patch_Network_for_Self-Supervised_Real-World_Denoising_CVPR_2023_paper.html): Local and global blind-patch network for self-supervised real-world denoising (CVPR 2023)
*  [CLIPDenoising](https://openaccess.thecvf.com/content/CVPR2024/papers/Cheng_Transfer_CLIP_for_Generalizable_Image_Denoising_CVPR_2024_paper.pdf): Transfer CLIP for Generalizable Image Denoising (CVPR 2024)
*  [Positive2Negative](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_Positive2Negative_Breaking_the_Information-Lossy_Barrier_in_Self-Supervised_Single_Image_Denoising_CVPR_2025_paper.pdf): Breaking the Information-Lossy Barrier in Self-Supervised Single Image Denoising (CVPR 2025)

### 2.5 **图像Raw域去噪**

> 结合本专题的研究背景和前面知识的铺垫，逐渐引导学生进入图像Raw域去噪。
>

*  [SID](https://openaccess.thecvf.com/content_cvpr_2018/papers/Chen_Learning_to_See_CVPR_2018_paper.pdf): Learning to See in the Dark (CVPR 2018)
*  [Unprocessing images for learned raw denoising](https://openaccess.thecvf.com/content_CVPR_2019/papers/Brooks_Unprocessing_Images_for_Learned_Raw_Denoising_CVPR_2019_paper.pdf) (CVPR 2019)
*  [K-sigma](https://arxiv.org/pdf/2010.06935): Practical deep raw image denoising on mobile devices (ECCV 2020)
*  [Rethinking noise synthesis and modeling in raw denoising](https://openaccess.thecvf.com/content/ICCV2021/papers/Zhang_Rethinking_Noise_Synthesis_and_Modeling_in_Raw_Denoising_ICCV_2021_paper.pdf) (ICCV 2021)
*  [SCI](https://openaccess.thecvf.com/content/CVPR2022/papers/Ma_Toward_Fast_Flexible_and_Robust_Low-Light_Image_Enhancement_CVPR_2022_paper.pdf): Toward fast, flexible, and robust low-light image enhancement (CVPR 2022)
*  [Lan](https://openaccess.thecvf.com/content/CVPR2022W/NTIRE/papers/Raimundo_LAN_Lightweight_Attention-Based_Network_for_RAW-to-RGB_Smartphone_Image_Processing_CVPRW_2022_paper.pdf): Lightweight attention-based network for raw to-rgb smartphone image processing (CVPR 2022)
*  [Learning srgb-to-raw-rgb de-rendering with content-aware metadata](https://openaccess.thecvf.com/content/CVPR2022/papers/Nam_Learning_sRGB-to-Raw-RGB_De-Rendering_With_Content-Aware_Metadata_CVPR_2022_paper.pdf) (CVPR 2022)
*  [RAW-to-sRGB](https://openaccess.thecvf.com/content/ICCV2021/papers/Zhang_Learning_RAW-to-sRGB_Mappings_With_Inaccurately_Aligned_Supervision_ICCV_2021_paper.pdf): Learning raw-to-srgb mappings with inaccurately aligned supervision (ICCV 2021)
*  [LRD](https://openaccess.thecvf.com/content/ICCV2023/papers/Zhang_Towards_General_Low-Light_Raw_Noise_Synthesis_and_Modeling_ICCV_2023_paper.pdf): Towards general low-light raw noise synthesis and modeling (ICCV 2023)
*  [LED](https://openaccess.thecvf.com/content/ICCV2023/papers/Jin_Lighting_Every_Darkness_in_Two_Pairs_A_Calibration-Free_Pipeline_for_ICCV_2023_paper.pdf): Lighting every darkness in two pairs: A calibration free pipeline for raw denoising (ICCV 2023)
*  [Learn ability enhancement for low-light raw image denoising: A data perspective](https://ieeexplore.ieee.org/abstract/document/10207751) (TAPMI 2023)
*  [Dnf](https://openaccess.thecvf.com/content/CVPR2023/papers/Jin_DNF_Decouple_and_Feedback_Network_for_Seeing_in_the_Dark_CVPR_2023_paper.pdf): Decouple and feedback network for seeing in the dark (CVPR 2023)
*  [CycleR2R](https://arxiv.org/pdf/2212.07778): Efficient visual computing with camera raw snapshots (TPAMI 2024)
*  [Noise Modeling in One Hour](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_Noise_Modeling_in_One_Hour_Minimizing_Preparation_Efforts_for_Self-supervised_CVPR_2025_paper.pdf): Minimizing Preparation Efforts for Self-supervised Low-Light RAW Image Denoising (CVPR 2025)

***

## 三、结语与期望

“新芽计划”的初心，是点燃新芽学子对未知探索的热情，并为大家提供一片成长的沃土。图像 **Raw 域去噪** 是一个兼具挑战与价值的研究方向，它既直面真实成像系统中的复杂噪声问题，又为智能视觉应用的高质量输入奠定坚实基础。希望通过这个专题，新芽学子们不仅能够深入理解 **成像原理与噪声建模**，掌握前沿的 **深度学习与优化方法**，更能在动手实践中培养出 **批判性思维、创新能力与解决实际问题的本领**。

我们热切期待，在最终的汇报中，能看到大家对 Raw 域去噪问题的独到见解，以及闪耀着智慧光芒的创新实践！
