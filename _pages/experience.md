---
layout: page
title: "工程实践"
permalink: /experience/
lang: zh-CN
alternate_url: /en/experience/
nav: false
---

<link rel="stylesheet" href="{{ '/assets/css/profile.css' | relative_url }}">
<div class="profile-content">
<section class="entry has-media" id="materials"><img class="entry-media" src="{{ '/assets/img/202207061457495.png' | relative_url }}" alt="稀土材料知识图谱与数据库" loading="lazy" decoding="async"><h3>国家重点研发计划：稀土催化材料知识图谱与全流程数字研发平台</h3><div class="meta">2021.09–2024.08 · 课题助理</div><ul class="project-points"><li>主导数据库与材料知识图谱构建，全程参与项目从申报到验收的完整落地，确保各阶段交付物按期通过评审。</li><li>设计并构建规模达 10^5 级别的多模态材料数据库，包含 46,701 条合成条件，整合多源异构数据。</li><li>将知识图谱应用于合成条件推荐与知识发现，支撑材料智能化研发流程。</li></ul><div class="entry-links"><a href="https://gitee.com/sun__ye/mofs-kg">代码 ↗</a></div></section>
<section class="entry has-media" id="geneticflow"><img class="entry-media" src="{{ '/assets/img/图片2.png' | relative_url }}" alt="GeneticFlow 学术文献可视化" loading="lazy" decoding="async"><h3>大规模学术文献可视化分析系统 GeneticFlow V2.0</h3><div class="meta">2023.09–2025.09 · 算法研究、软件开发、运维</div><ul class="project-points"><li>主导研发面向百万级学者学术文献的多维度可视化分析系统，设计并实现图布局计算与可视交互一体化方案；系统上线后累计服务全球 110,419 名用户，支撑 540,440 次访问，并获得软件著作权登记。</li><li>从 Graphviz C++ 源码编译浏览器端布局组件，打通图布局计算与前端可视交互链路，独立完成前后端开发与系统运维。</li><li>著名 ACM Fellow Ion Stoica 评价：“This is interesting, especially the visualization”。</li></ul><div class="entry-links"><a href="https://github.com/visdata/GeneticPrism">代码 ↗</a></div></section>
<section class="entry has-media" id="itas"><img class="entry-media" src="{{ '/assets/img/图片1.png' | relative_url }}" alt="ITAS 智能文本标注系统" loading="lazy" decoding="async"><h3>软件工程课程项目：多领域智能文本标注与挖掘系统（ITAS）</h3><div class="meta">2024.03–2025.01 · 产品经理、软件开发</div><ul class="project-points"><li>负责需求分析、产品规划与系统实现。ITAS 是面向科研文献的多领域智能文本标注与信息抽取系统。</li><li>支持 PDF 批量上传、段落与实体标注、审核、模型导出，并通过大语言模型与 few-shot 学习提取预设信息。</li><li>系统应用于大规模材料文献抽取，构建 BM25 + RAG few-shot 抽取流程，输出前驱体、用量和合成条件的结构化 JSON；三个 MOF 数据集 macro-F1 达 0.94，相比于 zero-shot 0.77 提升 32.9%。</li></ul><div class="entry-links"><a href="https://github.com/cs-anonymous/ITAS">代码 ↗</a></div></section>
<section class="entry has-media" id="classification"><img class="entry-media" src="{{ '/assets/img/screenshot-20261011-131013.png' | relative_url }}" alt="数据分类分级系统" loading="lazy" decoding="async"><h3>校企合作项目：基于深度科研智能体的数据分类分级</h3><div class="meta">2024.12–2025.05 · 架构设计、软件开发</div><ul class="project-points"><li>主导研发基于 LLM 的实体识别技术工具，构建 RAG 驱动的数据分类分级体系，实现敏感数据的自动标注与动态优化。</li><li>支持样本库、分类标准、项目、任务和环境管理，包含提示词生成、模型接口、RAG、结果处理和性能评价 5 个核心模块。</li><li>面向钢铁生产、教育等多个领域，数据库规模超过 10 万条。团队获评北京航空航天大学人工智能领域十大优秀团队称号。</li></ul><div class="entry-links"><a href="https://gitee.com/sun__ye/ler">代码 ↗</a></div></section>
<section class="entry has-media" id="materagent"><img class="entry-media" src="{{ '/assets/img/screenshot-20261011-125317.png' | relative_url }}" alt="MaterAgent MCP 工具链" loading="lazy" decoding="async"><h3>MaterAgent：面向材料研发全流程的 Agent Harness</h3><div class="meta">2026.03–至今 · 软件开发 · 新材智脑 / MaterBrain</div><ul class="project-points"><li>参与新材智脑的产学研合作项目，推动智能体运行支撑框架与配套工具在材料研发流程中的落地应用。深入理解 PI-Agent 框架与核心技术，梳理 agent loop、runtime、plugin 和智能体生命周期，参与材料研发全流程 Agent Harness 架构设计。</li><li>设计并开发 MCP 工具：Paper Browser 支持按 DOI、标题或正文检索论文，并读取论文或章节中的段落、表格等证据；Database MCP 面向材料研发数据库提供结构化查询与 BM25、dense 双路检索，返回排序记录、检索分数和元数据。</li><li>构建覆盖 10 个任务共 100 题的材料 QA benchmark，涵盖单条查询、条件筛选与排序、工艺归纳、论文取证和机理分析。</li></ul><div class="entry-links"><a href="https://lab.materialbrain.com/materialbrain/material-agent">代码 ↗</a></div></section>

</div>
