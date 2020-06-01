"""
Вы хотите добавить в замыкание функции, которые позволят получать доступ
и изменять внутренние переменные.

В обычном случае внутренние переменные замыкания полностью скрыты от
внешнего мира. Однако вы можете предоставить доступ путем написания функ-
ций для доступа и прикрепления их к замыканию в качестве атрибутов функции.
Например:
"""

def sample():
    n = 0

    # функция-замыкание
    def func():
        print('n =', n)

    # методы доступа к n
    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    # прикрепление в качестве атрибутов функции
    func.get_n = get_n
    func.set_n = set_n
    return func

f = sample()
f()

f.set_n(10)
f()

print(f.get_n())

"""
Две главные возможности языка позволяют этому рецепту работать. Во-первых,
инструкции nonlocal делают возможным написание функций, которые изменяют
внутренние переменные. Во-вторых, атрибуты функции дают возможность на-
прямую прикреплять методы для доступа к замыканию, и они работают практи-
чески так же, как методы экземпляра (хотя классы тут не используются).

Небольшое дополнение к этому рецепту позволит замыканиям эмулировать
экземпляры класса. Все, что вам нужно, – это скопировать внутренние функции
в словарь экземпляра и возвратить его. Например:
"""

import sys
class ClosureInstance:
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals

        # обновить словарь экземпляра вызываемыми объектами
        self.__dict__.update((key, value) for key, value in locals.items() if callable(value))

    # перегружаем специальные методы
    def __len__(self):
        return self.__dict__['__len__']()

# Пример использования
def Stack():
    items = []

    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()

"""Вот интерактивный сеанс, который показывает, как все это работает:"""

s = Stack()
print(s)

s.push(10)
s.push(20)
s.push('Hello')
print(len(s))

print(s.pop())
print(s.pop())
print(s.pop())

"""
Интересно, что этот код работает немного быстрее аналога, использующего
обычное определение класса. Например, вы можете проверить производитель-
ность по сравнению с таким классом:
"""


class Stack2:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)

from timeit import timeit
# Тест с использованием замыканий
s = Stack()
print(timeit('s.push(1);s.pop()', 'from __main__ import s'))
#Тест с использованием класса
s = Stack2()
print(timeit('s.push(1);s.pop()', 'from __main__ import s'))