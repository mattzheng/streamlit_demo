# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')
"""
## 1 数据探索性app - Create a data explorer app

在本教程中，您将使用Streamlit的核心功能来创建一个交互式应用程序;
探索纽约市打车软件优步的公共接送数据集。
完成后，您将知道如何获取和缓存数据、绘制图表、在地图上绘制信息，并使用交互式小部件(如滑块)来过滤结果。
"""


'''
## 2 加载数据
现在你有了一款应用程序，接下来你需要做的就是获取纽约市取车和落车的优步数据集。

streamlit好处就在于cache只加载最初一次即可,其他的时候都会保存到缓存之中.

只要执行：
load_data(10000)
后续的text都需要等他加载完才会出现。

'''
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)

data_load_state.text("在(using st.cache)之前一行！ ")
data_load_state.text("Done! (using st.cache)")
data_load_state.text("在(using st.cache)之后一行! ")  # 这里的三行 .text 最后只会显示最后一行


'''
## 3 复选框 - 是否显示数据

- subheader 添加副标题,Raw data
- 写出dataframe的data

'''
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


'''
## 4 画柱状图
'''
st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

'''
## 5 展示特定数据 + 画地图

这里也还是可以使用其他栏目，比如下拉框
```
option = st.selectbox(
    'Which number do you like best?',
      [1,2,3,4,5])
```

主要的数据格式为:
```
data/time | lat | lon | base
```
其中,这里的base,B02512,指的是不同的国家地区的编码？

'''
# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)



dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

'''
dataframe 显示方式一：sr.write
'''
st.write(dataframe)

'''
dataframe 显示方式二：直接键入最终结果dataframe
'''
dataframe

'''
dataframe 显示方式三：st.dataframe
'''
st.dataframe(dataframe.style.highlight_max(axis=0))

'''
dataframe 显示方式四：st.table 
最丑的一种方式，会变成无页面约束的宽表
'''
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)



