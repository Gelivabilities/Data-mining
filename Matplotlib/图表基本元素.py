import numpy as np
import pandas as pd
import matplotlib.pyplot as plt#注意目前的导包都是小写的

df=pd.DataFrame(np.random.rand(10,2),columns=['A','B'])#2列dataframe
f=plt.figure(figsize=(10,10))
fig=df.plot(figsize=(6,4))#对dataframe df的一个Figure
print(fig,type(fig),'\n') 
print(f,type(f))

plt.title('myname')
#x，y轴标签
plt.xlabel('x')
plt.ylabel('y')
#图例，参数代表显示的位置
plt.legend(loc='center')#loc参数：best（自适应）、lower、center和upper的right、center和left
#边界（x、y显示范围）
plt.xlim([0,10])
plt.ylim([0,1])
#刻度（列表）
plt.xticks(np.arange(10))
plt.yticks([0+0.1*x for x in range(10)])

fig.set_xticklabels(chr(ord('a')+i) for i in range(10))#刻度的label，以字符串的形式显示
fig.set_yticklabels(chr(ord('A')+i) for i in range(10))

#绘图
x=np.linspace(-np.pi,np.pi,256,endpoint=True)
c,s=np.cos(x),np.sin(x)
plt.clf()
plt.plot(x,c)
plt.plot(x,s)
#格网，第一个参数默认true。线型有很多种，“-”为实现，“--”为虚线
plt.grid(True,linestyle='--',color='red',linewidth=2,axis='both')