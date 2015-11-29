LANGS = """Disallow: /uk/your/
Disallow: /au/your/
Disallow: /ca/your/
Disallow: /ch-en/your/
Disallow: /dk-en/your/
Disallow: /hk-en/your/
Disallow: /ie/your/
Disallow: /il-en/your/
Disallow: /in-en/your/
Disallow: /no-en/your/
Disallow: /nz/your/
Disallow: /se-en/your/
Disallow: /sg-en/your/
Disallow: /fr/your/
Disallow: /be-fr/your/
Disallow: /ca-fr/your/
Disallow: /de/your/
Disallow: /nl/your/
Disallow: /pt/your/
Disallow: /ru/your/
Disallow: /es/your/
Disallow: /mx/your/
Disallow: /it/your/
Disallow: /jp/your/""".split('\n')
LANGS = [x.replace('Disallow: ','').replace('your/','').strip() for x in LANGS]

def url_is_foreign(url):
	for lang in LANGS:
		if 'etsy.com' + lang in url:
			return True
	return False

if __name__ == "__main__":
	a = "https://www.etsy.com/il-en/shop/APerfectParty5?ref=l2-shopheader-name"
	b = "https://www.etsy.com/listing/230602358/summer-hat-with-3-flower-soft-brimmed"
	print(a, url_is_foreign(a))
	print(b, url_is_foreign(b))