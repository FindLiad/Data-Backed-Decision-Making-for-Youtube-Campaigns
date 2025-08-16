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

[![Mock](images/dashboard_mock.png)](images/dashboard_mock.png)

- **Final Interface**

[![Dashboard](images/dashboard.png)](images/dashboard.png)

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
- **Raw data:** [`data/raw_youtube_data.csv`](data/raw_youtube_data.csv)  
- **Final dataset:** [`data/final_youtube_data.csv`](data/final_youtube_data.csv)  
- **SQLite DB (optional):** [`data/youtube.db`](data/youtube.db)  
- **Tableau workbook:** [`visualizations/Youtube_Visualization.twb`](visualizations/Youtube_Visualization.twb)  
- **Script (prep):** [`scripts/prep_youtube_uk.py`](scripts/prep_youtube_uk.py)  
- **PRD (PDF):** [`docs/Product_Requirements_Document.pdf`](docs/Product_Requirements_Document.pdf)

---

## How to Run (Reproduce Locally)
1. **Clone** this repo.  
2. Open SQL scripts / data in **Azure Data Studio** (or your SQL tool of choice).  
3. Use `final_youtube_data.csv` as your Tableau source (or connect to `youtube.db`).  
4. Open `visualizations/Youtube_Visualization.twb` in **Tableau**.  
5. (Optional) Publish to **Tableau Public**, then set the dashboard link above.

---

## Decision Inputs (Explained)
- **Avg Views per Video** — recency-adjusted performance proxy.  
- **Engagement Ratio** — comments/likes/views to gauge audience responsiveness.  
- **Views per Subscriber** — measures pull beyond base audience.  
- **Volume (Videos)** — throughput and consistency.  
- **Reach (Subscribers, Total Views)** — upper bound on campaign awareness.
