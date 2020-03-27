# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import os
from bilibili.items import BilibiliItem

class BilibiliPipeline(object):
    def process_item(self, item, spider):
        return item

class BibaVideoTitlesPipeline(object):
    def open_spider(self, spider):
        if not os.path.exists("spiders/bibaStat"):
            os.mkdir("spiders/bibaStat")
        self.f = open('spiders/bibaStat/BibaVideoTitles.txt','w')
        self.csvf = open('spiders/bibaStat/BibaVideoTitles.csv','w')
        self.itemf = open('spiders/bibaStat/BibaItems.csv','w')
        try:
            itemWriter = csv.writer(self.itemf)
            header = list(BilibiliItem().fields.keys())
            itemWriter.writerow(header)
        except:
            pass

    def close_spider(self, spider):
        self.f.close()
        self.csvf.close()

    def process_item(self, item, spider):
        try:
            line = str(dict(item['partsDict'])) + '\n'
            self.f.write(line)
            writer = csv.writer(self.csvf)
            writer.writerow(tuple(dict(item['partsDict']).values()))
            itemWriter = csv.writer(self.itemf)
            headers = list(item.fields.keys())
            values = []
            for header in headers:
                values.append(item[header])
            itemWriter.writerow(values)
        except:
            pass
        return item

class YeyinfuVideoTitlesPipeline(object):
    def open_spider(self, spider):
        if not os.path.exists("spiders/yeyinfuStat"):
            os.mkdir("spiders/yeyinfuStat")
        self.f = open('spiders/yeyinfuStat/YeyinfuVideoTitles.txt','w')
        self.csvf = open('spiders/yeyinfuStat/YeyinfuVideoTitles.csv','w')
        self.itemf = open('spiders/yeyinfuStat/YeyinfuItems.csv','w')
        try:
            itemWriter = csv.writer(self.itemf)
            header = list(BilibiliItem().fields.keys())
            itemWriter.writerow(header)
        except:
            pass

    def close_spider(self, spider):
        self.f.close()
        self.csvf.close()

    def process_item(self, item, spider):
        try:
            line = str(dict(item['partsDict'])) + '\n'
            self.f.write(line)
            writer = csv.writer(self.csvf)
            writer.writerow(tuple(dict(item['partsDict']).values()))
            itemWriter = csv.writer(self.itemf)
            headers = list(item.fields.keys())
            values = []
            for header in headers:
                values.append(item[header])
            itemWriter.writerow(values)
        except:
            pass
        return item
