
import scrapy
import json

class LinksSpider(scrapy.Spider):
    name = "links"
    start_urls = [
        'https://www.macys.com/shop/womens-clothing/womens-activewear?id=29891&edge=hybrid'
    ]

    # start_urls = json.load(open('fobs.json'))[0]['fob']
    # for i in range(len(start_urls)):
    #     start_urls[i] = 'https://www.macys.com' + start_urls[i]
    # print (start_urls)

    def parse(self, response):
        for link in response.css('div.productDetail'):
            yield {
                'link': link.css('a::attr(href').extract()
            }
        next_page = response.css('div#filterResultsBottom ul li ul li.nextPage a::attr(href)').extract_first()
        # next_page = response.css('li.ul.li.nextPage a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)