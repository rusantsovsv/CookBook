"""
Вашей программе требуется производить простые преобразования времени, та-
кие как выражение дней в секундах, часов в минутах и т. д.

Чтобы производить конвертирование и арифметические операции над различ-
ными единицами времени, используйте модуль datetime. Например, чтобы пред-
ставить интервал времени, создайте экземпляр timedelta:
"""
from datetime import timedelta

a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)

c = a + b

print(c)
print(c.days)
print(c.seconds)
print(c.seconds / 3600)
print(c.total_seconds() / 3600)

"""
Если вам нужно представить определенные даты и определенное время, соз-
дайте экземпляры datetime и проводите над ними обычные арифметические опе-
рации. Например:
"""

from datetime import datetime
a = datetime(2012, 9, 23)
print(a + timedelta(days=10))

b = datetime(2012, 12, 21)
d = b - a
print(d.days)
now = datetime.today()
print(now)
print(now + timedelta(minutes=10))

"""
Стоит отметить, что datetime знает о существовании високосных годов. На-
пример:
"""

a = datetime(2012, 3, 1)
b = datetime(2012, 2, 28)

print(a - b)
c = datetime(2013, 3, 1)
d = datetime(2013, 2, 28)
print(c - d)

"""
Для самых базовых операций над датой и временем модуля datetime достаточно.
Если перед вами стоят более сложные задачи, такие как работа с временными зо-
нами, нечеткими интервалами времени, подсчет дат выходных дней и т. д., по-
смотрите на модуль dateutil1.
Например, многие подобные вычисления над временем могут быть выполнены
с помощью функции dateutil.relativedelta(). Одна важная возможность заключает-
ся в том, что она заполняет разрывы, которые возникают при работе с месяцами
(и отличающимся количеством дней в них). Например:
"""

a = datetime(2012, 9, 23)
try:
    print(a + timedelta(months=1))
except TypeError as te:
    print('Ошибка типа данных (нет аргумента "месяц"): ', te)

from dateutil.relativedelta import relativedelta
print(a + relativedelta(months=+1))
print(a + relativedelta(months=+4))

# время между двумя датами
b = datetime(2012, 12, 21)
d = b - a
print(d)
d = relativedelta(b, a)
print(d)
print(d.months, d.days)

