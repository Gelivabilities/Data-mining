import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#直方图，之前讲过的hist

#直方图，和柱状图，是不一样的。柱状图是个概率的分布，性质是完全不一样的
s=pd.Series(np.random.randn(1000))
s.hist(alpha=0.5,
       bins=20,#统计成多少份
       normed=True,#标准化
       histtype='stepfilled',#风格
       align='mid',#对齐方式
       orientation='vertical',#水平还是垂直，默认垂直
       )
s.plot(kind='kde',style='--r',linewidth=2,xlim=[-4,4])
plt.grid()

f=lambda x:np.random.randn(x)
df=pd.DataFrame({'a':f(1000)+1,'b':f(1000),'c':f(1000)-1,'d':f(1000)-2})
df.plot.hist(stacked=True,#是否堆叠
             bins=20,
             colormap='Greens_r',
             alpha=0.5,
             grid=True)
#直接hist会怎样？
df.hist(bins=50)