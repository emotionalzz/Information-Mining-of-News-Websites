import scrapy
from goverment.items import GovermentItem

class GovSpider(scrapy.Spider):
    name = 'gov'   #爬虫文件的名称：就是爬虫源文件的唯一标识
    #allowed_domains = ['www.gov.cn']   #允许的域名：用来限定start_urls列表中哪些url可以进行请求发送
    start_urls = ['http://sousuo.gov.cn/column/31421/0.htm']   #起始的url列表：该列表中存放的url会被scrapy自动进行请求的发送
    url='http://sousuo.gov.cn/column/31421/%d.htm'
    page_num = 1
    #用作于数据解析：response参数表示请求成功后对应的响应对象
    #回调函数接受item
    def parse_text(self,response):
        item = response.meta['item']
        text=response.xpath('//*[@id="UCAP-CONTENT"]/p/text()').extract()
        text=''.join(text)
        item['text']=text
        yield item

    def parse(self, response):
        #解析要闻：正文、标题、日期、url
        li_list=response.xpath('//ul[@class="listTxt"]/li')
        for li in li_list:
            item=GovermentItem()
            #xpath返回的是列表，但是列表元素一定是Selector类型的对象
            #extract()返回的所有数据（字符串），存在一个list里。
            #extract_first()返回的是一个string，是extract()结果中第一个值。
            title=li.xpath('./h4/a/text()').extract_first()
            date=li.xpath('./h4/span/text()').extract_first()
            url=li.xpath('./h4/a/@href').extract_first()

            item['title']=title
            item['date']=date
            item['url']=url

            #对详情页发请求获取详情页的页码源码数据
            #手动请求的发送
            #请求传参：meta={}，可以将meta字典传递给请求对应的回调函数
            yield scrapy.Request(url,callback=self.parse_text,meta={'item':item})

        #分页操作
        if self.page_num<=214:
            new_url=format(self.url%self.page_num)
            self.page_num+=1

            yield scrapy.Request(new_url,callback=self.parse)






