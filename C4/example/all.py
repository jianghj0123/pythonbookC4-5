# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart
#
#
# x = Complex(3.0, -4.5)
# print(x.r, x.i)


# class MyClass:
#     """A simple example class"""
#     i = 12345
#
#     def f(self):
#         return 'hello world'
#
# x = MyClass()
# x.counter = 1
# while x.counter < 10:
#     x.counter = x.counter * 2
# print(x.counter)
# del x.counter



class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance


dog1 = Dog('Fido')
dog2 = Dog('Buddy')
print(dog1.kind)                  # shared by all dogs
print(dog2.kind)                  # shared by all dogs
print(dog1.name)                  # unique to d
print(dog2.name)                  # unique to e
