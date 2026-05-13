from playwright.sync_api import sync_playwright
import csv

with sync_playwright() as p:
  browser = p.chromium.launch(headless=False)
  page = browser.new_page()
  page.goto("https://news.naver.com/section/105")
  news = page.locator(".section_article.as_headline a.sa_text_title")
  # 이동할 뉴스 목록관리
  links = []

  for i in range(news.count()):
    news_item = news.nth(i)

    title = news_item.inner_text().strip()

    link = news_item.get_attribute("href")
    # print(f"{i+1}. {title}\n   {link}")

    links.append({"title": title, "link": link})
    
  for news in links:
    # 뉴스 상세 페이지 이동
    page.goto(news["link"])
    
    # 뉴스 상세 페이지 내용 추출
    content = page.locator("#dic_area").inner_html().strip()
    news["content"] = content

    print(f"뉴스 제목: {news['title']}\n뉴스 내용: {news['content']}\n뉴스 링크: {news['link']}")

  browser.close()