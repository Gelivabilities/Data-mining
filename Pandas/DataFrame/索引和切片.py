import numpy as np
import pandas as pd

#dataframe的索引、切片等操作
arr=np.reshape([x+1 for x in range(16)],[4,4])
frame=pd.DataFrame(arr,columns=['a','b','c','d'],index=['x','y','z','t'])
print(frame)
#选择列。注意，不同的选法返回的数据类型也不同，注意第1和第3个的区别
data1=frame['a']
data2=frame[['c','b']]
data3=frame[['a']]
print(data1,type(data1))#series
print(data2,type(data2))#dataframe
print(data3,type(data3))#dataframe
#选择行，和选择列相似，只是加个“.loc”就行了。选法不同数据类型也不同
data4=frame.loc['y']
data5=frame.loc[['y']]
data6=frame.loc[['x','z','t']]
print(data4,type(data4))#series
print(data5,type(data5))#dataframe
print(data6,type(data6))#dataframe


#切片
#如果只标数字，那么就相当于是切片，会选择行。需要有冒号才是切片，下面的data9是不行的
data7=frame[:1]#只输出一行，它依然还是dataframe
data8=frame[1:3]
#data9=frame[0]
print(data7,type(data7))
print(data8,type(data8))
#中括号直接填行名也不行
#data10=frame['y']

#切片不一定用数字。有了冒号，访问行加不加loc都可以
data11=frame['y':'t']
data12=frame.loc['x':'z']
print(data11)
print(data12)

#行列都限定的情况
data13=frame[['b','c']].loc[['t','x']]
print(data13)

#按整数标签索引，感觉有点像是，list切片，numpy下标访问，和matlab的结合起来了
#（1）和普通list一样都是末端不包含的
#（2）和numpy一样，可以用逗号隔开，左行右列
#（3）和Matlab一样，可以直接手动选择多个作为输入，用数组形式，例如下面的行[1,3]
#注意，iloc可以，但是普通中括号、loc不行，要像上面一样分步
data14=frame.iloc[[1,3],2::-1]
print(data14)


#布尔型索引，可以直接用，非常方便。另外加减乘除和mode都可以直接用，很容易想到,也很爽
print(frame%3==0)
print(frame<=10)
print(frame**2>100)
print(frame*3)
print(frame-6)
print(frame/frame)
print(frame[frame%3==0])
print(frame[frame<=10][['b','c']])

#2.6 作业
lst=np.reshape([100*np.random.rand(1) for x in range(16)],[4,4])
df=pd.DataFrame(lst,columns=['a','b','c','d'],index=['one','two','three','four'])
#（1） 
print(df[['b','c']])
print('-------')
#（2）
print(df[2:])
print(df.iloc[2:])
print('-------')
#(3)
print(df.iloc[:,::1].loc[['two','one']])
print(df.loc[['two','one']].iloc[:,::1])
print('-------')
#（4）
print(df[df>50])
print('-------')