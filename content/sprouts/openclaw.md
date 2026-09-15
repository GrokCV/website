---
title: 新芽专题介绍（28）：从入门到深入掌握 OpenClaw
date: 2025-09-18T01:32:00Z
draft: false
math: true
---

## 研究背景

OpenClaw（早期曾被称为 Moltbot、Clawdbot）是一个**本地优先、自托管的多渠道 AI 智能体框架**：你在自己的电脑或服务器上运行一个长期驻留的 Gateway（网关守护进程），它通过 WebSocket 统一管理各种聊天通道（WhatsApp、Telegram、Slack、Discord、iMessage、Matrix 等），并将这些通道接入一个或多个“大模型智能体”（如 Claude、OpenAI、Gemini 或本地 LLM）[1][2]。

其核心技术特征包括：

- **本地优先（local‑first）架构**：

- 会话状态、记忆文件、配置等都存放在本机工作区（workspace）中，多为 Markdown 和 JSONL 文件，而不是中心化云数据库[2]。
- 只在向 LLM 服务商（如 Anthropic、OpenAI、Gemini）发起推理请求时进行“出站访问”。

- **Gateway 控制平面**：

- 单一网关守护进程（Node.js daemon），统一维护所有通道会话、工具调用、会话路由与权限策略，通过 WebSocket（默认 127.0.0.1:18789）对外暴露 API[2][3]。
- Gateway 是“单一写入者”（single‑writer）和“单一事实来源”，负责会话有序写入和状态一致性。

- **多通道、多智能体路由**：

- 通过“Channel Bridges”与 WhatsApp（Baileys）、Telegram（grammY）、Slack、Discord、Signal、iMessage 等 SDK 建立长连接，将不同平台消息归一为内部事件信封，再路由给对应智能体或工作区[2]。
- 支持“多智能体”路由策略：按用户、群组、通道、工作区为粒度拆分不同 Agent 的会话和记忆。

- **丰富工具与技能生态**：

