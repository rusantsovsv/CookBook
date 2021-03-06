"""
Ваша программа создает большое количество (миллионы) экземпляров и исполь-
зует много памяти.

Для классов, которые в основном служат простыми структурами данных, вы часто
можете значительно уменьшить потребление памяти экземплярами путем до-
бавления атрибута __slots__ в определение класса. Например:
"""

class Date:
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

x = Date(2020, 9, 8)

print(x.day)

"""
Когда вы определяете __slots__, Python использует намного более компактное
внутреннее представление экземпляров. Вместо снабжения каждого экземпляра
словарем они создаются на базе небольшого массива фиксированного размера,
похожего на кортеж или список. Атрибуты, перечисленные в спецификаторе __
slots__, внутри отображаются на конкретные индексы в массиве. Побочный эф-
фект использования слотов в том, что теряется возможность добавления новых
атрибутов к экземплярам – у вас будет возможность использовать только атрибу-
ты, перечисленные в спецификаторе __slots__.
"""
