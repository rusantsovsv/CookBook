"""
Вы хотите, чтобы объект поддерживал кастомизированное форматирование че-
рез функцию format() и строковый метод.

Чтобы кастомизировать строковое форматирование, определите в классе метод
__format__(). Например:
"""

_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
}


class Date:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)


# Экземпляры класса Date теперь поддерживают операции форматирования:
d = Date(2012, 12, 21)
print(format(d))
print('The date is {:ymd}'.format(d))
print('The date is {:mdy}'.format(d))

"""
Метод __format__() предоставляет доступ к функциональности Python, касающейся
форматирования строк. Важно отметить, что интерпретация кодов форматирова-
ния полностью зависит от самого класса. Поэтому коды могут быть практически
любыми. Например, посмотрим на следующий пример из модуля datetime:
"""
from datetime import date
d = date(2012, 12, 21)
print(format(d))
print('The end is {:%d %b %Y}. Goodby'.format(d))

"""
Есть определенные стандартные соглашения для форматирования встроенных
типов. См. документацию модуля string, в которой приведена формальная спецификация.
"""