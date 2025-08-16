# Data-Backed Decision Making for YouTube Campaigns

A marketer-facing dashboard to **identify high-ROI YouTube channels** for brand collaborations using clean, comparable metrics.

- 🔗 **Live Dashboard (Tableau Public):**  
  [Live Dashboard](https://public.tableau.com/app/profile/liad.mizrachi/viz/YoutubeVisualization_17550201203060/Dashboard1?publish=yes)

- 📦 **Repository:**  
  [GitHub Repo](https://github.com/FindLiad/Data-Backed-Decision-Making-for-Youtube-Campaigns)

---

## Summary
A productized analytics workflow that lets marketing leaders **rank, screen, and shortlist** UK YouTube channels using **Subscribers, Videos, Views, Avg Views, Engagement Ratio, and Views per Subscriber**.  
Built to replace ad-hoc searches and expensive third-party lists with **transparent, reproducible, and explainable** decision criteria.

---

## Overview (PM framing)
The original tutorial shipped a similar dashboard with **Microsoft SQL Server + Power BI**.  
I **rebuilt the entire workflow on macOS** using **Azure Data Studio (SQL)** and **Tableau**, keeping the core idea but emphasizing **product requirements, acceptance criteria, data quality checks, and success metrics**.  
This repo includes the **PRD**, reproducible SQL/data prep, the Tableau workbook, and final assets, so the decision logic is **auditable and maintainable**.

- **Source → Transform → Validate → Visualize → Decide**
- Clear **“why”** (Problem & Success Criteria), **“what”** (Use Cases & AC), and **“how”** (Data, Checks, Scripts, Viz).

---

## Key Features
- **Top Channel Ranking:** Sort and filter by Subscribers, Videos, Views, Avg Views/Video, Engagement Ratio, Views per Subscriber.  
- **KPI Tiles:** At-a-glance metrics (Avg Views per Video, Engagement Ratio, Views per Subscriber).  
- **Top-N Controls:** Show Top 10 / Top 20 channels for focused evaluation.  
- **Treemap & Bars:** Visual dominance and distribution (long-tail vs. head creators).  
- **Shortlisting Workflow:** Screen → compare → annotate candidates for **campaign planning**.  
- **Data Quality Guardrails:** Row/column counts, types, and duplicate checks baked into prep.

---

## UI/UX
- **Mock Up**  
  <a href="/Data-Backed-Decision-Making-for-Youtube-Campaigns/assets/images/dashboard_mock.png" target="_blank" rel="noopener">
    <img src="/Data-Backed-Decision-Making-for-Youtube-Campaigns/assets/images/dashboard_mock.png" alt="Mockup">
  </a>

- **Final Interface**  
  <a href="/Data-Backed-Decision-Making-for-Youtube-Campaigns/assets/images/dashboard.png" target="_blank" rel="noopener">
    <img src="/Data-Backed-Decision-Making-for-Youtube-Campaigns/assets/images/dashboard.png" alt="Dashboard">
  </a>

---

## Use Cases & Acceptance Criteria (from PRD)
**Use Case 1 — Identify creators to collaborate with**  
- _AC:_ List top channels by the metrics above, allow simple sorting/filtering, and use the most recent dataset.

**Use Case 2 — Assess campaign potential**  
- _AC:_ Provide decision inputs for campaign types (product placement, sponsored series, influencer content) via **reach (subs/views)**, **engagement signals**, and **estimated impact**.

**Success Criteria**  
- VP of Marketing can quickly:  
  1) Identify top candidates,  
  2) Understand expected reach/engagement trad
