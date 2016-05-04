# -*- coding: utf-8 -*-
"""
Created on Mon May  2 12:09:38 2016

@author: 胡伴山
"""
#import csv
import requests
import urllib.error
from bs4 import BeautifulSoup
import sqlite3
import re

outlist=[]

def getKeyInfo(url, dic):
    rl=[]
    try:
        r = requests.get(url, dic)
        bs = BeautifulSoup(r.content.decode(),'lxml')
        ul = bs.find_all('ul', attrs = {'class' : 'vT-srch-result-list-bid'})
        for u in ul:
            li = u.find_all('li')
            for l in li:
                notice = l.a.get_text()
                url = l.a['href']
                text = l.a.next_sibling
                tenderNo = re.search(r'(?<=招标编号：).{1,25}(?=">)', text).group(0)
                keyinfo = ''.join(l.span.strings)
                rl.append((notice, tenderNo, url, keyinfo))
    except urllib.error.HTTPError as e:
        print(e)
    finally:
        return rl

conn = sqlite3.connect('d:/security.db')
c=conn.cursor()

c.execute('''create table notice (
   ID INTEGER PRIMARY KEY   AUTOINCREMENT,
   notice      nvarchar(50)      NOT NULL,
   tenderNo    nvarchar(50),
   url         nvarchar(100),
   keyinfo       TEXT
);
''')

url = 'http://search.ccgp.gov.cn/dataB.jsp'
dic = {'searchtype' : 2 ,
       'page_index' : 1 ,
       'dbselect' : 'infox' ,
       'kw' : '安防' ,
       'buyerName' : '',
       'projectId' :'' ,
       'start_time': '2015:11:02' ,
       'end_time' : '2016:05:02' ,
       'timeType' : 5 ,
       'bidSort' : 0 ,
       'pinMu' : 0 ,
       'bidType' : 0 ,
       'displayZone' : 0 ,
       'zoneId' : '' ,
       'pppStatus' : '' ,
       'agentName' : ''
       }

sqlkeyinfo = 'insert into notice (notice,tenderNo,url,keyinfo) values (?,?,?,?)'
pageNum = 81
for i in range(1, pageNum):
    dic['page_index'] = i 
    outlist.extend(getKeyInfo(url, dic))
    if i%20==0  or i == pageNum:
        print(i)
        c.executemany(sqlkeyinfo,outlist)
        conn.commit()
        outlist = []

c.close()
conn.close()
