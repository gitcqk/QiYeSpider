# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from qyxx import settings

class QyxxPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host = settings.MYSQL_HOST,
            port = settings.MYSQL_PORT,
            db = settings.MYSQL_DBNAME,
            user = settings.MYSQL_USER,
            passwd = settings.MYSQL_PASSWORD,
            charset = 'utf8',
            use_unicode = True )
        self.cursor = self.connect.cursor()

    # 数据入库方法
    def insertData(self, item):
        sql = "insert into qyxx(name, id_code, url_x, people, time, zhuangtai) VALUES(%s, %s, %s, %s, %s, %s);"
        params = (item['name'], item['id_code'], item['url_x'], item['people'], item['time'], item['zhuangtai'])
        self.cursor.execute(sql, params)
        self.connect.commit()

    # 数据清洗方法
    def cls(self, item):
        name_cls = item['name']
        if name_cls:
            item['name'] = name_cls.strip().replace('\n','').replace(' ','').replace('\t','')

        id_code_cls = item['id_code']
        if id_code_cls:
            item['id_code'] = id_code_cls.strip().replace('\n','').replace(' ','').replace('\t','')

        url_x_cls = item['url_x']
        if url_x_cls:
            item['url_x'] = url_x_cls.strip().replace('\n','').replace(' ','').replace('\t','')

        people_cls = item['people']
        if people_cls:
            item['people'] = people_cls.strip().replace('\n','').replace(' ','').replace('\t','')
        
        time_cls = item['time']
        if time_cls:
            item['time'] = time_cls.strip().replace('\n','').replace(' ','').replace('\t','')

        zhuangtai_cls = item['zhuangtai']
        if zhuangtai_cls:
            item['zhuangtai'] = zhuangtai_cls.strip().replace('\n','').replace(' ','').replace('\t','')

    # 执行    
    def process_item(self, item, spider):
        self.cls(item)
        self.insertData(item)
        return item