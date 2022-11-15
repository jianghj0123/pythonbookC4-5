"""
定义一个名为Car的类来表示汽车。这个类包括：
一个名为color的私有字符串表示车的颜色。
一个名为brand的私有字符串表示车的品牌。
一个名为plate的私有字符串表示车的车牌号。
一个名为price的私有浮点数据表示车的价格。
一个构造方法创建一辆具有特定颜色、品牌、车牌号、价格的汽车。
一个名为show_info的方法可以输出汽车的信息，包括颜色、品牌、车牌号、价格。
编写一个测试程序，创建一个Car对象（给汽车的属性赋值），并调用show_info方法来打印这个汽车对象的颜色、品牌、车牌号、价格属性。

属性有颜色、品牌、车牌号、价格，并实例化一个对象，给属性赋值，调用show_info方法输出汽车实例的颜色、品牌、车牌号、价格。


"""


class Car:
    def __init__(self, color, brand, plate, price):
        self.color = color
        self.brand = brand
        self.plate = plate
        self.price = price

    def show_info(self):
        print(self.color, self.brand, self.plate, self.price)


c1 = Car("白色", "比亚迪", "京A88888", 300000)
c1.show_info()
