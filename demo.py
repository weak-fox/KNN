from PIL import Image
import os
import cv2
import numpy as np
import random
from KNN_train import run

np.set_printoptions(threshold=np.inf)#用于显示所有结果
list = os.listdir("numpic_test")
root=os.getcwd()        #获取当前目录
random.shuffle(list)    #打乱类表，用于随机选取
for i in list[0:10]:    #取打乱的列表的前10个，相当于随机选取
    img = Image.open(root+"\\numpic_test\\"+i).convert('L')#打开图片并进行灰度化
    img=np.asarray(img) #将图片转换为numpy数组
    img =cv2.resize(img,(32,32))    #调整图片大小
    img=cv2.threshold(img,30,1,cv2.THRESH_BINARY)   #图像0/1二值化，阈值为30（像素点值高于30的为1，低于的为0）
    if not os.path.exists("numtxt"):                
        os.makedirs("numtxt")               #创建临时文件夹
    file = open(root+"\\numtxt\\"+i.split('.')[0]+'.txt','w')   
    text = ''
    for j in img[1]:                    #将数组中的数据保存到文本中，需要去掉[]
        text = text+str(j)          
    text=text.replace('[','')
    text=text.replace(']','\n')
    text=text.replace(' ','')
    file.write(text)
    file.close()
run() #在KNN_train中