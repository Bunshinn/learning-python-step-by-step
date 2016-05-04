# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 21:38:19 2016

@author: 胡伴山
"""

#from urllib.request import urlopen
import urllib
import http.cookiejar 
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import sys

#
#html=urlopen("http://pythonscraping.com/pages/page1.html")
#bsobj=BeautifulSoup(html.read())
#print(bsobj.h1)
#try:
#    html=urlopen("http://www.pythonscraping.com/exercises/se1.html")
#except HTTPError as e:
#    print(e)
#else:
#    print("OK")

login_page="https://passport.csdn.net/account/login"
try:
    cj=http.cookieJar.LWPCookieJar()
    opener=urllib.build_opener(urllib.request.HTTPCookieProcessor(cj),urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    h = urllib.request.urlopen(login_page)  
    
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',  
           'Referer' : '******'} 
           
    postData = {'op' : 'dmlogin',  
            'f' : 'st',  
            'user' : 'huisnotwu', #你的用户名  
            'pass' : '', #你的密码，密码可能是明文传输也可能是密文，如果是密文需要调用相应的加密算法加密  
            'rmbr' : 'true',   #特有数据，不同网站可能不同  
            'tmp' : '0.7306424454308195'  #特有数据，不同网站可能不同  
  
            }  
    
    postData = urllib.parse.urlencode(postData).encode('utf-8') 
    request = urllib.request.Request(login_page, postData, headers)  
    print(request)  
    response = urllib.request.urlopen(request)  
    text = response.read()  
    print(text)

#    op=opener.open("http://blog.csdn.net/")
#    data=op.read()
#    print(data)
except Exception:
    print("error")