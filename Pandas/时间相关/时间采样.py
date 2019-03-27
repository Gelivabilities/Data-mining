import numpy as np
import pandas as pd
from numpy.random import rand

#时间序列重采样
#降采样：高频→低频
#升采样：低频→高频
rng=pd.date_range('20180101',periods=12)
ts=pd.Series(np.arange(1,13),index=rng)
print(ts)
print('-------------')
ts_r=ts.resample('5D')
ts_sum=ts_r.sum()
print(ts_r,'\n',type(ts_r),'\n',ts_sum,type(ts_sum.index))
print('-------------')
#看来和groupby有点像
#不过和groupby的区别就是，groupby是对同一时间戳整合
#重采样是对时间戳整合，变成新的（还是）时间戳，注意不是时间段，所以为什么叫采样 

#其他重采样函数，ohlc: open开盘，close收盘，high、low是最值
print(ts_r.mean(),ts_r.max(),ts_r.last(),ts_r.median(),ts_r.first(),ts_r.ohlc())
print('-------------------')

#closed参数，和date_range的不一样
#不写的话，默认其实就是left
print(ts.resample('5D',closed='left').sum(),'\n',ts.resample('5D',closed='right').sum())
print('---------------')

#升采样：
#asfreq：用空值，不填充
#ffill、bfill前值、后值填充
print(ts_r.sum().resample('1D').asfreq())
print(ts_r.sum().resample('1D').ffill())
print(ts_r.sum().resample('1D').bfill())
print('-----------')

#采样同样适用于时期数据
prng=pd.period_range('2018-1',periods=10,freq='M')
ps=pd.Series(np.arange(1,11),index=prng)
print(ps)
print(ps.resample('W',closed='left').asfreq())
print(ps.resample('Q').sum())
print('---------------')


#作业
ts1=pd.Series(rand(10),index=pd.date_range('20170101',periods=10))
print(ts1)
ts2=ts1.resample('3D').sum()
print(ts2)
ts3=ts1.resample('12H').ffill()
print(ts3)