- 内建工具：文件读写、shell 命令执行、浏览器控制（CDP）、Web 抓取/搜索、内存搜索、Canvas 可视化、定时任务（cron）、TTS、会话管理、自我管理（gateway.restart / config）、多 Agent 协作（spawn sub‑agent）等[2]。
- “技能（Skill）”是一类以 [SKILL.md](http://SKILL.md) 为核心的 Markdown 描述包，通过 ClawHub 公共注册表进行发布、版本管理与搜索[4][5]。

- **文件化记忆体系**：

- 采用四层记忆架构：

- Layer 1：Session Context（当前会话，JSONL 记录）
- Layer 2：Daily Logs（memory/YYYY‑MM‑[DD.md](http://DD.md)）
- Layer 3：Long‑term Memory（[MEMORY.md](http://MEMORY.md)，人工筛选的长期记忆）
- Layer 4：向量检索层（SQLite + 向量嵌入 + BM25 混合检索）[3]。

- 强调“人类可读、可 git 版本管理”的工作区。

- **开放源代码与社区**：

- OpenClaw 以 MIT 协议在 GitHub 开源，2026 年 Star 数量已超过 20 万，衍生出的论文、技术博客、安全分析、技能市场生态异常活跃[1][3][6][7]。

总的来说，OpenClaw 既是一个“把各种聊天工具接到 LLM 上”的网关，又是一个“具备长期记忆、多 Agent、自动化工作流与插件生态”的通用智能体操作系统。

## 研究意义

1. 技术与工程意义

- **典型的“智能体操作系统”参考架构**
OpenClaw 将“LLM 认知层”与“工具/系统执行层”清晰解耦：Gateway 负责 I/O 与状态，Agent Runtime 负责推理与工具调用，Skill 与 Hook/Plugin 负责扩展。这种分层设计，为之后所有 agentic 系统的架构规划提供了可复用蓝本[2][3]。
- **文件化、可审计的记忆设计**
通过 Markdown + JSONL + 向量检索的组合，OpenClaw 将“可审计性”和“可编辑性”引入到传统黑盒 RAG/记忆系统中。研究其记忆机制，对构建可解释、可追踪的 AI 助手很有借鉴意义[3]。
- **多通道、多智能体协作**
OpenClaw 原生支持多通道和多智能体的隔离与路由（包括子 Agent 机制、会话键路由规则等），是研究“Agent 社区”“Agent 社交网络”和“多 Agent 分工协作”时最常被引用的开源平台之一[6]。
- **安全研究的理想样本**
因为其具备：

- 真实 OS 权限（文件、网络、浏览器控制、shell 等）；
- 丰富第三方技能供应链（ClawHub）；
- 大量实际用户部署。
所以 OpenClaw 成为了多篇关于“智能体安全、供应链攻击、提示注入”的实证研究核心案例[6][7][8]。

2. 产业与应用意义

- **个人与中小团队的“AI 助理标准件”**
不依赖云厂商的 SaaS，个人就可以拥有跨平台、可自定义的 AI 助手，助力开发、运维、知识管理与日常办公。
- **企业私有化部署与合规场景**
对于金融、医疗、法律等严格合规行业，OpenClaw 提供了一个可完全自托管、可审计的 agentic 平台，成为构建垂直领域智能体系统的基础设施[6][7]。
- **安全标准与治理框架探索对象**
在 OpenClaw 的诸多漏洞事件与供应链问题基础上，学术界和产业界提出了诸如“三层风险分类”“全生命周期智能体安全架构（FASA）”等框架，有望演化为行业标准[6][7]。

## 当前挑战

1. 安全风险（Security）

- **远程代码执行与权限滥用**

- 已披露的漏洞如 CVE‑2026‑25253（“ClawJacked”）：利用 Gateway 默认对本地 127.0.0.1 弱认证的特性，通过构造链接窃取 token 并远程执行命令[7]。
- Agent 拥有文件、shell、浏览器等强力工具，一旦策略配置不当或技能恶意，即可能导致主机被完全控制。

- **提示注入与顺序工具链攻击（STAC）​**

- 攻击者可将恶意指令隐藏于网页、邮件或技能输出中，诱导智能体绕过原有安全提示，执行数据窃取、批量操作等[7]。
- 顺序工具链攻击：通过多步工具调用组合，分步绕过安全检测。

- **供应链与技能市场风险**

- ClawHub 上已发现数百个恶意/后门技能（窃取 API Key、上传 PII、植入隐形提示注入等）[5][8]。
- 技能声明的 [SKILL.md](http://SKILL.md) frontmatter 与真实行为可能不一致，形成“软后门”。

- **记忆与数据泄露**

- 本地 Markdown 与 SQLite 中可能包含 API 密钥、中间推理“思考”、用户敏感信息，如缺乏加密与访问控制，主机被入侵即全盘暴露[3][7]。

2. 架构与运维挑战

- **沙箱与隔离不足**

- Reference Architecture 中指出：生产部署通常将 Gateway 以 systemd 方式运行在主机，并允许主会话直接执行工具，若未启用 Docker sandbox，将扩大攻击面与爆破半径[2][3]。
- 按 session/agent 进行容器级隔离虽有设计，但对普通用户来说配置复杂。

- **多 Agent / 子 Agent 调度复杂度**

- 子 Agent 拥有独立会话、工具集与并发限制（默认 8 并发），如何合理路由任务、控制成本与防止“Agent 炸群”是一大工程挑战[2][3]。

- **记忆与上下文管理的稳定性**

- 为了控制上下文窗口，OpenClaw通过“压缩+剪枝+预刷写（pre‑compaction flush）”策略自动摘要并写入 memory/YYYY‑MM‑[DD.md](http://DD.md)。不当配置可能导致“安全策略被压缩掉”的“情境遗忘”，引发错误行为[3][7]。

3. 使用体验与生态挑战

- **学习曲线**

- 完整掌握 OpenClaw 需要理解：Node 环境/Gateway 运行、通道接入、工作区组织、技能机制、沙箱和安全策略等，对非工程背景用户门槛偏高。

- **技能质量与标准化不足**

- ClawHub 上技能繁多，但文档质量、维护状态、安全水平参差不齐，对新手用户构成“选择风险”与“安全负债”。

## 基础资料

- [OpenClaw 官方文档（OpenClaw Docs）​](https://docs.openclaw.ai/) - 官方权威文档站点，概述 OpenClaw 的架构、安装方式、配置文件、通道接入、安全设置等，是所有学习路径的首要入口
- [OpenClaw GitHub 仓库与 README](https://github.com/openclaw/openclaw/blob/main/README.md) - 包含整体技术概览、Gateway 与 Onboard CLI 的工作方式、安装命令（npm/pnpm/bun）、核心特性列表，是了解系统结构与命令行入口的基础材料
- [Getting Started – 官方快速入门指南](https://github.com/openclaw/openclaw/blob/main/docs/start/getting-started.md) - 从 0 安装 OpenClaw、运行 Onboard 向导、启动 Gateway 并与第一个聊天通道对接的完整教程，适合第一次部署的用户
- [OpenClaw Reference Architecture（架构参考文档）​](https://robotpaper.ai/reference-architecture-openclaw-early-feb-2026-edition-opus-4-6/) - 第三方撰写但被广泛引用的“架构白皮书”，对 Gateway、Channel Bridges、Agent Runtime、记忆系统、子 Agent、Hooks/Plugins、安全分层进行了高度细致的技术剖析，是进阶开发者和架构师的必读文档
- [ClawHub – OpenClaw 公共技能注册表](https://github.com/openclaw/clawhub) - 官方技能目录，支持技能发布、版本管理与搜索，文档中对 SKILL.md 的格式、技能声明和验证流程有基础说明，是学习技能生态和供应链安全的入口
- [《What are OpenClaw Skills? – Developer’s Guide》](https://www.digitalocean.com/resources/articles/what-are-openclaw-skills) - 详细介绍 SKILL.md 结构、YAML frontmatter 字段、运行时环境声明以及多 Agent 环境下技能加载优先级（workspace > local > bundled），同时涵盖技能安装、生命周期管理和基本安全实践，是入门技能开发的核心教材
- [OpenClaw 安全加固实践指南（Valletta Software）](https://vallettasoftware.com/blog/post/openclaw-security-2026-best-practices-risks-hardening-guide) - 从 Zero‑Trust 视角系统梳理 OpenClaw 的威胁模型，并给出 TLS/网络分段、容器加固、RBAC、提示注入防御、日志与审计等一整套“企业级”安全加固清单

## 入门文献

- [Getting Started – Install OpenClaw and Run Your First Assistant](https://github.com/openclaw/openclaw/blob/main/docs/start/getting-started.md) (以“5 分钟搭建个人 AI 助手”为目标，从 Node 环境检查、全局安装 openclaw CLI，到运行 openclaw onboard --install-daemon 与启动 Gateway 的全过程示例)
- [OpenClaw Docs – Architecture & Quickstart](https://docs.openclaw.ai/) (概述“自托管 Gateway + 多通道 + Agent‑native + 开源”的设计理念，解释 Gateway 作为单一事实来源的作用)
- [OpenClaw README – Technical Overview & Installation](https://github.com/openclaw/openclaw/blob/main/README.md) (给出技术概览（多通道收发、浏览器控制、Canvas、语音唤醒、Nodes 等），列出核心子系统（Gateway WS 网络、Tailscale 暴露、Browser 控制、Canvas+A2UI、Voice、Onboard+Skills 等）)
- [OpenClaw Tutorial for Beginners – Setup, Workflows and More（视频）​](https://www.youtube.com/watch?v=0AmL_4s6wKo) (面向零基础用户的完整视频教学，从基础安装、通道接入，到设置简单工作流与技能调用，有直观演示。)
- [OpenClaw Full Tutorial for Beginners – freeCodeCamp](https://www.freecodecamp.org/news/openclaw-full-tutorial-for-beginners/) (由 freeCodeCamp 推出的系统入门文章+视频课程，结合代码示例讲解如何构建“本地自动化助手”，从安装到实战案例（如自动整理文件、推送提醒、代码生成等）。)
- [What are OpenClaw Skills? – A 2026 Developer’s Guide](https://www.digitalocean.com/resources/articles/what-are-openclaw-skills) (虽然偏向开发者，但内容从“什么是 Skill”开始，解释 SKILL.md 格式、技能目录结构、安装与加载优先级，对理解整个平台可扩展性非常关键。)

## 进阶文献

- [Reference Architecture: OpenClaw (Early Feb 2026 Edition, Opus 4.6)](https://robotpaper.ai/reference-architecture-openclaw-early-feb-2026-edition-opus-4-6/) (全面拆解 OpenClaw 的核心组件：Gateway Daemon、Channel Bridges、Agent Runtime（pi‑mono）、工具系统、记忆系统、Session 管理、子 Agent 机制、Hooks & Plugins、Sandboxing 与安全分层等)
- [Uncovering Security Threats and Architecting Defenses in Autonomous Agents: A Case Study of OpenClaw（arXiv 2603.12644）](https://arxiv.org/abs/2603.12644) (首篇以 OpenClaw 为主案例的系统安全研究论文，提出“三层风险分类”（AI & Cognitive Security、Software & Execution Security、Information & System Security），归纳提示注入驱动 RCE、顺序工具链攻击、上下文遗忘（context amnesia）、供应链污染等风险)
- [OpenClaw Security in 2026: Best Practices, Risks, and Hardening Guide](https://vallettasoftware.com/blog/post/openclaw-security-2026-best-practices-risks-hardening-guide) (从工程实践视角详细列出：TLS/传输安全、零信任网络分段、容器与主机加固、RBAC 角色模型、提示注入与数据投毒防御模式、日志与告警策略、审计与 incident runbook 等具体控制措施)
- [OpenClaw AI: Security Risks, Architecture – PDF Brief](https://www.scribd.com/document/1012257396/OpenClaw-AI-Security-Risks-Architecture) (总结 OpenClaw 的整体架构与主要安全风险，覆盖 CVE‑2026‑25253、技能供应链攻击、记忆泄露、提示注入等关键问题。)
- [OpenClaw as Language Infrastructure: A Case‑Centered Survey of Agent Ecosystem](https://www.preprints.org/manuscript/202603.1060) (以 OpenClaw–Moltbook 生态为中心，梳理 38 篇与 OpenClaw 相关的论文与报告，总结其在智能体社会、轨迹审核、安全实验、分布式协作中的角色)
- [OpenClaw‑RL: AI Agent Is Throwing Away Its Best Training Data](https://pub.towardsai.net/openclaw-rl-ai-agent-is-throwing-away-its-best-training-data-409a87775dad) (探讨如何利用 OpenClaw 的交互轨迹进行在线/离线强化学习，通过恢复用户重试、改写等隐式反馈作为训练信号，让 Agent“边用边学”)

## 相关文献



## 结语

给出一条**可执行的学习与研究路径**：

1. 入门阶段（目标：能在本机跑起来并完成简单自动化）

- **按顺序阅读并实践**：
1）OpenClaw Docs 首页[1] → 2）Getting Started 指南[1][2] → 3）GitHub README[2]
2. 在本机安装 Node 22.16+/24，运行 openclaw onboard，成功连通一个聊天通道（如 Telegram）。
- **完成第一个小项目**：

- 例如：

- 让 OpenClaw 自动归档每天的聊天摘要写入 memory/YYYY‑MM‑[DD.md](http://DD.md)；
- 通过一个简单技能实现“定时总结 GitHub issue”并推送到 Telegram。

- **初步理解技能机制**：

- 阅读《What are OpenClaw Skills?》[5]，尝试安装 1~2 个 ClawHub 上的热门技能，并在本地测试其行为。

2. 进阶阶段（目标：理解内部工作原理，能安全地做定制开发）

- **深入架构与记忆系统**：

- 通读 Reference Architecture 文档[3]，重点理解：

- Gateway/WS 协议、Channel Bridges 如何统一事件；
- Memory 四层架构与向量检索管线（Markdown → chunk → embedding → SQLite + BM25）；
- Session 键路由规则与子 Agent 机制。

- **开始自定义技能与插件**：

- 依据 Skills 文档与相关教程[4][5]，编写 [SKILL.md](http://SKILL.md) + 脚本的自定义技能；
- 尝试使用 Hooks/Plugins 实现日志记录、审计、自动健康检查等。

- **实践安全加固**：

- 按 Valletta 的安全指南逐条检查：TLS、Zero‑Trust 分段、非 root 容器、RBAC 与审批门、提示注入防御（工具调用策略验证）等[6]。
- 为敏感环境启用 Docker Sandbox，并为高风险工具配置“人工确认+审计日志”。

3. 研究与创新阶段（目标：以 OpenClaw 为平台开展 agentic 研究或产品化）

- **深读安全与生态研究文献**：

- 认真阅读 arXiv 2603.12644 论文，理解“三层风险分类”和 FASA 架构，并尝试在自己的 OpenClaw 部署中部分复现或实现 ClawGuard 思路[7]。
- 结合“OpenClaw as Language Infrastructure”[6]，了解当前围绕 OpenClaw 的研究热点：安全性测试、Agent 社区、轨迹分析等。

- **在 OpenClaw 上做实验或产品验证**：

- 例：

- 基于 OpenClaw‑RL 思路，收集用户交互数据，进行在线策略优化；
- 构建特定行业（如医疗、法律、运维）的“多 Agent 协同助手”，并制定相应安全策略与合规审计流程。

- **参与社区与标准建设**：

- 关注 ClawHub 技能供应链治理，尝试为技能生态贡献“安全基线”“质量标准”；
- 在团队和社区中推广诸如 FASA 这样的全生命周期安全框架，推动形成智能体安全标准。
