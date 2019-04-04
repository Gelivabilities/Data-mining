import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

_,axes=plt.subplots(4,1,figsize=(10,10))
s=pd.Series(np.random.randint(0,10,16),index=list('ABCDEFGHIJKLMNOP'))
df=pd.DataFrame(np.random.rand(5,3),
                columns='铂金或以下,钻石,钻石以上'.split(','),
                index=pd.date_range('2018-1-1',periods=5,freq='QS'))
#直接给指定subplot进行plot
axes[0].plot(df)  
axes[2].hist(s)
#df或s实施plot到指定subplot中
df.plot(kind='bar',legend='best',color=list('rgb'),ax=axes[1])
s.plot(kind='line',ax=axes[3])  

#多系列堆叠图：
df.plot(kind='barh',
        stacked=True,
        title='王者荣耀各赛季段位分布',
        grid=True,
        alpha=0.75,
        colormap='Oranges_r')

#barh、hist
df.plot.barh(title='a')
df.plot.hist()#hist也能用，但不适合df，很多都重叠了
df.plot.hist(stacked=True)#hist也有stack参数

#plt画下面的这个图（我也不知道叫啥图，比较特殊的柱状图吧算是）
plt.figure(figsize=(10,4))#其实每次执行一次plt.figure就是产生一个新的图表了
x=np.arange(10)
y1=np.random.rand(10)
y2=-np.random.rand(10)

#x,y就两个维度的数据，width宽度，facecolor柱图颜色，edge边色，yerr是误差线（到底是干嘛的）
plt.bar(x,y1,width=1,facecolor='yellowgreen',edgecolor='red',yerr=y1*0.1)
plt.bar(x,y2,width=1,facecolor='lightskyblue',edgecolor='green',yerr=y2*0.1)

#plt.text： 参数1、2：文本横纵位置，3：文本内容，4：颜色
for i,j in zip(x,y1):plt.text(i+0.3,0.1,'%.2f' % j,color='black')
for i,j in zip(x,y2):plt.text(i+0.3,-0.1,'%.2f' % j,color='black')

#外嵌图表
data=np.random.randint(0,100000,25).reshape([5,5])
d_columns=['Freeze','Wind','Flood','Quake','Hail']
d_rows=['%d year' % x for x in [10,40,50,100,200]]
df=pd.DataFrame(data,columns=d_columns,index=d_rows)
print(df)
#先创建一个堆叠图
df.plot(kind='bar',
        grid=True,
        colormap='Blues_r',
        figsize=(8,3),
        stacked=True,
        legend=False)
#绘制图表
plt.table(cellText=data,#内容
          cellLoc='center',#文本对齐位置
          cellColours=None,#表中元素颜色
          rowLabels=d_rows,#行标签
          colLabels=d_columns,#列标签
          rowColours=plt.cm.BuPu(np.linspace(0.25,0.75,5))[::-1],#
        colColours=plt.cm.Reds(np.linspace(0.25,0.75,5))[::-1],
        rowLoc='right',#行标签对齐位置
        loc='bottom')#表格相对于已plot内容的位置

plt.xticks([])