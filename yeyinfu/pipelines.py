# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class YeyinfuPipeline(object):
    def process_item(self, item, spider):
        return item

class YeyinfuVideoTitlesPipeline(object):
    def open_spider(self, spider):
        self.f = open('YeyinfuVideoTitles.txt','w')
        self.csvf = open('YeyinfuVideoTitles.csv','w')

    def close_spider(self, spider):
        self.f.close()
        self.csvf.close()

    def process_item(self, item, spider):
        try:
            line = str(dict(item)) + '\n'
            self.f.write(line)
            writer = csv.writer(self.csvf)
            writer.writerow(tuple(dict(item).values()))
        except:
            pass
        return item
