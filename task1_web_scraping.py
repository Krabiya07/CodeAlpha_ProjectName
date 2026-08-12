import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.indiatoday.in/india/story/paper-leak-2019-to-2024-analysis-neet-net-nta-exam-cancelled-2558404-2024-06-26"

headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(URL, headers=headers, timeout=20)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

title_tag = soup.select_one("h1")
title = title_tag.get_text(" ", strip=True) if title_tag else ""

date = ""
for selector in ["time", ".story-date", "[class*='date']"]:
    tag = soup.select_one(selector)
    if tag:
        date = tag.get_text(" ", strip=True)
        break

paragraphs = soup.select("article p, .story-content p, .article-body p")
article_text = " ".join(
    p.get_text(" ", strip=True) for p in paragraphs
)

result = pd.DataFrame([{
    "Source_URL": URL,
    "Title": title,
    "Published_Date": date,
    "Article_Text": article_text
}])

result.to_csv("paper_leak_web_source.csv", index=False)

print("Web scraping completed.")
print("Title:", title)
print("Published Date:", date)
print("Saved: paper_leak_web_source.csv")
