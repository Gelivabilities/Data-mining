import numpy as np
import pandas as pd

dic={'Jack':90,'Marry':92,'Tom':89,'Zack':65}
s_dic=pd.Series(dic,name='作业1',dtype='float64')

arr=[90,92,89,65]
indexes=['Jack','Marry','Tom','Zack']
s_arr=pd.Series(arr,index=indexes,dtype='float64',name='作业1')

print(s_dic)
print(s_arr)

arr=np.random.rand(10)*100
indexes=[chr(ord('a')+x) for x in range(ord('j')-ord('a')+1)]
s=pd.Series(arr,index=indexes,dtype=np.int)
print(s)
print(s['b'],s['c'])
print(s[3:6])
print(s[s>50])
