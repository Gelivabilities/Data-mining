import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

f=lambda x,y=None:np.random.randn(x) if y==None else np.random.randn(x,y)
plt.figure(figsize=(8,6))
x,y=f(1000),f(1000)
plt.scatter(x,y,marker='.',
            s=f(1000)*100,#s是点的大小，是一个维度
            cmap='Reds',#colormap
            c=f(1000),#颜色，也是一个维度
            alpha=0.8)
plt.grid()

#散点矩阵
df=pd.DataFrame(f(100,4),columns=list('abcd'))
pd.scatter_matrix(df,figsize=(10,6),
                  marker='o',
                  diagonal='kde',#可以写其他的，例如hist等
                  alpha=0.5,
                  range_padding=0.3)#留白大小