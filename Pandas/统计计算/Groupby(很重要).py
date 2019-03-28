import numpy as np
import pandas as pd
from numpy.random import rand

#分组，groupby
df=pd.DataFrame({'A':['x','y','x','y','x','y','x','x'],
                 'B':[1,1,2,3,2,2,1,3],
                 'C':np.random.rand(8),
                 'D':np.random.rand(8)})
print(df)
#下面4个都不难，就不注释了
print(df.groupby('A'),'\n',type(df.groupby('A')))
print(df.groupby('A').sum())
print(df.groupby(['A','B']).mean())
print(df.groupby('B')[['C','D']].mean())

#groupby存储的是，分好组后的元组，每个元组由组名和dataframe组成
[print(x,'\n',type(x),type(x[0]),type(x[1])) for x in list(df.groupby('A'))]
 
#因此我们还可以获取特定组，用get_group方法就行
print(df.groupby('A').get_group('y'))#返回完整组，是个dataframe
print(df.groupby('A').groups)#这种方法获得分组groupby中key列的index，返回一个字典

#size，按key统计数据
print(df.groupby('A').size())

#按类型groupby
print(df.dtypes)
[print(x,'\n',type(x),type(x[0]),type(x[1])) for x in list(df.groupby(df.dtypes,axis=1))]
print('----------')
 
#用字典来分组
dic={'A':'类1','B':'类1','C':'类2','D':'类2'}
print(df.groupby(dic,axis=1).sum())

#按series分组，和字典是一样的
s=pd.Series(dic)
print(df.groupby(s,axis=1).sum())
print('----------------')

#按字符串长度分组
dfl=pd.DataFrame(df.values,index=[chr(ord('a')+x)+('A' if x%2==0 else '')  for x in range(8)])
print(dfl)
print(dfl.groupby(len).sum())
print('--------------------')

#多函数计算，agg里的函数，还可以用numpy中的函数。可以是字典也可以是list
df['A']=[1,2,3,4,5,6,7,8]
print(df)
print(df.groupby('B').agg(['mean',np.sum,'prod']))
#注意，agg传字典的时候，如果不加[]会报错，不知道为什么
print(df.groupby('B')['A','D'].agg({'result1':np.mean,'result2':np.sum}))
print('----------------')

#作业
print('Homework:')
df=pd.DataFrame([['one','h',10,rand(),rand()],
                 ['two','h',12,rand(),rand()],
                 ['three','h',14,rand(),rand()],
                 ['one','h',16,rand(),rand()],
                 ['two','f',18,rand(),rand()],
                 ['three','f',20,rand(),rand()],
                 ['one','f',22,rand(),rand()],
                 ['two','f',24,rand(),rand()]],columns=['A','B','C','D','E'])
                 
print(df)
print(df.groupby('A')['C','D'].mean())#1
print('----------------')
print(df.groupby(['A','B'])['D','E'].sum())#2
print('----------------')
print(df.groupby('A').groups)#3
print('----------------')
print(df.groupby(df.dtypes,axis=1).sum())#4
print('----------------')
print(pd.DataFrame(df[['C','D']].sum(axis=1),columns=['r']))#5
print('----------------')
print(df.groupby('B').agg(['mean','sum','max','min']))#6