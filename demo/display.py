

import streamlit as st
import pandas as pd
import numpy as np
import time

"""
# Display 

文献参考：https://docs.streamlit.io/en/stable/api.html#display-text



"""

""" 

# 1 文本显示 display-text  

- 常规文本 - `st.text`
- 写markdown - `st.markdown`
- 写latex - `st.latex`
- 直接写标题 - `st.title`
- 写副标题 - `st.subheader`

"""

st.text('This will appear first')
# Appends some text to the app.

st.title('This is a title')
st.subheader('This is a subheader')

st.markdown('Streamlit is **_really_ cool**.')

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

"""1.1 **`st.write`的各种写法**
- text
- dataframe:可以穿插着写，非常方便
- 可以直接写出表格

"""

st.write('Hello, *World!* :sunglasses:')



data_frame = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
})

st.write(1234)
st.write(data_frame)


st.write('1 + 1 = ', 2)
st.write('Below is a DataFrame:', data_frame, 'Above is a dataframe.')


"""**1.2 直接写表格/图表**"""

import pandas as pd
import numpy as np
import altair as alt

df = pd.DataFrame(
    np.random.randn(200, 3),
   columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)


"""**1.3 直接写代码**"""
code = '''def hello():
     print("Hello, Streamlit!")'''
st.code(code, language='python')



""" 

# 2 数据展示 - Display data

其中主函数:
- 展示dataframe: `streamlit.dataframe(data=None, width=None, height=None)`
- 展示json : `st.json`

"""

df = pd.DataFrame(
   np.random.randn(50, 20),
  columns=('col %d' % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)

""" 可以规定显示多少行列 - (width,height) """
st.dataframe(df, 200, 100)

""" `st.dataframe`显示数据集 """
df = pd.DataFrame(
   np.random.randn(10, 20),
  columns=('col %d' % i for i in range(20)))

st.dataframe(df.style.highlight_max(axis=0))

""" `st.table`显示数据集 """
df = pd.DataFrame(
   np.random.randn(10, 5),
   columns=('col %d' % i for i in range(5)))

st.table(df)

""" `st.json`以json的形式展示 """
st.json({
     'foo': 'bar',
     'baz': 'boz',
     'stuff': [
         'stuff 1',
         'stuff 2',
         'stuff 3',
         'stuff 5',
     ],
 })


""" 

# 3 图表展示

- 直线图: `streamlit.line_chart(data=None, width=0, height=0, use_container_width=True)`
- 面积图: `streamlit.area_chart(data=None, width=0, height=0, use_container_width=True)`
- 柱状图: `streamlit.bar_chart(data=None, width=0, height=0, use_container_width=True)`
- 气泡图: `streamlit.altair_chart(altair_chart, use_container_width=False)`
- 气泡图2: `streamlit.altair_chart(altair_chart, use_container_width=False)`
- pyplot所有的图表:`streamlit.vega_lite_chart(data=None, spec=None, use_container_width=False, **kwargs)`
- plotly所有的图表: `streamlit.plotly_chart(figure_or_data, use_container_width=False, sharing='streamlit', **kwargs)`
- 逻辑导图 `streamlit.graphviz_chart(figure_or_dot, use_container_width=False)`
- 地图 `streamlit.map(data=None, zoom=None, use_container_width=True)`
    
    
需要安装一下:
```
pip install --pre plotly -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install --pre graphviz -i https://pypi.tuna.tsinghua.edu.cn/simple
```


参考url:
https://docs.streamlit.io/en/stable/api.html#display-charts

"""


""" 3.1 `st.line_chart`直线图 """
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

""" 3.2 `st.area_chart`面积图 """
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.area_chart(chart_data)

""" 3.3 `st.bar_chart`柱状图 """
chart_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=["a", "b", "c"])

st.bar_chart(chart_data)

""" 3.4 `st.altair_chart`气泡图 """
df = pd.DataFrame(
 np.random.randn(200, 3),
 columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
 x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.altair_chart(c, use_container_width=True)
 
 
""" 3.5 `st.vega_lite_chart`气泡图2 """
df = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])

st.vega_lite_chart(df, {
     'mark': {'type': 'circle', 'tooltip': True},
     'encoding': {
         'x': {'field': 'a', 'type': 'quantitative'},
         'y': {'field': 'b', 'type': 'quantitative'},
         'size': {'field': 'c', 'type': 'quantitative'},
         'color': {'field': 'c', 'type': 'quantitative'},
     },
 })

""" 3.6 `pyplot`所有的图表  """
import matplotlib.pyplot as plt
import numpy as np
import plotly.figure_factory as ff

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

""" 3.7 `plotly`所有图  """

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
         hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)


""" 3.7 逻辑导图`graphviz_chart`  """
import streamlit as st
import graphviz as graphviz

# Create a graphlib graph object
graph = graphviz.Digraph()
graph.edge('run', 'intr')
graph.edge('intr', 'runbl')
graph.edge('runbl', 'run')
graph.edge('run', 'kernel')
graph.edge('kernel', 'zombie')
graph.edge('kernel', 'sleep')
graph.edge('kernel', 'runmem')
graph.edge('sleep', 'swap')
graph.edge('swap', 'runswap')
graph.edge('runswap', 'new')
graph.edge('runswap', 'runmem')
graph.edge('new', 'runmem')
graph.edge('sleep', 'runmem')

st.graphviz_chart(graph)


st.graphviz_chart('''
    digraph {
        run -> intr
        intr -> runbl
        runbl -> run
        run -> kernel
        kernel -> zombie
        kernel -> sleep
        kernel -> runmem
        sleep -> swap
        swap -> runswap
        runswap -> new
        runswap -> runmem
        new -> runmem
        sleep -> runmem
    }
''')


""" 3.8 地图`map`  """

df = pd.DataFrame(
     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
     columns=['lat', 'lon'])

st.map(df)



""" 

# 4 Display media

图片/视频该如何展示

展示图片:
`streamlit.image(image, caption=None, width=None, use_column_width=False, 
                 clamp=False, channels='RGB', output_format='auto', **kwargs)`
    
展示音频：
`streamlit.audio(data, format='audio/wav', start_time=0)`

展示视频:
`streamlit.video(data, format='video/mp4', start_time=0)`


> Some videos may not display if they are encoded using MP4V (which is an export option in OpenCV),\
>    as this codec is not widely supported by browsers. 
>    Converting your video to H.264 will allow the video to be displayed in Streamlit. 
>    See this StackOverflow post or this Streamlit forum post for more information.

需要安装一下:
```

```


参考url:
https://docs.streamlit.io/en/stable/api.html#display-media

"""

filepath = 'demo/'

""" 4.1 展示图片  """
from PIL import Image
image = Image.open(filepath + 'sunrise.jpg')

st.image(image, caption='Sunrise by the mountains',
         use_column_width=True)



""" 4.2 打开音频  """
audio_file = open(filepath + 'myaudio.ogg', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/ogg')

""" 4.3 打开视频  """

video_file = open(filepath + 'myvideo.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)


""" 

# 5 展示代码 - Display code

`st.echo()`

""" 

with st.echo():
    st.write('This code will be printed')



""" 

# 6 展示进度与状态 - 时间组件
 Display progress and status

""" 

import time

""" 6.1 按时间的进度
`my_bar.progress`
 """
my_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)


""" 6.2 时间组件 - 进行中的标识

如果有一段代码在运行，那么可以使用这个，
在执行的时候会有"wait for it"的提示.

"""

with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')


""" 6.3 进击的气球

有一排气球往上飞

"""
st.balloons()

""" 6.4 展示报错

"""
st.error('This is an error')























