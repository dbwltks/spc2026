import requests

url = "https://www.google.com"

resp = requests.get(url)

html = resp.text
print(html)