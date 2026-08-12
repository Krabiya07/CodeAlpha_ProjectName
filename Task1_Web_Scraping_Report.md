# TASK 1 — WEB SCRAPING
## Project: Paper Leaks in India

### Objective
Collect paper-leak information from public web sources and convert unstructured
web content into structured data that can be used for analysis.

### Public source used for project research
India Today published an analysis of paper leaks in India based on public records
and media reports. The article reported at least 65 major exam-paper-leak incidents
since 2019.

Source:
https://www.indiatoday.in/india/story/paper-leak-2019-to-2024-analysis-neet-net-nta-exam-cancelled-2558404-2024-06-26

### Web-scraping method
1. `requests` sends an HTTP request to the public article.
2. `BeautifulSoup` parses the returned HTML.
3. The scraper extracts:
   - article title
   - publication date
   - article paragraphs/text
   - source URL
4. `pandas` stores the extracted information in CSV format.

### Supplied Paper Leak India dataset
The supplied `Paper_leaks_India(3).csv` is the project's main structured dataset.
It contains 66 incident records and 11 original columns.

For Task 1, the dataset has been normalized into:
`paper_leaks_web_scraped_dataset.csv`

Fields:
- Date
- Exam_Name
- Conducting_Body
- Conducting_Body_Type
- Incident_Area
- Leak_Status
- Action_Taken
- Action_Notes
- Incident_Notes
- Source_URL

### Important distinction
The supplied CSV is a structured dataset, not an HTML web page. Therefore, it would
be misleading to claim that all 66 rows were scraped directly from a website.

The project includes a REAL reproducible web-scraping script:
`task1_paper_leak_web_scraping.py`

Run it in VS Code/PowerShell to scrape the public India Today article.

### Installation
```powershell
pip install -r task1_requirements.txt
```

### Run
```powershell
python task1_paper_leak_web_scraping.py
```

### Task 1 deliverables
- `task1_paper_leak_web_scraping.py`
- `paper_leak_web_source.csv`
- `paper_leaks_web_scraped_dataset.csv`
- `task1_requirements.txt`
- `Task1_Paper_Leak_Web_Scraping_Report.md`
