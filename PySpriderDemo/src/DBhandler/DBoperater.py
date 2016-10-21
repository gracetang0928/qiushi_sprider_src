'''
Created on Oct 19, 2016

@author: grace.tang
'''
#-*- coding:utf-8 -*-
import MySQLdb
class DBhandler:
    def __init__(self,dbhost,uname,pword,dbname,charset):
        self.db = MySQLdb.connect(dbhost,uname,pword,dbname,charset=charset)
        self.cursor = self.db.cursor()
    def commit(self):
        self.db.commit()
 
    def insert(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()
    
    def close(self):
        self.db.close()