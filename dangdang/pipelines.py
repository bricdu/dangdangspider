# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#from scrapy.conf import settings
#from .items import DangdangItem
#from dangdang.items import DangdangItem

class DangdangPipeline(object):
    def process_item(self, item, spider):
        print(item['title'])
        print(item['press'])
        print(item['_id'])
        print(item['price'])
        print(item['oldprice'])
        print(item['discount'])
        #print(item['time'])
        print(item['link'])
        #print(item['comment'])
        
        
       
        #print(item['category1'])
        #print(item['category2'])
        
        print(item['detail'])
        return item
