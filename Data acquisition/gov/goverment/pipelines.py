# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from openpyxl import Workbook
#创建工作簿,同时页建一个sheet
#wb = Workbook()
#调用得到的sheet,并命名为test1
#ws = wb.active
#active返回的是一个列表
#ws.title = 'test1'
#插入数据
#ws.append([...])
#保存工作簿,在当前目录下文件名为test1.xlsx
#wb.save('test1.xlsx')

class GovermentPipeline:
    #fp = None
    #重写父类的一个方法:该方法只在开始爬虫的时候被调用一次
    def __init__(self):
        self.spider = None
        self.count = 0

    def open_spider(self,spider):
        print('开始爬虫……')
        self.wb = Workbook() #class实例化
        self.ws = self.wb.active #激活工作表
        self.ws.append(['正文','标题','日期','url']) #设置表头
        #self.fp = open('./gov.txt','w',encoding='utf-8')

    #专门用来处理item类型对象
    #该方法可以接收爬虫文件提交过来的item对象
    #该方法每接收到一个item就会被调用一次
    def process_item(self, item, spider):
        line= [item['text'],item['title'],item['date'],item['url']]
        self.ws.append(line)
        self.wb.save('gov4.xlsx')
        #title = item['title']
        #date = item['date']
        #url = item['url']
        #text=item['text']
        #print(item)
        #self.fp.write(item['title']+'\n'+item['date']+'\n'+item['url']+'\n'+item['text'])
        return item

    def close_spider(self,spider):
        print('结束爬虫！')
        #self.fp.close()

