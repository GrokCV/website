---
title: 空间邻近红外小目标解混资源精选 
date: 2025-11-17
draft: false
math: true
authors: 
- Mengze Xu
- Ximeng Zhai
- Shengdong Han
- Yimian Dai
---

**作者**: 许孟泽, 翟曦盟, 韩圣东, **戴一冕***

**English Version:** [Link to English Version](https://github.com/GrokCV/Awesome-CSIST-Unmixing)

>一个关于空间邻近红外小目标解混 (Closely-Spaced Infrared Small Target Unmixing, CSIST Unmixing) 技术的精选资源列表（包含论文、代码、数据集等）。 

**空间邻近红外小目标解混** 是红外搜索与跟踪系统中的一项关键且具有挑战性的任务。它专注于解混和检测焦平面上彼此非常靠近的多个弱小目标，这些目标通常会光学扩散现象导致红外成像混叠严重，多目标可能集中在几个像素中，导致难以准确识别目标的数量和位置。本资源库旨在收集和整理这一特定领域的最新进展。

## 目录

- [空间邻近红外小目标解混资源精选](#awesome-closely-spaced-infrared-small-target-unmixing-)
  - [目录](#目录)
  - [论文](#论文)
    - [按年份排序](#按年份排序)
      - [2025](#2025)
      - [2024](#2024)
      - [2023](#2023)
      - [2022](#2022)
      - [2020](#2020)
      - [Pre-2020](#Pre-2020)
    - [按方法分类](#按方法分类)
      - [基于模型/优化算法的方法](#按方法分类)
      - [基于深度学习的方法](#基于深度学习的方法)
  - [数据集与基准](#数据集与基准)
  - [评估指标](#评估指标)
  - [相关研究团队](#相关研究团队)

## 论文

### 按年份排序

#### 2025
-   **DISTA-Net: Dynamic Closely-Spaced Infrared Small Target Unmixing** - *Shengdong Han, Shangdong Yang, Xin Zhang, Yuxuan Li, Xiang Li, Jian Yang, Ming-Ming Cheng, Yimian Dai*, ICCV 2025 \
    [[论文](https://arxiv.org/abs/2505.19148)]
    [[代码](https://github.com/GrokCV/GrokCSO) :star: ]
-   **SeqCSIST: Sequential Closely-Spaced Infrared Small Target Unmixing** - *Ximeng Zhai, Bohan Xu, Yaohong Chen, Hao Wang, Kehua Guo and Yimian Dai*, TGRS 2025 \
    [[论文](https://arxiv.org/abs/2507.09556)]
    [[代码](https://github.com/GrokCV/SeqCSIST) :star: ]
#### 2024
-   **A Resolution and Localization Algorithm for Closely-Spaced Objects Based on Improved YOLOv5 Joint Fuzzy C-Means Clustering** - *Li et al.*, IEEE Photonics Journal, 2024 \
    [[论文](https://ieeexplore.ieee.org/document/10418965)]

#### 2023
-   **Closely-Spaced Object Classification Using MuyGPyS** - *Zhang et al.*, Advanced Maui Optical and Space Surveillance Technologies Conference (AMOS), 2023 \
    [[论文](https://arxiv.org/pdf/2311.10904)]

#### 2022
-   **Closely spaced object detection utilizing spatial information in spectroastrometric observations** - *J. Zachary Gazak, Ryan Swindle, Zachary Funke, Matthew Phelps, Justin Fletcher*, Sensors and Systems for Space Applications XV. SPIE, 2022 \
    [[论文](https://neurophotonics.spiedigitallibrary.org/conference-proceedings-of-spie/12121/121210K/Closely-spaced-object-detection-utilizing-spatial-information-in-spectroastrometric-observations/10.1117/12.2625366.full)]

#### 2020
-   **采用分裂 Bregman 的空间邻近目标红外超分辨算法** - *左芝勇*, 电讯技术, 2020 \
    [[论文](https://openurl.ebsco.com/EPDB%3Agcd%3A11%3A31617819/detailv2?sid=ebsco%3Aplink%3Ascholar&id=ebsco%3Agcd%3A144824734&crl=c&link_origin=scholar.google.com)]

#### Pre-2020

-   **The infrared image closely spaced objects super resolution method based on sparse reconstruction under the noise environment** - *J Zeng, J Yang, H Wu*, International Conference on Optical and Photonics Engineering (icOPEN 2016). SPIE, 2017 \
    [[论文](https://nanophotonics.spiedigitallibrary.org/conference-proceedings-of-spie/10250/102502V/The-infrared-image-closely-spaced-objects-super-resolution-method-based/10.1117/12.2266856.full)]

-   **Electromagnetic Imaging of Closely Spaced Objects using Matching Pursuit Based Approaches** - *Şenyuva, R. V., Özdemir, Ö., Kurt, G. K., & Anarım*, IEEE Antennas and Wireless Propagation Letters, 2015 \
    [[论文](https://ieeexplore.ieee.org/abstract/document/7327171/)]

-   **Bayesian approach to joint super-resolution and trajectory estimation for midcourse closely spaced objects via space-based infrared sensor** - *Liangkui Lin, Weidong Sheng, Dan Xu*, Optical Engineering, 2012 \
    [[论文](https://www.spiedigitallibrary.org/journals/optical-engineering/volume-51/issue-11/117003/Bayesian-approach-to-joint-super-resolution-and-trajectory-estimation-for/10.1117/1.OE.51.11.117003.full)]

-   **QPSO-based algorithm of CSO joint infrared super-resolution and trajectory estimation** - *Lin, Liangkui and Xu, Hui and Xu, Dan and An, Wei and Xie, Kai*, Journal of Systems Engineering and Electronics, 2011 \
    [[论文](https://ieeexplore.ieee.org/abstract/document/6077736/)]

-  **基于 Gibbs 抽样的红外成像小间距目标分辨方法** - *刘涛*, 信号处理, 2010 \
    [[论文](https://signal.ejournal.org.cn/article/id/8568)]

-   **Hierarchical Closely-Spaced Object (CSO) Resolution for IR Sensor Surveillance** - *Macumber, Daniel and Gadaleta, Sabino and Floyd, Allison and Poore, Aubrey*, Signal and Data Processing of Small Targets, 2005 \
    [[论文](https://www.spiedigitallibrary.org/conference-proceedings-of-spie/5913/591304/)]

-   **Model-based superresolution CSO processing** - *John T. Reagan, Theagenis J. Abatzoglou*, Signal and Data Processing of Small Targets, 1993 \
    [[论文](https://opticalengineering.spiedigitallibrary.org/conference-proceedings-of-spie/1954/0000/Model-based-superresolution-CSO-processing/10.1117/12.157809.full)]


### 按方法分类

####  **基于模型 / 优化方法**
  -   **Closely spaced object detection utilizing spatial information in spectroastrometric observations** - *J. Zachary Gazak, Ryan Swindle, Zachary Funke, Matthew Phelps, Justin Fletcher*, Sensors and Systems for Space Applications XV. SPIE, 2022 \
      [[论文](https://neurophotonics.spiedigitallibrary.org/conference-proceedings-of-spie/12121/121210K/Closely-spaced-object-detection-utilizing-spatial-information-in-spectroastrometric-observations/10.1117/12.2625366.full)]
  
  -   **采用分裂 Bregman 的空间邻近目标红外超分辨算法** - *左芝勇*, 电讯技术, 2020 \
      [[论文](https://openurl.ebsco.com/EPDB%3Agcd%3A11%3A31617819/detailv2?sid=ebsco%3Aplink%3Ascholar&id=ebsco%3Agcd%3A144824734&crl=c&link_origin=scholar.google.com)]

  -   **The infrared image closely spaced objects super resolution method based on sparse reconstruction under the noise environment** - *J Zeng, J Yang, H Wu*, International Conference on Optical and Photonics Engineering (icOPEN 2016). SPIE, 2017 \
      [[论文](https://nanophotonics.spiedigitallibrary.org/conference-proceedings-of-spie/10250/102502V/The-infrared-image-closely-spaced-objects-super-resolution-method-based/10.1117/12.2266856.full)]

  -   **Electromagnetic Imaging of Closely Spaced Objects using Matching Pursuit Based Approaches** - *Şenyuva, R. V., Özdemir, Ö., Kurt, G. K., & Anarım*, IEEE Antennas and Wireless Propagation Letters, 2015 \
      [[论文](https://ieeexplore.ieee.org/abstract/document/7327171/)]

  -   **Bayesian approach to joint super-resolution and trajectory estimation for midcourse closely spaced objects via space-based infrared sensor** - *Liangkui Lin, Weidong Sheng, Dan Xu*, Optical Engineering, 2012 \
      [[论文](https://www.spiedigitallibrary.org/journals/optical-engineering/volume-51/issue-11/117003/Bayesian-approach-to-joint-super-resolution-and-trajectory-estimation-for/10.1117/1.OE.51.11.117003.full)]

  -   **QPSO-based algorithm of CSO joint infrared super-resolution and trajectory estimation** - *Lin, Liangkui and Xu, Hui and Xu, Dan and An, Wei and Xie, Kai*, Journal of Systems Engineering and Electronics, 2011 \
      [[论文](https://ieeexplore.ieee.org/abstract/document/6077736/)]
      
  -  **基于 Gibbs 抽样的红外成像小间距目标分辨方法** - *刘涛*, 信号处理, 2010 \
      [[论文](https://signal.ejournal.org.cn/article/id/8568)]

  -   **Hierarchical Closely-Spaced Object (CSO) Resolution for IR Sensor Surveillance** - *Macumber, Daniel and Gadaleta, Sabino and Floyd, Allison and Poore, Aubrey*, Signal and Data Processing of Small Targets, 2005 \
      [[论文](https://www.spiedigitallibrary.org/conference-proceedings-of-spie/5913/591304/)]

  -   **Model-based superresolution CSO processing** - *John T. Reagan, Theagenis J. Abatzoglou*, Signal and Data Processing of Small Targets, 1993 \
      [[论文](https://opticalengineering.spiedigitallibrary.org/conference-proceedings-of-spie/1954/0000/Model-based-superresolution-CSO-processing/10.1117/12.157809.full)]
      
####  **基于深度学习的方法**
  -   **DISTA-Net: Dynamic Closely-Spaced Infrared Small Target Unmixing** - *Shengdong Han, Shangdong Yang, Xin Zhang, Yuxuan Li, Xiang Li, Jian Yang, Ming-Ming Cheng, Yimian Dai*, ICCV 2025 \
      [[论文](https://arxiv.org/abs/2505.19148)]
      [[代码](https://github.com/GrokCV/GrokCSO) :star: ]

  -   **SeqCSIST: Sequential Closely-Spaced Infrared Small Target Unmixing** - *Ximeng Zhai, Bohan Xu, Yaohong Chen, Hao Wang, Kehua Guo and Yimian Dai*, TGRS 2025 \
      [[论文](https://arxiv.org/abs/2507.09556)]
      [[代码](https://github.com/GrokCV/SeqCSIST) :star: ]
      
  -   **A Resolution and Localization Algorithm for Closely-Spaced Objects Based on Improved YOLOv5 Joint Fuzzy C-Means Clustering** - *Li et al.*, IEEE Photonics Journal, 2024 \
      [[论文](https://ieeexplore.ieee.org/document/10418965)]
  
  -   **Closely-Spaced Object Classification Using MuyGPyS** - *Zhang et al.*, Advanced Maui Optical and Space Surveillance Technologies Conference (AMOS), 2023 \
      [[论文](https://arxiv.org/pdf/2311.10904)]

## 数据集与基准

-   **CSIST-100K** - 一个用于空间邻近红外点目标解混的大规模合成数据集（10万样本）。模拟每张图像包含 1-5 个目标，扩散函数标准差为 σ=0.5 像素，最小间距 ≥0.52 瑞利单位，且强度随机。目标在 3×3 区域内显著重叠，对计数和定位提出了严峻挑战。（按 80k/10k/10k 划分）\
    [[百度网盘](https://pan.baidu.com/s/1nuedV5Okng8rgFWKy_sMoA?pwd=Grok)  [OneDrive](https://1drv.ms/f/c/698f69b8b2172561/EnQbsEb_rXpJlsNXinWyBbsBkhCsnSPM7UEgtczt7FDjmQ)]

-   **SeqCSIST** - 序列空间邻近红外小目标解混数据集 \
    *一个用于序列空间邻近红外小目标解混的序列基准数据集。这是一个合成数据集，生成的图像尺寸为11×11像素。每张图像包含2到4个目标，强度从特定范围内随机采样。目标遵循随机轨迹。目标渲染基于84%能量集中分辨率标准和0.5像素的扩散标准差。XML文件中提供每个目标的精确坐标和强度等真实值。* \
    [[百度网盘](https://pan.baidu.com/s/1_sxGh5oFQ8-3RpUUeMN2Mg?pwd=kxe9)  [OneDrive](https://1drv.ms/f/c/698f69b8b2172561/EuBC8549kZJIp_syz2Glft4BU2Fu5Ri-wYE888HJ9kmiiQ?e=zEISNc)]

-   **自定义仿真数据集** - 自定义红外目标仿真数据生成方法 \
    - **中段弹道目标群的红外成像仿真研究** - *林两魁, 谢恺, 徐晖*, 红外与毫米波学报, 2009. [[论文](https://www.researching.cn/ArticlePdf/m00032/2009/28/3/2009-03-0218.pdf)]
    - **弹道目标识别的红外辐射数据仿真研究** - *刘俊良, 陈尚锋, 卢焕章*, 红外与激光工程, 2016. [[论文](https://www.researching.cn/ArticlePdf/m00018/2016/45/10/1004002.pdf)]
    - **深空动态场景目标红外图像仿真研究** - *李志军, 王卫华, 陈曾平*, 红外技术, 2007. [[论文](http://hwjs.nvir.cn/article/doi/10.3969/j.issn.1001-8891.2007.07.010)]
    - **空间目标在轨红外成像仿真** - *王盈, 黄建明, 魏祥泉*, 红外与激光工程, 2015. [[论文](https://www.researching.cn/ArticlePdf/m00018/2015/44/9/2015-09-2593.pdf)]
    - **红外运动目标轨迹重构动态仿真平台** - *姚成喆, 郭伟兰, 陈钱*, 红外与激光工程, 2022. [[论文](https://www.researching.cn/ArticlePdf/m00018/2022/51/2/20210901.pdf)]
    - **天基空间小目标复杂场景数字成像仿真** - *李鹏飞, 徐伟, 朴永杰*, 系统仿真学报, 2025. [[论文](https://www.china-simulation.com/CN/10.16182/j.issn1004731x.joss.24-0900)]
    - **红外成像系统噪声测量仿真研究** - *邹前进, 戴睿, 刘鑫*, 红外技术, 2008. [[论文](http://hwjs.nvir.cn/cn/article/pdf/preview/10.3969/j.issn.1001-8891.2008.06.010.pdf)]
    - **Exploring Video Denoising in Thermal Infrared Imaging: Physics-Inspired Noise Generator, Dataset, and Model** - *Cai L, Dong X, Zhou K*，IEEE Transactions on Image Processing, 2024. [[论文](https://ieeexplore.ieee.org/document/10507231)]

    

## 评估指标

-   **CSO-mAP**: 空间邻近红外小目标平均检测精度 在多个亚像素距离阈值 (δ=0.05 - 0.25px) 上的平均精度的均值。 受平均检测精度（mAP）启发的指标，旨在评估目标间距小于瑞利判据场景下的精确定位性能。[[论文](https://arxiv.org/abs/2505.19148)]
    [[代码](https://github.com/GrokCV/GrokCSO) :star: ]

## 相关研究团队

-   **[GrokCV](https://yimian.grokcv.ai/)** - [南开大学](https://www.nankai.edu.cn/) - *由戴一冕副教授领导。长期致力于红外弱小目标检测和遥感多模态视觉感知。*

