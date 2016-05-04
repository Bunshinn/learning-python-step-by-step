# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 20:50:39 2016

@author: 胡伴山
"""
import sys
from io import BytesIO
import numpy as np;
#import scipy as sp;
from matplotlib.pyplot import plot;
from matplotlib.pyplot import show;
#import pylab as pl;
#import codecs
#import struct
#from binascii import *

#s=u'hello'
#sa=b2a_hex(s)
#print(sa)
#print(unicode(s))
#b=struct.pack('5s',s)

a=np.array([1,2,3,4])
b=np.array([5,6,7,8,9])
a = np.arange(9)
a[3:7]
a[:7:2]
a[::-1]

b = np.arange(24).reshape(2,3,4)
b.shape
b
b[0,0,0]
b[:,0,0]
b[0,:,:]
b[0,...]
b[0,1]
b[0,1,::2]
b[...,1]
b[:,1]
b[0,:,1]
b[0,:,-1]
b[0,::-1,-1]
b[::-1]

b.ravel()
b.flatten()
b.shape=(6,4)
b.transpose()
b.resize((2,12))

a = a.reshape(3,3)
b = 2 * a
np.hstack((a,b))
np.concatenate((a,b), axis=0)
np.vstack((a, b))
np.vstack((b, a))
np.dstack((a, b))

oned = np.arange(2)
toned = 2 * oned
np.column_stack((oned,toned))
np.row_stack((oned, toned))

np.hsplit(a, 3)
np.vsplit(a, 3)
np.split(a, 3, axis = 0)
np.median()

#
#s = '电影双击查看原图'
#type(s)
#s1 = s.encode('utf8')
#type(s1)
#print(s1)
#s2 = s1.decode('latin-1')
#print(s2)
#s3 = s2.encode('latin-1').decode('utf-8')
#print(s3)

b = np.arange(24).reshape(2,12)
b.ndim
b.size
b.itemsize
b.nbytes
b.resize(4,6)
b.T
b.transpose()

b = np.array([1.j + 1,3 + 2.j])
b.real
b.imag
b.dtype
b.dtype.str

b = np.arange(4).reshape(2,2)
f = b.flat
for i in f: print(i)
b.flat[3]
b.flat[[1,3]]

b.tolist()
b.astype(int)

i2 = np.eye(2)
np.savetxt("d:/eye.txt",i2)

#c,v = np.loadtxt('d:/data.csv',delimiter=',',usecols=(6,7),unpack=True)
o,h,l,c,v = np.loadtxt(BytesIO(open('d:/table.csv').read().encode()),delimiter=',',
                       usecols=(1,2,3,4,5),unpack=True)
vwap = np.average(c,weights=v)

N = int(sys.argv[1])
N = 20
h = h[-N:]
l = l[-N:]
pc = c[-N-1: -1]
w = np.ones(N)/N
sma = np.convolve(w,c)[N-1:-N+1]
t = np.arange(N-1, len(c))
plot(t,c[N-1:],lw = 1.0)
plot(t,sma, lw=2.0)
show()

x = np.arange(5)
np.exp(x)
np.linspace(-1 ,0, 5)

w = np.exp(np.linspace(-1, 0, N))
w /= w.sum()
ema = np.convolve(w, c)[N-1:-N+1]
t = np.arange(N-1,len(c))
plot(t,c[N-1:], lw = 1.0)
plot(t,ema,lw = 2)

dev = []
C = len(c)
for i in range(N-1,C):
    if i + N < C:
        d = c[i: i+ N]
    else:
        d = c[-N]
    avg = np.zeros(N)
    avg.fill(sma[i - N - 1])
    d = d - avg
    d = d ** 2
    d = np.sqrt(np.mean(d))
    dev.append(d)
dev = 2 * np.array(dev)
ub = sma + dev
lb = sma - dev

t = np.arange(N-1, C)
c_slice = c[N-1:]
plot(t,c_slice, lw=1.)
plot(t,sma,lw=2)
plot(t,ub, lw = 3)
plot(t, lb, lw = 4)
show()

s = 'hello,world'
s[::-1]

l = ['helLo','gO',5,4]
[e.lower() if  type(e) is str else e for e in l]