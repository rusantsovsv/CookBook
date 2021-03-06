"""
Вам нужно создать или протестировать такие значения с плавающей точкой: бес-
конечность, минус бесконечность, NaN (not a number, «не число»).
В Python нет специального синтаксиса для представления таких специальных
значений с плавающей точкой, но они могут быть созданы с помощью float(). На-
пример:
"""
import math

a = float('inf')
b = float('-inf')
c = float('nan')

print(a, b, c, sep='.'*3)

"""
Чтобы проверить, не является ли значение таким, используйте функции math.
isinf() и math.isnan(). Например:
"""
print(math.isinf(a))
print(math.isnan(c))

"""
За подробностями об этих специальных значениях с плавающей точкой вы мо-
жете обратиться к спецификации IEEE 754. Однако здесь есть несколько хитрых
деталей, о которых нужно знать. Особенное внимание нужно обратить на темы,
связанные со сравнениями и операторами.
Бесконечные значения распространяются в вычислениях согласно математи-
ческим правилам. Например:
"""
a = float('inf')
print(a + 45)

print(a * 10)

print(10 / a)

"""Однако некоторые операции не определены и выдают NaN. Например:"""
print(a / a)
print(a + b)

"""
Значения NaN распространяются через все операции, не возбуждая исключе-
ний. Например:
"""
c = float('nan')
print(c + 23)

print(c / 2)

print(c * 2)

print(math.sqrt(c))

"""
Тонкость с NaN заключается в том, что они никогда не будут равны друг другу.
Например:
"""
c = float('nan')
d = float('nan')
print(c == d)
print(c is d)

"""
По причине этого единственный безопасный способ проверить значение на
NaN – это использовать math.isnan(), как показано в данном рецепте.
Иногда программисты хотят изменить поведение Python таким образом, чтобы
при возникновении в ходе вычислений бесконечностей или NaN возбуждались
исключения. Для такого изменения поведения может быть использован модуль
fpectl, но он не включен в стандартную поставку Python, является платформоза-
висимым и на самом деле предназначен только для программистов-экспертов. За
деталями обратитесь к онлайн-документации Python.
"""
