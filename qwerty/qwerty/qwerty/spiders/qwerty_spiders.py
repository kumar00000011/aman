import scrapy
from qwerty.items   import QwertyItem



class QwertSpider(scrapy.Spider):
        name='qwertyspider'
        start_urls=['https://www.gucci.com/uk/en_gb/ca/women/womens-ready-to-wear/coats-c-women-readytowear-coats-furs']#G



        def parse(self,response):
            for items in  response.xpath("//article[contains(@class,'product-tiles-grid-item ')]"):
                cloth=QwertyItem()
                cloth['name']=items.xpath("./a/div[@class='product-tiles-grid-item-detail']/div[@class='product-tiles-grid-item-info']/h2/text()").extract()
                cloth['price']=items.xpath(" ./a/div[@class='product-tiles-grid-item-detail']/div[@class='product-tiles-grid-item-info']/p/span[@class='sale']/text()").extract()
                cloth['uuid']=items.xpath("./a/@data-style-id").extract()
                cloth['crawled_from']=response.url
                cloth['link']=items.xpath("./a/@href").extract()
                cloth['brand']="Gucci"
                cloth['image']=items.xpath("./a/div[@class='product-tiles-grid-item-image-wrapper']/div[@class='product-tiles-grid-item-image ']/img/@src").extract()
                yield cloth
