#-*- coding:utf-8 -*-
'''
Created on Oct 19, 2016

@author: grace.tang
'''

from HttpHandler import HttpClient
from DataHandler import ExpectedData
from TargetInfo import TargetClass

qiushi_url = "http://www.qiushibaike.com"
qiushi_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36"}
page_re = r's="page-numbers">\n(\d{2})\n.*?next'
target_re = r'.*?<h2>(.*?)<.*?<span>(.*?)</s.*?"number">(.*?)<.*?single-clear"></div>(.*?)\n</div>'
hot_re = r'.*?name">(.*?)</span>.*?text">(.*?)</d'


html = HttpClient.gethtml(qiushi_url, qiushi_headers)
'''
joke_list = ExpectedData.getTargetInfo(html, target_re, hot_re)
for item in joke_list:
    print item[0]
    print item[1]
    print "好笑： ",item[2]
    print "热评： "+item[3]+item[4]
    print "\n"
print "------------------------------------------------------------------------"
'''
last_page = ExpectedData.getLastPage(html, page_re)
for i in range(2,last_page):
    url = HttpClient.getEndURL(qiushi_url,"/8hr/page/%d/?s=4923178"%i )
    print url
    html2= HttpClient.gethtml(url, qiushi_headers)
    jokes = ExpectedData.getTargetInfo(html2, target_re, hot_re)
    for item in jokes:
        print item[0]
        print item[1]
        print "好笑： ",item[2]
        print "热评： "+item[3]+item[4]
        print "\n"
    print "------------------------------------------------------------------------"

    

