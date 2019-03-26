import numpy as np
import pandas as pd

#由一维数组（列表）创建series
ar=np.random.rand(5)
#Series是一个带有标签的一维数组
s=pd.Series(ar)
print(ar)
print(s)
#在整个的pandas里面，都有一个数据结构，叫做index
print(list(s.index),type(s.index))
print(s.values,type(s.values))
#index可以是字母，不一定是数字
ss=pd.Series(ar,index=list('abcde'))#index元素个数一定和ar相同，否则报错
print(ss,type(ss.index))

#由字典创建series
dic={'a':1,'b':2,4:3}
s=pd.Series(dic)
print(s)#可见索引不一定要相同数据类型。当然，dtype是可以手动设置的

#dtype有：np.str,np.int,np.object,np.float等

#name参数，可以设定，默认为None
s=pd.Series(dic,name='mytable')
print(s.name)
s_=s.rename('fuck')#rename，并复制
print(s_.name)

#通过标量创建series(如果不给index，默认应该就一个，否则就取决于index个数)
s=pd.Series(100,index=range(5))
print(s)