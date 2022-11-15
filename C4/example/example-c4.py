



# 常用标准模块介绍

# time模块，书上的形式是在IDLE中运行的结果
import time
time.localtime()
time.localtime(1696784252.8902779)
time.gmtime()
time.time()
time.mktime(time.localtime())
time.asctime()
time.ctime()

# random模块，书上的形式是在IDLE中运行的结果
import sys
print(sys.argv)

import re
print(re.match('www', 'www.ncu.edu.cn').span())  # 在起始位置匹配
print(re.match('cn', 'www.ncu.edu.cn'))         # 不在起始位置匹配

#import re

print(re.search('www', 'www.ncu.edu.cn').span())  # 在起始位置匹配
print(re.search('cn', 'www.ncu.edu.cn').span())  # 不在起始位置匹配



phone = "10068 # 这是一个电话号码"

# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print("电话号码 : ", num)








