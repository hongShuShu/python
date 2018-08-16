# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BeikeItem(scrapy.Item):
    # 小区名称
    name = scrapy.Field()
    # 小区位置
    location = scrapy.Field()
    # 面积
    area = scrapy.Field()
    # 单价
    price = scrapy.Field()
    # 总价(30万起)
    total = scrapy.Field()
    # 楼盘介绍页
    detailurl = scrapy.Field()
