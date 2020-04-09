import numpy as np
import pandas as pd
import os
from KNN import KNN
import shutil


def  img2vector(filename):              #将文本中的文件化到一行
	rows = 32  
	cols = 32  
	imgVector = np.zeros((1, rows * cols))         #初始化数组
	fileIn = open(filename)         #读入文件
	for row in range(rows):         #遍历每一行
		lineStr = fileIn.readline()  #读入行内容
		for col in range(cols):  #遍历每一列
			imgVector[0, row * 32 + col] = int(lineStr[col])  #以行优先的方式分别读入
	return imgVector  
def run():
        root=os.getcwd()                #获取根目录文件夹位置
        list = os.listdir("trainDigits")        #获取trainDigits文件夹下所有文件名保存到list中
        x_train = np.zeros((1,1024))            #初始化训练数组
        y_train=[]                              #初始化训练标签列表
        j=0                                     #用于判断是不是第一次进入循环
        for i in list:
                data=img2vector(root+"\\trainDigits\\"+i)
                if(j==0):
                        x_train=data[:]         #第一次需要赋值
                        j=j+1
                else:
                        x_train = np.vstack((x_train,data[:]))#之后每一次都在最下面一行底下添加一行
                y_train.append(int(i.split("_")[0]))             #将训练标签导入
        knn = KNN(k=5)                  #创建类对象
        knn.train(x_train,y_train)      #对类训练
        list = os.listdir("numtxt")     #遍历文件夹下所有文件将文件名保存到list中
        for i in list:
                data=img2vector(root+"\\numtxt\\"+i)#读入文件并保存到data中
                #文件名对应结果
                x_test = np.zeros((1,1024))     #初始化测试数组
                x_test=data[:]                  #将数据存入测试数组中
                result = knn.predict(x_test)    #对数组进行预测
                print('文件名：{}  结果：{}'.format(i,result))#输出结果
        shutil.rmtree('numtxt')#删除创建的临时文件夹
        