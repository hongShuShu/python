# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from beike.items import BeikeItem
from scrapy.spiders import Spider

class BeiKeSpider(Spider):
    name = "zhaofang"
    allowed_domains = ["fang.ke.com"]
    url = "https://ty.fang.ke.com/loupan/pg"
    page = 1
    start_urls = [url + str(page)]

    def parse(self, response):
        for each in response.xpath("//div[@class='resblock-name']"):
            item = BeikeItem()

            name = each.xpath("./a/text()").extract()[0]
            detailurl = each.xpath("./a/@href").extract()[0]


            # 表示当前节点的兄弟节点中的 第 1 个 div标签
            location_area = each.xpath("./following-sibling::div[1]/span/text()").extract()[0]
            location_block = each.xpath("./following-sibling::div[1]/span/text()").extract()[1]
            location_road = each.xpath("./following-sibling::div[1]/a/text()").extract()[0]
            location = location_area + location_block + location_road

            area = each.xpath("./following-sibling::div[2]/span/text()").extract()

            price_list= each.xpath("./following-sibling::div[5]/div[@class='main-price']/span/text()").extract()
            price = ''
            if len(price_list) > 1:
                price_number = price_list[0]
                price_unit = price_list[1]
                price = price_number + price_unit

            total = each.xpath("./following-sibling::div[5]/div[@class='second']/text()").extract()

            item['name'] = name
            item['detailurl'] = "https://ty.fang.ke.com"+detailurl
            item['location'] = location
            item['area'] = area
            item['price'] = price
            item['total'] = total

            yield item

        if self.page < 22:
            self.page += 1

            newurl = self.url + str(self.page)
            # 回调parse方法，接着爬下一个页面
            yield scrapy.Request(newurl, callback = self.parse, dont_filter=True)
