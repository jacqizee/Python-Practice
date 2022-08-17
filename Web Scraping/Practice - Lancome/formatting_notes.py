import json

with open('scraped-details.json', 'r') as f:
    products = json.load(f)

for key in products.keys():
    notes = str(products[key]['notes']).lower()
    if notes.find('top note') != -1:
        top = notes.find('top note')
        heart = notes.find('middle note')
        if heart == -1:
            heart = notes.find('heart note')
        base = notes.find('base note')
        if base == -1:
            base = notes.find('transversal note')

        products[key]['top_notes'] = notes[top:heart]
        products[key]['heart_notes'] = notes[heart:base]
        products[key]['base_notes'] = notes[base:]

        print(products[key]['top_notes'])
        print(products[key]['heart_notes'])
        print(products[key]['base_notes'])

with open('scraped-details-with-notes.json', 'w') as f:
    products = json.dump(products, f)