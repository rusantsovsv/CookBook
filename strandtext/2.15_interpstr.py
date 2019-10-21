"""
Вы хотите создать строку, в которой на место переменных будут подставляться
строковые представления значений этих переменных.

В Python нет прямой поддержки простой подстановки значений переменных
в строках. Однако строковый метод format() предоставляет приближенную по
смыслу возможность. Например:
"""

s = '{name} has {n} messages.'
print(s.format(name='Guido', n=37))

"""
Если значения, которые должны быть подставлены, на самом деле находятся
в переменных, вы можете использовать сочетание format_map() и vars(), как по-
казано тут:
"""
name = 'Guido'
n = 37
print(s.format_map(vars()))

"""
Также есть f-строки
"""
print(f'{name} has {n} messages.')

# Стоит отметить, что vars() также работает с экземплярами. Например:


class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n


a = Info('Guido', 37)
print(s.format_map(vars(a)))

"""
Недостаток format() и format_map() в том, что они не могут аккуратно справить-
ся с отсутствующими значениями. Например:
"""

# print(s.format(name='Guido'))             # KeyError: 'n'

"""
Этого можно избежать путем определения альтернативного класса словаря
с методом __missing__(), как показано ниже:
"""


class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'


"""
Теперь этот класс можно использовать, чтобы обернуть значения, которые по-
даются на вход в format_map():
"""

del n
print(s.format_map(safesub(vars())))

"""
Если вы обнаружите, что часто делаете такие вещи в своей программе, то мо-
жете спрятать процесс подстановки переменных в небольшую функцию, которая
использует так называемый фреймхак (frame hack). Например:
"""

import sys
def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

# теперь можно делать вот так:

name = 'Guido'
n = 37
print(sub('Hello {name}'))
print(sub('You have {n} message.'))
print(sub('Your favorite color is {color}'))
