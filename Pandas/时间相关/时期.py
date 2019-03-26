import numpy as np
import pandas as pd
import datetime as dt
from numpy.random import rand

#period（时间段）,pd.Period、pd.period_range
p=pd.Period('2019',freq='M')
t=pd.DatetimeIndex(['2017-1-1'])

#普通index是直接字符串赋值，date_range是时间戳索引，period也有index，代表时期索引

print(p,type(p))
print(t,type(t))

print(p+1,p-1)

pr=pd.period_range('2019-1',periods=10,freq='M')
print(pr,type(pr))
print(pr[0],type(pr[0]))

ps=pd.Series([rand() for x in range(10)],index=pr)
print(ps)

#period时期转换(只转换设定好的时间)
pt=pd.Series([rand() for x in range(10)],index=pr.asfreq('W-MON',how='start'))
print(pt.head(4))

#时间戳与时间之间的转换(to_period, to_stamp
print(pr.to_timestamp())
print(pd.Series([rand() for x in range(10)],index=pr.to_timestamp().to_period()).tail(4))

#作业2.11
ps1=pd.Series([rand() for x in range(5)],index=pd.period_range('201701',periods=5,freq='M'))
print(ps1)
ps2=pd.Series([rand() for x in range(5)],index=pd.period_range('20170101',periods=5,freq='2H'))
print(ps2)