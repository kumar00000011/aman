import scrapy
from gucci.items import GucciItem

class Spider(scrapy.Spider):
    name = "gucci_spider"

    start_urls = [
        "https://www.gucci.com/uk/en_gb/ca/women/womens-ready-to-wear/coats-c-women-readytowear-coats-furs"
    ]

    def parse(self, response):
        for kapada in response.xpath("//article[contains(@class,'product-tiles-grid-item')]"):
            # Initiaise an object == product detail
            product = GucciItem()
            product['crawled_from'] = response.url
            product['name'] = kapada.xpath("./a/div[@class='product-tiles-grid-item-detail']/div[@class='product-tiles-grid-item-info']/h2/text()").extract()
            product['link']=kapada.xpath("./a/@href").extract()
            yield product
