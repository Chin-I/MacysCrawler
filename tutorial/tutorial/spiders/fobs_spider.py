"""
import scrapy

class FobsSpider(scrapy.Spider):
    name = "fobs"
    start_urls = [
        'https://www.macys.com/',
    ]

    def parse(self, response):
        for fob in response.css('ul.redesign-header-fobs'):
              
            yield {
                'fob': fob.css('li.fob a::attr(href)').extract()
            }
"""