import scrapy
from scrapy.selector import Selector



class GucciSpider(scrapy.Spider):
        name = "guccispider"
        allowed_domains = ['www.gucci.com']

        start_urls=['https://www.gucci.com/uk/en_gb/ca/women/womens-ready-to-wear/coats-c-women-readytowear-coats-furs']


        def parse(self,response):
            for kapada in response.xpath("//div [contains(@class,'product-tiles-grid')]"):
                count=0
                count=count+1
                cloth = Item()
                cloth['link']=response.xpath("//a/@href").extract_first()[0]
                cloth['image']=response.xpath("//div(@class,'product-tiles-grid-item-image-wrapper')/div(@class,'product-tiles-grid-item-image ')/img/@src").extract_first()[0]
                cloth['uuid']=response.xpath("//a/@data-style-id").extract_first()[0]
                cloth['name']=response.xpath("//div[(@class,'product-tiles-grid-item-detail')]/div[(@class,'product-tiles-grid-item-info')]/h2/text()").extract_first()[0]
                cloth['price']=response.xpath("//div[(@class,'product-tiles-grid-item-detail')]/div[(@class,'product-tiles-grid-item-info')]/p/span(@class,'sale')/text()").extract_first()[0]
                r=scrapy.Request(start_urls,callback=self.parse,method=GET)

                yield cloth
