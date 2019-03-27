import numpy as np
import pandas as pd
from numpy.random import rand
#连接堆叠（concat），按行按列都而可以
s1=pd.Series([1,2,3])
s2=pd.Series([2,3,4])
print(pd.concat([s1,s2]))#和numpy的两个stack一样，以list的形式作为concat函数输入

df1=pd.DataFrame(np.reshape(np.arange(1,17),[4,4]))
df2=pd.DataFrame(np.reshape(np.arange(17,33),[4,4]))
print(pd.concat([df1,df2]))#按行
print(pd.concat([df1,df2],axis=1))#按列

df3=pd.DataFrame(df1.values,columns=['a','b','c','d'])
df4=pd.DataFrame(df2.values[:,1:3],columns=['x','y'])
print(pd.concat([df3,df4]).sort_index())#排序还可以用sort（'key'）的办法

df5=pd.DataFrame(df1.values,index=['x','y','z','t'],columns=['a','b','c','d'])
df6=pd.DataFrame(df1.values[:,2:4],index=['x','y','u','v'],columns=['c','e'])
print(df5)
print(df6)
print(pd.concat([df5,df6]))#默认是并集，也可以写outer
print(pd.concat([df5,df6],join='inner'))

#可以增加连接的keys
c_k=pd.concat([df5,df6],keys=['df5','df6'])
print(c_k,'\n',type(c_k),'\n',type(c_k.index))#类型仍然是给dataframe，index变成了multiindex
c_k2=pd.concat([df5,df6],keys=['df5','df6'],axis=1)
print(c_k2,'\n',type(c_k2),'\n',type(c_k2.columns))#Column变成multiindex

#修补（修改，按index），update函数和combine_first函数（combine_first作业里写算了）
df7=pd.DataFrame(np.reshape([1,3,3,5,9,np.nan,7,2,9,10,np.nan,20,17,14,35,16],[4,4]))
print(df7,'\n-------------')
df7.update(df1)#nan会被覆盖，非nan不会被nan覆盖。直接覆盖，不会返回可赋值的df
print(df7)

#作业
df1=pd.DataFrame(rand(4,2),columns=['values1','values2'],index=['a','b','c','d'])
df2=pd.DataFrame(rand(4,2),columns=['values1','values2'],index=['e','f','g','h'])
df3=pd.concat([df1,df2])
print(df1,'\n',df2,'\n',df3)
#merge也可以，但index会重新制定，而且会少掉重复的情况
df4=pd.merge(df1,df2,how='outer')
print(df4)
print('-------------')

df1=pd.DataFrame(rand(4,2),columns=['values1','values2'],index=['a','b','c','d'])
df1.iloc[1,0]=df1.iloc[2,0]=np.nan
df2=pd.DataFrame([[0,1],[2,3],[4,5],[6,7]],columns=['values1','values2'],index=['a','b','c','d'])
print(df1,'\n',df2)
print(df1.combine_first(df2))
