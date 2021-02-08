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



# # 下载yolov3文件

# This file downloader demonstrates Streamlit animation.
def download_file(file_path):
    # Don't download the file twice. (If possible, verify the download using the file length.)
    if os.path.exists(file_path):
        if "size" not in EXTERNAL_DEPENDENCIES[file_path]:
            return
        elif os.path.getsize(file_path) == EXTERNAL_DEPENDENCIES[file_path]["size"]:
            return

    # These are handles to two visual elements to animate.
    weights_warning, progress_bar = None, None
    try:
        weights_warning = st.warning("Downloading %s..." % file_path)
        progress_bar = st.progress(0)
        with open(file_path, "wb") as output_file:
            with urllib.request.urlopen(EXTERNAL_DEPENDENCIES[file_path]["url"]) as response:
                length = int(response.info()["Content-Length"])
                counter = 0.0
                MEGABYTES = 2.0 ** 20.0
                while True:
                    data = response.read(8192)
                    if not data:
                        break
                    counter += len(data)
                    output_file.write(data)

                    # We perform animation by overwriting the elements.
                    weights_warning.warning("Downloading %s... (%6.2f/%6.2f MB)" %
                        (file_path, counter / MEGABYTES, length / MEGABYTES))
                    progress_bar.progress(min(counter / length, 1.0))

    # Finally, we remove these visual elements by calling .empty().
    finally:
        if weights_warning is not None:
            weights_warning.empty()
        if progress_bar is not None:
            progress_bar.empty()

# This sidebar UI lets the user select parameters for the YOLO object detector.
def object_detector_ui():
    st.sidebar.markdown("### 第二步:调整目标检测参数:")
    confidence_threshold = st.sidebar.slider("Confidence threshold", 0.0, 1.0, 0.5, 0.01)
    overlap_threshold = st.sidebar.slider("Overlap threshold", 0.0, 1.0, 0.3, 0.01)
    return confidence_threshold, overlap_threshold

# Draws an image with boxes overlayed to indicate the presence of cars, pedestrians etc.
def draw_image_with_boxes(image, boxes, header, description):
    # Superpose the semi-transparent object detection boxes.    # Colors for the boxes
    LABEL_COLORS = {
        "car": [255, 0, 0],
        "pedestrian": [0, 255, 0],
        "truck": [0, 0, 255],
        "trafficLight": [255, 255, 0],
        "biker": [255, 0, 255],
    }
    image_with_boxes = image.astype(np.float64)
    for _, (xmin, ymin, xmax, ymax, label) in boxes.iterrows():
        image_with_boxes[int(ymin):int(ymax),int(xmin):int(xmax),:] += LABEL_COLORS[label]
        image_with_boxes[int(ymin):int(ymax),int(xmin):int(xmax),:] /= 2

    # Draw the header and image.
    st.subheader(header)
    st.markdown(description)
    st.image(image_with_boxes.astype(np.uint8), use_column_width=True)




# Run the YOLO model to detect objects.
def yolo_v3(image, confidence_threshold, overlap_threshold):
    # Load the network. Because this is cached it will only happen once.
    @st.cache(allow_output_mutation=True)
    def load_network(config_path, weights_path):
        net = cv2.dnn.readNetFromDarknet(config_path, weights_path)
        output_layer_names = net.getLayerNames()
        output_layer_names = [output_layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        return net, output_layer_names
    net, output_layer_names = load_network("yolov3.cfg", "yolov3.weights")

    # Run the YOLO neural net.
    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    layer_outputs = net.forward(output_layer_names)

    # Supress detections in case of too low confidence or too much overlap.
    boxes, confidences, class_IDs = [], [], []
    H, W = image.shape[:2]
    for output in layer_outputs:
        for detection in output:
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]
            if confidence > confidence_threshold:
                box = detection[0:4] * np.array([W, H, W, H])
                centerX, centerY, width, height = box.astype("int")
                x, y = int(centerX - (width / 2)), int(centerY - (height / 2))
                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                class_IDs.append(classID)
    indices = cv2.dnn.NMSBoxes(boxes, confidences, confidence_threshold, overlap_threshold)

    # Map from YOLO labels to Udacity labels.
    UDACITY_LABELS = {
        0: 'pedestrian',
        1: 'biker',
        2: 'car',
        3: 'biker',
        5: 'truck',
        7: 'truck',
        9: 'trafficLight'
    }
    xmin, xmax, ymin, ymax, labels = [], [], [], [], []
    if len(indices) > 0:
        # loop over the indexes we are keeping
        for i in indices.flatten():
            label = UDACITY_LABELS.get(class_IDs[i], None)
            if label is None:
                continue

            # extract the bounding box coordinates
            x, y, w, h = boxes[i][0], boxes[i][1], boxes[i][2], boxes[i][3]

            xmin.append(x)
            ymin.append(y)
            xmax.append(x+w)
            ymax.append(y+h)
            labels.append(label)

    boxes = pd.DataFrame({"xmin": xmin, "ymin": ymin, "xmax": xmax, "ymax": ymax, "labels": labels})
    return boxes[["xmin", "ymin", "xmax", "ymax", "labels"]]


@st.cache(show_spinner=False)
def load_local_image(uploaded_file):
    bytes_data = uploaded_file.getvalue()  
    # 所有内容都读入，并不是读入一个地址链接 
    # 相当于 filename.read()的方式读入
    # st.write(bytes_data[:100])
    
    # Image.open(BytesIO(bytes_data))
    	# 转成array格式——常规
    image = np.array(Image.open(BytesIO(bytes_data)))
    # st.write(image)
    # st.sidebar.success('sccess load image ')
    return image

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
