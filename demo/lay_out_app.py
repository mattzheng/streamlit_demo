import streamlit as st
import pandas as pd
import numpy as np
import time


'''
## 1 lay out your app

'''


""" ### 1.1 `streamlit.beta_container()`

通过`with st.beta_container():`，可以Book一个组件模块
将一个不可见的容器插入到你的应用程序中，可以用来保存多个元素。
    """
    
# with写法
with st.beta_container():
   st.write("This is inside the container")
   # You can call any Streamlit command, including custom components:
   st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")

# 常规写法
container = st.beta_container()
container.write("This is inside the container")
st.write("This is outside the container")

# Now insert some more in the container
container.write("This is inside too")



""" ### 1.1 分列展示

 `streamlit.beta_columns(spec)`

以并排列的形式插入容器。插入多个并排放置的多元素容器，并返回容器对象列表。

要向返回的容器添加元素，可以使用“with”表示法(首选)，或者直接调用返回对象的方法。

请参见下面的例子。

"""


col1, col2, col3 = st.beta_columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", use_column_width=True)

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", use_column_width=True)

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", use_column_width=True)


""" ### 1.2 按照比例分列展示


"""
col1, col2 = st.beta_columns([3, 1])
data = np.random.randn(10, 1)

col1.subheader("A wide column with a chart")
col1.line_chart(data)

col2.subheader("A narrow column with the data")
col2.write(data)


""" ### 1.2 折叠/展开

`streamlit.beta_expander(label=None, expanded=False)`

"""


st.line_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.beta_expander("See explanation"):
    st.write("""
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    """)
    st.image("https://static.streamlit.io/examples/dice.jpg")






