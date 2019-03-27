import numpy as np
import pandas as pd
from numpy.random import rand

#合并
df1=pd.DataFrame(np.reshape(np.arange(1,17),[4,4]),columns=['a','b','key1','key2'])
df2=pd.DataFrame(np.reshape(np.arange(9,25),[4,4]),columns=['c','d','key1','key2'])
print(df1,'\n')
print(df2,'\n')

#on表示合并时需要根据的key，按完全一样的key来求，默认求交集。默认根据所有key，因此想求交集必须写on
#交集和并集
print(pd.merge(df1,df2,on=['key1','key2'],how='inner'))#默认取交集，how可以不写
print(pd.merge(df1,df2,on=['key1','key2'],how='outer'))#inner是交集，outer是并集
#差集
print(pd.merge(df1,df2,on=['key1','key2'],how='left'))#df1全保留，df2取共同
print(pd.merge(df1,df2,on=['key1','key2'],how='right'))#df2全保留，df1取共同

#键名不一样
df3=pd.DataFrame(np.reshape(np.arange(1,17),[4,4]),columns=['a','b','keyl','key2'])
df4=pd.DataFrame(np.reshape(np.arange(9,25),[4,4]),columns=['c','d','keyr','key2'])
print(pd.merge(df3,df4,left_on='keyl',right_on='keyr',how='inner'))
print(pd.merge(df3,df4,left_on='keyl',right_on='keyr',how='outer'))
print('------------')
#拿index为key
df5=pd.DataFrame(np.reshape(['c',0,1,'b',1,0,'d',0,0],[3,3]),index=['a','b','c'],columns=['x','y','z'])
df6=pd.DataFrame(np.reshape([1,0,2,0,2,0,2,0,1],[3,3]),index=['a','b','c'],columns=['x','y','z'])
print(df5)
print(df6)
#left+right搭配，左边，右边两个dataframe（以index为键）
print(pd.merge(df5,df6,left_on='x',right_index=True,sort=True))#left中的bcd和right的abc键相对应
#所以上面这个index并不是指行，而是指一个叫index的特殊列。这东西理了挺久才理清
#sort: 按你on的东西排序

#join连接left和right，默认保留left求差集，也可以求其他集合
right=pd.DataFrame(np.reshape([1,0,2,0,2,0,2,0,1],[3,3]),index=['b','a','d'],columns=['t','u','v'])
print(df5.join(right))
print(df6.join(right,how='outer'))
print(df6.join(right,how='inner'))

#merge 左右on的key值不同时候的设定：默认是“_x”和“_y”，但也可以做修改
print(pd.merge(df1,df2,left_on='key1',right_on='key2',how='outer',suffixes=('_A','_B')))
print('------------')

#join里的其他参数
left=pd.DataFrame({'A':['A0','A1','A2','A3'],'B':['B0','B1','B2','B3'],'key':['K0','K1','K0','K1']})
right=pd.DataFrame({'C':['C0','C1'],'D':['D0','D1']},index=['K0','K1'])
print(left,'\n',right)
print(left.join(right,on='key'))
print('--------------')

#作业
df1=pd.DataFrame([[chr(ord('a')+x),rand()] for x in range(3)],columns=['key','values1'])
df2=pd.DataFrame([[chr(ord('b')+x),rand()] for x in range(3)],columns=['key','values2'])
df3=pd.merge(df1,df2,how='outer')
print(df1,'\n',df2,'\n',df3)

df1=pd.DataFrame(df1.values,columns=['lkey','values1'])
df2=pd.DataFrame(df2.values,columns=['rkey','values2'])
df3=pd.merge(df1,df2,left_on='lkey',right_on='rkey',how='left')
print(df1,'\n',df2,'\n',df3)

df1=pd.DataFrame(df1.values,columns=['key','values1'])
df2=pd.DataFrame(np.array([rand(3),[5,6,7]]).T,index=['b','c','d'],columns=['values2','values3'])
df3=pd.merge(df1,df2,left_on='key',right_index=True)
print(df1,'\n',df2,'\n',df3)