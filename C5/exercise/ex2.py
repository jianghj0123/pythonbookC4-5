"""
请用三种不同的方法（函数）创建三个数组，这对三个数组要求是：
创建第一个数组，一个长度为10且元素全为1数组。
创建第二个数组，一个长度为20且元素全为0数组。
创建第三个数组，一个长度为10且元素全为2数组。
"""

import numpy as np

# np.empty 构造一个大小为 shape 的未初始化数组,
# np.zeros 构造一个大小为 shape 的全0数组,
# np.ones 构造一个大小为 shape 的全1数组,
# np.ones 构造一个大小为 shape 的全1数组,
# np.full 构造一个大小为 shape 的用指定值填满的数组,
#
a = np.empty(10)
for i in range(10):
    a[i] = 1
print(a)
print(np.zeros(20))
print(np.full(10, 2.0))
