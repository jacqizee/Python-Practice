import requests
import json
from bs4 import BeautifulSoup

with open("product-links.json", "r") as f:
    PRODUCT_URLS = json.load(f)

products = {}

for URL in PRODUCT_URLS:
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find('h1', class_='c-product-main__name')
    if title: title = title.text

    type = soup.find('span', class_='c-product-main__subtitle')
    if type: type = type.text

    content_block = soup.find("div", class_="c-tabs__content")
    if not content_block:
        continue
    
    description = content_block.find(attrs={'data-tab-hash': 'description'})
    if description: description = description.text

    notes = content_block.find(attrs={'data-tab-hash': 'fragrance-notes'})
    if notes: notes = notes.text

    ingredients = content_block.find(attrs={'data-tab-hash': 'ingredients'})
    if ingredients: ingredients = ingredients.text

    entry = {
        'type': type,
        'description': description,
        'notes': notes,
        'ingredients': ingredients
    }

    products[title] = entry

with open('scraped-details.json', 'w') as f:
    json.dump(products, f)