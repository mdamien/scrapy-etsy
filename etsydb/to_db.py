from scripts.load import streamload

import django, os
os.environ['DJANGO_SETTINGS_MODULE'] = 'etsydb.settings'
django.setup()

from etsy.models import Product

previous_size = Product.objects.all().count()
Product.objects.all().delete()
print(previous_size,"products deleted")

ids = set()

to_insert = []
for i, item in enumerate(streamload()):
	id = item['id']
	if id not in ids:
		ids.add(id)
		product = Product(
			id=id,
			name=item['name'],
			shop=item['shop']['title'],
			rating_score=item.get('rating_score',None),
			rating_count=item.get('rating_count',None),
			price=item['price'],
			price_currency=item['currency'],
			available=item.get('availability','') == 'in_stock',
			views=item['views'],
			imgs=item['imgs'],
			tags=item['tags'],
			description=item['description'])
		to_insert.append(product)
		if len(to_insert) > 10000:
			print(i,'=> commit')
			Product.objects.bulk_create(to_insert)
			to_insert = []
Product.objects.bulk_create(to_insert)