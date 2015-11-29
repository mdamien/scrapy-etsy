import scrapy
from extruct.w3cmicrodata import MicrodataExtractor
from langs import url_is_foreign

from pprint import pprint as pp

def clean(url):
    return url.split('?')[0]

def e0(x):
    e = x.extract()
    if len(e) > 0:
        return e[0]

class EtsySpider(scrapy.Spider):
    name = 'etsy'
    allowed_domains = ['etsy.com']
    start_urls = ['https://www.etsy.com/']
    custom_settings = {
        'HTTPCACHE_ENABLED': True,
        'HTTPCACHE_DIR': '/tmp/httpcache',
    }

    def parse(self, response):
        for url in response.css('a::attr("href")').extract():
            if 'etsy.com' in url and not url_is_foreign(url):
                priority = 1 if 'listing/' in response.url else 0
                yield scrapy.Request(response.urljoin(clean(url)), self.parse, priority=priority)
        if 'listing/' in response.url:
            for it in self.parse_listing(response):
                yield it
        if 'shop/' in response.url:
            #TODO # of sales for the shop
            pass

    def parse_listing(self, response):
    	mde = MicrodataExtractor()
        data = mde.extract(response.body)['items']
        if data:
            it = {}
            it['shop'] = data[0]['properties']
            prod = data[1]['properties']
            it.update(prod['offerDetails']['properties'])
            it['name'] = prod['name']
            it['url'] = response.url
            it['properties'] = [x for x in response.css('#item-overview .properties li::text').extract() \
                if all(y not in x.lower() for y in ['materials','feedback', 'favorited', 'ships'])]
            it['materials'] = e0(response.css('#overview-materials::text'))
            it['origin'] = e0(response.css('.origin::text'))
            it['imgs'] = response.css('#image-carousel img::attr("src")').extract()
            it['description'] = e0(response.css("#description-text"))
            it['tags'] = response.css('#listing-tag-list li a::text').extract()
            it['fineprints'] = [x.strip() for x in response.css('#fineprint li::text').extract()[:4]]
            it['rating'] = response.css('.review-rating meta::attr("content")').extract()
            #it['html'] = response.body
            yield it


