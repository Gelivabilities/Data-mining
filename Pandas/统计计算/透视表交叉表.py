import numpy as np
import pandas as pd

#透视表（pivot table）
date_index=list(pd.date_range('2017-5-1',periods=3))*3
key=list('abcdabcda')
values=np.random.rand(9)
df=pd.DataFrame({'date':date_index,'key':key,'values':values})
print(df)
print('---------')

pvt=pd.pivot_table(df,values='values',index='date',columns='key',aggfunc='sum')
print(pvt,'\n',type(pvt))#透视表也是个dataframe

#也可以多列聚合，表示数据的方式不一样
pvt_mc=pd.pivot_table(df,values='values',index=['date','key'],aggfunc='sum')
print(pvt_mc,type(pvt_mc),type(pvt_mc.index))#一般也是变成一个dataframe，不过这个例子的values只有一列，所以type是series了
print('-----------')

#交叉表（crosstab）
df=pd.DataFrame({'A':[1,2,2,2,2],'B':[3,3,4,4,4],'C':[1,1,np.nan,1,1]})
print(df,'\n')
print(pd.crosstab(df['A'],df['B']),'\n')
print(pd.crosstab(df['A'],df['B'],normalize=True),'\n')#归一化参数，默认false，否则归一化成百分比
print(pd.crosstab(df['A'],df['B'],values=df['C'],aggfunc=sum),'\n')#用A、B的不同取值，对C列求和
print(pd.crosstab(df['A'],df['B'],margins=True))#margin它会给你加个合计
print('-----------')

#作业
df=pd.DataFrame({'A':['one','two','three','one','two','three','one','two'],
                 'B':list('hhhhffff'),
                 'C':[10+2*x for x in range(8)],
                 'D':np.random.rand(8),
                 'E':np.random.rand(8)})
print(df,'\n')

#以A列聚合，求C、D列的平均值
print(pd.pivot_table(df[['A','B','C','D']],index='A',aggfunc='mean'),'\n')#透视表实现
print(df.groupby('A')['C','D'].mean(),'\n')#重温groupby方法

#以A、B列聚合，求D、E的均值和求和
print(df.groupby(['A','B'])['D','E'].agg({'mean':np.mean,'sum':np.sum}),'\n')#重温groupby的agg方法
#只能拆开做了，pivot_table根本不可能做成groupby的那样子
print(pd.pivot_table(df[['A','B','D','E']],index=['A','B'],aggfunc='sum'),'\n')
print(pd.pivot_table(df[['A','B','D','E']],index=['A','B'],aggfunc='mean'),'\n')


#以B聚合，计算A列元素频率
print(pd.crosstab(df['B'],df['A']),'\n')#交叉表实现
print(pd.pivot_table(df,index='B',columns='A',values='C',aggfunc='count'))#如果C都是数，那么也可以用透视表来实现

