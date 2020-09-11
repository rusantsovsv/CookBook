"""
Вы хотите вызвать метод родительского класса вместо метода, который был пере-
определен в подклассе.

Чтобы вызвать метод из родительского класса (суперкласса), используйте функ-
цию super(). Например:
"""


class A:

    def spam(self):
        print('A.spam')


class B(A):

    def spam(self):
        print('B.spam')
        super().spam()      # вызов spam() родителя

x = B()

x.spam()

"""
Очень распространенный случай использования super() – это применение ее
к методу __init__(), чтобы убедиться в правильной инициализации родителей:
"""

class A:

    def __init__(self):
        self.x = 0


class B(A):

    def __init__(self):
        super().__init__()
        self.y = 1

x = B()

print(x.x, x.y)
print(B.__mro__)

"""
Также super() часто используется в коде, который переопределяет один из спе-
циальных методов Python. Например:
"""

class Proxy:

    def __init__(self, obj):
        self._obj = obj

    # передача поиска атрибута внутреннему obj
    def __getattr__(self, name):
        return getattr(self._obj, name)

    # передача присвоения атрибута
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
            # вызов изначального __setattr__
        else:
            setattr(self._obj, name, value)

class A:
    def spam(self):
        print('A.spam')
        super().spam()

class B:
    def spam(self):
        print('B.spam')

class C(A, B):
    pass

c = C()

c.spam()