from __future__ import division
import xlrd
import pylab as plt
import math as mt
from numpy import sign as sign
import numpy as np

book = xlrd.open_workbook('ssn.xls')
sheet = book.sheets()[0]
x = sheet.col_values(0, start_rowx=0)
y = sheet.col_values(1, start_rowx=0)
o=0
def run():
    p=[]
    o=abs(max(y,key=abs))
    for i in range(0,len(y)):
        y[i]=y[i]*4096/o
        q=alaw(y[i])
        p.append(q)
    s=[]
    for i in range(0,len(y)):
        r=dealaw(p[i])
        s.append(r)
        
    plt.plot(x,y,'b',label='Input Signal')
    plt.plot(x,s,'r--',label='Decoded Signal')
    plt.plt.legend(loc='upper center',bbox_to_anchor=(0.5,-0.09),  shadow=True, ncol=2)
def alaw(z):
    j=sign(z)
    if(j==1):
        j=0
        
    else:
        j=1
    z=abs(z)
    d=0
    for i in range(0,8):
        q=32*(2**i)
        if(z<q):
            d=i
            break 
    z=z-16*(2**d)
    e=0
    f=2
    if(d!=0):
        f=2**d
    for i in range(0,32):
        g=f*(i+1)
        if(z<g):
            e=i
            break
    h=""
    k=np.binary_repr(j,1)
    l=np.binary_repr(d,3)
    m=np.binary_repr(e,4)
    h=h+k+l+m
    return h

def dealaw(z):
    a=int(z[0])
    if(a==1):
        a=-1
    else:
        a=1
    b=2
    c=int(z[1:4],2)
    if(c!=0):
        b=2**c
    d=int(z[4:],2)
    e=b*(d+1)
    e=e+16*(2**c)
    return e*a
    
run()