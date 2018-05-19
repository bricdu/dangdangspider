# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
    title = scrapy.Field() #标题
    detail = scrapy.Field() #详情
    #time = scrapy.Field() #时间
    link = scrapy.Field() #链接
    price = scrapy.Field() #价格
    #comment = scrapy.Field() #评论数
    oldprice = scrapy.Field() #原价
    _id = scrapy.Field() #商品id
    discount = scrapy.Field() #折扣
    #category1 = scrapy.Field()  # 种类(小)
    #category2 = scrapy.Field()  # 种类(大)
    #rebate = scrapy.Field() #折扣
    press = scrapy.Field() #出版社
   # shop = scrapy.Field() #店铺名
    #e_book = scrapy.Field() #电子书
   # e_price = scrapy.Field() #电子书价格
