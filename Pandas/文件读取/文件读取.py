import numpy as np
import pandas as pd
import os

#read_table read_excel read_csv
os.chdir('c:/users/gelivability/desktop/')

#盗版的视频没有找到给的文件，就自己做一个吧

#不同方式读取，读取出来的类型都是dataframe
data1=pd.read_table('data1.txt')
print(data1,type(data1))
data1_csv=pd.read_table('data1.csv')
print(data1_csv,type(data1_csv))

#指定参数：delimiter是分隔符，index_col是用来做index的列，没有的话，默认0123这样的index
#header默认0，表示用第0行的来做columns，也可以指定其他行作为columns
data_1_multi_para=pd.read_table('data1.txt',delimiter=',',header=0,index_col='var1')#index_col还可以写数字
print(data_1_multi_para,type(data_1_multi_para))

#注：csv格式的读取要比excel快很多
data2=pd.read_excel('a.xlsx')#貌似默认只读第一个表格，read_excel想读多个表格还要设个参数
print(data2)
print('------------')
#engine也可以用c，c速度更快，python功能更全。encoding可以用gbk或utf-8等
data2=pd.read_csv('data1.csv',engine='python',encoding='gbk')
print(data2,type(data2))#dataframe

#read excel
data3=pd.read_excel('a.xlsx',sheetname='Sheet1',header=0)
data4=pd.read_excel('a.xlsx',sheetname=0,header=0)#sheetname还可以是索引
print(data3)
print(data4)
print('------------')

#如果sheetname填none，会自动给你把表按字典分出来
data5=pd.read_excel('a.xlsx',sheetname=None,header=0)
print(type(data5))
[print(key,'\n',data5[key]) for key in data5.keys()]
print('------------')

#还可以多个表
data6=pd.read_excel('a.xlsx',sheetname=[0,1],header=0,index_col=0)
print(type(data6))
[print(key,'\n',data6[key]) for key in data6.keys()]#字典的key是跟着sheetname中的输入的