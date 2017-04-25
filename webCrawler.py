import scrapy
from bs4 import BeautifulSoup
import requests
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
import json

dbURL = 'https://roswell.stmarksschool.org/~arbitrage/api/v1/CallawayData'

class Arbitrage(scrapy.Spider):

    name = 'arbi'
    dbURL = 'https://roswell.stmarksschool.org/~arbitrage/api/v1/CallawayData'
    start_urls = ["http://www.ebay.com/sch/i.html?_from=R40&_nkw=CALLAWAY%20GOLF%202015%20GREAT%20BIG%20BERTHA%20DRIVER&rt=nc&LH_ItemCondition=4&_udlo&_udhi&LH_PrefLoc=1&LH_AllListings=1"]

    Rules = (Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@class="pg"]',)), callback="parse", follow=True),)

    def parse(self, response):
        soup = BeautifulSoup(response, 'html.parser')
        for item in soup.select('#ListViewInner li'):

            data = {
                'name': item.find_next("h3", class_="lvtitle"),
                'price': item.find_next("li", class_="lvprice prc")
            }

            print(data)
            print(requests.post(dbURL, params=data).text)

        next_page = response.xpath('.//a[@class="pg"]/@href').extract()

        if next_page:
            next_href = next_page[0]
            next_page_url = "http://www.ebay.com" + next_href
            request = scrapy.Request(callback=self.parse, url = next_page_url)
            yield request
