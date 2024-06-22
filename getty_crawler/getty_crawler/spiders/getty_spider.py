import scrapy


class GettySpiderSpider(scrapy.Spider):
    name = "getty_spider"
    allowed_domains = ["www.gettyimages.in"]
    start_urls = ["https://www.gettyimages.in/photos/aamir-khan-actor"]

    def parse(self, response):
        pass
