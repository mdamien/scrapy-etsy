import scrapy

URL = "https://www.etsy.com/c?order=date_desc&ref=catlink-a&page={page}"

class EtsySpider(scrapy.Spider):
    name = 'etsy'
    start_urls = [URL.format(page=1)]
    custom_settings = {
        'HTTPCACHE_ENABLED': True,
        'HTTPCACHE_DIR': '/tmp/httpcache',
    }

    def parse(self, response):
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
    	pass