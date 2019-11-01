"""
У вас есть код, которому необходимо пройти в цикле по каждой дате текущего
месяца, и вам нужен эффективный способ поиска диапазонов дат.

Прохождение в цикле по датам не требует предварительного создания списка
всех дат. Вы можете просто вычислить стартовую и конечную даты в диапазоне,
а затем использовать объекты datetime.timedelta, инкрементируя дату.
Вот функция, которая принимает любой объект datetime и возвращает кортеж,
содержащий первую дату месяца и начальную дату следующего месяца:
"""

from datetime import datetime, date, timedelta
import calendar


def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date, end_date)


# Получив эти данные, очень просто пройти в цикле по диапазону дат:
a_day = timedelta(days=1)
first_day, last_day = get_month_range()
print(first_day, last_day)
while first_day < last_day:
    print(first_day)
    first_day += a_day

"""
Этот рецепт работает так: сначала вычисляется дата, соответствующая первому
дню месяца. Быстрый способ сделать это – использовать метод replace() объектов
date или datetime, чтобы присвоить атрибуту days значение 1. Приятно, что метод
replace() создает объект того же типа, к которому он был применен. В данном слу-
чае, поскольку на входе у нас был экземпляр date, результат тоже является экземпляром
date. Точно так же мы бы получили экземпляр datetime, если бы на входе
у нас был экземпляр datetime.
Затем функция calendar.monthrange() используется для нахождения количества
дней в рассматриваемом месяце. Модуль calendar весьма полезен для получения
базовых данных о календарях. Функция monthrange() возвращает кортеж, который
содержит день недели и количество дней в месяце.
Когда мы знаем количество дней в месяце, конечная дата вычисляется путем
добавления соответствующего timedelta к стартовой дате. Тонкий, но важный
аспект этого рецепта – конечная дата не включается в диапазон (на самом деле
это первая дата следующего месяца). Это отражает присущее срезам и диапазо-
нам Python поведение, которое также не подразумевает включение последнего
элемента.
Чтобы пройти в цикле по диапазону дат, используются стандартные математи-
ческие операции и операторы сравнения. Например, экземпляр timedelta может
быть использован для инкрементирования даты. Оператор < используется для
проверки того, не достигнута ли конечная дата.
В идеальном случае стоит создать функцию, которая будет работать как встро-
енная range(), но с датами. К счастью, есть чрезвычайно простой способ сделать
это с помощью генератора:
def date_range(start, stop, step):
while start < stop:
yield start
start += step
Вот пример ее использования:
"""


def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step


for d in date_range(datetime(2012, 9, 1), datetime(2012, 10, 1), timedelta(hours=6)):
    print(d)

"""
Повторимся, самое большое преимущество такой реализации в том, что дата-
ми и временем можно манипулировать с помощью стандартных математических
операторов и операторов сравнения.
"""
