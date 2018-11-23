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
                cloth['link']=kapada.xpath("//a/@href").extract_first()
                cloth['image']=kapada.xpath("//div(@class,'product-tiles-grid-item-image-wrapper')/div(@class,'product-tiles-grid-item-image ')/img/@src").extract()
                cloth['uuid']=kapada.xpath("//a/@data-style-id").extract_first()
                cloth['name']=kapada.xpath("//div[(@class,'product-tiles-grid-item-detail')]/div[(@class,'product-tiles-grid-item-info')]/h2/text()").extract()
                cloth['price']=kapada.xpath("//div[(@class,'product-tiles-grid-item-detail')]/div[(@class,'product-tiles-grid-item-info')]/p/span(@class,'sale')/text()").extract()
                r=scrapy.Request(start_urls,callback=self.parse,method=GET)

                yield cloth



#href open kar k
import scrapy
from guc.items  import Item




class GucciSpider(scrapy.Spider):
        name = "guccispider"
        allowed_domains = ['www.gucci.com']
        start_urls=['https://www.gucci.com/uk/en_gb/ca/women/womens-ready-to-wear/coats-c-women-readytowear-coats-furs']


       def parse(self,response):
           for kapada in response.xpath("//div[contains(@class,'product-tiles-grid')]"):
               if kapada.xpath("/article[contains(@class,'product-tiles-grid-item product-tiles-grid-item-medium product-tiles-grid-item-small hover-link border-right')]"):
                   cloth= Item()
                   cloth['link']=kapada.xpath("/a[contains(@class,'product-tiles-grid-item-link')]/@href").extract()
                   cloth['image']=kapada.xpath("//div[contains(@class,'js--zoomcarousel-opener item product-detail-image-slide zoom-in anchor-point-C active slick-slide slick-current slick-active')]/picture//img[contains(@class,'item-content product-detail-carousel-image zoom-item ')]/@srcset").extract()
                   cloth['uuid']=kapada.xpath("//div[contains(@class,'style-number-title')]/span/text()").extract().split()
                   cloth['name']=kapada.xpath("//div[contains(@class,'productnameandprice-container-standard')]/h1[contains(@class,'product-name product-detail-product-name')]/text()").extract()
                   cloth['price']=kapada.xpath("//div[contains(@class,'productnameandprice-container-standard')]/div[contains(@class,'product-price product-detail-price')]/div[contains(@class,'price-column product-detail-price-column')]/span[contains(@class,'price')]/text()").extract()
                   r=scrapy.request(url=cloth['link'],callback=self.parse)

                   yield r
