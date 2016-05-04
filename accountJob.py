# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 20:51:35 2016

@author: 胡伴山
"""
import urllib.error
import urllib.request
from bs4 import BeautifulSoup
import sqlite3

def getDetails(jid,url):
    dict={'jd': None, 'title': None, 'company': None, '工作地点' : None, '性质' : None, '薪资' : None, '招聘' : None, '发布时间' : None }
    try:
        r = urllib.request.urlopen(url)
        bs = BeautifulSoup(r.read(),'lxml')
        divs = bs.find_all('div',attrs = {'class':'wbox'})
        dict['title'] = divs[0].h1.string
        dict['company'] = divs[0].a.string
        for s in divs[0].aside.find_all('span'):
            l = [t for t in s.stripped_strings]
            dict[l[0]] = l[1]
        dict['jd'] = divs[1].get_text(" ", strip=True)
    except:
        print(jid,url)
#    else:
#        print('OK')
    finally:
        return dict

conn = sqlite3.connect('d:/jobs.db')
c=conn.cursor()

#c.execute("drop table jobsdetail")
c.executescript("""CREATE TABLE jobsdetail (id INTEGER PRIMARY KEY,
    title NVARCHAR(32) ,
    company NVARCHAR(32), 
    工作地点  NVARCHAR(50), 
    性质 nvarchar(16), 
    薪资 nvarchar(32), 
    招聘 nvarchar(50),
    jd TEXT,
    发布时间 nvarchar(50),
    server_time DATETIME);
    """)

sql = "INSERT INTO jobsdetail (id, title, company, 工作地点, 性质, 薪资, 招聘, jd, 发布时间, server_time) VALUES (:id , :title, :company, :工作地点, :性质, :薪资, :招聘, :jd, :发布时间, DATETIME('NOW'))"
dl = []

c.execute('select id,url from accountJobs order by id')
l = c.fetchall()
lenl = len(l) - 1
for (jid,url) in l:
    d = getDetails(jid,url)
    d['id']=jid
    dl.append(d)
    if jid % 200 == 0 or jid == lenl:
        print(jid)
        c.executemany(sql, dl)
        conn.commit()
        dl = []

#for row in c.execute("select * from jobdetail"):
#    print( row)

c.close()
conn.close()
