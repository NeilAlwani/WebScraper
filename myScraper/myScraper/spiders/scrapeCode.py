import scrapy


class QuotesSpider(scrapy.Spider):
   #Name of the crawler
    name = "crawler"

    # Method that starts requests
    def start_requests(self):
        urls = [
            'https://www.bol.com/nl/s/?searchtext=wireless+earphones&searchContext=media_all&appliedSearchContextId=&suggestFragment=&adjustedSection=&originalSection=main&originalSearchContext=media_all&section=main&N=0&defaultSearchContext=media_all&suggestionType=search_history'
        ]

        # For each url open a request to that page
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Method that parses the response object using css operators
    def parse(self, response):
        post = response.css('div.results-area')
        # Small check to add the correct price tags to the titles
        for x in range(0,13):
            if x % 2 == 0:
                y = x
            else:
                y = x + 1
            yield{
                'title': post.css('div.product-title--inline a::text')[x].get(),
                'price': post.css('.promo-price::text')[y].get()
            }



            
# Run with: scrapy crawl crawler -o qoutes.json