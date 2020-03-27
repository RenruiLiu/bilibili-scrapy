'''
#video -> av号 ->
0.加请求头，编码用GB18030
1.视频列表:
    videoLstUrl = 'http://space.bilibili.com/ajax/member/getSubmitVideos?mid='+ userid +'&pagesize=100&page='+ pageNum
    获取一共n页json，获取所有aid进入aidLst
2.合并成为视频url
    VideoUrl = 'https://www.bilibili.com/video/av' + aid
3.进入av号html中 用re取到 "pages"字典里
"part":"瞬间斩杀蛮王，打野皇子对螳螂"
4.存所有的标题进入TitleLst
5.查找标题里有几个'皇子'
'''

# -*- coding: utf-8 -*-
import urllib.request
import scrapy
import re
import json
from bs4 import BeautifulSoup
from bilibili.items import BilibiliItem

class BibaSpider(scrapy.Spider):
    #配置 爬虫名
    name = 'biba'
    #配置 B站用户ID
    userid = '367877'
    #配置 接口
    videoLstUrl = 'http://space.bilibili.com/ajax/member/getSubmitVideos?mid='+ userid +'&pagesize=100&page='
    # 加了allowed_domains之后跑不动
    # allowed_domains = ['https://bilibili.com/','https://space.bilibili.com/']

    #先进第一页，看总数有多少页
    with urllib.request.urlopen(videoLstUrl+str(1)) as response:
        html = response.read()
        reJson = json.loads(html)
        maxPages = reJson.get('data').get('pages')
        pages = range(1,maxPages+1)
        # pages = range(1,2) #瑞兽dummy
        urls = []
        for i in pages:
            urls.append(videoLstUrl+ str(i))
        start_urls = urls
        print('即将开始爬以下url:========================================================================')
        print(start_urls)
        print('开始:========================================================================')

        def parse(self, response):
            reJson = json.loads(response.body)
            aidLst = self.getAidLst(reJson)
            for i in range(len(aidLst)):
                # print('这个aidLst是' + str(aidLst))
                avAddress = 'https://www.bilibili.com/video/av'
                videoUrl = avAddress + str(aidLst[i])
                try:
                    yield scrapy.Request(videoUrl, callback=self.parse_video)
                except:
                    continue

        def getAidLst(self, reJson):
            vlist = reJson.get('data').get('vlist')
            aidSubLst = []
            try:
                for i in range(len(vlist)):
                    aidSubLst.append(vlist[i].get('aid'))
                return aidSubLst
            except:
                print('找aidSubLst出错了')
                return []

        def parse_video(self, response):
            item = BilibiliItem()

            try:
                soup = BeautifulSoup(response.body)
                scriptText = soup.findAll('script')[3].get_text()
            except:
                print('soup里找不到东西')
            else:
                #title
                titles = re.findall(r'"title":".+?"',scriptText)
                title = titles[0].replace('"title":','').replace('"','')
                item['title'] = title
                #related
                relatedArr = []
                for rawRelateTitle in titles[2:] :
                    relatedtitle = rawRelateTitle.replace('"title":','').replace('"','')
                    relatedArr.append(relatedtitle)
                item['related'] = relatedArr
                #aid
                aids = re.findall(r'"aid":\d+',scriptText)
                item['av'] = aids[0].replace('"aid":','')
                #bvid
                bvids = re.findall(r'"bvid":"BV.+?"',scriptText)
                item['bv'] = bvids[0].replace('"bvid":','').replace('"','')
                #pic
                pics = re.findall(r'"pic":".+?"',scriptText)
                pic = pics[0].replace('"pic":','').replace('"','')
                item['pic'] = pic.encode('latin-1').decode('unicode_escape')
                #desc
                descs = re.findall(r'"desc":".+?"',scriptText)
                desc = descs[0].replace('"desc":','').replace('"','')
                item['desc'] = desc
                #partsDict
                matchLst = re.findall(r'"part":".*?"',scriptText)
                if matchLst != []:
                    titleDic = {}
                    for titleTxt,count in zip(matchLst,range(len(matchLst))):
                        title = titleTxt.replace('"','').replace('part:','')
                        titleDic[count] = title
                    #此处yield的东西会出现在pipeline中
                    item['partsDict'] = titleDic
                #pubdate
                pubdate = re.findall(r'"pubdate":\d+',scriptText)
                item['pubdate'] = pubdate[0].replace('"pubdate":','')
                #viewseo
                viewseo = re.findall(r'"viewseo":\d+',scriptText)
                item['viewseo'] = viewseo[0].replace('"viewseo":','')
                #numOfComments
                numOfComments = re.findall(r'"reply":\d+',scriptText)
                item['numOfComments'] = numOfComments[0].replace('"reply":','')
            yield item
