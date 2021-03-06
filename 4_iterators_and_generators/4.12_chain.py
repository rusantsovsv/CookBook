"""
Вам нужно выполнить одинаковую операцию над большим количеством объек-
тов, но объекты находятся в различных контейнерах, а вам хотелось бы избежать
написания вложенных циклов, причем без потери читабельности кода.

Для упрощения этой задачи можно использовать метод itertools.chain(). Он прини-
мает список итерируемых объектов и возвращает итератор, который скрывает тот
факт, что вы на самом деле работаете с несколькими контейнерами. Рассмотрим
пример:
"""

from itertools import chain
a = [1, 2, 3, 4]
b = ['x', 'y', 'z']

for x in chain(a, b):
    print(x)

"""
Обычно chain() используется, если вы хотите выполнить некоторые операции
над всеми элементами за один раз, но элементы разнесены по разным рабочим
наборам. Например:
"""

# различные наборы элементов
active_items = set()
inactive_items = set()

# итерируем по всем элементам
for item in chain(active_items, inactive_items):
    # обработка элемента
    ...

"""
Это решение намного более элегантно, нежели использование двух отдельных
циклов, как показано в этом примере:"""
for item in active_items:
    # Обработка элемента
    ...
for item in inactive_items:
    # Обработка элемента
    ...

"""
itertools.chain() принимает один или более итерируемых объектов в качестве аргу-
ментов. Далее она создает итератор, который последовательно потребляет и воз-
вращает элементы, производимые каждым из предоставленных итерируемых
объектов. Это тонкое различие, но chain() эффективнее, чем итерирование по
предварительно объединенным последовательностям. Например:
"""

# Неэффективно
for x in a + b:
    ...

# Уже лучше
for x in chain(a, b):
    ...

"""
В первом случае операция a + b создает новую последовательность и допол-
нительно требует, чтобы a и b относились к одному типу. chain() не выполняет
такую операцию, намного эффективнее обращается с памятью, если входные по-
следовательности большие, а также легко применяется к итерируемым объектам
различных типов.
"""