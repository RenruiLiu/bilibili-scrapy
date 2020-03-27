# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliItem(scrapy.Item):
    #视频标题
    title = scrapy.Field()
    #av号
    av = scrapy.Field()
    #bv号
    bv = scrapy.Field()
    #封面图 
    pic = scrapy.Field()
    #简介 需要unicode转中文
    desc = scrapy.Field()
    #分P标题
    partsDict = scrapy.Field()
    #发布时间(时间戳)
    pubdate = scrapy.Field()
    #播放量
    viewseo = scrapy.Field()
    #评论数
    numOfComments = scrapy.Field()
    #相关推荐标题
    related = scrapy.Field()
    pass
