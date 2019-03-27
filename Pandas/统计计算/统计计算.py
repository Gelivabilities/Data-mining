import numpy as np
import pandas as pd

#pandas数据分析工具
df=pd.DataFrame(np.reshape([x+1 for x in range(16)],[4,4]),index=['a','b','c','d'],columns=['x','y','z','t'])
print(df)
print(df.mean(),type(df.mean()))#按列求平均
print(df.T.mean(),'\n',df.mean(axis=1))#按行求平均（空值、非数值会被跳过）
print('-----------')
nan_df=df.copy()
nan_df.iloc[2,3]=np.nan
nan_df.iloc[1,1]=np.nan
print(df,'\n',nan_df.mean(skipna=False))

#常见数学方法
print(df.count(),df.mean(),df.mean(),df.median(),df.std(),df.var(),df.sum())
print('--------')
#skew是样本的偏度，kurt是样本的峰度
print(df.skew(),df.kurt())
print('----------------')
#统计分位数
print(df.quantile(q=0.25))

#累积计算
df['x_sum']=df['x'].cumsum()
df['y_prod']=df['y'].cumprod()#累积乘积
df['z_max']=df['z'].cummax()
df['z_min']=df['z'].cummin()
print(df,'\n-----------------')

#unique
sq=pd.Series(['b','c','a','b','a'])
print(sq,'\n',sq.unique(),'\n')
sq.sort()
print(sq)

#计数，计算每个值出现的频率（默认会排序）
print(sq.value_counts(sort=False))

#成员资格，返回series、df每个元素是否满足条件（注意不是条件里的东西是否在series里面）
print(sq.isin(['a','c','e']))
print(df.isin([2,6,7,12]))
print(sq.isin(['c']))#只有一个元素，也要加个中括号


#作业
df=pd.DataFrame(100*np.random.rand(4,2),columns=['key1','key2'])
print(df,'\n----------------------')
print(df['key1'].mean(),df['key1'].median())
print(df['key2'].mean(),df['key2'].median())
df['key1_cumsum']=df['key1'].cumsum()
df['key2_cumsum']=df['key2'].cumsum()
print(df,'\n------------------')

def SeriesIsUnique(s):
su=s.unique()
return len(su)==len(s)

print(SeriesIsUnique(sq))
print(SeriesIsUnique(pd.Series(['1','啊','a',6])))