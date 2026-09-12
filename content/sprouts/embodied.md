---
title: 新芽专题介绍（21）：具身智能
date: 2025-09-18T01:39:00Z
draft: false
math: true
---

## 一、专题介绍

### 1\.1 研究背景与统一定义

定义：**具身智能（Embodied AI）**指的是将人工智能集成到物理实体中，使其能够感知、学习并与环境互动 。

具身智能的研究源于对**传统符号主义人工智能**的反思。早期人工智能强调符号推理与规则处理，但在**复杂、动态、开放环境**中暴露出适应性不足、依赖先验知识强、难以实现真实感知等问题。研究者因此认识到，脱离身体与环境的“纯计算智能”难以形成真正接近生命体的智能。

认知科学中的**具身认知理论**指出，人的认知与**身体结构、感知经验和行动过程**密切相关，身体不仅是执行工具，也是智能形成的重要基础。另一方面，机器人在真实世界中面临**环境不确定、任务多变、感知噪声大**等挑战，传统“先建模、再规划、后执行”的方法已难以满足需求。

近年来，随着**深度学习、强化学习、大模型和多模态技术**的发展，具身智能快速兴起，成为连接**感知智能与行动智能**的重要方向，也被视为通向更高水平**通用人工智能**的关键路径。

### 1\.2 研究意义

1. **缓解数据匮乏与跨模态瓶颈**  

真实世界数据采集成本高，具身智能通过**自监督学习、多模态模型和数据共享**提升技能获取效率，降低开发门槛。 

2. **提升跨形态通用性**  

传统机器人常是一机一程，而具身智能强调**通用基础模型**，希望实现同一套智能适配不同硬件形态。  

3. **增强安全性与鲁棒性**  

具身智能关注机器人在真实物理环境中的**自适应、避障与稳定交互**能力，以保障复杂场景下的安全运行。  

4. **推动虚实迁移与闭环进化**  

通过**Sim\-to\-Real**技术，可在仿真中低成本迭代训练，再迁移到现实环境中验证和优化系统性能。

### 1\.3 当前主要挑战

1. **感知与语义鸿沟**：多模态传感器存在噪声、标注误差与模态异构，智能体难以从原始数据中形成支撑操作决策的**语义理解**。

2. **感知\-行动闭环的实时性**：动态环境要求毫秒级完成感知\-规划\-执行闭环，而大模型推理延迟与机器人控制频率之间存在显著的**时序不匹配**。

3. **Sim\-to\-Real迁移失效**：仿真环境在接触力学、材质形变等**物理保真度**上与真实世界差距显著，导致习得策略迁移至真实场景时性能大幅衰退。

4. **长程任务规划能力不足**：面对指令模糊、子任务依赖复杂的开放场景，智能体需具备**常识推理与多步因果推断**能力，远超当前模型的规划深度上限。

5. **具身数据获取成本高昂**：带物理交互标注的真实操作数据采集成本高、规模化难，远不及语言或视觉数据丰富，严重**制约模型训练与泛化**。

6. **安全性与鲁棒性的双重约束**：人机共存环境中须同时保证**物理安全与决策鲁棒性**，二者之间存在内在权衡，现有方法尚难兼顾。

## 二、基础\-文献综述与具身智能基础

### 2\.1 基础教材与学习材料

