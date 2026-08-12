# Paper Leaks in India — CodeAlpha Data Analytics Project

## Dataset
`Paper_leaks_India(3).csv`

This project uses ONE dataset/theme throughout all three tasks.

## Tasks
### Task 1 — Web Scraping
Collect paper-leak information from a public web source using:
- Requests
- BeautifulSoup
- Pandas

The scraper extracts article title, date, article text and source URL, then saves
the result as `paper_leak_web_source.csv`.

### Task 2 — Exploratory Data Analysis
Analyze the supplied Paper Leak India dataset:
- dataset shape and data types
- missing values
- duplicate checks
- yearly incidents
- incident areas
- leak confirmation status
- conducting body type
- actions taken
- data-quality observations

### Task 3 — Data Visualization
Create:
- incidents by year
- top incident areas
- confirmation status
- conducting body type vs status
- actions taken
- combined dashboard

## Run
```powershell
pip install -r requirements.txt
python task1_paper_leak_web_scraping.py
python task2_eda.py
python task3_visualization.py
```

## Important
The supplied CSV is the main analysis dataset. Task 1 is a separate web-scraping
activity related to the same Paper Leak India topic. The project does not use the
Books dataset.
