"""
Вам нужно отформатировать текст с применением некоего выравнивания.

Для базового выравнивания строк можно использовать методы ljust(), rjust()
и center(). Например:
"""

text = 'Hello world'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))

# Все эти методы могут принимать опциональный символ заполнения. Например:
print(text.rjust(20, '='))
print(text.center(20, '*'))

"""
Функция format() также может быть использована для выравнивания. Вам нуж-
но просто использовать символы <, > или ^ вместе с желаемой шириной. Напри-
мер:
"""
print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))

# Если вы хотите использовать в качестве заполняющего символа не пробел, определите его перед символом выравнивания:
print(format(text, '=>20s'))
print(format(text, '*^20s'))

"""
Эти коды форматирования могут быть также использованы с методом format()
при обработке нескольких значений. Например:
"""

print('{:>10s} {:>10s}'.format('Hello', 'World'))

"""
У format() есть преимущество – он работает не только со строками. Он работает
с любыми значениями, что делает его назначение очень широким. Например, вы
можете использовать его с числами:
"""
x = 1.2345
print(format(x, '>10'))
print(format(x, '^10.2f'))

"""
В старых программах вы также можете увидеть, как для форматирования текста
использовался оператор %. Например:
>>> '%-20s' % text
'Hello World '
>>> '%20s' % text
' Hello World'
>>>
Однако в новых программах вы должны предпочитать функцию или метод
format(). Она намного мощнее оператора %. Более того, format() может применять-
ся более широко, нежели строковые методы ljust(), rjust() или center(), поскольку
работает с любыми объектами.
За полным списком возможностей функции format() обратитесь к документа-
ции Python1.
"""

