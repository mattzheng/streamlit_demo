# streamlit_demo
streamlit一些样例

其中文件夹：

- `demo`文件夹是常规的练习代码

- `demo1-uber-pickups`是数据探索的一个案例，博客：https://mattzheng.blog.csdn.net/article/details/113531457


更新日志：

- 20210201 上传`demo1-uber-pickups`文件夹

- 20210208 上传`demo2-opencv+yolov3`文件夹

- 20210218 上传`demo3-interactive_datetime_filter`文件夹

---

## `demo1-uber-pickups`

在本教程中，您将使用Streamlit的核心功能来创建一个交互式应用程序;探索纽约市打车软件优步的公共接送数据集。

完成后，您将知道如何获取和缓存数据、绘制图表、在地图上绘制信息，并使用交互式小部件(如滑块)来过滤结果。

![av_final_optimized](https://img-blog.csdnimg.cn/20210201224312608.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NpbmF0XzI2OTE3Mzgz,size_16,color_FFFFFF,t_70)




---

## `demo2-opencv+yolov3`

原案例中无法自己上传本地图片进行检测,事先提供好了图片url连接（标记了所有图像Ground Truth的[原标签数据集](https://streamlit-self-driving.s3-us-west-2.amazonaws.com/labels.csv.gz)），

直接download使用，所以不太满足要求  。原来的界面如下：


![av_final_optimized](https://raw.githubusercontent.com/streamlit/demo-self-driving/master/av_final_optimized.gif)


现在的界面如下：
![opencv](https://img-blog.csdnimg.cn/20210208161448931.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NpbmF0XzI2OTE3Mzgz,size_16,color_FFFFFF,t_70
)


---
## `demo3-interactive_datetime_filter`

该案例我还没尝试，只是挪到这里，参考的是：https://github.com/mkhorasani/interactive_datetime_filter

关于他的介绍可以到该文章看一下：[用Pandas和Streamlit对时间序列数据集进行可视化过滤](https://mp.weixin.qq.com/s/TV1MJfaOq27y2DVCGMuqhA)

![具体效果如下：](https://camo.githubusercontent.com/66ae4c74254d04811c253c666b43f92d739a48df607cfae0e5eb0592dc2ef70f/68747470733a2f2f6d69726f2e6d656469756d2e636f6d2f6d61782f3730302f312a4d585a44516861733434364e336b66425f4d615651512e676966)



---


**系列参考：**

[python︱写markdown一样写网页，代码快速生成web工具：streamlit介绍（一）](https://mattzheng.blog.csdn.net/article/details/113484942)

[python︱写markdown一样写网页，代码快速生成web工具：streamlit 重要组件介绍（二）](https://mattzheng.blog.csdn.net/article/details/113485525)

[python︱写markdown一样写网页，代码快速生成web工具：streamlit 展示组件（三）](https://mattzheng.blog.csdn.net/article/details/113486304)

[python︱写markdown一样写网页，代码快速生成web工具：streamlit lay-out布局（四）](https://mattzheng.blog.csdn.net/article/details/113530944)

[python︱写markdown一样写网页，代码快速生成web工具：streamlit 缓存（五）](https://mattzheng.blog.csdn.net/article/details/113531087)

[python︱写markdown一样写网页，代码快速生成web工具：streamlit 数据探索案例（六）](https://mattzheng.blog.csdn.net/article/details/113531457)

[streamlit + opencv/YOLOv3 快速构建自己的图像目标检测demo网页（七）](https://mattzheng.blog.csdn.net/article/details/113758554)

github代码链接：[mattzheng/streamlit_demo](https://github.com/mattzheng/streamlit_demo)



