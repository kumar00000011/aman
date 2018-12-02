
import scrapy
from lavie.items import bagItem





class Laespider(scrapy.Spider):
    name="pageno3"

    start_urls=['http://www.lavieworld.com/backpacks/categories/backpacks.html#/page/{no}'.format(no=no)
                 for no in range(2,4)]




    def parse(self,response):
        for bags in response.xpath("//li[contains(@class,'item last')]"):
            backpack=bagItem()
            backpack['name']=bags.xpath("./div[@class='product-image arw-hover-actions arw-hover-image']/a/@title").extract()
            backpack['price']= bags.xpath("./div[@class='product-info']/div[@class='price-box']/span[@class='regular-price']/span[@class='price']/text()").extract() or bags.xpath("./div[@class='product-info']/div[@class='price-box']/p[@class='special-price']/span[@class='price']/text()").extract()
            backpack['link']=bags.xpath("./div[@class='product-image arw-hover-actions arw-hover-image']/a/@href").extract()
            backpack['brand']="lavie"
            backpack['image']=bags.xpath("./div[@class='product-image arw-hover-actions arw-hover-image']/a/img[@class='first-img']/@src").extract()
            yield backpack
