import scrapy


class MiddleSpider(scrapy.Spider):
    # 进行请求的拦截并且设定UA和IP的更改，爬取百度
    name = 'middle'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.baidu.com/s?wd=ip']

    def parse(self, response):
        page_text = response.text

        with open('ip.html','w',encoding='utf-8') as fp:
            fp.write(page_text)
