import scrapy
import BeautifulSoup
import requests
from centralFunction import arbObject

url = 'http://roswell.stmarksschool.org/~arbitrage/api/v1/test/1'

print(requests.put(url, params = data).text)

class Arbitrage(scrapy.Spider):

    name = 'arbi'
    dbURL = 'http://roswell.stmarksschool.org/~arbitrage/api/v1/test/1'
    start_urls = ["http://www.ebay.com/sch/i.html?_from=R40&_nkw=CALLAWAY%20GOLF%202015%20GREAT%20BIG%20BERTHA%20DRIVER&rt=nc&LH_ItemCondition=4&_udlo&_udhi&LH_PrefLoc=1&LH_AllListings=1"]

    def parse(self, response):
        soup = BeautifulSoup(response, 'html.parser')
        for item in soup.select('#ListViewInner li'):

            data = {
                'name': item.find_next("h3", class_="lvtitle"),
                'price': item.find_next("li", class_="lvprice prc")
            }

            print(requests.put(dbURL, params=data).text)

        NEXT_PAGE_SELECTOR = '.gspr.next a ::attr(href)'
        next_page = response.select(NEXT_PAGE_SELECTOR)

        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )

parse()