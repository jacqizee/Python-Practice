import requests
from bs4 import BeautifulSoup

URL = 'https://www.lancome-usa.com/fragrance/?start=0&sz=48#view-mode=grid'

# Make Request
page = requests.get(URL)

# Parse Page Content
soup = BeautifulSoup(page.content, 'html.parser')

# Main Element
main = soup.find("main", class_="l-plp")

# Pull Out a Elements from Products
products = main.find_all('a', class_='c-product-image')
for product in products:
    print(product.get_attribute_list, end='\n'*2)