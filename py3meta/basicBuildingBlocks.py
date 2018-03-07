# Functions
# Default values set at definition time
def func(x,y,z, bias=10):
    return x+y+z + bias

print(func(x=1,y=2,z=3))

# Closures
def make_adder(x,y):
    def add():
        return x + y
    return add

# Classes
class Spam:
    a = 1
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def foo(self):
        pass

    def imethod(self):
        pass

    @classmethod
    def cmethod(cls):
        pass

    @staticmethod
    def smethod():
        pass

print(Spam.a) # Classes variable
print(Spam(2,3).x) # Instance variable
print(Spam(2,3).__dict__) # Object are layered on dictionaries
print(Spam(2,3).imethod()) #  Instance method
print(Spam.cmethod()) # Class method
print(Spam.smethod()) # static method

# Almost everything can be customized
class Array:
    def __getitem__(self, item):
        pass
    def __setitem__(self, key, value):
        pass
    def __delitem__(self, key):
        pass
    def __contains__(self, item):
        pass

# Inheritance
class Base:
    def spam(self):
        pass

class Foo(Base):
    def spam(self):
        # Call method in base class
        super().spam()

