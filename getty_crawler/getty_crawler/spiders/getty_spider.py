import scrapy
import os
from urllib.parse import urlparse


class GettySpider(scrapy.Spider):
    name = "getty_spider"
    allowed_domains = ["www.gettyimages.in",'media.gettyimages.com']
    start_urls = ["https://www.gettyimages.in/photos/aamir-khan-actor"]

    downloaded_images = 0
    total_images_to_download = 60

    custom_settings = {
        'LOG_LEVEL': 'WARNING',
        'LOG_FORMAT': '%(message)s'
    }
    def parse(self, response):
        if not os.path.exists('images'):
            os.makedirs('images')

        for img in response.css('img::attr(src)').getall():
            if "media.gettyimages.com/id" in img:
                yield scrapy.Request(img, callback=self.save_image)
    def save_image(self, response):
        parsed_url = urlparse(response.url)        
        path_segments = parsed_url.path.split('/')
        img_id = path_segments[-3]  
        img_desc = path_segments[-1].split('.')[0]  
        filename = f"{img_desc}-id{img_id}.jpg"
        path = os.path.join('images', filename)

        with open(path, 'wb') as f:
            f.write(response.body)
            self.downloaded_images += 1
            print(f'\rDownloaded {self.downloaded_images} out of {self.total_images_to_download} images', end='', flush=True)
            
            if self.downloaded_images >= self.total_images_to_download:
                print( '\rDownloaded all required 60 images')