- 入门综述：

    - [Aligning Cyber Space with Physical World: A Comprehensive Survey on Embodied AI](https://arxiv.org/abs/2407.06886)

    - [A Comprehensive Survey on Embodied Intelligence: Advancements, Challenges, and Future Perspectives](https://www.sciopen.com/article/pdf/10.26599/AIR.2024.9150042.pdf?ifPreview=0)

    - [A Survey on Vision\-Language\-Action Models for Embodied AI](https://arxiv.org/abs/2405.14093)

    - 中文综述：[面向具身操作的视觉\-语言\-动作模型综述](https://arxiv.org/pdf/2508.15201)

- 课程：[Building and Working in Environments for Embodied AI](https://ai-workshops.github.io/building-and-working-in-environments-for-embodied-ai-cvpr-2022/)

### **2\.2 机器人学与系统构建**

理解机器人系统的组成，包括感知、决策、执行等模块。

- [Robotics, Embodied AI, and Learning \- CMU](https://www.cmu.edu/real/)

- [Deep Learning for Robotics](https://16-884.github.io/)

- [Introduction to Robot Learning](https://16-831-s24.github.io/)

    - CMU Robotics官方视频账号：[https://www\.youtube\.com/@cmurobotics](https://www.youtube.com/@cmurobotics)

### 2\.3 深度学习基础

- [吴恩达深度学习deeplearning\.ai](https://www.bilibili.com/video/BV1FT4y1E74V/?vd_source=44e9333995c149a4a2417d66a98a3d8c)

- [Deep Learning for Robotics](https://16-884.github.io/)

- [Multimodal machine learning \(MMML\)](https://cmu-mmml.github.io/)

    - [Video](https://youtu.be/DPkwjgaRvyI?si=XvJfBSD2HiDum3pS)

## 三\.初级学习路径\-决策算法与仿真平台

### 3\.1 算法与决策

**强化学习：**

- [李宏毅《深度强化学习》](https://youtu.be/z95ZYgPgXOY?si=CtCrb4ffWhOfhj_t)

    - [蘑菇书EasyRL](https://datawhalechina.github.io/easy-rl/#/)

- [CS285: Deep Reinforcement Learning](https://rail.eecs.berkeley.edu/deeprlcourse/)

    - [Video](https://youtube.com/playlist?list=PL_iWQOsE6TfVYGEGiAOMaOzzv41Jfm_Ps&si=hvE4iXFzWkOeWNPD)

- [Deep Reinforcement Learning \& Control](https://cmudeeprl.github.io/403website_s22/)

**模仿学习：**

- [MIT：Imitation Learning](https://underactuated.mit.edu/imitation.html)

- [A Survey of Imitation Learning: Algorithms, Recent Developments, and Challenges](https://arxiv.org/abs/2309.02473)

### 3\.2 仿真平台

- AI Habitat

- AI2\-THOR

- AirSim

- CHALET

- Isaac Sim

- Isaac Gym

- Gazebo

- [Habitat](https://github.com/facebookresearch/habitat-sim)

- PyBullet

- Webots

- MuJoCo

- Matterport 3D

- MORSE

- RoboTHOR

- SAPIEN

- SofyGym

- Virtual Home

- iGibson

- V\-REP \(CoppeliaSim\)

- Unity ML\-Agents

- TDW

- Virtual Home

- VRKitchen

- [SonoGym](https://sonogym.github.io/)：High Performance Simulation for Challenging Surgical Tasks with Robotic Ultrasound

- [AgentWorld](https://yizhengzhang1.github.io/agent_world/)

学习资源：

Building and Working in Environments for Embodied AI

## 四\.进阶学习路径\-\-前沿文献与开源项目实践

## 4\.1前沿文献

- 最新综述

    - [Embodied Robot Manipulation in the Era of Foundation Models: Planning and Learning Perspectives](https://arxiv.org/pdf/2512.22983)** **基础模型时代下的具身机器人操作综述：规划与学习视角

    - [An Anatomy of Vision\-Language\-Action Models: From Modules to Milestones and Challenges](https://suyuz1.github.io/VLA-Survey-Anatomy/)视觉语言动作VLA模型综述：从模块到里程碑和挑战

    - [What Is The Best 3D Scene Representation for Robotics? From Geometric to Foundation Models](https://arxiv.org/pdf/2512.03422)机器人领域中最优的3D场景表示是什么？从几何表示到基础模型

    - [The Reality Gap in Robotics: Challenges, Solutions, and Best Practices](https://arxiv.org/pdf/2510.20808)机器人技术的现实差距：挑战、解决方案和最佳实践

- 文献

    #### 任务规划与通用具身智能

    - [PaLM\-E：An Embodied Multimodal Language Model](https://arxiv.org/pdf/2303.03378) 【被引 **3100 **次】

    - [RT\-2: Vision\-Language\-Action Models Transfer Web Knowledge to Robotic Control](https://proceedings.mlr.press/v229/zitkovich23a) 【被引 **2962** 次】

    - [Voyager: An Open\-Ended Embodied Agent with Large Language Models ](https://arxiv.org/pdf/2305.16291)【被引 **1914** 次】

    - [Recurrent Reasoning with Vision\-Language Models for Estimating Long\-Horizon Embodied Task Progress](https://arxiv.org/pdf/2603.17312)【CVPR 2026】

    #### 视觉导航与环境交互

    - [Learning to Navigate in Complex Environments](https://arxiv.org/pdf/1611.03673) 【被引 **1166** 次】

    - [Object Goal Navigation using Goal\-Oriented Semantic Exploration ](https://proceedings.neurips.cc/paper/2020/hash/2c75cf2681788adaca63aa95ae028b22-Abstract.html)【NeurlPS 2020，被引 **823 **次】

    - [Habitat: A Platform for Embodied AI Research](https://openaccess.thecvf.com/content_ICCV_2019/html/Savva_Habitat_A_Platform_for_Embodied_AI_Research_ICCV_2019_paper.html) 【ICCV 2019，被引 **2211** 次】

    - [AgentVLN: Towards Agentic Vision\-and\-Language Navigation](https://arxiv.org/pdf/2603.17670)

    - [CoT\-VLA: Visual Chain\-of\-Thought Reasoning for Vision\-Language\-Action Models](https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.html) 【CVPR 2025，被引 **305 **次】

    #### 交互操作与机器人学习

    - [Transporter Networks: Rearranging the Visual World for Robotic Manipulation](https://proceedings.mlr.press/v155/zeng21a.html) 【被引 **658** 次】

    - [Perceiver\-Actor: A Multi\-Task Transformer for Robotic Manipulation](https://proceedings.mlr.press/v205/shridhar23a.html) 【被引 **855** 次】

    - [CLIPort: What and Where Pathways for Robotic Manipulation ](https://proceedings.mlr.press/v164/shridhar22a.html)【被引 **1015 **次】

    - [Towards Generalizable Robotic Manipulation in Dynamic Environments](https://arxiv.org/pdf/2603.15620)【大规模数据集】

    - [Core4d: A 4d human\-object\-human interaction dataset for collaborative object rearrangement](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_CORE4D_A_4D_Human-Object-Human_Interaction_Dataset_for_Collaborative_Object_REarrangement_CVPR_2025_paper.html) 【CVPR 2025，4D交互数据集】

    #### 多模态学习与基础模型

    - [Flamingo: a Visual Language Model for Few\-Shot Learning ](https://proceedings.neurips.cc/paper_files/paper/2022/hash/960a172bc7fbf0177ccccbb411a7d800-Abstract-Conference.html)【NeurlPS 2022，被引 **7667 **次】

    - [BLIP\-2: Bootstrapping Language\-Image Pre\-training with Frozen Image Encoders and Large Language Models ](https://proceedings.mlr.press/v202/li23q)【ICML 2023，被引** 10868 **次】

    - [Segment anything](https://openaccess.thecvf.com/content/ICCV2023/html/Kirillov_Segment_Anything_ICCV_2023_paper.html) 【ICCV 2023，被引 **19241 **次】

    - [SaPaVe: Towards Active Perception and Manipulation in Vision\-Language\-Action Models for Robotics](https://lmzpai.github.io/SaPaVe/)  【CVPR 2026】

### 4\.2开源项目

- [Genesis](https://github.com/Genesis-Embodied-AI/Genesis)

- [Cosmos](https://github.com/NVIDIA/Cosmos)

- [Open X\-Embodiment](https://github.com/google-deepmind/open_x_embodiment)

## 五、结语与期望

跨越“感知→决策→行动”的闭环鸿沟，是具身智能从算法走向真实世界的关键一步。通过本专题，你将系统掌握具身智能基础理论、机器人系统组成、强化/模仿学习方法、仿真平台使用以及VLA与基础模型前沿进展，逐步完成从**文献阅读 → 平台实践 → 方法复现 → 小型创新**的科研训练链条。期待你在最终汇报中：

1）清晰**界定研究问题与任务场景**，说明所关注的是导航、操作、任务规划还是通用具身智能；

2）完成**扎实的基线复现与实验评测**，能够结合仿真平台或开源项目开展验证；

3）**提出小而有效的改进思路**，例如：更高效的多模态对齐、更稳健的Sim\-to\-Real迁移、更可靠的长程规划机制、更安全的交互控制策略等，推动具身智能系统向更强泛化、更高鲁棒、更易落地的方向发展。



