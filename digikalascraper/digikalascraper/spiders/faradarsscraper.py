import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["faradars.org"]
    start_urls = ["https://faradars.org/how-to-learn/stock-and-technical-analysis"]

    def parse(self, response):
        pass
