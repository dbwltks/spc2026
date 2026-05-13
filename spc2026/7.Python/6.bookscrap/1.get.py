# 1. boooks.toscrape.com에 접속해서 페이지를 받아온다
# 2. DOM을 bs4로 구성한다.
# 3. 첫 페이지의 도서명, 평점, 가격을 받아온다.
# 4. CSV 파일로 저장한다.

import requests
from bs4 import BeautifulSoup
import csv



url = "https://books.toscrape.com/"
data = []
resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")
books = soup.find_all("article", class_="product_pod")

for book in books:
  title = book.find("h3").find("a")["title"]
  rating = book.find("p", class_="star-rating").get("class")[1]
  price = book.find("p", class_="price_color").text.replace("£", "").replace("Â", "")
  data.append([title, rating, price])

with open("books.csv", "w", newline="", encoding="utf-8") as file:
  writer = csv.writer(file)
  writer.writerow(["title", "rating", "price"])
  writer.writerows(data)