"""
Вы хотите создать общее решение для поиска даты ближайшего прошедшего дня
недели – например, последней прошедшей пятницы.

В модуле datetime есть полезные функции и классы, которые помогают проводить
такого рода вычисления. Хорошее обобщенное решение этой задачи выглядит
как-то так:
"""

from datetime import datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.now()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    print(target_date)


print(datetime.today())
get_previous_byday('Monday')
get_previous_byday('Friday')

"""
Необязательный параметр start_date может быть предоставлен с использовани-
ем другого экземпляра datetime. Например:
"""
get_previous_byday('Sunday', datetime(2012, 12, 21))

"""
Этот рецепт работает путем отображения стартовой и интересующей даты на но-
мера их позиций в неделе (где понедельник – это 0). Далее используется модуль-
ная арифметика, с ее помощью мы вычисляем, сколько дней назад была нужная
дата. Потом нужная дата высчитывается от стартовой даты путем вычитания со-
ответствующего экземпляра timedelta.

Если вы выполняете много подобных вычислений, рекомендуем установить
пакет python-dateutil. Например, вот так можно выполнить аналогичную работу
с использованием функции relativedata() из модуля dateutil:
"""

from dateutil.relativedelta import relativedelta
from dateutil.rrule import *

d = datetime.now()
print(d)

# следующий понедельник
print(d + relativedelta(weekday=MO))

# предыдущий понедельник
print(d + relativedelta(weekday=MO(-1)))