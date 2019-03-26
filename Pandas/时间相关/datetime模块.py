import numpy as np
import pandas as pd
import datetime

#date，只有日期，没有时分秒
today=datetime.date.today()
print(today,type(today))
date=datetime.date(2020,1,1)
print(date)

#完整时间，理论能精确到百万分之一秒
now=datetime.datetime.now()
print(now,type(now))
t1=datetime.datetime(2100,12,21,16)
t2=datetime.datetime(2100,12,21,16,34,51)

#时间差
dt=t2-t1
print(t1,t2,'\n',dt,type(dt))
td=datetime.timedelta(100,2425)#参数：天数、秒数
print(t1+td)

#字符串转日期函数（很牛逼的一个函数）
from dateutil.parser import parse
date_str='2017 February 15 2:15:00 PM'
date=parse(date_str)
print(date)

#作业2.8
#1
print(datetime.datetime.now())
print(datetime.datetime(2017,5,1,12,30))
print(datetime.datetime(2000,12,1))
#2
print(datetime.date(2000,5,1)+datetime.timedelta(1000))