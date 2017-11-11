"""
import scrapy
import json


class HeadersSpider(scrapy.Spider):
	name = "headers"

	start_urls = json.load(open('fobs.json'))[0]['fob']

	for i in range(len(start_urls)):
		start_urls[i] = 'https://www.macys.com' + start_urls[i]


	def parse(self, response):
		for header in response.css('ul.categoryHeader'):
			yield {
				'header': header.css('a::attr(href)').extract()
			}
"""