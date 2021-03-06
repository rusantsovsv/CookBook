"""
Вы хотите проитерировать по последовательности в обратном порядке.

Используйте встроенную функцию reversed(). Например:
"""

a = [1, 2, 3, 4]
for x in reversed(a):
    print(x)

"""
Обратная итерация сработает только в том случае, если объект имеет опреде-
ленный размер или если в нем реализован специальный метод __reversed__(). Если
ни одно из этих условий не выполнено, вы должны будете сначала конвертиро-
вать объект в список. Например:
"""

f = open('passw.txt')
for line in reversed(list(f)):
    print(line, end='')
f.close()

"""
Обратите внимание, что конвертирование итерируемого объекта в список мо-
жет съесть много памяти, если список получится большим.
"""

"""
Многие программисты не знают, что итерирование в обратном порядке может
быть переопределено в собственном классе, если он реализует метод __reversed__().
Например:
"""


class Countdown:

    def __init__(self, start):
        self.start = start

    # прямой итератор
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # обратный итератор
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


"""
Определение обратного итератора делает код намного более эффективным,
а также снимает необходимость предварительного помещения данных в список
для выполнения итераций в обратном порядке.
"""

