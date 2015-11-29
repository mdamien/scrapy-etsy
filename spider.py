import scrapy
from extruct.w3cmicrodata import MicrodataExtractor
from langs import url_is_foreign

from pprint import pprint as pp

def clean(url):
    return url.split('?')[0]

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
                yield scrapy.Request(response.urljoin(clean(url)), self.parse)
        if 'listing/' in response.url:
            for it in self.parse_listing(response):
                yield it

    def parse_page(self, response):
    	page = response.meta.get('page',1)
    	yield scrapy.Request(URL.format(page=page+1), meta={'page': page+1}, callback=self.parse)
        for i in response.css('.block-grid-item'):
        	item = {}
        	item['url'] = i.css('a::attr("href")').extract()[0]
        	item['img'] = i.css('img::attr("src")').extract()[0]
        	item['name'] = i.css('.card-title::text').extract()[0].strip()
        	item['shop'] = i.css('.card-shop-name::text').extract()[0].strip()
        	item['price'] = i.css('.card-price::text').extract()[0].strip()
        	yield item
            #yield scrapy.Request(response.urljoin(url), self.parse_listing)

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
            #it['html'] = response.body
            yield it


