# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import *
# 导入setting文件
from scrapy.conf import settings


class DoubanPipeline(object):
    def __init__(self):
        # 获取配置文件
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        doubanDb = settings["MONGODB_NAME"]
        doubanTable = settings["MONGODB_TABLE_NAME"]
        # 建立MongoDB连接
        client = MongoClient(host=host, port=port)
        # 创建数据库
        mydb = client[doubanDb]
        # 创建表名
        self.table = mydb[doubanTable]

    def process_item(self, item, spider):
        data = dict(item)
        self.table.insert(data)
        return item
