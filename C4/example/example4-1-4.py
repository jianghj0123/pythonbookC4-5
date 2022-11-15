# 4.1.4 类和实例 代码示例

# 创建一个学生类
class Student(object):  # 创建Student类，Student为类名
    pass  # 此处可添加方法和属性


# Class对象
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

    def __init__(self):
        self.data = []


x = MyClass()


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
x.r, x.i
