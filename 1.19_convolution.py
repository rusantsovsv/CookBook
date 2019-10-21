"""
Вам нужно выполнить функцию сокращения (т. е. sum(), min(), max()), но сначала
необходимо преобразовать или отфильтровать данные.

Есть весьма элегантное решение для объединения сокращения (свертки) и преоб-
разования данных – выражение-генератор в аргументе. Например, если вы хотите
подсчитать сумму квадратов, попробуйте следующее:
"""

nums = [1, 2, 3, 4, 5]
s = sum(x*x for x in nums)

# определяем, есть ли файлы .py в каталоге
import os
files = os.listdir(r'D:\РСВ_файлы\Python\PyCharm')
if any(name.endswith('.py') for name in files):
    print('There by python!')
else:
    print('Sorry, no python')

# выводим кортеж как csv
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# сокращение (reduction) данных по полям в структуре данных
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]

min_shares = min(s['shares'] for s in portfolio)
print(min_shares)

# Альтернативный подход: возвращает {'name': 'AOL', 'shares': 20}
min_shares = min(portfolio, key=lambda s: s['shares'])
print(min_shares)