import numpy as np
import pandas as pd
import datetime as dt
from numpy.random import rand

rng=pd.date_range('2017-1','2017-3',freq='D')
sr=pd.Series(np.random.rand(len(rng)),index=rng)
print(sr)
print('----------')
#索引和切片（0开始，末端不包含），还是一样，随便切
print(sr[:5],type(sr[:5]))#返回的是满足条件的子series，下面同理
print(sr[6:12])
print(sr[0],type(sr[0]))#直接返回一个值，下面都一样
print(sr['20170109'],type(sr['20170109']))
print(sr[pd.to_datetime('20170109')])
print(sr[dt.date(2017,1,9)])
print(sr[pd.Timestamp('20170109')])
print(sr[pd.date_range('2017-1-10','2017-1-20')])
print(sr[[12,21]])
#更变态的，日期字符串输入还可以少写个日，会把整个月给你直接打印出来
print(sr['2017-1'])#最好还是用标准写法 
print('-----------')

#重复索引（index不一定是唯一值）
print(sr.is_unique,sr.index.is_unique)
#index不唯一的时候，都会返回一个series，包含多个数据项
s_rep=pd.Series(rand(4),index=pd.to_datetime(['20171107','20180105','20190203','20180105']))
print(s_rep)
print(s_rep.is_unique,s_rep.index.is_unique)
print(s_rep['20180105'])
gb=s_rep.groupby(level=0)
print('------------')
print(gb)
print(gb.mean(),gb.sum())#groupby后可以求平均值、求和等

df=pd.DataFrame(rand(10,3),index=pd.date_range('2017-12-1',periods=10,freq='12H'),columns=['value1','value2','value3'])
print(df)
print(df.head(4))#1
print(df.loc[pd.to_datetime('2017-12-4 12')])#2
print(df.loc[pd.date_range('20171204','20171206',closed='left',freq='12H')])