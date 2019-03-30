import numpy as np
import pandas as pd

#transform apply
df=pd.DataFrame({'data1':np.random.rand(5),
                 'data2':np.random.rand(5),
                 'key1':list('aabba'),
                 'key2':['one','two','one','two','one']})
k1_mean=df.groupby('key1').mean()
print(df)
print(k1_mean)

#merge还是只能按列来merge的
print(pd.merge(df,k1_mean,left_on='key1',right_index=True).add_prefix('mean_'))
print('-----------')

#transform和apply
print(df)
print(df.groupby('key2').transform(np.mean))
print('----------------')

#python基础，在函数中传函数参数
def f(g,x):return g(x)
def g(x):return 2*x
print(f(g,3))
print('------------')

#说白了，apply的参数是个函数，将分组的data传入需要apply的函数中
print(df.groupby('key2').apply(lambda x:np.mean(x)))
print(df.groupby('key2').apply(np.mean))
print(df.groupby('key2').apply(g))

def sort_df(d):return d.sort_index()
print(df.groupby('key2').apply(sort_df))

#apply中还可以传函数的参数
def my_multi_para_f(x,n):return n*x
print(df.groupby('key2').apply(my_multi_para_f,5))
print('-------------')

#作业
df=pd.DataFrame({'data1':np.random.rand(8),'data2':np.random.rand(8),'key':['a','a','b','b','a','b','a','b']})
print(df)
df_gb=df.groupby('key').transform(np.mean)
print(df_gb)
print(pd.merge(df,df_gb,left_index=True,right_index=True,suffixes=['','_mean']))