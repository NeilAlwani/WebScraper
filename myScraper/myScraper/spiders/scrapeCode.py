import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://www.bol.com/nl/s/?searchtext=wireless+earphones&searchContext=media_all&appliedSearchContextId=&suggestFragment=&adjustedSection=&originalSection=main&originalSearchContext=media_all&section=main&N=0&defaultSearchContext=media_all&suggestionType=search_history'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
       for title in response.css('.product-title::text'):
        yield{
            "title": title.get()
        }

        #for post in response.css('div.results-area).
        #   title = post.css('div.product-title--inline a::text')[0].get()
        #   price = post.css('meta')[0].get