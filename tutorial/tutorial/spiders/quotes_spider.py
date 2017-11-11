import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text2': quote.css('span.text::text').extract_first(),
                'author2': quote.css('span small::text').extract_first(),
                'tags2': quote.css('div.tags a.tag::text').extract(),
            }

        # next_page = response.css('li.next a::attr(href)').extract_first()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse) #(..)

        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, callback=self.parse)

########################################################
# import scrapy

# class QuotesSpider(scrapy.Spider):
#     name = "quotes"
#     start_urls = [
#         'http://quotes.toscrape.com/page/1/',
#     ]

#     def parse(self, response):
#         for quote in response.css('div.quote'):
#             yield {
#                 'text': quote.css('span.text::text').extract_first(),
#                 'author': quote.css('span small::text').extract_first(),
#                 'tags': quote.css('div.tags a.tag::text').extract(),
#             }

#         next_page = response.css('li.next a::attr(href)').extract_first()
#         if next_page is not None:
#             yield response.follow(next_page, callback=self.parse) #(..)

########################################################
# import scrapy
# class QuotesSpider(scrapy.Spider):
#     name = "quotes"
#     start_urls = [
#         'http://quotes.toscrape.com/page/1/',
#     ]
#     def parse(self, response):
#         for quote in response.css('div.quote'):
#             yield {
#                 'text': quote.css('span.text::text').extract_first(),
#                 'author': quote.css('small.author::text').extract_first(),
#                 'tags': quote.css('div.tags a.tag::text').extract()
#             }
#         next_page = response.css('li.next a::attr(href)').extract_first()
#         if next_page is not None:
#             next_page = response.urljoin(next_page)
#             yield scrapy.Request(next_page, callback=self.parse)
#########################################################

# import scrapy

# class QuotesSpider(scrapy.Spider):
#     name = "quotes"
#     start_urls = [
#         'http://quotes.toscrape.com/page/1/',
#         'http://quotes.toscrape.com/page/2/',
#     ]

#     def parse(self, response):
#         for quote in response.css('div.quote'):
#             yield {
#                 'text': quote.css('span.text::text').extract_first(),
#                 'author': quote.css('small.author::text').extract_first(),
#                 'tags': quote.css('div.tags a.tag::text').extract(),
#             }

##########################################################

# import scrapy

# class QuotesSpider(scrapy.Spider):
#     name = "quotes"

#     start_urls = [
#         'http://quotes.toscrape.com/page/1/',
#         'http://quotes.toscrape.com/page/2/',
#         'http://quotes.toscrape.com/page/3/'
#     ]

#     # def start_requests(self):
#     #     urls = [
#     #         'http://quotes.toscrape.com/page/1/',
#     #         'http://quotes.toscrape.com/page/2/',
#     #         'http://quotes.toscrape.com/page/3/'
#     #     ]
#     #     for url in urls:
#     #         yield scrapy.Request(url=url, callback=self.parse)


#     def parse(self, response):
#         page = response.url.split("/")[-2]
#         filename = 'quotes-%s.html' % page
#         with open(filename, 'wb') as f:
#             f.write(response.body)        
#         # self.log('Saved file %s' % filename)
