import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#面积图、填图、饼图

#面积图（折线图的填充）
_,axes=plt.subplots(2,1,figsize=(8,6))
df1=pd.DataFrame(np.random.rand(10,4),columns=list('abcd'))
df2=pd.DataFrame(np.random.randn(10,4),columns=list('abcd'))

df1.plot.area(colormap='Greens_r',alpha=0.5,ax=axes[0]) 
#堆叠参数，默认是True
df2.plot.area(stacked=False,colormap='Set2',alpha=0.5,ax=axes[1])
#因此，想要画正确的堆叠图，默认要全部是正数，否则报错

#没事复习下
df1.plot(kind='kde',style='--')
df2.plot(kind='line',style='-o')

#填图
_,ax_fill=plt.subplots(2,1,figsize=(8,6))
x=np.linspace(0,1,500)
y1=np.sin(4*np.pi*x)*np.exp(-5*x)
y2=-np.sin(4*np.pi*x)*np.exp(-5*x)

ax_fill[0].fill(x,y1,'r',alpha=0.5,label='y1(x)')
ax_fill[0].fill(x,y2,'g',alpha=0.5,label='y2(x)')#同一个表，下标要一样

ax_fill[1].fill_between(x,np.sin(10*x),-np.sin(20*x),color='b',alpha=0.5,label='area')

for i in range(2):
    ax_fill[i].legend()
    ax_fill[i].grid()
    
#面积图（大鹏就是不一样，天天说非常简单（吐槽向
s=pd.Series(np.random.rand(4),index=list('abcd'),name='series')


#饼图，好像没得传figsize这个参数
plt.figure(figsize=(4,4))
plt.pie(s,
        explode=[0.5,0.1,0.1,0.1],#每一部分移开中心多少位置
        labels=s.index,#标签
        colors=list('rgbc'),#颜色
        shadow=True,#阴影
        labeldistance=1.2,#标签距离
        radius=1.5,#半径
        frame=False,#图框（什么鬼）
        startangle=0,#起始角度
        pctdistance=0.6,#也有相关注释，但是我没看懂
        autopct='百分之%.2f'#显示百分比
        )