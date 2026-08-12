# Task 1 — Web Scraping

## Objective
Collect web-based information related to paper leaks in India and convert HTML into structured data.

## Source
India Today article: "India saw 65 exam paper leaks since 2019: Data analysis".

The article states that its analysis was based on public records and media reports and covered 64 major exams across 19 states plus NEET-UG 2024.

## Tools
Requests, BeautifulSoup, Pandas.

## Output
`paper_leak_web_source.csv`

## Run
```powershell
pip install -r requirements.txt
python task1_paper_leak_web_scraping.py
```

The supplied `Paper_leaks_India(3).csv` remains the main structured dataset for Tasks 2 and 3.
