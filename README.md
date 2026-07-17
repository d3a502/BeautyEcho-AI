# BeautyEcho AI / 妆声引擎 AI

**面向逸仙集团的美妆社媒洞察与内容策略闭环系统**

> 听见用户回响，看见美妆趋势。

## 当前阶段

本仓库目前是报名阶段的研究基础包，不是完整产品实现。我们先完成三件事：

1. 梳理美妆社媒传播与内容策略优化的背景。
2. 搜集可用于用户反馈分析的公开美妆数据集。
3. 搭建基础机器学习与可视化分析流程，为后续飞书 AI + 多 Agent 方案提供数据依据。

## 项目问题

逸仙集团命题关注“基于 AI 的美妆社交媒体传播分析与内容策略优化”。这类问题不能只做文案生成，而需要先理解用户真实反馈、竞品内容打法、平台热门表达和产品卖点之间的关系。

BeautyEcho AI 将全网美妆声量视为品牌需要持续捕捉的“妆声”，目标是将社媒趋势、用户评论、竞品内容和投放反馈转化为可执行、可复盘的内容策略。

## 研究路线

```text
公开美妆评论/产品数据
-> 数据清洗与 EDA
-> 用户反馈主题聚类
-> 评分/满意度预测 baseline
-> 可视化洞察
-> 内容策略闭环方案
```

## 仓库结构

```text
research/     背景研究、公开数据集、参考资料
data/         数据说明与小样例
analysis/     基础 EDA、聚类、预测脚本
outputs/      图表与初步发现
proposal/     轻量概念说明
```

## 当前可运行内容

使用仓库内的小样例数据运行：

```bash
pip install -r requirements.txt
python analysis/01_sample_eda.py
python analysis/02_topic_clustering.py
python analysis/03_rating_prediction.py
```

输出图表会生成到：

```text
outputs/figures/
```

## 数据说明

当前仓库不直接上传大型公开数据集，只记录数据来源与使用方式。后续可基于公开数据集进行抽样分析：

- Amazon Reviews 2023: Beauty and Personal Care / All Beauty
- Sephora Products and Skincare Reviews
- Cosmetics Ingredients Dataset

详见：

```text
research/public_datasets.md
```

## 合规说明

本仓库不包含命题企业内部数据，不包含未经授权的社媒平台大规模抓取数据，不声称已接入真实平台全量数据。当前脚本使用小样例数据验证分析流程；公开数据集将在符合其使用条款的前提下用于研究与演示。

