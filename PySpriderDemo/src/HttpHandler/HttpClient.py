#-*- coding:utf-8 -*-

'''
Created on Oct 19, 2016

@author: grace.tang
'''
import urllib2

def getEndURL(url,urlprame):
    endurl = url+urlprame
    return endurl


def gethtml(url,headers,**arg):
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    html = response.read()
    return html
    