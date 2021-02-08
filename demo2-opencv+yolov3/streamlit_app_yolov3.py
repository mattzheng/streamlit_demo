# -*- coding: utf-8 -*-
# Copyright 2018-2019 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This demo lets you to explore the Udacity self-driving car image dataset.
# More info: https://github.com/streamlit/demo-self-driving

import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import os, urllib, cv2

# 画图
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

from utils import download_file,yolo_v3,draw_image_with_boxes,load_local_image

# This sidebar UI lets the user select parameters for the YOLO object detector.
def object_detector_ui():
    st.sidebar.markdown("### 第二步:调整目标检测参数:")
    confidence_threshold = st.sidebar.slider("Confidence threshold", 0.0, 1.0, 0.5, 0.01)
    overlap_threshold = st.sidebar.slider("Overlap threshold", 0.0, 1.0, 0.3, 0.01)
    return confidence_threshold, overlap_threshold


# 目标检测
# This is the main app app itself, which appears when the user selects "Run the app".
def run_the_app():
    # 自己文件上传  -   单文件载入
    st.sidebar.markdown("### 第一步：选择本地的一张图片(png/jpg)...")
    uploaded_file = st.sidebar.file_uploader(" ")
    
    confidence_threshold, overlap_threshold = object_detector_ui()
    
    left_column,middle_column, right_column = st.sidebar.beta_columns(3)
    
    if middle_column.button('检测'):
        image = load_local_image(uploaded_file)
        st.image(uploaded_file, caption='The original image',
                 use_column_width=True)
        
        yolo_boxes = yolo_v3(image, confidence_threshold, overlap_threshold)
        draw_image_with_boxes(image, yolo_boxes, "Real-time Computer Vision",
            "**YOLO v3 Model** (overlap `%3.1f`) (confidence `%3.1f`)" % (overlap_threshold, confidence_threshold))

@st.cache(show_spinner=False)
def read_markdown(path):
    with open(path, "r",encoding = 'utf-8') as f:  # 打开文件
        data = f.read()  # 读取文件
    return data

# Streamlit encourages well-structured code, like starting execution in a main() function.
def main():
    # 1 初始化界面
    # Render the readme as markdown using st.markdown.
    readme_text = st.markdown(read_markdown("instructions_yolov3.md"))
    
    # 2 下载yolov3的模型文件
    # Download external dependencies.
    for filename in EXTERNAL_DEPENDENCIES.keys():
        download_file(filename)
        # 下载yolov3文件

    # Once we have the dependencies, add a selector for the app mode on the sidebar.
    st.sidebar.title("图像检测参数调节器")   # 侧边栏
    app_mode = st.sidebar.selectbox("切换页面模式:",
        ["Run the app","Show instructions", "Show the source code"])
    
    # 展示栏目三
    if app_mode == "Run the app":
        #readme_text.empty()      # 刷新页面
        st.markdown('---')
        st.markdown('## YOLOv3 检测结果:')
        run_the_app() # 运行内容
    # 展示栏目一
    elif app_mode == "Show instructions":
        st.sidebar.success('To continue select "Run the app".')
    # 展示栏目二
    elif app_mode == "Show the source code":
        readme_text.empty()     # 刷新页面
        st.code(read_markdown("streamlit_app_yolov3.py"))



if __name__ == "__main__":
    file_path = 'yolov3.weights'
    # Path to the Streamlit public S3 bucket
    DATA_URL_ROOT = "https://streamlit-self-driving.s3-us-west-2.amazonaws.com/"
    
    # External files to download.
    EXTERNAL_DEPENDENCIES = {
        "yolov3.weights": {
            "url": "https://pjreddie.com/media/files/yolov3.weights",
            "size": 248007048
        },
        "yolov3.cfg": {
            "url": "https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg",
            "size": 8342
        }
    }
    
    
    main()
