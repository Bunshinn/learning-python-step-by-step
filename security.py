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

def getKeyInfo(url):
    rl=[]
    try:
        r = requests.get(url)
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

def getDetails(url):
    dict={'jd': None, 'title': None, 'company': None, '工作地点' : None, '性质' : None, '薪资' : None, '招聘' : None, '发布时间' : None }
    try:
        r = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        print(e)
    else:
        bs = BeautifulSoup(r.read(),'lxml')
        divs = bs.find_all('div',attrs = {'class':'wbox'})
        if len(divs)>1 :
            dict['jd'] = divs[1].get_text(" ", strip=True)
        else:
            print(url)
        dict['title'] = divs[0].h1.string
        dict['company'] = divs[0].a.string
        for s in divs[0].aside.find_all('span'):
            l = [t for t in s.stripped_strings]
            dict[l[0]] = l[1]
        return dict

url = 'http://search.ccgp.gov.cn/dataB.jsp?searchtype=2&page_index=&dbselect=infox&kw=%E5%AE%89%E9%98%B2&buyerName=&projectId=&start_time=2015%3A11%3A02&end_time=2016%3A05%3A02&timeType=5&bidSort=0&pinMu=0&bidType=0&displayZone=&zoneId=&pppStatus=&agentName='

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

sqlkeyinfo = 'insert into notice (notice,tenderNo,url,keyinfo) values (?,?,?,?)'
for i in range(1,279):
    outlist.extend(getKeyInfo(url.replace('page_index=','page_index='+ str(i))))
    if i%20==0  or i == 278:
        print(i)
        c.executemany(sqlkeyinfo,outlist)
        conn.commit()
        outlist = []

c.close()
conn.close()

##c.executescript("""CREATE TABLE jobdetail (id INTEGER PRIMARY KEY AUTOINCREMENT,
##    title NVARCHAR(32) NOT NULL ,
##    company NVARCHAR(32), 
##    工作地点  NVARCHAR(50), 
##    性质 nvarchar(16), 
##    薪资 nvarchar(32), 
##    招聘 nvarchar(50),
##    jd TEXT,
##    发布时间 nvarchar(50),
##    server_time DATETIME);
##    """)
#
#sqldetail = "INSERT INTO jobdetail (title, company, 工作地点, 性质, 薪资, 招聘, jd, 发布时间, server_time) VALUES (:title, :company, :工作地点, :性质, :薪资, :招聘, :jd, :发布时间, DATETIME('NOW'))"
#
#outlist = []
#diclist = []

#        with open('jobs2.csv','a',newline='',encoding='utf-8') as f:
#            writer = csv.writer(f)
#            writer.writerows(outlist)
#        outlist=[]
#
##for i in range(5):
##    url = t[4]
##    d = getDetails(url)
##    diclist.append(d) 
##    c.executemany(sqldetail, diclist)
##    diclist = []
#    
#    
#conn.commit()
#c.close()
#conn.close()
#
##l=getKeyInfo(url+str(1))
##for i in l:
##    print(l)
#
#
##sql ='''create table accountJobs (
##   ID INTEGER PRIMARY KEY   AUTOINCREMENT,
##   title           nvarchar(50)      NOT NULL,
##   company         nvarchar(100),
##   city            nvarchar(50),
##   salaryRange     nvarchar(50),
##   url         TEXT
##)
##'''
##c.execute(sql)
#
##con = sqlite3.connect(":memory:") #:memory:
##con.text_factory = str
#
##c.executescript("""CREATE TABLE jobdetail (id INTEGER PRIMARY KEY AUTOINCREMENT,
##    title NVARCHAR(32) NOT NULL ,
##    company NVARCHAR(32), 
##    工作地点  NVARCHAR(50), 
##    性质 nvarchar(16), 
##    薪资 nvarchar(32), 
##    招聘 nvarchar(50),
##    jd TEXT,
##    发布时间 nvarchar(50),
##    server_time DATETIME);
##    """)
#
##dl =[]
##sql = "INSERT INTO jobdetail (title, company, 工作地点, 性质, 薪资, 招聘, jd, 发布时间, server_time) VALUES (:title, :company, :工作地点, :性质, :薪资, :招聘, :jd, :发布时间, DATETIME('NOW'))"
##for t in l:
##    url = t[4]
##    d = getDetails(url)
##    c.execute(sql,d)
###    print(d.items())
##    dl.append(d)
#    
##    for (k, v) in d.items():
##        print( "%s : %s" % (k, v))
#    
##cursor.executemany(sql, dl)
#
#
##for row in c.execute("select * from jobdetail"):
##    print( row)
#
#

