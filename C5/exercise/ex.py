"""
导入numpy库并取别名为np
import numpy as np

打印输出numpy的版本和配置信息
print (np.__version__)
np.show_config()

创建长度为10的零向量
Z = np.zeros(10)
print (Z)

获取数组所占内存大小
Z = np.zeros((10, 10))
print (Z.size * Z.itemsize)

怎么用命令行获取numpy add函数的文档说明？
np.info(np.add)

创建一个长度为10的零向量，并把第五个值赋值为1
Z = np.zeros(10)
Z[4] = 1
print (Z)

创建一个值域为10到49的向量
Z = np.arange(10, 50)
print (Z)

将一个向量进行反转（第一个元素变为最后一个元素）
Z = np.arange(50)
Z = Z[::-1]
print (Z)

创建一个3x3的矩阵，值域为0到8
Z = np.arange(9).reshape(3, 3)
print (Z)

从数组[1, 2, 0, 0, 4, 0]中找出非0元素的位置索引
nz = np.nonzero([1, 2, 0, 0, 4, 0])
print (NZ)

创建一个3x3的单位矩阵
Z = np.eye(3)
print (Z)





"""
import numpy as np
Z = np.arange(10, 50)
print (Z)