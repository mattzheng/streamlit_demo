# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import numpy as np
import time

'''
# cache

整个文档可参考:https://docs.streamlit.io/en/stable/caching.html

当您用@st标记一个函数时。缓存装饰器，它告诉Streamlit无论何时调用函数都需要检查以下几件事:

- The input parameters that you called the function with
- The value of any external variable used in the function
- The body of the function
- The body of any function used inside the cached function

**cache在后台操作的步骤为：**
```
For example, when the function expensive_computation(a, b), decorated with @st.cache, is executed with a=2 and b=21, Streamlit does the following:

1 Computes the cache key
    
2 If the key is found in the cache, then:

- Extracts the previously-cached (output, output_hash) tuple.

- Performs an Output Mutation Check, where a fresh hash of the output is computed and compared to the stored output_hash.

    - If the two hashes are different, shows a Cached Object Mutated warning. (Note: Setting allow_output_mutation=True disables this step).

3 If the input key is not found in the cache, then:

- Executes the cached function (i.e. output = expensive_computation(2, 21)).

- Calculates the output_hash from the function’s output.

- Stores key → (output, output_hash) in the cache.

4 Returns the output.
```


'''

"""
## 1 不适用cache的方式

比如求指数，如果不缓存，重新刷新一次还是需要重新计算
"""

import streamlit as st
import time

def expensive_computation(a, b):
    time.sleep(2)  # 👈 This makes the function take 2s to run
    return a * b

a = 2
b = 21
res = expensive_computation(a, b)

st.write("Result:", res)


# @st.cache  # 👈 Added this
# def expensive_computation(a, b):
#     time.sleep(2)  # This makes the function take 2s to run
#     return a * b

# a = 2
# b = 21
# res = expensive_computation(a, b)

# st.write("Result:", res)

"""
## 2 cache
cache能不能被使用得到，可以通过st.write检测

suppress_st_warning可以关闭一些因为缓存还没计算出，带来的报错

- cache状态下,支持随时修改函数的参数
- cache状态下,支持任意函数结构改变

"""

@st.cache(suppress_st_warning=True)  # 👈 Changed this
def expensive_computation(a, b):
    # 👇 Added this
    st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
    time.sleep(2)  # This makes the function take 2s to run
    return a * b

a = 2
b = 21
res = expensive_computation(a, b)

st.write("Result:", res)


"""
## 3 cache + 可选项

设置一个slider选项，这种情况会发生：
- 如果之前没有看到过slider里面的数字，那么就会重新执行
- 如果有，那么就会直接跳出
- 另外一种，如果接下来这个web会被多人使用，其他人调用过的，也是没有问题的！

功能强大，就不用自己写cache了,简直`神器`！

"""

@st.cache(suppress_st_warning=True)
def expensive_computation(a, b):
    st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
    time.sleep(2)  # This makes the function take 2s to run
    return a * b

a = 2
b = st.slider("Pick a number", 0, 10)  # 👈 Changed this
res = expensive_computation(a, b)

st.write("Result:", res)


"""
## 4 cache 返回字典型

如果返回字典性，会以json的格式展示，非常方便

同时缓存机制有一个比较大的问题:
    - 比如第一次正常执行`res['output'] = 1`
    - 然而，不改变a/b的情况下，再刷新页面一次，因为a/b没变，所以就没有重新计算`expensive_computation(a, b)`
    就会造成`res['output'] = "result was manually mutated" `， 这个时候就有问题，会报错提醒：

```
CachedObjectMutationWarning: Return value of expensive_computation() was mutated between runs.
```

**所以尽量避免生成值之后的再赋值。**

"""


@st.cache(suppress_st_warning=True)
def expensive_computation(a, b):
    st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
    time.sleep(2)  # This makes the function take 2s to run
    return {"output": a * b}  # 👈 Mutable object

a = 2
b = 21
res = expensive_computation(a, b)

st.write("Result:", res)

res["output"] = "result was manually mutated"  # 👈 Mutated cached value

st.write("Mutated result:", res)









