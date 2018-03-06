# foo.py
from . import export

__all__ = ['Foo'] # Controlling Exports

@export
def blah():
    pass

@export
class Foo(object):
    pass

print('foo imported')
