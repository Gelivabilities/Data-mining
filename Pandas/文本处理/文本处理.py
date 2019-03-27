import numpy as np
import pandas as pd

#文本数据
ss=pd.Series(['a..a.a',np.nan,15,'随便写.点.东西 '])
df=pd.DataFrame(np.reshape([chr(ord('a')+x)if (x+1)%2==1 else x for x in range(16)],[4,4]),index=['a','b','c','d'],columns=['x','   y ','z','t'])
print(ss)
print(df)
print('----------')

print(ss.str.count('a'),'\n---------')
print(ss.str.len(),'\n-----------')
print(df['z'].str.upper())
print(ss.str.upper())
print(ss.str.startswith('随便'))
print(ss.str.endswith('a'))
print(ss.str.strip())#去前后空格，还有lstrip和rstrip这两种去空格的方法
print(df.columns,'\n',df.columns.str.strip(),'\n',df.columns.str.lstrip())

#去掉中间东西
print(ss.str.replace('.',''))

#分裂（注意区分下面几种不同情况），还有从右到左split，叫rsplit
print(ss.str.split('.'))
print(ss.str.split('.')[0],'\n-------------')
print(ss.str.split('.').str[0])
print(ss.str.split('.').get(0))
print(ss.str.split('.').str.get(2))
print(ss.str.split('.',expand=True))
print(ss.str.split('.',expand=True,n=1))

#索引（索引方式和以前是一样的）
print(ss.str[0])#注意，不是获得第0个index的字符串
print(ss.str[2:])
print('---------------')
#作业
f=lambda g,n,x:[g,n,x+','+x+','+x]
l=[f('M','jack','90'),f('M  ','tom','89'),f(' F','marry','90'),f('M','zack','78'),f('  F      ','heheda','60')]
df=pd.DataFrame(l,columns=['gender','name','score'])
print(df)

#1
print(df['name'].str[0].str.upper()+df['name'].str[1:])
#2
print(df['gender'].str.strip())
#3
print(df['score'].str.split(','))