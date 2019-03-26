import numpy as np
import pandas as pd

a=['20100609','20130607']
dti=pd.DatetimeIndex(a)
print(dti,type(dti))
print('----------')

s=pd.Series(100*np.random.rand(2),index=dti,name='mytimedata')
print(s)
print(s.index,type(s.index))#以datatime为index的series，即时间序列（time series）
print('----------')

#时间范围，pd.daterange，默认以天为单位
#参数：start（开始）, end（结束）, periods（偏移量）, freq（频率，默认天）, name等
rng1=pd.date_range('2017-1-1','2019-3-24')
print(rng1,type(rng1))
rng2=pd.date_range('2017-1-1','2017-1-5',freq='6H')#D、B、H、T/MIN、S、L、U代表日、工作日、时分秒、毫秒、微秒
print(rng2)
rng3=pd.date_range('2010-1-1 15:30',periods=20,freq='6H',name='mytime')#,normalize=True)
print(rng3)
rng4=pd.date_range('2017-1-1','2018-1-1',closed='left')
print(rng4)

#工作日
print(pd.bdate_range('2019-1-1','2020-1-1',closed='left'))

#freq，每周的星期几，和每月的第几个星期几

#下面两种情况，最前面加个B代表工作日，否则就默认是普通日

#“-”的前面加个S，就是那个月的第1天，否则就默认是那个月最后一天

#周
print(pd.date_range(start='2019-1-1',end='2020-1-1',freq='WOM-3WED'))
print(pd.date_range(start='2019-1-1',end='2020-1-1',freq='W-FRI'))

#月、季度、年
print(pd.date_range('2017','2020',freq='M'))#月末(Month)
print(pd.date_range('2017','2020',freq='Q-JAN'))#季度末(Quarter)，1月开始
print(pd.date_range('2017','2020',freq='A-JUN'))#年指定月的月末（Anniversary）

#改变时间频率，比如原来公司是要一天统计一次，现在改成一天统计四次
ts=pd.Series([np.random.rand() for x in range(4)],index=pd.date_range('2017-1-1','2017-1-4'))
print(ts)
print(ts.asfreq('6H'))#method为填充方法，默认不填充，ffill是前面值填充，bfill是后面值填充

#shift（注意：是把值往前或后移）
a=ts.shift(-1)#值前移
b=ts.shift(1)#值后移
print(a)
print(b)
print(ts-b)#可以看后台和前天比，是赚还是亏

#还是shift，加个freq，可以把索引进行移动
a=ts.shift(-1,freq='D')
b=ts.shift(1,freq='H')
print(a)
print(b)
print('------------')
#作业2.10
#1. 
ts1=pd.Series([np.random.rand() for x in range(5)],index=pd.date_range('2017-1-1','2017-1-5'))
print(ts1)
ts2=pd.Series([np.random.rand() for x in range(4)],index=pd.date_range('2017-1-1','2018-1-8',freq='3M'))
print(ts2)#用Q-JAN也是一样的
ts3=pd.DataFrame(np.reshape([np.random.rand() for x in range(16)],[4,4]),
    columns=['value'+chr(ord('1')+x) for x in range(4)], 
    index=pd.date_range('2017-12-01',periods=4,freq='10min'))
print(ts3)
print('-----------')
#2.
ts1=pd.Series([np.random.rand() for x in range(5)],index=pd.date_range('2017-5-1 12',periods=5,freq='10T'))
print(ts1)
ts2=ts1.asfreq('5T',method='ffill')
print(ts2)