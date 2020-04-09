# KNN
## 文件及文件夹介绍
- numpic_test : 测试图片文件jpg格式，大小为32*32
- numpic_train: 训练图片文件
- testDigits：测试图片0/1二值化后文本形式
- trainDigits: 训练图片0/1二值化后文本形式
- demo.py: 识别numpic_test中的图片
- KNN.py: KNN类
- KNN_test.py: 对testDigits测试集全部进行识别，输出正确率
- KNN_train.py: KNN识别numtxt，中途生成，结束删除，由demo.py，KNN_test.py或运行其里面的函数run()

## 使用说明
    运行demo.py识别numpic_text中随机选择的10张图片，修改demo.py中的list[0:10]可以修改随机选取范围
    numpic_text中的图片可以修改为自己的图片，大小为32 * 32，如果不为32 * 32，会自动转化为32 * 32。
    运行KNN_test.py可以查看测试集testDigits的正确率
 
