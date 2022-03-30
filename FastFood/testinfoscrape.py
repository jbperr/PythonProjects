import requests
from bs4 import BeautifulSoup

### WORKS
# chipotle, qdoba, kfc, pizzahut, subway, dunkin, wendys, papa johns,
# hardees, carls jr, panera, jack in box, whataburger, churches

### NO WORKS
# tacobell, dairy queen, sonic, chik fil a, arbys, popeyes, bk, panda, jimm jans,

store_url = "https://locations.sonicdrivein.com/al/auburn/1703-south-college-street.html"
page = requests.get(store_url)

soup = BeautifulSoup(page.content, "html.parser")
header = soup.find('head')

location = header.find('meta', attrs={'name': 'address'})['content']

# address = header.find('meta', attrs={'property': 'og:street-address'})['content']
# city = header.find('meta', attrs={'property': 'og:locality'})['content']
# state = header.find('meta', attrs={'property': 'og:region'})['content']
# zipcode = header.find('meta', attrs={'property': 'og:postal-code'})['content']
# lat = header.find('meta', attrs={'property': 'og:latitude'})['content']
# lon = header.find('meta', attrs={'property': 'og:longitude'})['content']

address = location.split(',')[0]
city = location.split(',')[1].strip()
state = location.split(',')[2].strip()
zipcode = location.split(',')[3].strip()
if len(zipcode) == 10:
    zipcode = zipcode[:-5]

# city = soup.find(class_="c-address-city").get_text()
# state = soup.find(class_="c-address-state").get_text()
# address = soup.find(class_="c-address-street-1").get_text()
# zipcode = soup.find(class_="c-address-postal-code").get_text()

# coords = soup.find(class_="coordinates")

# lat = (coords.find("meta", itemprop="latitude"))["content"]
# lon = (coords.find("meta", itemprop="longitude"))["content"]

print(address, city, state, zipcode)
