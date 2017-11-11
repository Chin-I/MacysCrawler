import scrapy

class QuotesSpider(scrapy.Spider):
    name = "products"
    start_urls = [
        'https://www.macys.com/shop/product/hotel-collection-finest-modal-robe-luxury-turkish-cotton-created-for-macys?ID=1591625&CategoryID=51483',
    ]

    def parse(self, response):
        for product_name in response.css('.columns.small-16'):
            yield {
                'product_name': product_name.css('.productName::text').extract_first()
            }


        # for href in response.css('li.next a::attr(href)'):
        #     yield response.follow(href, callback=self.parse)


    # def parse(self, response):
    #     yield {
    #         'product_name': response.css('.productName::text').extract_first()
    #     }
