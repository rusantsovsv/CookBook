"""
У вас есть данные внутри последовательности, и вы хотите извлечь значения или
сократить последовательность по какому-либо критерию.
"""
import math
from itertools import compress

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n > 0])
print([n for n in mylist if n < 0])

"""
Потенциальная проблема с использованием генераторов списков заключает-
ся в том, что они могут создать большой результат, если размер входных данных
тоже большой. Если это вас беспокоит, вы можете использовать выражения-гене-
раторы для итеративного возврата отфильтрованных значений.
"""

pos = (n for n in mylist if n > 0)
print(pos)

for x in pos:
    print(x)

"""
Иногда критерий фильтрования не может быть легко выражен в форме гене-
ратора списка или выражения-генератора. Предположим, например, что процесс
фильтрования включает обработку исключений или какой-то другой сложный
момент. Чтобы справиться с этим, поместите фильтрующий код в функцию и ис-
пользуйте встроенную функцию filter().
"""

values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))
print(ivals)

"""
filter() создает итератор, так что если вы хотите получить список результатов, не
забудьте использовать list(), как показано выше.


Генераторы списков и выражения-генераторы часто являются самым легким
и прямым способом фильтрования простых данных. Но у них также есть допол-
нительная способность – одновременно изменять данные. Например:
"""

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

print([math.sqrt(x) for x in mylist if x > 0])

"""
Одна из разновидностей фильтрования включает замену значений, которые не
подходят под определенный критерий, другими значениями (вместо отбраковки
неподходящих). Например, вместо простого поиска положительных значений вы
также хотите обрезать «плохие» значения, чтобы они попадали в определенный
диапазон. В большинстве случаев это легко сделать с помощью перемещения кри-
терия фильтрования в условное выражение:
"""

clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)
clip_pos = [n if n < 0 else 0 for n in mylist]
print(clip_pos)

"""
Другой важный инструмент для фильтрации – itertools.compress(), который при-
нимает итерируемый объект вместе с последовательностью-селектором из буле-
вых значений. На выходе функция выдает все элементы итерируемого объекта,
для которых совпадающий элемент в селекторе – True. Это может быть полезно,
если вы пытаетесь применить результаты фильтрования одной последователь-
ности к другой связанной последовательности. Например, у вас есть две колонки
данных:
"""

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]

"""
Теперь предположим, что вы хотите создать список всех адресов, где соответ-
ствующие значения из counts больше 5. Вот как это можно сделать:
"""

more5 = [n > 5 for n in counts]
print(more5)
print(list(compress(addresses, more5)))

"""
Ключевой момент – сначала создать последовательность булевых значений,
которые будут указывать, какие элементы удовлетворяют заданному условию.
Далее функция compress() выберет элементы, соответствующие значениям True.
Как и filter(), функция compress() возвращает итератор. Поэтому если вы хотите
на выходе получить список, вам придется использовать list().
"""