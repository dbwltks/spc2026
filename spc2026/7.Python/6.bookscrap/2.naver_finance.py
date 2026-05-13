import requests
from bs4 import BeautifulSoup
import csv

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent": "Mozilla/5.0"}

resp = requests.get(url, headers=headers)
resp.encoding = "euc-kr"
soup = BeautifulSoup(resp.text, "html.parser")

rows = soup.select("table.type_5 tr")

data = []
for row in rows:
    cols = row.select("td")
    if len(cols) < 2:
        continue
    name = cols[1].text.strip()
    price = cols[3].text.strip().replace(",", "").replace("\n", "")
    if name and price:
        data.append([name, price])
        print(f"종목명: {name}  현재가: {price}원")

with open("naver_stock.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["종목명", "현재가"])
    writer.writerows(data)

print(f"\n총 {len(data)}개 저장 완료 → naver_stock.csv")
