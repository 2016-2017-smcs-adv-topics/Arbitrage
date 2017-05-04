# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import requests
import json


class EbaySpider(scrapy.Spider):
    name = "ebay"
    allowed_domains = ["ebay.com"]
    start_urls = ['http://www.ebay.com/sch/i.html?_from=R40&_nkw=CALLAWAY%20GOLF%202015%20GREAT%20BIG%20BERTHA%20DRIVER&rt=nc&LH_ItemCondition=4&_udlo&_udhi&LH_PrefLoc=1&LH_AllListings=1']
    dbURL = 'https://roswell.stmarksschool.org/~arbitrage/api/v1/CallawayData'

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        for item in soup.select('#ListViewInner > li'):
            data = {
                'Name': item.find("h3", class_="lvtitle").get_text().strip(),
                'Price': item.find("li", class_="lvprice prc").find("span").get_text().strip()
            }

            requests.post(self.dbURL, params=data)
            print(data)

        next_page = response.xpath('.//a[@class="pg"]/@href').extract()

        if next_page:
            next_href = next_page[0]
            next_page_url = "http://www.ebay.com" + next_href
            request = scrapy.Request(callback=self.parse, url = next_page_url)
            yield request

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)