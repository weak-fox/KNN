import numpy as np

class KNN:
    def __init__(self, k):  #k表示所选点周围邻居个数
        self.k = k


    def train(self , X , y):        #X为待训练的样本数组，y为样本的标签
        self.X = np.asarray(X)      #用于训练数据的的输入，用于predict距离的对比
        self.y = np.asarray(y)      #用于训练数据的的输入，用于predict结果的确定
    
    def predict(self,X):    #X为待训练的样本数组
        X = np.asarray(X)   #转化为numpy数组，好进行数据处理
        result = []         #初始化result，用于返回
        for x in X:         #用于遍历每一行，一行一张图片，由k-means算法联想到
            dis=np.sqrt(np.sum((x - self.X) ** 2,axis=1)) #欧式距离，目的进行图像识别，只有0,1不需要马氏距离的归一化
            index = dis.argsort()       #对距离进行排序，返回排序后的索引list
            index = index[:self.k]      #取最近的k个邻居
            count = np.bincount(self.y[index]) #返回这些邻居中每个出现的个数
            result.append(count.argmax())   #将出现最多的标签传入result中
        return np.asarray(result)   #程序返回结果





