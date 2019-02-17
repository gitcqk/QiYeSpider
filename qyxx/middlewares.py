# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
from scrapy import signals
import time
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By   # 查找方式
from selenium.webdriver.support.ui import WebDriverWait   # 负责循环等待
from selenium.webdriver.support import expected_conditions as EC   # 负责条件

class SeleniumMiddleware(object):
    '''
    此类被用于调用浏览器，
    因为是调用浏览器来访问的，所以要使用代理ip必须在浏览器里定义，
    而不是去scrapy里定义，我目前自己没有稳定的付费ip池，所以没有使用。
    另外，验证码问题。目前是手动的。
    '''    
    def process_request(self, request, spider):
        # 使用标记符来判断项目目前所处的状态，0为正常，1为异常,3为爬取详情页信息。
        if spider.flge == 0:
            try:
                spider.browser.get(request.url)
                # 页面循环，直到判断搜索栏出现,超时10秒，0.1秒循环一次。
                try:
                    wait_0 = WebDriverWait(spider.browser,10,0.1).until(
                        EC.presence_of_element_located((By.ID, 'keyword'))
                    )
                except TimeoutException as e:
                    print('*****************首页加载超时啦*****************')
                
                # 这里可以新建对象，用来获取其他地方的企业名称
                key_word = input('请输入要查询的企业名称：')
                spider.browser.find_element_by_id('keyword').send_keys(key_word)
                
                # 经测试，如果下方的强制睡眠时间太短，可能导致无法正常触发搜索。
                time.sleep(1.5)
                spider.browser.find_element_by_id('btn_query').click()
                print('************如有验证码，请进行验证码验证************')

                # 页面循环，直到判断查询页出现，超时20秒，0.1秒循环一次。
                try:
                    wait_1 = WebDriverWait(spider.browser,20,0.1).until(
                        EC.presence_of_element_located((By.ID, 'advs'))
                    )
                except TimeoutException as e:
                    print('*****************加载查询页超时啦*****************')

            except TimeoutException as e:
                # 捕获来自爬虫页设置的加载时间可能造成的异常
                print('*****************窗口开启太久了*****************')
                spider.browser.execute_script('window.stop()')
            time.sleep(1.5)
            return HtmlResponse(url=spider.browser.current_url, body=spider.browser.page_source,
                                encoding="utf-8", request=request)
        elif spider.flge == 1:
            pass

        elif spider.flge == 3:
            pass        


class QyxxSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class QyxxDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
