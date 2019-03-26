import numpy as np
import pandas as pd
import datetime

#pandas的时间模块（pandas时间戳）
date1='20170101 14:35:27'
date2=datetime.datetime(2016,10,1,15)
    t1=pd. (date1)
t2=pd.Timestamp(date2)
print(t1,type(t1))
print(t2,type(t2))
print('------------')

t3=pd.to_datetime(date1)
t4=pd.to_datetime(date2)
print(t3,type(t3))
print(t4,type(t4))
print('------------')

#时间索引，timestamp和to_datetime就不同了
date_list=['2018-12-21','2007-7-6','1995-7-29']
t5=pd.to_datetime(date_list)
#t6=pd.Timestamp(date_list) #datelist就不能转换成timestamp了
print(t5,type(t5))#datetimeIndex类型
print('------------')

d_list=['2102-6-6','非时间字符串','1966-6-6']
t6=pd.to_datetime(d_list,errors='coerce')#ignore返回数组，啥都不填默认raise
print(t6)
print('------------')

#作业2.9
#1.
year,month=2016,2
days=(datetime.date(year,month+1 if not month==12 else 1,1)-datetime.date(year,month,1)).days
date_lst=[str(year)+str('-')+str(month)+str('-')+str(x+1) for x in range(days)]
t=pd.to_datetime(date_lst)
print(t,'\n月中：',t[(days+days%2)/2-1])
print('------------')
#2.
a=open('d:\\a.txt','r').readlines()
print(a)
print(pd.to_datetime(a[0].split(',')))