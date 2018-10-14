# -*- coding: utf-8 -*-
"""

@author: QQ:412319433
"""

import requests
from bs4 import BeautifulSoup
import sqlite3
import time

s = time.clock()
        
def htmlparse(bs, tag, attr = None, attrs= None):
    '''
    bs : BeautifulSoup对象
    tag : 要处理的标签名
    attr : 要获取属性值的属性名
    attrs : 要查找的属性值对
    '''
    content = bs.find_all(tag, attrs = attrs)
    if attr != None and attrs == None:
        for i in range(len(content)):
            content[i] = content[i][attr]
    else:
        for i in range(len(content)):
            content[i] = content[i].get_text()
    return content
    
def getcontents(url, data):
    try:
        joblist = []
        r = requests.get(url, data)
        bs = BeautifulSoup(r.content.decode())
        bs = bs.find('div', attrs={'class' : 'r_searchlist positiolist'})
        jobname = htmlparse(bs, 'div',attrs={'class' : 'jobname'})
        companyname = htmlparse(bs, 'div',attrs={'class' : 'companyname'})
        education = htmlparse(bs, 'span',attrs={'class' : 'education'})
        salary = htmlparse(bs, 'div',attrs={'class' : 'salary'})
        url = htmlparse(bs, 'a', 'href')
        joblist.extend(list(zip(jobname, companyname, education, salary, url)))
    except:
        print(url)
    finally:
        return joblist

conn = sqlite3.connect('d:/jobs.db')
c = conn.cursor()
c.execute('''
create table jobs(id INTEGER PRIMARY KEY AUTOINCREMENT,
jobname nvarchar(50),
companyname nvarchar(100),
education nvarchar(100),
salary nvarchar(50),
url nvarchar(50)
);
''')

#sql = 'insert into details (id,stime,buyer,agency,noticetype,privonce,memo) values(?, ?, ?, ?, ?, ?,?)'
sql = 'insert into jobs (jobname,companyname,education,salary,url) values(?, ?, ?, ?, ?)'

outlist = []
#for idn,keyinfo in c.fetchall():
#    text = re.split(r'[|]+', keyinfo)
#    agency, noticeclass, _ = text[2].split('\n')
#    outlist.append((idn,text[0].strip(), text[1].strip(), agency.strip(), noticeclass.strip(), text[3].strip(), text[4].strip()))

url = 'http://m.zhaopin.com/shenzhen-765/?'
data = {
        'keyword': '数据分析',
        'maprange' : 3,
        'islocation' : 0,
        'pageindex' : 1
        }
pageNum = 455
for i in range(pageNum):
    data['pageindex'] = i +1
    outlist.extend(getcontents(url, data))
    if i%20 == 0 or i == pageNum:
        c.executemany(sql, outlist)
        conn.commit()
    
c.close()
conn.close()

e = time.clock()
print('use: %f s' % (e - s))