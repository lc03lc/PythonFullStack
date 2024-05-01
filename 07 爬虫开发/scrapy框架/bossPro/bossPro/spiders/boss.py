import scrapy
from bossPro.items import BossproItem

class BossSpider(scrapy.Spider):
    name = 'boss'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.zhipin.com/c101220100-p100109/?ka=search_100109']

    # 回调函数接收item
    def parse_detail(self,response):
        item = response.meta['item']
        job_desc = response.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div//text()').extract()
        job_desc = ''.join(job_desc)
        print(job_desc)
        item['job_desc'] = job_desc
        yield item

    def parse(self, response):
        li_list = response.xpath('//*[@id="main"]/div/div[3]/ul/li')
        for li in li_list:
            item = BossproItem()
            job_name = li.xpath('./div/div[1]/div[1]/div/div[1]/span[1]/a/text()')[0].extract()
            item['job_name'] = job_name
            print(job_name)
            detail_url ='https://www.zhipin.com/' +  li.xpath('./div/div[1]/div[1]/div/div[1]/span[1]/a/@href')[0].extract
            # 对详情页发请求，获取源码数据
            # 手动请求的发送
            # 请求传参：meta={},可以将meta字典传递给对应的回调函数
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})