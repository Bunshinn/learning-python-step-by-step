#-*- coding: utf-8 -*-

import sqlite3

def maxs(li):   
    li=[float(i) for i in li]
    tmp=max(li)
    outli=list()
    for i in range(len(li)):
        if li[i]==tmp:
            outli.append(i)
    return outli

outlist=list()
f=open(r'd:\document\myPython\avgrate2.txt','rt',encoding='utf-8',errors='ignore')
for l in f.readlines():
	li=l.split('|')
	outlist.append(maxs(li))
	
print(outlist)
#
#con = sqlite3.connect(":memory:")
#con.isolation_level = None
#c = con.cursor()
#
#c.execute('''create table dictable(word text,frequency integer,tags text)
#''')
#
#purchases = []
#for l in t.splitlines():
#    li=l.split(" ")
#    if len(li)==2:
#        c.execute("insert into dictable (word,frequency) values(?,?)",li)
#    elif len(li)==3:
#        c.execute("insert into dictable values(?,?,?)",li)
#    else:
#        pass
#
## c.executemany('INSERT INTO dictable VALUES (?,?,?)', purchases)
# 
## print(c.fetchone())
#for row in c.execute('SELECT * FROM dictable order by frequency desc'):
#    print(row)
#
#c.close()