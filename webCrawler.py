import scrapy

class Arbitrage(scrapy.Spider):
    name = 'arbi'
    start_urls = ["http://www.ebay.com/sch/i.html?_from=R40&_nkw=CALLAWAY%20GOLF%202015%20GREAT%20BIG%20BERTHA%20DRIVER&rt=nc&LH_ItemCondition=4&_udlo&_udhi&LH_PrefLoc=1&LH_AllListings=1"]

    def parse(self, response):
        SET_SELECTOR = '.set'
        for set in response.css(SET_SELECTOR):

            NAME_SELECTOR = './/ul[li]/a/text()'
            PRICE_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
            
            yield {
                'name': set.css(NAME_SELECTOR).extract_first(),
                'pieces': set.xpath(PRICE_SELECTOR).extract_first(),
            }

        NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
