# Data-Backed Decision Making for YouTube Campaigns

A marketer-facing dashboard to **identify high-ROI YouTube channels** for brand collaborations using clean, comparable metrics.

- 🔗 **Live Dashboard (Tableau Public):**  
  [Live Dashboard](https://public.tableau.com/app/profile/liad.mizrachi/viz/YoutubeVisualization_17550201203060/Dashboard1?publish=yes)

- 📦 **Repository:**  
  [GitHub Repo](https://github.com/FindLiad/Data-Backed-Decision-Making-for-Youtube-Campaigns)

---

## A time I went above and beyond to deliver for the customer

<div class="story-grid">

  <!-- Row 1: CONTEXT (copy left, image right) -->
  <div class="story-row">
    <div class="story-copy">
      <h3>Context</h3>
      <p>
        A brand agency needed to decide—fast—which YouTube creators could move the needle for an upcoming campaign.<br><br>
        The data existed (subscribers, views, video counts) but lived in scattered exports that told different stories. Decisions were slow, debates were subjective, and every day lost meant missed reach.<br><br> 
        Even though it sat outside my formal scope, I stepped in to productize the process.<br><br>
        The goal was one enterprise-ready dashboard
        that turned messy inputs into a clear, explainable short-list of creators.
      </p>
    </div>
    <figure class="story-img-wrap">
      <img class="story-img"
           src="/Data-Backed-Decision-Making-for-Youtube-Campaigns/assets/images/story-context.png"
           alt="Context scene: scattered spreadsheets and subjective debates">
    </figure>
  </div>

  <!-- Row 2: ACTION (image left, copy right) -->
  <div class="story-row rev">
    <figure class="story-img-wrap">
      <img class="story-img"
           src="/Data-Backed-Decision-Making-for-Youtube-Campaigns/assets/images/story-action.png"
           alt="Action scene: SQL/Python cleanup, Tableau build, prioritization by impact">
    </figure>
    <div class="story-copy">
      <h3>Action</h3>
      <p>
        I built an interactive analytics dashboard end-to-end: light Python to clean and normalize CSVs, then Tableau
        to surface defensible KPIs (Avg Views per Video, Views per Subscriber, reach consistency).<br><br> 
        Instead of boiling the ocean, I prioritized fixes by business impact—cleaning high-value channels first so the team could move
        immediately. 
        <br><br>I added guardrails (type checks, dedupes) and a simple refresh path: replace CSV → run <i>prep_youtube_uk.py</i> → open dashboard.
      </p>
    </div>
  </div>

  <!-- Row 3: RESULT (copy left, image right) -->
  <div class="story-row">
    <div class="story-copy">
      <h3>Result</h3>
      <p>
        The team shifted from subjective debates to transparent, comparable metrics. Shortlisting creators went from
        hours of manual sifting to a repeatable workflow that explained <i>why</i> each pick made sense. 
        <br><br>Stakeholders saw the same truth: clear rankings, clean inputs, and a one-click path to refresh when new data arrived.
        <br><br>The dashboard became the standard for campaign planning and unlocked faster, higher-confidence decisions.
      </p>
    </div>
    <figure class="story-img-wrap">
      <img class="story-img"
           src="/Data-Backed-Decision-Making-for-Youtube-Campaigns/assets/images/story-result.png"
           alt="Result scene: stakeholders aligning on a defensible short-list">
    </figure>
  </div>

</div>

<div align="right"><a href="#site-top">↑ Back to top</a></div>

---

## Table of Contents
- [Objective & Success Criteria](#objective--success-criteria)
- [What I Built & Why](#what-i-built--why)
- [End-to-End Walkthrough](#end-to-end-walkthrough)
  - [1) Data In](#1-data-in)
  - [2) Clean & Normalize (Python)](#2-clean--normalize-python)
  - [3) Guardrails (Data Quality Checks)](#3-guardrails-data-quality-checks)
  - [4) Derive Metrics](#4-derive-metrics)
  - [5) Visualize in Tableau](#5-visualize-in-tableau)
  - [6) Publish & Share](#6-publish--share)
- [Design Notes](#design-notes)
- [Results (Screenshots)](#results-screenshots)
- [Files & Folders](#files--folders)
- [How to Reproduce](#how-to-reproduce)
- [Limitations & Next Steps](#limitations--next-steps)
- [Credits](#credits)

---

## Objective & Success Criteria
**Problem:** Scouting YouTube creators is slow and subjective.  
**Objective:** Ship a repeatable workflow that surfaces high-potential UK channels for brand collabs.

**Success Criteria**
1. Rank channels by comparable KPIs (reach, consistency, responsiveness).
2. Explain *why* a channel is shortlisted (transparent inputs).
3. Refresh quickly when new data arrives.

<div align="right"><a href="#site-top">↑ Back to top</a></div>

---

## What I Built & Why
- A **single CSV-based pipeline** (no databases to set up).  
- A small **Python prep script** to clean/normalize inputs and write a **final CSV** for visualization.  
- A **Tableau dashboard** that surfaces top channels across KPIs with simple, defensible calculations.  
- A **GitHub Pages site** (this page) that documents assumptions, steps, and outcomes.

**Why this approach?** It’s **fast, portable, and auditable**—teams can open the script, CSVs, and workbook to understand exactly how rankings are produced.

<div align="right"><a href="#site-top">↑ Back to top</a></div>

---

## End-to-End Walkthrough

### 1) Data In
- **Raw input:** `/Data-Backed-Decision-Making-for-Youtube-Campaigns/assets/data/raw_youtube_data.csv`  
  Columns of interest: `channel_name`, `subscribers`, `total_views`, `videos` (+ optional engagement fields if available).

### 2) Clean & Normalize (Python)
- Script: `/Data-Backed-Decision-Making-for-Youtube-Campaigns/scripts/prep_youtube_uk.py`  
- Output: `/Data-Backed-Decision-Making-for-Youtube-Campaigns/assets/data/final_youtube_data.csv`

**What the script does (at a glance):**
- trims `channel_name`
- coerces numeric types (`subscribers`, `total_views`, `videos`)
- drops unused columns
- handles empties/nulls with simple rules (drop or fill where safe)
- writes **final_youtube_data.csv**

### 3) Guardrails (Data Quality Checks)
Before visualizing, I run a few quick checks (baked into the script/notebook or run ad-hoc):
- **Row count** — expected volume present  
- **Column & type sanity** — integers where expected, text for names  
- **Duplicates** — no duplicate `channel_name` rows

### 4) Derive Metrics
All metrics are either precomputed in Python or calculated in Tableau:

- **Avg Views per Video** = `total_views / videos` (0-safe)  
- **Views per Subscriber** = `total_views / subscribers` (0-safe)  
- **Engagement Ratio (proxy)** = based on available fields; if likes/comments aren’t present, omit or mark as N/A.

These create a **balanced scorecard**: reach (subs/views) × responsiveness (engagement/efficiency).

### 5) Visualize in Tableau
- Workbook: `/Data-Backed-Decision-Making-for-Youtube-Campaigns/visualizations/Youtube_Visualization.twbx`  
- Data source: `/Data-Backed-Decision-Making-for-Youtube-Campaigns/assets/data/final_youtube_data.csv`

**Dashboard Components**
- Top-N lists by each KPI (subscribers, views, videos, avg views/video, views/subscriber).  
- KPI tiles for quick scanning.  
- Treemap/bars for distribution and dominance.  
- Controls to toggle Top 10/Top 20, simple filtering.

### 6) Publish & Share
- Published to **Tableau Public**, linked at the top of this page.  
- Repo includes raw/clean CSVs, the script, the workbook, and this write-up so the logic is **inspectable and reproducible**.

<div align="right"><a href="#site-top">↑ Back to top</a></div>

---

## Design Notes
- **Why these KPIs?** They balance *scale* (subs/views) and *performance* (avg views, views/sub).  
- **Why CSV pipeline?** Lightweight, easy for non-engineers, zero infra.  
- **Why Tableau?** Fast iteration and simple publishing for stakeholders.

<div align="right"><a href="#site-top">↑ Back to top</a></div>

---

## Results (Screenshots)

<figure class="centered-figure">
  <a href="/Data-Backed-Decision-Making-for-Youtube-Campaigns/assets/images/mockup-dashboard.png" target="_blank" rel="noopener">
    <img src="/Data-Backed-Decision-Making-for-Youtube-Campaigns/assets/images/mockup-dashboard.png" alt="Mock Up">
  </a>
  <figcaption>Mock Up</figcaption>
</figure>

<figure class="centered-figure">
  <a href="/Data-Backed-Decision-Making-for-Youtube-Campaigns/assets/images/finished-dashboard.png" target="_blank" rel="noopener">
    <img src="/Data-Backed-Decision-Making-for-Youtube-Campaigns/assets/images/finished-dashboard.png" alt="Final Interface">
  </a>
  <figcaption>Final Interface</figcaption>
</figure>

<div align="right"><a href="#site-top">↑ Back to top</a></div>

---

## Files & Folders
- **Raw data:**  
  [/Data-Backed-Decision-Making-for-Youtube-Campaigns/assets/data/raw_youtube_data.csv](/Data-Backed-Decision-Making-for-Youtube-Campaigns/assets/data/raw_youtube_data.csv)
- **Final dataset:**  
  [/Data-Backed-Decision-Making-for-Youtube-Campaigns/assets/data/final_youtube_data.csv](/Data-Backed-Decision-Making-for-Youtube-Campaigns/assets/data/final_youtube_data.csv)
- **Prep script:**  
  [/Data-Backed-Decision-Making-for-Youtube-Campaigns/assets/scripts/prep_youtube_uk.py](/Data-Backed-Decision-Making-for-Youtube-Campaigns/assets/scripts/prep_youtube_uk.py)
- **Tableau workbook:**  
  [/Data-Backed-Decision-Making-for-Youtube-Campaigns/assets/visualizations/Youtube_Visualization.twbx](/Data-Backed-Decision-Making-for-Youtube-Campaigns/assets/visualizations/Youtube_Visualization.twbx)
- **PRD:**  
  [/Data-Backed-Decision-Making-for-Youtube-Campaigns/assets/docs/Product_Requirements_Document.pdf](/Data-Backed-Decision-Making-for-Youtube-Campaigns/assets/docs/Product_Requirements_Document.pdf)

<div align="right"><a href="#site-top">↑ Back to top</a></div>

---

## How to Reproduce
1. **Clone** this repo.  
2. Run `scripts/prep_youtube_uk.py` (writes `assets/data/final_youtube_data.csv`).  
3. Open `visualizations/Youtube_Visualization.twbx` in **Tableau** and point it at `assets/data/final_youtube_data.csv`.  
4. Explore the dashboard; publish to Tableau Public if desired.  
5. To refresh later: replace `raw_youtube_data.csv` → re-run script → open workbook (data updates).

<div align="right"><a href="#site-top">↑ Back to top</a></div>

---

## Limitations & Next Steps
- Engagement details (likes/comments) may be missing; **Engagement Ratio** is a placeholder when fields aren’t available.  
- Add **recency weighting** or **growth trends** (subs/view velocity).  
- Introduce **cost data** to estimate **ROI** (views × conv. rate × margin − fee).  
- Optional: creator **categories/verticals** to filter comparisons.

<div align="right"><a href="#site-top">↑ Back to top</a></div>

---

## Credits
Concept inspired by a public learning project; this version uses a **CSV-only pipeline** with **Python + Tableau**, documented for product stakeholders.  
© Liad Mizrachi.

<div align="right"><a href="#site-top">↑ Back to top</a></div>
