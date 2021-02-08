
## streamlit + opencv/YOLOv3 几行代码构建图像目标检测的demo网页

本案例脱胎于[Udacity自动驾驶汽车图像识别](https://github.com/streamlit/demo-self-driving)

代码链接:[implemented in less than 300 lines of Python](https://github.com/streamlit/demo-self-driving/blob/master/streamlit_app.py)

原案例中无法自己上传,图表开源都是事先准备好,当然也有标记了所有图像Ground Truth的[原标签数据集](https://streamlit-self-driving.s3-us-west-2.amazonaws.com/labels.csv.gz)
可见案例:


![av_final_optimized](https://raw.githubusercontent.com/streamlit/demo-self-driving/master/av_final_optimized.gif)


### 依赖安装

使用之前需要加载:

```
pip install --upgrade streamlit opencv-python
```


或者直接用线上的文件也是可以的:

```
streamlit run https://raw.githubusercontent.com/streamlit/demo-self-driving/master/streamlit_app.py
```

### 使用

- 第一步：选择本地的一张图片(png/jpg)...
- 第二步:调整目标检测参数
- 第三步：点击检测的按钮




