import requests
from bs4 import BeautifulSoup

url = "https://bahisrehberi.com/bahis-tahminleri"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

selectors = [
    "div.post-inner-content:last-child > h2:nth-child(3)",
    "div.post-inner-content:last-child > div.gunluktahminler:nth-child(4) > div.gtbaslik > div.gttarihsaat:first-child",
    "div.post-inner-content:last-child > div.gunluktahminler:nth-child(4) > div.gtbaslik > div.gtbkarsilasma:nth-child(2)",
    "div.post-inner-content:last-child > div.gunluktahminler:nth-child(4) > div.gtbaslik > div.gttercih:nth-child(3)",
    "div.post-inner-content:last-child > div.gunluktahminler:nth-child(4) > div.gtbaslik > div.gtoran:last-child",
]

data = []
for selector in selectors:
    elements = soup.select(selector)
    if elements:
        text = elements[0].get_text(strip=True)
    else:
        text = ""
    data.append(text)

table_markdown = f"""
| Başlık | Tarih/Saat | Karşılaşma | Tercih | Oran |
|:---|:---|:---|:---|:---|
| {data[0]} | {data[1]} | {data[2]} | {data[3]} | {data[4]} |
"""

with open("bahis_tahminleri.md", "w", encoding="utf-8") as f:
    f.write(table_markdown)
