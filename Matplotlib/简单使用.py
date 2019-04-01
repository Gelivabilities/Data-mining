import numpy as np
import pandas as pd
import matplotlib.pyplot as plt#python版的matlab绘图接口，可以画2d、3d图表，总之很牛逼
#%matplotlib inline 只能在jupyter上用，一般没必要写

plt.plot(np.arange(0,16))
plt.show()

x=np.random.randn(1000)
y=np.random.randn(1000)
plt.scatter(x,y)
plt.show()

s=pd.Series(np.random.randn(100))
s.plot(style='k--o',figsize=(10,5))
plt.show()

df=pd.DataFrame(np.random.rand(50,2),columns=['A','B'])
#figsize：横纵尺寸，color：颜色，alpha：透明度
df.hist(figsize=(12,5),color='r',alpha=0.7)

#plt.gcf.clear()清空之前的图表