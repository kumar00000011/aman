import scrapy
from cuyana.items     import CuyanaItem



class CuyanaSpider(scrapy.Spider):
    name='cuyana'
    allowed_domain=['www.cuyana.com']
    def start_requests(self):
        yield scrapy.Request('https://www.cuyana.com/bestsellers.html',callback= self.parse)



    def parse (self,response):
        for items in response.xpath("//nav/ol/li/ol/li"):
            if ".html" in items.xpath("./a/@href").extract()[0]:

                    cloth=CuyanaItem()
                    cloth['link']=items.xpath("./a/@href").extract()[0]
                    cloth['title']=items.xpath("./a/text()").extract()[0]
                    yield cloth

            for links in items.xpath("./ul/li/ul/li"):
                if ".html" in links.xpath("./a/@href").extract()[0]:

                    cloth=CuyanaItem()
                    cloth['link']=links.xpath("./a/@href").extract()[0]
                    cloth['title']=links.xpath("./a/text()").extract()[0]
                    yield cloth
