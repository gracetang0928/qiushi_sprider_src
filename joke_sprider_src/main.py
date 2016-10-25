#-*- coding:utf-8 -*-
'''
Created on Oct 19, 2016

@author: grace.tang
'''

from HttpHandler import HttpClient
from DataHandler import ExpectedData
from TargetInfo import TargetClass
from DBhandler import DBoperater
import re
import time

qiushi_url = "http://www.qiushibaike.com"
qiushi_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36"}
page_re = r's="page-numbers">\n(\d{2})\n.*?next'
#target_re 中依次对应的糗事百科内容是：作者，内容，点赞数，文章编号，[热评]
target_re = r'.*?<h2>(.*?)<.*?<span>(.*?)</s.*?number">(\d+)</.*?href="/article/(\d+)".*?single-clear"></div>(.*?)\n</div>'
hot_re = r'.*?name">(.*?)</span>.*?text">(.*?)</d'


db = DBoperater.DBhandler("localhost","test","123456","pythontestdb",charset="utf8")

html = HttpClient.gethtml(qiushi_url, qiushi_headers)
#获取页面数
last_page = ExpectedData.getLastPage(html, page_re)
for i in range(1,last_page):
#因为首页时加上页面1不能正确跳转，所以加了一个判断
    if i==1 :
        url = qiushi_url
    url = HttpClient.getEndURL(qiushi_url,"/8hr/page/%d/?s=4924538"%i )
    html2= HttpClient.gethtml(url, qiushi_headers)
    jokes = ExpectedData.getTargetInfo(html2, target_re, hot_re)
    for item in jokes:
#检查当前数据库是否存在这条数据，已存在则不操作，否则执行insert
        check_sql='select count(*) from joke_list where url_number='
        check_sql = check_sql+'"%s"'%item[3]+';'
        result = db.getSelectResult(check_sql)
        if result > 0 :
            continue
        now_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())    
        insert_sql = '''INSERT INTO joke_list(joke_author, joke_content, thumbs_number, hot_author, hot_comment, url_number, operate_time) VALUES ("%s","%s",%d,"%s","%s","%s","%s");'''%(item[0],item[1],item[2],item[4],item[5],item[3],now_time)
        db.insertData(insert_sql)
print "操作完毕！"        
db.close()


