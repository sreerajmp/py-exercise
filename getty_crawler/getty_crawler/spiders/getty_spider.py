import scrapy
import os
from urllib.parse import urlparse


class GettySpiderSpider(scrapy.Spider):
    name = "getty_spider"
    allowed_domains = ["www.gettyimages.in",'media.gettyimages.com']
    start_urls = ["https://www.gettyimages.in/photos/aamir-khan-actor"]

    def parse(self, response):
        if not os.path.exists('images'):
            os.makedirs('images')

        for img in response.css('img::attr(src)').getall():
            if "media.gettyimages.com/id" in img:
                # Ensure the URL is complete
                img_url = response.urljoin(img)
                self.log(f'Found image URL: {img_url}')
                yield scrapy.Request(img_url, callback=self.save_image)
    def save_image(self, response):
        self.log(f'Downloading image from: {response}')
        # self.log(f'Downloading image from: {response.url}')
        parsed_url = urlparse(response.url)
        filename = parsed_url.path.split('/')[-1] 
        path = os.path.join('images', filename)

        with open(path, 'wb') as f:
            f.write(response.body)