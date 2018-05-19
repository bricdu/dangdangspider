# -*- coding: utf-8 -*-
import scrapy
#from scrapy import Selector
#from scrapy.spiders import Spider
#from dangdang.items import Website
from dangdang.items import DangdangItem
from scrapy.http import Request
import re
import urllib.request
from lxml import etree
import requests
#from scrapy_redis.spiders import RedisSpider
class DdSpider(scrapy.Spider):
    name = 'dd'
    #redis_key = 'dangdangspider:urls'
    allowed_domains = ['dangdang.com']
    start_urls = (
        'http://category.dangdang.com/pg1-cp01.03.00.00.00.00.html',
    )
 

    def parse(self,response):
    #for i in range(1,101):
        
        #contents = requests.get(url)
        #contents = etree.HTML(contents.content.decode('gbk'))
        goodslist = response.xpath('/html/body/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li')
        for goods in goodslist:
            item = DangdangItem()
            #fronturl='/html/body/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li'
            #item['comments'] = goods.xpath('div/p[4]/a/text()').extract()
            #item['detail'] = goods.xpath('div/p[2]/text()').pop()
            item['link'] = goods.xpath('p[1]/a/@href').extract()
            item['_id'] = goods.xpath('@id').extract()#.split('.')[3]
            item['title'] = goods.xpath('a/@title').extract()[0]
            item['detail'] = goods.xpath('p[2]/text()').extract()
            #item['time'] = goods.xpath('div/div/p[2]/text()').pop().replace("/", "")
            item['price'] = goods.xpath('p[3]/span[1]/text()').extract()#.lstrip('¥')
            item['oldprice'] = goods.xpath('p[3]/span[2]/text()').extract()#.lstrip('¥')
            press = goods.xpath('p[5]/span[3]/a/text()').extract()
            if len(press) >0:
                item['press']=press
            else:
                item['press']='unknow'
            #item['time'] = goods.xpath('div/p[5]/span[2]/text()').pop()
            item['discount'] = goods.xpath('p[3]/span[3]/text()').extract()
            #item['category1'] = response.meta["ID4"]       # 种类(小)
            #item['category2'] = response.meta["ID2"]       # 种类(大)
            yield item
        
            #yield item
            for i in range(2,101):
                url = 'http://category.dangdang.com/pg{}-cp01.03.00.00.00.00.html'.format(str(i))#,response.meta["ID1"],response.meta["ID3"])
                yield Request(url,callback=self.parse)