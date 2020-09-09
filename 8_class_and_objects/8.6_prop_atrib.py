"""
Вы хотите добавить дополнительную обработку (например, проверку типов или
валидацию) в получение или присваивание значения атрибуту экземпляра.

Простой способ кастомизировать доступ к атрибуту заключается в определении
свойства (property). Например, этот код определяет свойство, которое добавляет
простую проверку типов к атрибуту:
"""

class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    # функция геттер
    @property
    def first_name(self):
        return self._first_name

    # функция сеттер
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # функция делитер (необязательная)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")
"""
В представленном коде есть три относящихся друг к другу метода, которые
должны иметь одинаковое имя. Первый метод – это функция геттер (getter), она
делает first_name свойством. Два других метода прикрепляют необязательные
функции сеттер (setter) и делитер (deleter) к свойству (property) first_name. Важ-
но подчеркнуть, что декораторы @first_name.setter и @first_name.deleter не будут
определены, если first_name не было превращено в свойство с помощью @property.
Важнейшая особенность свойства в том, что оно выглядит так же, как обыч-
ный атрибут, но при попытке доступа автоматически активируются геттер, сеттер
и делитер. Например:
"""

a = Person('Guido')
print(a.first_name)

# a.first_name = 42
# del a.first_name

"""
Когда вы реализуете свойство, данные (если они имеются) нужно где-то сохра-
нять. Поэтому в методах получения и присваивания вы видите прямую манипу-
ляцию атрибутом _first_name, в котором и находятся данные. Вы также можете
спросить, почему метод __init__() устанавливает self.first_name, а не self._first_name.
В этом примере весь смысл свойства заключается в применении проверки типа
при присваивании значения атрибуту. Поэтому есть вероятность, что вы также за-
хотите провести такую проверку при инициализации. Присваивая значение self.
first_name, операция присваивания тоже использует метод-сеттер (в противопо-
ложность обходному пути прямого доступа к self._first_name).

Свойства также могут быть определены для существующих методов получения
и присваивания значения. Например:
"""
class Person_2:
    def __init__(self, first_name):
        self.set_first_name(first_name)

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    def del_first_name(self):
        raise AttributeError("Can't delete attribute")

    name = property(get_first_name, set_first_name, del_first_name)

"""
Свойства также могут быть способом определить вычисляемые атрибуты. Это
атрибуты, которые не хранятся, а вычисляются по запросу. Например:
"""

import math
class Circle:

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimetr(self):
        return 2 * math.pi * self.radius

"""
Здесь использование свойств позволяет создать единообразный интерфейс эк-
земпляра, в котором к radius, area и perimeter доступ осуществляется как к простым
атрибутам, в противоположность смеси простых атрибутов и вызовов мето-
дов. Например:
"""

c = Circle(16.0)
print(c.radius, c.area, c.perimetr)