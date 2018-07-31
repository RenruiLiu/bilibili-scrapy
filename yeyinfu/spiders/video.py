'''
#video -> av号 ->
0.加请求头，编码用GB18030
1.视频列表:
    VideoLstUrl = 'http://space.bilibili.com/ajax/member/getSubmitVideos?mid='+ userid +'&pagesize=100&page='+ pageNum
    获取一共3页json，获取所有aid进入aidLst
2.合并成为视频url
    VideoUrl = 'https://www.bilibili.com/video/av' + aid
3.进入av号html中 用re取到 "pages"字典里
"part":"瞬间斩杀蛮王，打野皇子对螳螂"
4.存所有的标题进入TitleLst
5.查找标题里有几个'打野皇子'
'''


# -*- coding: utf-8 -*-
import scrapy
import re
import json
from bs4 import BeautifulSoup

class VideoSpider(scrapy.Spider):
    name = 'video'
    userid = '9954236'
    VideoLstUrl = 'http://space.bilibili.com/ajax/member/getSubmitVideos?mid='+ userid +'&pagesize=100&page='
    #allowed_domains = ['https://space.bilibili.com/9954236/#/video']
    start_urls = [VideoLstUrl+'1',VideoLstUrl+'2',VideoLstUrl+'3']

    def parse(self, response):
        reJson = json.loads(response.body)
        aidLst = self.getAidLst(reJson)
        for i in range(len(aidLst)):
            print('这个aidLst是' + str(aidLst))
            VideoUrl = 'https://www.bilibili.com/video/av' + str(aidLst[i])
            try:
                yield scrapy.Request(VideoUrl, callback=self.parse_video)
            except:
                continue

    def getAidLst(self, reJson):
        vlist = reJson.get('data').get('vlist')
        AidSubLst = []
        try:
            for i in range(len(vlist)):
                AidSubLst.append(vlist[i].get('aid'))
            return AidSubLst
        except:
            print('找AidSubLst出错了')
            return []

    def parse_video(self, response):
        try:
            soup = BeautifulSoup(response.body)
            text = soup.findAll('script')[3].get_text()
        except:
            print('soup里找不到东西')
        else:
            matchLst = re.findall(r'"part":".*?"',text)
            if matchLst != []:
                titleDic = {}
                for titleTxt,count in zip(matchLst,range(len(matchLst))):
                    title = titleTxt.replace('"','').replace('part:','')
                    titleDic[count] = title
                yield titleDic
            else:
                print('我日re没找到东西是因为soup找的不对')
