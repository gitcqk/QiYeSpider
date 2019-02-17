# -*- coding: utf-8 -*-
import scrapy
from qyxx.items import QyxxItem
from selenium import webdriver

class MySpider(scrapy.Spider):
    name = 'my'
    allowed_domains = ['gsxt.gov.cn']
    start_urls = ['http://www.gsxt.gov.cn/index.html']

    def __init__(self):
        # 创建浏览器
        self.browser = webdriver.Firefox(executable_path='C:\Program Files\Mozilla Firefox\geckodriver.exe')
        # 设定浏览器大小（半屏）
        self.browser.set_window_size(960,1080)
        # 控制最大时间，超时会在中间件中停止
        self.browser.set_page_load_timeout(300)
        self.flge = 0

    # 复写关闭爬虫时触发关闭浏览器
    def closed(self,spider):
        print('*****************爬虫关闭啦*****************')
        self.browser.close()

    def parse(self, response):
        item = QyxxItem()
        # 这里判断下请求是否正常
        if response.status == 200:
            a_list = response.xpath('//*[@id="advs"]/div/div[2]/a')
            for a in a_list:
                # 网站里公司的名字分为搜索关键字名字（红色）,和黑色的，两者位置不同都要读取。
                name_red = a.xpath('./h1/font/text()').extract_first()
                name_black = a.xpath('./h1/text()').extract()[-1]
                # print('测试黑名字' + str(name_black) + '数量' + str(len(name_black)))
                item['name'] = name_red + name_black
                item['id_code'] = a.xpath('./div[2]/div[1]/span/text()').extract_first()
                item['url_x'] = a.xpath('./@href').extract_first()
                item['people'] = a.xpath('./div[2]/div[2]/span/text()').extract_first()
                item['time'] = a.xpath('./div[2]/div[3]/span/text()').extract_first()
                item['zhuangtai'] = a.xpath('./div[1]/span/text()').extract_first()

                # 已读取了详情页url_x，下边访问并设定新的callback即可。这里不写了。
                # yield scrapy.Request(item['url_x'], callback=self.parse_ziye,meta=item)
                yield item
        else:
            pass
    
        def parse_ziye(self, response):
            pass

