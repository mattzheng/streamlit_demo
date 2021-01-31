

import streamlit as st
import pandas as pd
import numpy as np
import time

"""
# 一些elements/组件

文献参考：https://docs.streamlit.io/en/stable/advanced_concepts.html

"""

""" ## 1 空白占位符placeholder: st.empty()  """

st.text('This will appear first')
# Appends some text to the app.

my_slot1 = st.empty()
# Appends an empty slot to the app. We'll use this later.

my_slot2 = st.empty()
# Appends another empty slot.

st.text('This will appear last')
# Appends some more text to the app.

my_slot1.text('This will appear second')
# Replaces the first empty slot with a text string.

my_slot2.line_chart(np.random.randn(20, 2))
# Replaces the second empty slot with a chart.

""" 
## 2 Animate elements 动画元素

原理还是定时任务，不断新增。

最后的`st.balloons()` 是一个有有意思的气球动画。


"""
progress_bar = st.progress(0)
status_text = st.empty()
chart = st.line_chart(np.random.randn(10, 2))

for i in range(100):
    # Update progress bar.
    progress_bar.progress(i + 1)

    new_rows = np.random.randn(10, 2)

    # Update status text.
    status_text.text(
        'The latest random number is: %s' % new_rows[-1, 1])

    # Append data to the chart.
    chart.add_rows(new_rows)

    # Pretend we're doing some computation that takes time.
    time.sleep(0.01)

status_text.text('Done!')
st.balloons()



""" 
## 3 录制视频 - Record a screencast

原理还是定时任务，不断新增。

最后的`st.balloons()` 是一个有有意思的气球动画。

在web右上角menu (☰) 
![avatar](https://docs.streamlit.io/en/stable/_images/screenshare.gif)
"""



'''
## 4 显示交互组件 - Display interactive widgets

'''



""" ### 4.1 单个点击按钮-显示内容 `streamlit.button(label, key=None)`  """

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')


""" ### 4.2 单个点击按钮 - 显示内容
`streamlit.checkbox(label, value=False, key=None)`  """
agree = st.checkbox('I agree')
if agree:
    st.write('Great!')


""" ### 4.3 单选按钮 - 多个选项

`streamlit.radio(label, options, index=0, format_func=<class 'str'>, key=None)`  """
genre = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy.")

""" ### 4.4 下拉框按钮
`streamlit.selectbox(label, options, index=0, format_func=<class 'str'>, key=None)`  """

option = st.selectbox(
     'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))
st.write('You selected:', option)


""" ### 4.5 多个选择框 - 选上了就会上记录
`streamlit.multiselect(label, options, default=None, format_func=<class 'str'>, key=None)` """

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])
st.write('You selected:', options)


""" ### 4.6 拉选框
`streamlit.slider(label, min_value=None, max_value=None, value=None, step=None, format=None, key=None)` 

包括：
- 常规滑块 - range slider
- 时间滑块 - time slider
- 日期选项 - datetime slider

"""



age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# 常规滑块 - range slider
values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)


# 时间滑块 - time slider
from datetime import time
appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# 日期选项 - datetime slider
from datetime import datetime
start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)



""" ### 4.7 选择滑块
`streamlit.select_slider(label, options=[], value=None, format_func=<class 'str'>, key=None)` """
# 常规
color = st.select_slider(
     'Select a color of the rainbow',
     options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)

# range select slider 区域范围的选择滑块
start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
     options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
     value=('red', 'blue'))
st.write('You selected wavelengths between', start_color, 'and', end_color)


""" ### 4.8 文本 + 数字输入
- 文字输入:
`streamlit.text_input(label, value='', max_chars=None, key=None, type='default')` 
- 数字输入:
`streamlit.number_input(label, min_value=None, max_value=None, value=<streamlit.elements.utils.NoValue object>, step=None, format=None, key=None)`

"""
# 文本
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

# 数字
number = st.number_input('Insert a number')
st.write('The current number is ', number)

""" ###  4.9  文本输入并执行的框 - 可以直接做一些文本分析的组件
`streamlit.text_area(label, value='', height=None, max_chars=None, key=None)` """

txt = st.text_area('Text to analyze', '''
     It was the best of times, it was the worst of times, it was
     the age of wisdom, it was the age of foolishness, it was
     the epoch of belief, it was the epoch of incredulity, it
     was the season of Light, it was the season of Darkness, it
     was the spring of hope, it was the winter of despair, (...)
     ''')
# st.write('Sentiment:', run_sentiment_analysis(txt))
st.write('Sentiment:', txt)



""" ### 4.10 时间载入

时间载入的两种方式,一般组合时间：日历 + 具体时间  
- `streamlit.date_input(label, value=None, min_value=None, max_value=None, key=None)`

- `streamlit.time_input(label, value=None, key=None)`

"""
import datetime
# 1 
d = st.date_input(
    "When's your birthday",
    datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)

# 2 
t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Alarm is set for', t)


""" ### 4.11 文件载入 - 很重要

`streamlit.file_uploader(label, type=None, accept_multiple_files=False, key=None)`

演示了单个文件 + 多个文件载入的情况

"""
# 单文件载入
uploaded_file = st.file_uploader("Choose a file... csv")
if uploaded_file is not None:
     # To read file as bytes:
     bytes_data = uploaded_file.read()
     st.write(bytes_data)

     # To convert to a string based IO:
     stringio = StringIO(uploaded_file.decode("utf-8"))
     st.write(stringio)

     # To read file as string:
     string_data = stringio.read()
     st.write(string_data)

     # Can be used wherever a "file-like" object is accepted:
     st.write(uploaded_file)
     dataframe = pd.read_csv(uploaded_file)
     st.write(dataframe)

# 多文件载入
uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)


""" ### 4.12 颜色选择

`streamlit.color_picker(label, value=None, key=None)`

选择颜色的一个组件

"""

color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)


'''
## 4 控制组件 - Control flow

'''


""" ### 4.1 输入框  
    只有输入了，才会继续进行下去...
    """

name = st.text_input('Name')
if not name:
    st.warning('Please input a name.')
    st.stop()
st.success(f'Thank you for inputting a name. {name}')



