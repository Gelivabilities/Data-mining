import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#plt.plot
ts=pd.Series(np.random.randn(100),index=pd.date_range('2019-1-1',periods=100)).cumsum()
ts.plot()#或plt.plot(ts)
plt.clf()

#plot的各种参数
ts.plot(kind='line',#图表类型，线型、柱状等
        label='fuck',#标签？哪的标签
        style='--g.',#线型和颜色
        alpha=0.6,#透明度
        grid=True,#网格线
        rot=45,#横坐标的文字旋转
        use_index=True#是否拿index做索引，不是的话，会自动用数字做索引。默认True
        )

#dataframe，可以印在同一个表，也可以弄成subplot
df=pd.DataFrame(np.random.rand(20,4),columns=list('ABCD'),index=pd.date_range('2019-1-1',periods=20)).cumsum()
df.plot(kind='barh',#bar是竖柱状图，加个h就是横向柱状图
        style='-o',
        alpha=0.8,
        grid=True,
        subplots=True,#子图，可以直接创建
        colormap='Blues',
        figsize=(10,20),
        legend=False,
        title='mygraph'
        )

#密度图
df.plot(kind='kde',
        figsize=(6,4),
        color=list('rgb')+['purple'])