from playwright.sync_api import sync_playwright
import csv

with sync_playwright() as p:
  browser = p.chromium.launch(headless=False)
  page = browser.new_page()
  page.goto("https://news.naver.com/section/105")
  news = page.locator(".section_article.as_headline a.sa_text_title")
  

  for i in range(news.count()):
    news_item = news.nth(i)

    title = news_item.inner_text().strip()

    link = news_item.get_attribute("href")
    print(f"{i+1}. {title}\n   {link}")

  browser.close()