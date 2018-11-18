import scrapy
from scrapy import Spider
from scrapy.http import Request




class GucciSpider(scrapy.Spider):
        name = "guccispider"



        start_urls=['https://www.gucci.com/uk/en_gb/ca/women/womens-ready-to-wear/coats-c-women-readytowear-coats-furs']


        def parse(self,response):

            kapadas= response.xpath("//div[contains(@class,'product-tiles-grid')]").extract()
            yield Request('https://www.gucci.com/uk/en_gb/ca/women/womens-ready-to-wear/coats-c-women-readytowear-coats-furs',callback=self.parse_tuni)
        def parse_tuni(self, response):
                if item.xpath("./article[contains(@class,'product-tiles-grid-item product-tiles-grid-item-medium product-tiles-grid-item-small hover-link border-right')]").extract():
                    count=0
                    count=count+1
                    cloth = Item()
                    cloth['link']=response.xpath("./a/@href").extract()[0]
                    cloth['image']=response.xpath("/div[contains(@class,'product-tiles-grid-item-image-wrapper')]/div[contains(@class,'product-tiles-grid-item-image ')]/img/@src").extract()[0]
                    cloth['uuid']=response.xpath("/a/@data-style-id").extract()[0]
                    cloth['name']=response.xpath("/div[contains(@class,'product-tiles-grid-item-detail')]/div[contains(@class,'product-tiles-grid-item-info')]/h2/text()").extract()[0]
                    cloth['price']=response.xpath("/div[contains(@class,'product-tiles-grid-item-detail')]/div[contains(@class,'product-tiles-grid-item-info')]/p/span[contains(@class,'sale')]/text()").extract()[0]
                    res.meta['item'] = cloth
                    yield cloth
