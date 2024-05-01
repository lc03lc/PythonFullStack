# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 管道文件中一个管道类对应将一组数据存储到一个平台或者载体中
class QiubaiproPipeline:
    fp = None
    # 重写父类的方法：该方法只会被调用一次
    def open_spider(self,spider):
        print('开始爬虫......')
        self.fp = open('./qiubai.txt','w',encoding='utf-8')

    # 接收item对象
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        # 持久化存储
        self.fp.write(author+': '+content+'\n')
        # 如果return item，就会传递给下一个管道类
        return item

    def close_spider(self,spider):
        print('结束爬虫！')
        self.fp.close()
