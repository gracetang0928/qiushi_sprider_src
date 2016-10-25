'''
Created on Oct 19, 2016

@author: grace.tang
'''
#-*- coding:utf-8 -*-
import re
from TargetInfo import TargetClass

def getLastPage(html,page_re):
    pageObj = re.search(page_re,html,re.S)
    if pageObj:
        last_page = int(pageObj.group(1))
    else:
        print "No this data"
        last_page = 0
    return last_page

def getTargetInfo(html,target_re,hot_re):
    com_re = re.compile(target_re,re.S)
    targets = re.findall(com_re, html)
    targetList = []
    for item in targets:
        qiushijoke = TargetClass.Joke(item,hot_re)
        targetList.append(qiushijoke.getData())
    return targetList
