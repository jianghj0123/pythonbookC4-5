# 水果类
class Fruits(object):
    def __init__(self, color):
        self.color = color

    def showcolor(self):
        print(self.color)

# 苹果对象
apple = Fruits("red")
# apple.color = "red"
apple.showcolor()

# 橘子对象
tangerine = Fruits()
tangerine.color = "orange"

# 西瓜对象
watermelon = Fruits()
watermelon.color = "green"


# 定义一个汽车类（Car），属性有颜色，品牌，车牌号，价格，并实例化两个对象，给属性赋值，并输入属性值
