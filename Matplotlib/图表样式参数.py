import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#复习
df=pd.DataFrame({'x':[x*np.sin(x) for x in range(1500)],'y':[x for x in range(1500)]})
fig=df.plot(figsize=(6,4),linestyle='-')

plt.xticks([100*i for i in range(10)])
plt.yticks([200*(i-5) for i in range(10)])
plt.xlim([0,1000])
plt.ylim([-1000,1000])
fig.set_xticklabels([chr(ord('a')+x) for x in range(11)])
fig.set_yticklabels([('-' if x<5 else '')
                    +('0' if x==5 else chr(ord('a')+abs(x-5)-1)) for x in range(11)])
#plt.show()
plt.clf()

#linestyle: '-' '--' '-.' ':'（实线、虚线、虚线+点、纯点）
plt.plot([i**2 for i in range(100)],linestyle='-.')
#plt.show()
plt.clf()

#marker
s=pd.Series(np.random.randn(100).cumsum())
s.plot(figsize=(10,4),linestyle='--',marker='o',linewidth=4,color='green')
#plt.show()
plt.clf()


#柱状图（复习）
plt.hist(np.random.randn(100),color='r',alpha=0.8)
plt.xticks=[0.25*(x-3) for x in range(15)]
plt.grid(True,color='blue')
#plt.show()
plt.clf()

#风格
import matplotlib.style as psl
print(plt.style.available)#有什么风格
psl.use('dark_background')
ts=pd.Series(np.random.randn(100).cumsum(),index=pd.date_range('2019-1-1',periods=100))
#style：线型、颜色、marker一起设定
ts.plot(style='--go',linewidth=3,grid=True)
plt.show()
#plt.clf()