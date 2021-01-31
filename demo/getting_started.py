
import streamlit as st
import pandas as pd
import numpy as np


'''
## 1 新增标题

本篇主要参考的是streamlit的[doc getting_started ](https://docs.streamlit.io/en/stable/getting_started.html)

'''

st.title('My first app')

'''
## 2 新增正文
'''

st.write('可以支持中文吗？')

'''
## 3 新增表格

专门的data展示模块：https://docs.streamlit.io/en/stable/tutorial/create_a_data_explorer_app.html
'''

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

'''
## 4 Magic commands

**工作台markdown模式**,它允许你用很少的按键将markdown和数据写入应用程序。


- `"""a"""` = st.write
- `df = st.write(pd.DataFrame)`

可以参考具体文档:[magic-commands](https://docs.streamlit.io/en/stable/api.html#magic-commands)


Here's our first attempt at using data to create a table:
'''

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

'''
## 5 画图 - Draw charts and maps

streamlit可以支持很多地图

这边先展示两个图：
- 直线图
- 地图

'''

st.write("这边是直线图:")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.write("这边是地图:")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)



'''
## 6 新增交互组件和小组件

- 使用复选框(checkboxes)去展示/隐藏数据
- 使用下拉框(selectbox)

'''
st.write("这里是复选框:")
if st.checkbox('是否展示内容:'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)




'''
---
'''

st.write("这里是下拉框:")
option = st.selectbox(
    'Which number do you like best?',
      df['first column'])

'You selected: ', df[df['first column'] == option]



# '''
# ## 7 布局你的app

# 与下拉框只能存在一个

# - 下拉框在页面的左边，不跟上面的一样，瀑布流累计
# '''
# option = st.sidebar.selectbox(
#     'Which number do you like best?',
#      df['first column'])

# 'You selected:', option

'''
## 8 同一行，分模块展示
布局按钮
'''
left_column,middle_column, right_column = st.beta_columns(3)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("哈哈，别乱点!")
    middle_column.write("我在中间!")


'''
## 9 横向下拉框，beta_expander隐藏一些大型的内容
'''
expander = st.beta_expander("FAQ")
expander.write(df[df['first column'] == option])
expander.write("选项二")


'''
## 10 进度条 Show progress

其中`bar.progress()`不能超过100

'''

import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'

