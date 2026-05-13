# pip install beautifulsoup4
from bs4 import BeautifulSoup

html = "<html><body><h1>Hello, World!</h1></body></html>"

soup = BeautifulSoup(html, "html.parser")
print(soup.prettify())