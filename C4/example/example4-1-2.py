# 4.1.2 面向过程和面向对象 代码示例


# 面向过程方式处理学生的成绩表举例
std1 = {'name': 'Li Ming', 'score': 98}
std2 = {'name': 'Zhang San', 'score': 81}


def print_score(std):
    print('%s: %s' % (std['name'], std['score']))


print_score(std1)
print_score(std2)


# 定义一个Student类
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


# 创建两个学生对象
LiMing = Student('Li Ming', 66)
ZhangSan = Student('Zhang San', 90)

# 调用print_score方法
LiMing.print_score()
ZhangSan.print_score()


# 定义函数
def function_name():
    print("这是一个函数")


function_name()  # 调用函数


# 定义类和方法
class ClassName(object):

    def method(self):
        print("这是一个方法")


C = ClassName()  # 实例化对象
C.method()  # 调用方法
