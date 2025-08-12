
## Overview

📊 **Tableau dashboard + SQL data prep** to help marketing teams identify the most impactful UK YouTube channels for brand collaborations.

- 🔗 **Live Dashboard:** [View on Tableau Public](https://public.tableau.com/app/profile/liad.mizrachi/viz/YoutubeVisualization_17550201203060/Dashboard1?publish=yes)
- 🌐 **Project Page (themed):** [View on GitHub](https://github.com/FindLiad/Data-Backed-Decision-Making-for-Youtube-Campaigns)

## Summary
This project rebuilds a YouTube analytics dashboard originally designed with Microsoft SQL Server & Power BI — but re-implemented entirely on macOS using **Azure Data Studio (SQL)** and **Tableau**.  
It includes the **Product Requirements Document (PRD)**, reproducible data prep scripts, quality checks, and the final Tableau workbook.

```
Assets/
Data/ # Raw & cleaned CSVs, SQLite DB
Images/ # Dashboard & mockup PNGs
Docs/
Product_Requirements_Document.pdf
Scripts/
prep_youtube_uk.py # Data prep script
Visualizations/
Youtube_Visualization.twb
```

## How to Run
1. Clone this repo.
2. Open `Scripts/prep_youtube_uk.py` in **Azure Data Studio** or any Python-capable SQL IDE.
3. Use `Assets/Data/final_youtube_data.csv` as the Tableau source (or connect to `Assets/Data/youtube.db`).
4. Open `Visualizations/Youtube_Visualization.twb` in **Tableau**.
5. Optional: publish to Tableau Public.

## Tech
SQL · Tableau · Azure Data Studio · CSV/SQLite

---
© Liad Mizrachi

