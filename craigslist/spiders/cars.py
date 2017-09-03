# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider, Request

class CarsSpider(Spider):
  name = 'cars'
  # cars and trucks from owners only. for all, use 'cta' instead of 'cto'
  allowed_domains = ['https://sfbay.craigslist.org/search/cto']
  # my usual search string for automatic minis that are not red
  start_urls = ['https://sfbay.craigslist.org/search/cta?search_distance=30&postal=94041&max_price=11000&auto_make_model=mini+cooper&min_auto_year=2011&max_auto_miles=60000&auto_paint=1&auto_paint=2&auto_paint=20&auto_paint=3&auto_paint=4&auto_paint=5&auto_paint=6&auto_paint=8&auto_paint=9&auto_paint=10&auto_paint=11&auto_title_status=1&auto_transmission=2']

  def parse(self, response):
    # -*- print titles to check that scrapy is working -*- 
    #titles = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()
    #print (titles)
    cars = response.xpath('//p[@class="result-info"]')
    print (cars)
    for car in cars:
        title = car.xpath('a/text()').extract_first()
        price = car.xpath('span[@class="result-meta"]/span[@class="result-price"]/text()').extract()[0]
        relative_url = car.xpath('a/@href').extract_first()
        absolute_url = response.urljoin(relative_url)
        print( {
          'Title': title,
          'Price': price,
          'URL': absolute_url
        })