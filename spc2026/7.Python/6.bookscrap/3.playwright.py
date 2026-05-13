# 1. platwright 모듈을 사용하여 브라우저를 실행한다.
# 2. 브라우저를 실행한 후, 웹 페이지를 연다.
# 3. 웹 페이지를 연 후, 페이지의 내용을 출력한다.

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
  # 브라우저를 실행한다.  
  browser = p.chromium.launch()
  # 새로운 페이지를 연다.
  page = browser.new_page()
  # 웹 페이지를 연다.
  page.goto("https://www.google.com")
  # 페이지의 내용을 출력한다.
  print(page.content())
  # 브라우저를 종료한다.
  browser.close()