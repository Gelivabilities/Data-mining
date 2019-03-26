import numpy as np
import pandas as pd

#由list组成的字典创建
data={'name':['a','b','c'],'score':[90,60,85],'age':[25,21,23]}
      
#可以设定非默认的index
frame=pd.DataFrame(data,index=[101,102,103])
print(frame)
print(type(frame),frame.index,frame.columns)

#可以设定columns的顺序，还可以增加新的column，也可以减少原来的column
frame2=pd.DataFrame(data,columns=['name','age','gender'])
print(frame2)


#由series组成的字典创建
data={'x':pd.Series([1,2],index=['a','b']),'y':pd.Series([4,5,6],index=['a','e','c'])}
frame3=pd.DataFrame(data,index=['a','b','c','d','e'])
print(frame3)


#由二维数组直接创建
arr=np.reshape([x+1 for x in range(16)],[4,4])
#注意columns、index个数要和二维list（应该不能算是矩阵）一致
frame4=pd.DataFrame(arr,columns=['x','y','z','t'],index=['a','b','c','d'])
print(frame4)
#二维数组元素个数可以不一致
arr2=[[1,2,3,4],[1],[2,4,6],[3]]
frame5=pd.DataFrame(arr2)
print(frame5)


#由字典组成的list创建
lst=[{'a':1,'b':2},{'b':3,'c':4}]
frame6=pd.DataFrame(lst,index=['x','y'])
print(frame6)


#字典组成的字典创建。columns是字典的key，index是子字典的key
#同样是不能改变index，只能添加新标签，否则新增的index会变成空值。columns也同理
dic={'Tom':{'age':1,'gender':2},'Jerry':{'age':2,'gender':1}}
frame7=pd.DataFrame(dic)
print(frame7)


#2.5：多种不同方法创建一个dataframe
#1.最简单的，二维数组，然后赋index和columns
arr=[[4,1,3,2],[5,2,4,3],[6,3,5,4],[7,4,6,5],[8,5,7,6]]
frame=pd.DataFrame(arr,columns=['four','one','three','two'],index=['a','b','c','d','e'])
print(frame)
#2. list组成的字典
dic={'one':[1,2,3,4,5],'two':[2,3,4,5,6],'three':[3,4,5,6,7],'four':[4,5,6,7,8]}
frame=pd.DataFrame(dic,index=['a','b','c','d','e'])
print(frame)
#3. 字典组成的list
lst=[{'one':1,'two':2,'three':3,'four':4},
     {'one':2,'two':3,'three':4,'four':5},
     {'one':3,'two':4,'three':5,'four':6},
     {'one':4,'two':5,'three':6,'four':7},
     {'one':5,'two':6,'three':7,'four':8}]
frame=pd.DataFrame(lst,index=['a','b','c','d','e'])
print(frame)
#4. Series组成的字典
dic={'one':pd.Series([1,2,3,4,5],index=['a','b','c','d','e']),'two':pd.Series([2,3,4,5,6],index=['a','b','c','d','e']),'three':pd.Series([3,4,5,6,7],index=['a','b','c','d','e']),'four':pd.Series([4,5,6,7,8],index=['a','b','c','d','e'])}
frame=pd.DataFrame(dic)
print(frame)
#5. 字典组成的字典
dic={'one':{'a':1,'b':2,'c':3,'d':4,'e':5},'two':{'a':2,'b':3,'c':4,'d':5,'e':6},'three':{'a':3,'b':4,'c':5,'d':6,'e':7},'four':{'a':4,'b':5,'c':6,'d':7,'e':8}}
frame=pd.DataFrame(dic)
print(frame)