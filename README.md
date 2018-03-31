# MNIST_CNN
## Requirements

- Python 2.7
- TensorFlow 
- Numpy
- keras 

## Introduction

该代码主要利用Keras框架实现分类模型的训练与预测。<br>
该代码利用MNIST数据库训练了一个含2个卷积层、2个池化层、1个Flatten层、2个全连接层的神经网络，并利用Adam函数进行模型优化。<br>
该神经网络的整体架构为：输入图片→卷积层→池化层→卷积层→池化层→Flatten层→全连接层→输出层。<br>
通过model.summary()函数输出的网络模型的具体参数如下图所示：
![](https://github.com/Goody7/MNIST_CNN/blob/master/result/summary.png)<br>
MNIST数据集包含70000张手写数字的灰度图片，其中每一张图片包含 28 * 28 个像素点。数据集被分成两部分：60000行的训练数据集和10000行的测试数据集，其中60000行的训练集分拆为55000行的训练集和5000行的验证集。利用MNIST数据集中的训练集对搭建好的神经网络进行训练，并用测试集对训练后神经网络进行准确率测试。在迭代10次后，准确率稳定在0.9942。

## Usage

result文件夹:存储输入图片的预测结果<br>
test文件夹: 测试图像（包含手写数字图片和其他类别的图片）<br>
mnist_model.py: 训练模型并保存<br>
predict.py: 将待预测图片输入训练好的模型，并输出预测结果<br>
model.h5: 已经训练好的模型<br>

由于本人已将训练好的mnist_cnn模型保存下来，使用者只需运行predict.py文件就可以得到测试图片的预测结果。<br>
如果你想自己设计一个网络结构进行训练，可以对mnist_model.py文件中的网络搭建部分代码进行修改并训练保存自己的模型，然后再运行predict.py文件得到预测结果。<br>
`运行之前记得将每个文件的路径修改为自己的路径！！`

## Result

写这个代码的本意是想做个测试，当对一个已经训练好的模型输入不在数据集内的类别的图片时，模型输出的预测概率能达到多少。下面是本人的一些预测结果。<br>
### Category 1
首先，本人向已训练好模型输入一些不在Mnist数据集中的手写数字图片。<br>
输入模型的测试图片1：<br>
![](https://github.com/Goody7/MNIST_CNN/blob/master/test/2.jpg)<br>
经过预处理后的测试图片：<br>
![](https://github.com/Goody7/MNIST_CNN/blob/master/result/2.png)<br>
输出预测结果：<br>
![](https://github.com/Goody7/MNIST_CNN/blob/master/result/2_.png)<br>

输入模型的测试图片2：<br>
![](https://github.com/Goody7/MNIST_CNN/blob/master/test/7.jpg)<br>
经过预处理后的测试图片：<br>
![](https://github.com/Goody7/MNIST_CNN/blob/master/result/7.png)<br>
输出预测结果：<br>
![](https://github.com/Goody7/MNIST_CNN/blob/master/result/7_.png)<br>

### Category 2
然后，向模型输入一些包含多个数字的图片。<br>
输入模型的测试图片3：<br>
![](https://github.com/Goody7/MNIST_CNN/blob/master/test/16.jpg)<br>
经过预处理后的测试图片：<br>
![](https://github.com/Goody7/MNIST_CNN/blob/master/result/16.png)<br>
输出预测结果：<br>
![](https://github.com/Goody7/MNIST_CNN/blob/master/result/16_.png)<br>

输入模型的测试图片4：<br>
![](https://github.com/Goody7/MNIST_CNN/blob/master/test/22.jpg)<br>
经过预处理后的测试图片：<br>
![](https://github.com/Goody7/MNIST_CNN/blob/master/result/22.png)<br>
输出预测结果：<br>
![](https://github.com/Goody7/MNIST_CNN/blob/master/result/22_.png)<br>

输入模型的测试图片5：<br>
![](https://github.com/Goody7/MNIST_CNN/blob/master/test/504192.jpg)<br>
经过预处理后的测试图片：<br>
![](https://github.com/Goody7/MNIST_CNN/blob/master/result/504192.png)<br>
输出预测结果：<br>
![](https://github.com/Goody7/MNIST_CNN/blob/master/result/504192_.png)<br>

### Category 3
最后，向模型输入不在Mnist数据集中的类别的图片（例如飞机、汽车、动物等）。<br>
输入模型的测试图片6：<br>
![](https://github.com/Goody7/MNIST_CNN/blob/master/test/airplane.jpg)<br>
经过预处理后的测试图片：<br>
![](https://github.com/Goody7/MNIST_CNN/blob/master/result/airplane.png)<br>
输出预测结果：<br>
![](https://github.com/Goody7/MNIST_CNN/blob/master/result/airplane_.png)<br>

输入模型的测试图片7：<br>
![](https://github.com/Goody7/MNIST_CNN/blob/master/test/car.jpg)<br>
经过预处理后的测试图片：<br>
![](https://github.com/Goody7/MNIST_CNN/blob/master/result/car.png)<br>
输出预测结果：<br>
![](https://github.com/Goody7/MNIST_CNN/blob/master/result/car_.png)<br>

输入模型的测试图片8：<br>
![](https://github.com/Goody7/MNIST_CNN/blob/master/test/cat.jpg)<br>
经过预处理后的测试图片：<br>
![](https://github.com/Goody7/MNIST_CNN/blob/master/result/cat.png)<br>
输出预测结果：<br>
![](https://github.com/Goody7/MNIST_CNN/blob/master/result/cat_.png)<br>

输入模型的测试图片9：<br>
![](https://github.com/Goody7/MNIST_CNN/blob/master/test/dog1.jpg)<br>
经过预处理后的测试图片：<br>
![](https://github.com/Goody7/MNIST_CNN/blob/master/result/dog1.png)<br>
输出预测结果：<br>
![](https://github.com/Goody7/MNIST_CNN/blob/master/result/dog1_.png)<br>

输入模型的测试图片10：<br>
![](https://github.com/Goody7/MNIST_CNN/blob/master/test/pen.jpg)<br>
经过预处理后的测试图片：<br>
![](https://github.com/Goody7/MNIST_CNN/blob/master/result/pen.png)<br>
输出预测结果：<br>
![](https://github.com/Goody7/MNIST_CNN/blob/master/result/pen_.png)<br>
