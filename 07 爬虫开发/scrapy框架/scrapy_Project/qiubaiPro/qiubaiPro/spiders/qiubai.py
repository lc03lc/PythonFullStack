import scrapy
from qiubaiPro.items import QiubaiproItem

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.pearvideo.com/category_5']

    # def parse(self, response):
    #     # pass
    #     # 解析作者名称和段子内容
    #     li_list = response.xpath('//*[@id="listvideoListUl"]/li')
    #     all_data = []
    #     for li in li_list:
    #         # extract可以将Selector对象中的data参数存储在字符串中提取出来
    #         author = li.xpath('./div/div/a/text()')[0].extract()
    #         content = li.xpath('./div/a/div[2]/text()')[0].extract()
    #         # print(author,content)
    #         dic = {
    #             'author': author,
    #             'content': content
    #         }
    #         all_data.append(dic)
    #     return all_data

    def parse(self, response):
        # pass
        # 解析作者名称和内容
        li_list = response.xpath('//*[@id="listvideoListUl"]/li')
        all_data = []
        for li in li_list:
            # extract可以将Selector对象中的data参数存储在字符串中提取出来
            author = li.xpath('./div/div/a/text()')[0].extract()
            content = li.xpath('./div/a/div[2]/text()')[0].extract()
            # print(author,content)

            item = QiubaiproItem()
            item['author'] = author
            item['content'] = content

            yield item #将item提交给了管道