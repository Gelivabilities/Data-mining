import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#这次可以画多个图了
fig1=plt.figure(num=1,figsize=(4,2))
plt.plot(np.random.randn(50).cumsum(),'--ro')
plt.clf()
fig2=plt.figure(num=2,figsize=(6,3))
plt.plot(np.random.randn(50).cumsum(),'--bo')
plt.clf()

#子图
fig=plt.figure(figsize=(10,10),facecolor='gray')

ax1=fig.add_subplot(2,2,1)
plt.plot(np.random.rand(50).cumsum(),'--r.')
plt.plot(np.random.rand(50).cumsum(),'--b')

ax2=fig.add_subplot(2,2,2)
ax2.hist(np.random.rand(50),alpha=0.4)

ax4=fig.add_subplot(2,1,2)
df2=pd.DataFrame(np.random.randn(100,4),columns=list('ABCD')).cumsum()
ax4.plot(df2,'-')
plt.clf()

fig,axes=plt.subplots(2,3,figsize=(10,4))#share共享刻度，sharex或sharey，默认都是false
print(axes,axes.shape,type(axes),type(axes[0,0]))#axes是个数组，存了2*3=6个subplot类型的图表

for i in range(2):
    for j in range(3):
        if i==0:
            axes[i,j].plot(pd.DataFrame(np.random.randn(100,4),columns=list('abcd')).cumsum())
        else:
            axes[i,j].hist(pd.Series(np.random.randn(100)))
            
            