import json

def streamload():
    for line in open('data.jl'):
        try:
            yield enhance(json.loads(line))
        except Exception as e:
            print(e)
            break

def load(small=False):
    DATA = []
    for i, item in enumerate(streamload()):
        DATA.append(item)
        if i % 100000 == 0:
            print('loaded',i,'items')
        if small and i > 1000:
            break
    return DATA

def enhance(i):
    i['id'] = i['url'].split('listing/')[1].split('/')[0]
    i['views'] = int(i['fineprints'][1].split()[0])
    #i['favs'] = int(i['fineprints'][1].split()[0])
    i['price'] = float(i['price'])
    if i['rating']:
        i['rating_score'] = float(i['rating'][0])
        i['rating_count'] = int(i['rating'][1])
        del i['rating']
    return i

def example():
    x = """{"shop": {"url": "https://www.etsy.com/shop/robinsvintage?ref=l2-shopheader-name", "title": "robinsvintage"}, "origin": "Pennsylvania, United States", "rating": ["4.7215", "6834"], "name": "vintage necklace black beads", "tags": ["Vintage", "Jewelry", "vintage", "necklace", "black", "beads", "jewelry"], "url": "https://www.etsy.com/listing/97003287/vintage-necklace-black-beads", "price": "6", "availability": "in_stock", "currency": "USD", "materials": null, "fineprints": ["Listed on Oct 13, 2015", "30 views", "", ""], "imgs": ["https://img0.etsystatic.com/000/0/6191217/il_570xN.326777798.jpg"], "properties": ["Vintage item", "."], "description": "<div id=\"description-text\">\n                            vintage necklace. very nice shape. size is 24 inches<br><br>I am happy to ship internationally so please ask for shipping quote. i am also happy to combine where possible<br><br>If you have any questions please feel free to email me and thank you for looking            \n        </div>"}"""
