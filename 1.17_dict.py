"""
Вы хотите создать словарь, который будет подмножеством другого словаря.

Эту задачу можно легко решить с помощью генератора словаря (dictionary comprehension).
"""

prices = {'ACME': 45.23,
          'AAPL': 612.78,
          'IBM': 205.55,
          'HPQ': 37.20,
          'FB': 10.75}

# Создать словырь всех акций с ценами больше 200

p1 = {key:value for key, value in prices.items() if value > 200}

# Создать словарь акций технологических компаний
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key:value for key, value in prices.items() if key in tech_names}

"""
Большую часть того, что можно сделать с помощью генераторов словарей, можно
осуществить путем создания последовательности кортежей и передачи их в функ-
цию dict().
"""

p1 = dict((key, value) for key, value in prices.items() if value > 200)

"""
Однако решение на основе генератора словаря яснее и работает немного быстрее
(в рассмотренном выше примере генератор отработал в два раза быстрее).
Иногда существует множество путей решить задачу. К слову, второй пример
можно переписать так:
"""

p2 = {key:prices[key] for key in prices.keys() & tech_names}