import requests
from bs4 import BeautifulSoup

url = "https://korean.visitseoul.net/attractions"

req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
body = soup.find("body")

for p in body.find_all("span", class_="title"):
    print(p.get_text())
