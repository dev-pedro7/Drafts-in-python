from abc import ABC, abstractmethod

class AbstractFoo(ABC):
    def __init__(self, name):
        self.name = name

    @property
    def name(self):...
    @name.setter
    def name(self, name):...

class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        print('any')

foo = Foo('Bar')
print(foo.name)