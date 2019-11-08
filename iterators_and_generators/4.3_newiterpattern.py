"""
Вы хотите реализовать собственный паттерн итераций, который будет отличаться
от обычных встроенных функций (таких как range(), reversed() и т. п.).

Если вы хотите реализовать новый тип итерационного паттерна, определите его
с помощью генератора. Вот, например, генератор, который создает диапазон чи-
сел с плавающей точкой:
"""

def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

"""
Чтобы использовать такую функцию, вы должны проитерировать по ней в цикле
или применить ее с какой-то другой функцией, которая потребляет итерируе-
мый объект (например, sum(), list() и т. п.). Например:
"""

for n in frange(0, 4, 0.5):
    print(n)

print(list(frange(0, 1, 0.125)))

"""
Само присутствие инструкции yield в функции превращает ее в генератор. В отли-
чие от обычной функции, генератор запускается только в ответ на итерацию. Вот
эксперимент, который вы можете провести, чтобы понять внутренний механизм
работы таких функций:
"""


def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')

# Создаем генератор - обратите внимание на отсутствие вывода
c = countdown(3)
print(c)

# выполняется до первого yield и выдает значение
print(next(c))

# выполняется до слудующего yield
print(next(c))

# выполняется до слудующего yield
print(next(c))

# выполнить до следущего yield (итерирование останавливается)
print(next(c))

"""
Ключевая особенность функции-генератора состоит в том, что она запускается
только в ответ на операции next в ходе итерирования. Когда генератор возвра-
щает значение, итерирование останавливается. Однако цикл for, который обычно
используется для выполнения итераций, сам заботится об этих деталях, поэтому
в большинстве случаев вам не стоит волноваться о них.
"""