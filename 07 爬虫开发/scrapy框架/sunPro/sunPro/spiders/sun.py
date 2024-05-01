import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SunSpider(CrawlSpider):
    name = 'sun'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.qctsw.com/tousu/tslist/1_0_1.html']

    Link = LinkExtractor(allow=r'tslist/1_\d_1.html')
    rules = (
        # Rule规则解析器:将链接提取器提取到的链接您行制定规则（callback）的解析操作
        # LinkExtrator链接提取器:根据指定规则（allow=“正则”）进行指定链接的提取
        # follow=True:可以将链接提取器继续作用到链接提取器提取到的链接所对应的页面中
        Rule(Link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        li_list = response.xpath('//*[@id="wrapper"]/div[1]/div[1]/ul/li')
        for li in li_list:
            title = li.xpath('./h3/span/@class').extract_first()
            time = li.xpath('./p/span[6]/em/text()').extract_first()
            print(title,time)
        return item
