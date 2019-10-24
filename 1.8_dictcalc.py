"""
Задача
Вы хотите проводить различные вычисления (например, поиск минимального
и максимального значений, сортировку) на словаре с данными.
"""

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

"""
Чтобы выполнить вычисления на содержимом словаря, часто бывает полезно
обратить ключи и значения, используя функцию zip(). Например, вот так можно
найти минимальную и максимальную цены, а также соответствующий тикер:
"""

min_price = min(zip(prices.values(), prices.keys()))
print(min_price)

max_price = max(zip(prices.values(), prices.keys()))
print(max_price)

zipdict = zip(prices.values(), prices.keys())
print(list(zipdict))

"""
Похожим образом для ранжирования данных можно использовать zip() с sorted(),
как показано ниже:
"""

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

"""
Когда вы производите эти вычисления, обратите внимание, что zip() создает
итератор, по которому можно пройти только один раз. Например, следующий
фрагмент кода – неправильный:
"""

prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names)) # OK
# print(max(prices_and_names)) # ValueError: max() arg is an empty sequence
