import requests
from bs4 import BeautifulSoup

a = requests.get('https://quotes.toscrape.com')
soup = BeautifulSoup(a.text, "html.parser")
print(soup)

print("Status:", a.status_code)
print("URL:", a.url)
print("Tamanho:", len(a.text))
print("Content-Type:", a.headers.get("Content-Type"))

print(a.text[:2000])