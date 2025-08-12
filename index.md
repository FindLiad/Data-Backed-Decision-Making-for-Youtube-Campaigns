---
layout: default
title: Data-Backed Decision Making for YouTube Campaigns
---

# Data-Backed Decision Making for YouTube Campaigns

A marketer-facing dashboard to **identify high-ROI YouTube channels** for brand collaborations using clean, comparable metrics.

- 🔗 **Live Dashboard (Tableau Public):** https://public.tableau.com/app/profile/liad.mizrachi/viz/YoutubeVisualization_17550201203060/Dashboard1?publish=yes  
- 📦 **Repository:** https://github.com/FindLiad/Data-Backed-Decision-Making-for-Youtube-Campaigns

---

## Summary
A productized analytics workflow that lets marketing leaders **rank, screen, and shortlist** UK YouTube channels using **Subscribers, Videos, Views, Avg Views, Engagement Ratio, and Views per Subscriber**. Built to replace ad-hoc searches and expensive third-party lists with **transparent, reproducible, and explainable** decision criteria.

---

## Overview (PM framing)
The original tutorial shipped a similar dashboard with **Microsoft SQL Server + Power BI**.  
I **rebuilt the entire workflow on macOS** using **Azure Data Studio (SQL)** and **Tableau**, keeping the core idea but emphasizing **product requirements, acceptance criteria, data quality checks, and success metrics**. This repo includes the **PRD**, reproducible SQL/data prep, the Tableau workbook, and final assets, so the decision logic is **auditable and maintainable**.

- **Source → Transform → Validate → Visualize → Decide**
- Clear **“why”** (Problem & Success Criteria), **“what”** (Use Cases & AC), and **“how”** (Data, Checks, Scripts, Viz).

---

## Key Features
- **Top Channel Ranking:** Sort and filter by Subscribers, Videos, Views, Avg Views/Video, Engagement Ratio, Views per Subscriber.  
- **KPI Tiles:** Fast at-a-glance metrics (Avg Views per Video, Engagement Ratio, Views per Subscriber).  
- **Top-N Controls:** Show Top 10 / Top 20 channels for focused evaluation.  
- **Treemap & Bars:** Visual dominance and distribution (e.g., long-tail awareness vs. head creators).  
- **Shortlisting Workflow:** Screen → compare → annotate candidates for **campaign planning**.  
- **Data Quality Guardrails:** Row/column counts, types, and duplicate checks baked into prep.

---

## Screenshots
![Dashboard](Images/dashboard.png)
*Primary Tableau dashboard.*

![Mock](Images/dashboard_mock.png)
*Initial concept mock and layout exploration.*

---

## Use Cases & Acceptance Criteria (from PRD)
**Use Case 1 — Identify creators to collaborate with**  
- _AC:_ List top channels by the metrics above, allow simple sorting/filtering, and use the most recent dataset.

**Use Case 2 — Assess campaign potential**  
- _AC:_ Provide decision inputs for campaign types (product placement, sponsored series, influencer content) via **reach (subs/views)**, **engagement signals**, and **estimated impact**.

**Success Criteria**  
- VP of Marketing can quickly:  
  1) Identify top candidates,  
  2) Understand expected reach/engagement tradeoffs,  
  3) Make **defensible, data-backed** collaboration choices.

---

## Data & Files
- **Raw data:** [`Assets/Data/raw_youtube_data.csv`](Assets/Data/raw_youtube_data.csv)  
- **Final dataset:** [`Assets/Data/final_youtube_data.csv`](Assets/Data/final_youtube_data.csv)  
- **SQLite DB (optional):** [`Assets/Data/youtube.db`](Assets/Data/youtube.db)  
- **Tableau workbook:** [`Visualizations/Youtube_Visualization.twb`](Visualizations/Youtube_Visualization.twb)  
- **Script (prep):** [`Scripts/prep_youtube_uk.py`](Scripts/prep_youtube_uk.py)  
- **PRD (PDF):** [`Docs/Product_Requirements_Document.pdf`](Docs/Product_Requirements_Document.pdf)

---

## How to Run (Reproduce Locally)
1. **Clone** this repo.  
2. Open SQL scripts / data in **Azure Data Studio** (or your SQL tool of choice).  
3. Use `final_youtube_data.csv` as your Tableau source (or connect to `youtube.db`).  
4. Open `Visualizations/Youtube_Visualization.twb` in **Tableau**.  
5. Optional: Publish to **Tableau Public**, then set the dashboard link in this page.

---

## Decision Inputs (Explained)
- **Avg Views per Video** — recency-adjusted performance proxy.  
- **Engagement Ratio** — comments/likes/views (or your available proxy) to gauge audience responsiveness.  
- **Views per Subscriber** — measures content pull beyond base audience.  
- **Volume (Videos)** — throughput and consistency signal.  
- **Reach (Subscribers, Total Views)** — upper bound on campaign awareness.

> These metrics provide a **balanced scorecard** (reach × responsiveness) suitable for **screening** and **prioritization**. Final campaign selection can add price and brand-fit.

---

## Data Quality Checks (Guardrails)
- **Row/Column Count Check**  
- **Type Validation** (ints, strings expected)  
- **Duplicates** on channel identifiers  
- **Null / missing value scan**  
Documented in prep steps and validated before visualization.

---

## PM Notes (Why this improves decisions)
- Reduces decision **cycle time** and **ad-hoc** channel scouting.  
- Makes inputs **comparable and transparent** for stakeholders (Marketing, Analytics, Product).  
- Enables **repeatable** monthly refreshes with the same checks and viz, improving longitudinal learning.

---

## Tech
**SQL (Azure Data Studio)** · **Tableau** · **CSV/SQLite** · **GitHub Pages**

---

## Credits & License
Based on a public learning project reimagined with a macOS toolchain and a product-requirements lens.  
© Liad Mizrachi. All rights reserved unless otherwise stated.
