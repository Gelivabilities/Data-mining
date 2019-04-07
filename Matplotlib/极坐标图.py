import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

s=pd.Series(np.arange(20))
theta=np.arange(0,2*np.pi,0.02)#下面用弧度制
print(s)
print(theta[:10])

fig=plt.figure(figsize=(8,4))
ax1=plt.subplot(121,projection='polar')#projection=polar代表是创建极坐标图，不写的话，默认就是二维关系的图
ax2=plt.subplot(122)
#上面这个，还可以写成211、212，就变成两行一列。前两个参数是行和列，最后一个是先行后列的第几个
#如果是222、223，就变成了右上和左下两个子图有图
#还可以写：ax=fig.add_subplot(111,polar=True)

#对于设定好是极坐标的图，可以直接plot
#lw应该是线宽吧
ax1.plot(theta,3*theta,linestyle='--',lw=1)#这个叫，螺旋线？
ax1.plot(s,linestyle='-',marker='.',lw=2)#0到19的距离，所以它是均匀分配给所有的theta？
ax2.plot(theta,theta*3,linestyle='--',lw=1)
ax2.plot(s)
plt.grid()

plt.clf()
a1=plt.subplot(121,projection='polar')
a2=plt.subplot(122,projection='polar')
a1.plot(theta,theta/6,'--',lw=2)
a2.plot(theta,theta/6,'--',lw=2)

#修改
a2.set_theta_direction(-1)#默认逆时针，改完后就变成顺时针了

#格网
a2.set_thetagrids(np.arange(0.0,360.0,30),list('abcdefghijkl'))#角度网格，90度还可以做东南西北什么的
a2.set_rgrids(np.arange(0.2,1.4,0.4))#极径网格线

#角度偏移值（set_theta_offset）
a2.set_theta_offset(np.pi/4)#逆时针方向，偏移45度，pi/4弧度

a2.set_rlim(0.2,0.8)#设置显示的极径范围(但好像不会改变其他值)
a2.set_rmax(1.4)#设置显示的极径的最大值，整个圆盘的最大值
a2.set_rticks(np.arange(0.1,1.5,0.2))#为啥感觉它和极径网格线（set_rgrids）是一样的。。。。
#上面三个函数会相互影响，需要注意


#雷达图：极坐标折线图/填图
ax1=plt.subplot(111,projection='polar')
ax1.set_title('radar map\n')
ax1.set_rlim(0,20)

data1=[i for i in range(20)]
data2=[0.75*x for x in range(20)]
theta=np.arange(0,4*np.pi,np.pi/5)

ax1.plot(theta,data1,'.--b',label='data1')
ax1.fill(theta,data1,color='r',alpha=0.2)
ax1.plot(theta,data2,'-r',label='data2')
ax1.fill(theta,data2,color='g',alpha=0.2)

labels=list('abcdef')
dataLength=6
data1=np.random.randint(0,10,6)
data2=np.random.randint(0,10,6)
angles=np.linspace(0,2*np.pi,dataLength,endpoint=False)#0到2π，6份
data1=np.concatenate((data1,[data1[0]]))#闭合，可以画闭合曲线，否则线没法连成环
data2=np.concatenate((data2,[data2[0]]))
angles=np.concatenate((angles,[angles[0]]))

plt.figure()#新图
plt.polar(angles,data1,'o-r',linewidth=1)
plt.fill(angles,data1,color='g',alpha=0.75)
plt.polar(angles,data2,'o-b',linewidth=1)
plt.fill(angles,data2,color='r',alpha=0.25)

plt.thetagrids(angles/np.pi*180,labels)#角度网格和标签，注意这个是角度制的
plt.ylim(0,10)#ylim不只是平面直角才能用，极坐标也可以用

#极轴图：极坐标柱状图
plt.figure()
ax1=plt.subplot(111,projection='polar')
ax1.set_rlim(0,12)
data=np.random.randint(1,10,10)
theta=np.linspace(0,2*np.pi,10)
bar=ax1.bar(theta,data,alpha=0.5)

for r,bar_ in zip(data,bar):#改变颜色
    bar_.set_facecolor(plt.cm.jet(r/10.))#jet是彩色的