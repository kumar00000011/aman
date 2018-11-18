import scrapy




class GucciSpider(scrapy.Spider):
        name = "guccispider"
        allowed_domains = ['www.gucci.com']


        start_urls=['https://www.gucci.com/uk/en_gb/ca/women/womens-ready-to-wear/coats-c-women-readytowear-coats-furs']


        def parse(self,response):
            for item in response.xpath("//div[contains(@class,'product-tiles-grid')]"):
                if item.xpath("./article[contains(@class,'product-tiles-grid-item product-tiles-grid-item-medium product-tiles-grid-item-small hover-link border-right')]").extract():
                    count=0
                    count=count+1
                    cloth = Item()
                    cloth['link']=response.xpath("./a/@href").extract()[0]
                    cloth['image']=response.xpath("/div[contains(@class,'product-tiles-grid-item-image-wrapper')]/div[contains(@class,'product-tiles-grid-item-image ')]/img/@src").extract()[0]
                    cloth['uuid']=response.xpath("/a/@data-style-id").extract()[0]
                    cloth['name']=response.xpath("/div[contains(@class,'product-tiles-grid-item-detail')]/div[contains(@class,'product-tiles-grid-item-info')]/h2/text()").extract()[0]
                    cloth['price']=response.xpath("/div[contains(@class,'product-tiles-grid-item-detail')]/div[contains(@class,'product-tiles-grid-item-info')]/p/span[contains(@class,'sale')]/text()").extract()[0]
                    res=scrapy.Request(url=start_urls,callback=self.parse,method=GET,meta={'item': cloth})
                    res.meta['item'] = cloth
                    yield res
        def parse_items(self, response):
            hxs = HtmlXPathSelector(response)
            yield res
