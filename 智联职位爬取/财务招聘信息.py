# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 08:27:25 2016

@author: 胡伴山
"""

#import csv
import requests
import urllib.error
from bs4 import BeautifulSoup
import sys
import sqlite3

outlist=[]

def getKeyInfo(url):
    l=[]
    try:
        r = requests.get(url)
        bs = BeautifulSoup(r.content.decode(),'lxml')
        getContent = bs.find_all('a',attrs={'class':'e e2 eck'})
        for t in getContent:
#            t.h3.label.unwrap()
            l.append((''.join(t.h3.strings), t.aside.string, t.i.string, t.em.string, t['href']))
    except urllib.error.HTTPError as e:
        print(e)
    finally:
        return l

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

url = 'http://m.51job.com/search/joblist.php?jobarea=020000&keyword=%E8%B4%A2%E5%8A%A1&keywordtype=2&pageno='

conn = sqlite3.connect('d:/jobs.db')
c=conn.cursor()

c.execute('''create table accountJobs (
   ID INTEGER PRIMARY KEY   AUTOINCREMENT,
   title           nvarchar(50)      NOT NULL,
   company         nvarchar(100),
   city            nvarchar(50),
   salaryRange     nvarchar(50),
   url         TEXT
);
''')
#c.executescript("""CREATE TABLE jobdetail (id INTEGER PRIMARY KEY AUTOINCREMENT,
#    title NVARCHAR(32) NOT NULL ,
#    company NVARCHAR(32), 
#    工作地点  NVARCHAR(50), 
#    性质 nvarchar(16), 
#    薪资 nvarchar(32), 
#    招聘 nvarchar(50),
#    jd TEXT,
#    发布时间 nvarchar(50),
#    server_time DATETIME);
#    """)

sqlkeyinfo = 'insert into accountJobs (title,company,city,salaryRange,url) values (?,?,?,?,?)'
sqldetail = "INSERT INTO jobdetail (title, company, 工作地点, 性质, 薪资, 招聘, jd, 发布时间, server_time) VALUES (:title, :company, :工作地点, :性质, :薪资, :招聘, :jd, :发布时间, DATETIME('NOW'))"

outlist = []
diclist = []
for i in range(1,2257):
    outlist.extend(getKeyInfo(url+str(i)))
    if i%200==0  or i == 2256:
        print(i)
        c.executemany(sqlkeyinfo,outlist)
        conn.commit()
        outlist = []

#        with open('jobs2.csv','a',newline='',encoding='utf-8') as f:
#            writer = csv.writer(f)
#            writer.writerows(outlist)
#        outlist=[]

#for i in range(5):
#    url = t[4]
#    d = getDetails(url)
#    diclist.append(d) 
#    c.executemany(sqldetail, diclist)
#    diclist = []
    
    
conn.commit()
c.close()
conn.close()

#l=getKeyInfo(url+str(1))
#for i in l:
#    print(l)


#sql ='''create table accountJobs (
#   ID INTEGER PRIMARY KEY   AUTOINCREMENT,
#   title           nvarchar(50)      NOT NULL,
#   company         nvarchar(100),
#   city            nvarchar(50),
#   salaryRange     nvarchar(50),
#   url         TEXT
#)
#'''
#c.execute(sql)

#con = sqlite3.connect(":memory:") #:memory:
#con.text_factory = str

#c.executescript("""CREATE TABLE jobdetail (id INTEGER PRIMARY KEY AUTOINCREMENT,
#    title NVARCHAR(32) NOT NULL ,
#    company NVARCHAR(32), 
#    工作地点  NVARCHAR(50), 
#    性质 nvarchar(16), 
#    薪资 nvarchar(32), 
#    招聘 nvarchar(50),
#    jd TEXT,
#    发布时间 nvarchar(50),
#    server_time DATETIME);
#    """)

#dl =[]
#sql = "INSERT INTO jobdetail (title, company, 工作地点, 性质, 薪资, 招聘, jd, 发布时间, server_time) VALUES (:title, :company, :工作地点, :性质, :薪资, :招聘, :jd, :发布时间, DATETIME('NOW'))"
#for t in l:
#    url = t[4]
#    d = getDetails(url)
#    c.execute(sql,d)
##    print(d.items())
#    dl.append(d)
    
#    for (k, v) in d.items():
#        print( "%s : %s" % (k, v))
    
#cursor.executemany(sql, dl)


#for row in c.execute("select * from jobdetail"):
#    print( row)



