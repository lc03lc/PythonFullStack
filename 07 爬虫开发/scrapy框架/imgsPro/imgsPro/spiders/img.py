import scrapy
from imgsPro.items import ImgsproItem

class ImgSpider(scrapy.Spider):
    name = 'img'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://sc.chinaz.com/tupian/']

    def parse(self, response):
        div_list = response.xpath('//*[@id="container"]/div')
        for div in div_list:
            # name = div.xpath('./p/a[1]/text()')[0].extract()
            src = 'https:' + div.xpath('./div/a/img/@src2').extract_first()
            # print(img)
            item = ImgsproItem()
            item['src'] = src
            yield item