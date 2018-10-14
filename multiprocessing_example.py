# -*- coding: utf-8 -*-
"""
Created on Thu May  5 17:14:24 2016

@author: Administrator
"""
    
import multiprocessing
import time

def func(msg,t):
    global l
    for i in [x for x in range(3)]:
        l.append(msg)
        print(msg)
        time.sleep(1)
        
l = []
lis = [x for x in range(10)]
if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=4)
    result = []
    for i in lis:
        msg =  i
        result.append(pool.apply_async(func,args= (i, 1)))
    pool.close()
    pool.join()
    for r in result:
        if r.successful():
            print('OK')
        print(r.get())
    print( "Sub-process(es) done.")
print(l)