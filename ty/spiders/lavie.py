import scrapy
from lavie.items import bagItem






class Laiespider2(scrapy.Spider):
    name="lavie"


    start_urls=['http://www.lavieworld.com/backpacks/categories/backpacks.html#page/1',
            'http://www.lavieworld.com/backpacks/categories/backpacks.html#page/2',
            'http://www.lavieworld.com/backpacks/categories/backpacks.html#page/3']
    def start_requests(self):
        for u in self.start_urls:
                yield scrapy.Request(u,callback=self.parse,dont_filter=True)

    def parse(self,response):

        for bags in response.xpath("//li[contains(@class,'item last')]"):
                backpack=bagItem()
                backpack['crawled_from']=response.url
                backpack['name']=bags.xpath("./div[@class='product-image arw-hover-actions arw-hover-image']/a/@title").extract()
                backpack['price']= bags.xpath("./div[@class='product-info']/div[@class='price-box']/span[@class='regular-price']/span[@class='price']/text()").extract() or bags.xpath("./div[@class='product-info']/div[@class='price-box']/p[@class='special-price']/span[@class='price']/text()").extract()
                backpack['link']=bags.xpath("./div[@class='product-image arw-hover-actions arw-hover-image']/a/@href").extract()
                backpack['brand']="lavie"
                backpack['image']=bags.xpath("./div[@class='product-image arw-hover-actions arw-hover-image']/a/img[@class='first-img']/@src").extract()

                yield backpack
