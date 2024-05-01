import scrapy
from selenium import webdriver
from newsPro.items import NewsproItem
from selenium.webdriver.edge.options import Options
edge_options = Options()
edge_options.add_argument('--headless')
edge_options.add_argument('--disable-gpu')
# 如何规避检测
edge_options.add_experimental_option('excludeSwitches',['enable-automation'])

class NewsSpider(scrapy.Spider):
    name = 'news'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.163.com/']
    module_urls = []

    def __init__(self):
        self.bro = webdriver.Edge(executable_path='../edgedriver_win64/msedgedriver.exe',options=edge_options)

    def parse(self, response):
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        alist = [2,3]
        for index in alist:
            src = li_list[index].xpath('./a/@href').extract_first()
            self.module_urls.append(src)
            # print(src)
            yield scrapy.Request(url=src,callback=self.detail_parse)

    def detail_parse(self,response):
        div_list = response.xpath('/html/body/div/div[3]/div[4]/div[1]/div[1]/div/ul/li/div/div')
        for div in div_list:
            title = div.xpath('./div/div/h3/a/text()').extract_first()
            detail_src = div.xpath('./div/div/h3/a/@href').extract_first()
            # print(title,detail_src)
            item = NewsproItem()
            item['title'] = title
            yield scrapy.Request(url=detail_src, callback=self.content_parse,meta={'item':item})

    def content_parse(self,response):
        content = response.xpath('//*[@id="content"]/div[2]//p/text()').extract()
        content = ''.join(content)
        # print(content)
        item = response.meta['item']
        item['content'] = content
        yield item



    def closed(self,spider):
        self.bro.quit()