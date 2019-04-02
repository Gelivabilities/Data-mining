import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#文本和主次刻度（主次刻度不好记，先不练手）
s=pd.Series(np.random.randn(100)).cumsum()
plt.text(50,0,'abc',fontsize=10)
s.plot(figsize=(6,4))
plt.clf()

#保存图表
df=pd.DataFrame(np.random.randn(100,4),columns=list('abcd')).cumsum()
df.plot(style='--',marker='.',alpha=0.5)
plt.legend('ABCD',loc='best')#图例名还可以改
plt.savefig('c:\\users\\gelivability\\desktop\\myfig.png',
            dpi=400,#分辨率
            bbox_inches='tight',#图表需要保存的部分，tight会剪去图表周围空白部分
            facecolor='g',#图的背景色和边色
            edgecolor='b')
