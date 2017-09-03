# -*- coding: utf-8 -*-
import scrapy


class CarsSpider(scrapy.Spider):
    name = 'cars'
    allowed_domains = ['https://sfbay.craigslist.org/search/cta']
    start_urls = ['http://https://sfbay.craigslist.org/search/cta/']

    def parse(self, response):
        pass
