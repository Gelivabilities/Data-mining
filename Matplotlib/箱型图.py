import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#箱型图，反映数据的分散情况

#这几章参数实在是太多了，好难记

#箱型图组成：
#0. Q几，表示最小值开始算起四分之几的数；IQR=Q3-Q1，叫做四分位距
#1. 上下边界，代表最小值最大值，一条线
#2. 上下四分位数（Q3和Q1），这个四分是指数据总数前后四分之一位置的数值大小
#3. 中位数，中值
#4. 异常值，小于Q1-1.5IQR或大于Q3+1.5IQR的值

_,axes=plt.subplots(2,figsize=(10,6))
df=pd.DataFrame(np.random.rand(10,5),columns=list('abcde'))
color=dict(boxes='DarkGreen',#箱线色
           whiskers='DarkOrange',
           medians='DarkBlue',#中位数线颜色
           caps='Gray')

df.plot.box(ylim=[0,1.2],grid=True,color=color,ax=axes[0])

#第二种方法
f=df.boxplot(sym='o',#异常点形状
             vert=True,#垂直，默认True
             whis=[5,0.95],#IQR前面的系数，默认是1.5，也可以改成其他
             patch_artist=True,#上下四分位之内（方框）填充
             ax=axes[1],
            showbox=True,#显示箱线（去掉填充才能有啥不同）
            showcaps=True,#是否显示边缘线（上下的线）
            grid=True,
            meanline=False,showmeans=True,#是否显示均值线（show才有），meanline设定到底是一条线还是个点
            showfliers=True,#显示异常值，默认True
            notch=False,#中间箱体是否缺口（不过这外观是什么鬼）
            return_type='dict'#返回类型：字典（所以f是个字典，我print一下试试）
             )#居然不能设颜色
print(f,type(f))#可以，有意思
plt.title('gelivability')

#f是个字典，里面这些信息可以这样访问。全都有set方法

for box in f['boxes']:
    box.set(color='g',linewidth=1)#箱体边框颜色
    box.set(facecolor='g',alpha=0.5)#填充色，上面的patch_artist要设置成True才行
    
for whisker in f['whiskers']:
    whisker.set(color='red',linewidth=3,linestyle='-')#四分位到边界的竖线
    
for cap in f['caps']:
    cap.set(color='gray',linewidth=2)#上下线色
    
for flier in f['fliers']:
    flier.set(marker='o',color='y',alpha=0.5)#异常值，不过颜色好像变不了额
    
df=pd.DataFrame(np.random.rand(10,2),columns='Col1,Col2'.split(','))
df['X'],df['Y']=pd.Series(list('AAAAABBBBB')),pd.Series(list('ABABABABAB'))
print(df)
#算是一种groupby？
df.boxplot(by='X')
df.boxplot(by='Y')
df.boxplot(column=['Col1','Col2'],by=['X','Y'],figsize=(8,4))