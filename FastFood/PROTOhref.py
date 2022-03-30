import requests
from bs4 import BeautifulSoup

### WORKS
# chipotle, kfc, pizzahut, hardees, carls jr, whataburger, churches

### NO WORK
# PANERA

### TODO
# SUBWAY, DUNKIN, WENDYS, PAPA JOHNS, JACK IN BOX HAS EXTRA STUFF AT BEGINING. BUT WORKS

headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Max-Age": "3600",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
}
store_url = "https://locations.whataburger.com/directory.html/"
loc_url = "https://locations.whataburger.com/"

page = requests.get(store_url, headers)
soup = BeautifulSoup(page.content, "html.parser")
parent = soup.find(class_="Directory-listLinks")

hrefstatelinks = []
for li in parent.find_all("li"):
    a = li.find(class_="Directory-listLink")
    print(a["href"])
    hrefstatelinks.append(loc_url+a["href"])

for href in hrefstatelinks:
    if ".html" in href:
        href = href[:-5]
        href = href + "/"
    print(href)