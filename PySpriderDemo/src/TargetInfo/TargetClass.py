#-*- coding:utf-8 -*-
import re
class Joke:
    def __init__(self,tjoke,joke_hot):
        self.author = tjoke[0]
        self.content = tjoke[1].replace('<br/>',"\n")
        self.number = int(tjoke[2])
        self.matchObj = re.search(joke_hot,tjoke[3],re.S)
        if self.matchObj:
            self.hot_author = self.matchObj.group(1)
            self.hot_comment = self.matchObj.group(2)
        else:
            self.hot_author = ""
            self.hot_comment = ""

    def getData(self):
        return (self.author,self.content,self.number,self.hot_author,self.hot_comment)
    