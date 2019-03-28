import numpy as np
import pandas as pd

#去重及替换
s=pd.Series([1,2,2,2,2,1,1,3,4,5,5,5,5])
print(s.duplicated(),type(s.duplicated()))#判断一个值是否被重复，从上往下判断确认重复
print(s[s.duplicated()==False])#注意，不能像下面这样写，否则报错
'''s[not s.duplicated()]'''#错误写法

#series应该没有not方法好像，但是判断语句还是有的，让它判断是否等于False就行了
print(s.unique())#unique也可以去重，但是对于series，返回的是个list
df=pd.DataFrame(np.random.rand(4,4))
print(df.duplicated())#dataFrame也可以判重，但是就没有unique方法
'''df.unique()'''#错误写法

#去重还可以drop_duplicates，返回内容和用duplicated==False方法一样
print(s.drop_duplicates())
#特别地，drop如果给它一个参数，还可以直接对s去重，不用赋值。参数默认为False，默认是需要赋值的
s.drop_duplicates(inplace=True)
print(s)

#replace方法
#之前的str方法只是适用于字符串的，这里的replace是通用的一个方法，随便换
s=pd.Series([1,2,2,2,2,1,1,3,4,5,5,5,5])
print(s.replace([2,4],['fuck',np.nan]))#加括号则替换成对应值，对应不上会报错
print(s.replace(2,4))
'''s.replace(2,[3,4])'''#错误写法1
'''s.replace([2,3],[1])'''#错误写法2
print(s.replace([1,2,5],np.nan))#不加括号，则全部替换为同一个值

#还可以用字典替换
print(s.replace({2:123,5:456}))

