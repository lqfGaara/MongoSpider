# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem


class DoubanspiderSpider(scrapy.Spider):
    name = 'doubanSpider'
    allowed_domains = ['douban.com']
    url = "http://movie.douban.com/top250?start="
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        for node in response.xpath('//div[@class="item"]'):
            item = DoubanItem()
            # 标题
            item["title"] = node.xpath('.//div[ @class ="hd"]/a/span[@class="title"][1]/text()').extract()[0]
            #  剧情简介 strip()去掉字符串中的空格
            item["introduction"] =node.xpath('.// div[ @class ="bd"] / p[@ class =""] / text()').extract()[0].strip()
            #  评价星级
            item["star"] = node.xpath('// div[ @class ="star"] / span[@ class ="rating_num"] / text()').extract()[0]
            #  剧情主题
            movieTheme = node.xpath('.// div[ @class ="bd"] // span[@ class ="inq"] / text()').extract()
            if len(movieTheme) != 0:
                item["movieTheme"] = movieTheme[0]
            yield item
        if self.offset < 250:
            self.offset += 25
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
