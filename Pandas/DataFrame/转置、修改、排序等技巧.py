import numpy as np
import pandas as pd

data=np.reshape([int(100*np.random.rand()) for x in range(16)],[4,4])
df=pd.DataFrame(data,columns=[chr(ord('a')+x) for x in range(4)],index=['x','y','z','t'])

#pandas的奇技淫巧

#修改：直接索引然后修改就行了，很简单。但列好像只能一列一列的增
df['e']=10
df['f']=30
df.loc['u']=20
print(df)
print('-------')

#删除列：用del
del df['e']
print(df)

#删除行或列：用drop，默认是删行（0），但也可以删除列（1）。注意：原数据是不改变的
print(df.drop(['f'],axis=1).drop(['u']))

#排序（肯定是按列排序），默认升序
print(df.sort_values(['a','c'],ascending=False))
print(df.sort_index())


#作业2.7
#（1）降序排序
data=np.reshape([100*np.random.rand(1) for x in range(9)],[3,3])
df=pd.DataFrame(data,columns=['v1','v2','v3'],index=['a','b','c'])
#按index排
print(df.sort_index(ascending=False))
#按第二列排
print(df.sort_values(['v2'],ascending=False))

#（2）修改
data=np.reshape([100*np.random.rand(1) for x in range(10)],[5,2])
df1=pd.DataFrame(data,columns=['v1','v2'],index=['a','b','c','d','e'])
df2=df1.T#转置
df2['b']=100
del df2['e']
print(df2)