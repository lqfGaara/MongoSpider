# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # 电影标题
    title = scrapy.Field()
    # 电影简介
    introduction=scrapy.Field()
    # 电影评级
    star=scrapy.Field()
    # 电影主题
    movieTheme=scrapy.Field()