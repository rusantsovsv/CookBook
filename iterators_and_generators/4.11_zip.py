"""
Вы хотите за один раз проитерировать по элементам, содержащимся более чем
в одной последовательности.

Чтобы итерировать по более чем одной последовательности за раз, используйте
функцию zip(). Например:
"""

xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]

for x, y in zip(xpts, ypts):
    print(x, y)

"""
zip(a, b) работает путем создания итератора, который производит кортежи (x, y),
где x берется из a, а y – из b. Итерирование останавливается, когда заканчивается
одна из последовательностей. Поэтому результат будет таким же по длине, как
и самая короткая из входных последовательностей. Например:
"""

a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']

for i in zip(a, b):
    print(i)

"""
Если такое поведение нежелательно, используйте функцию itertools.zip_longest().
Например:
"""

from itertools import zip_longest
for i in zip_longest(a, b, fillvalue=0):
    print(i)

"""
zip() обычно используется тогда, когда вам нужно создать пары из данных. Пред-
положим, что у вас есть список заголовков столбцов и значения столбцов:
"""

headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]

"""Используя zip(), вы можете создать пары значений и поместить их в словарь:"""
s = dict(zip(headers, values))

"""Если вы хотите вывести результат, можно поступить так:"""
for name, val in zip(headers, values):
    print(name, '=', val)

"""
Менее распространенное применение zip() заключается в том, что функции мо-
жет быть передано не две последовательности, а больше. В этом случае кортежи
результата будут иметь такое количество элементов, каким было количество по-
следовательностей. Например:
"""
a = [1, 2, 3]
b = [10, 11, 12]
c = ['x', 'y', 'z']

for i in zip(a, b, c):
    print(i)

"""
И последнее: важно подчеркнуть, что zip() возвращает итератор. Если вам нуж-
ны сохраненные в списке спаренные значения, используйте функцию list(). На-
пример:
"""
print(zip(a, b))
print(list(zip(a, b)))
