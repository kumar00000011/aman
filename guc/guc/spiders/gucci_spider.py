import scrapy#import scrapy
from guc.items  import GucItem#from guc folder we are importing items.py file and within that file we are importing Gucitem class




class GucciSpider(scrapy.Spider):#class  GucciSpider is made which extract on the principal of scrapy sider or base spider
        name = "guccispider"#name is guccispider

        start_urls=['https://www.gucci.com/uk/en_gb/ca/women/womens-ready-to-wear/coats-c-women-readytowear-coats-furs']#starting url is this


        def parse(self,response):#parse the website
            for kapada in response.xpath("//div[contains(@class,'product-tiles-grid')]"):# agar ye h response m too
                if kapada.xpath("./article[contains(@class,'product-tiles-grid-item product-tiles-grid-item-medium product-tiles-grid-item-small hover-link border-right')]").extract():#agar y bhi h too extract all
                    count+=1

                    cloth= GucItem()#making a object in GucItem class where all the response is collected in form of items and these are defined as Field
                    cloth['link']=kapada.xpath("./a[contains(@class,'product-tiles-grid-item-link')]/@href").extract()
                    cloth['image']=kapada.xpath("./div(@class,'product-tiles-grid-item-image-wrapper')/div(@class,'product-tiles-grid-item-image ')/img/@src").extract()
                    cloth['uuid']=kapada.xpath("./a/@data-style-id").extract_first()
                    cloth['name']=kapada.xpath("./div[(@class,'product-tiles-grid-item-detail')]/div[(@class,'product-tiles-grid-item-info')]/h2/text()").extract()
                    cloth['price']=kapada.xpath("./div[(@class,'product-tiles-grid-item-detail')]/div[(@class,'product-tiles-grid-item-info')]/p/span(@class,'sale')/text()").extract()
                    yield cloth
                    yield  scrapy.Request(url=cloth['link'],method=GET,callback=self.parse)
