import scrapy


class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://nice.ruyile.com/?f=3&p=1']
    # 生成一个url模板
    url = 'https://nice.ruyile.com/?f=3&p='
    for i in range(2,21):
        url = url + str(i)
        start_urls.append(url)

    def parse(self, response):
        # pass
        list = []
        div_list = response.xpath('/html/body/div[4]/div[1]/div[2]/div[@class="tp_list"]')
        for div in div_list:
            data = div.xpath('./div[2]/a/text()')[0].extract()
            # print(data)
            dic = {
                'data': data
            }
            list.append(dic)

        # if self.page_num<=11:
        #     new_url = format(self.url%self.page_num)
        #     self.page_num+=1
        #     # 手动请求发送:callback回调函数用于数据解析
        #     yield scrapy.Request(url=new_url,callback=self.parse)
        print(list)
        return list