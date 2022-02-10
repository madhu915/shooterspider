import scrapy

class ShooterSpider(scrapy.Spider):
    name='shooter'
    start_urls=['https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1']
    
    def parse(self, response):
        for pdts in response.css('div.product'):
            yield{
                'price': (float)(pdts.css('.price span::text').get().replace('$','')),
                'title': pdts.css('a.catalog-item-name::text').get(),
                'stock': False if pdts.css('.status span::text').get()=='Out of Stock' else True,
                'maftr': pdts.css('a.catalog-item-brand::text').get(),
            }