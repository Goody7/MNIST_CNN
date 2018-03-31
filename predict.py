#coding=utf-8

from __future__ import print_function
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from keras.models import Sequential
from keras.models import load_model

path='/home/goody7' # 修改路径

# 加载已保存的模型 
model = load_model(path+'/mnist_test/model.h5') 

#对测试图片进行预处理
img = Image.open(path+'/mnist_test/test/pen.jpg')
img = img.convert('L') #转换为灰度图像
img = img.resize((28,28)) #缩放为网络要求的输入大小
plt.imshow(img)
plt.show() #显示灰度转换和缩放后的图像
img_array = np.asarray(img,dtype="float32")
img_array = (255 - img_array) / 255 #归一化
img_array = np.reshape(img_array, (28, 28, 1))
img_array = np.expand_dims(img_array,axis=0)

#对测试图像进行分类预测
pred = model.predict(img_array)[0]
bestconf = -1
for n in [0,1,2,3,4,5,6,7,8,9]: 
	if(pred[n] > bestconf):
		bestclass = str(n)
		bestconf = pred[n]
	print(' '+str(n)+' : '+str(pred[n]*100)+'%') #输出每个分类预测到的概率
print(' This digit is most likely to be '+bestclass+'\n')

