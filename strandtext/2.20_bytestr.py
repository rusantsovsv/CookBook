"""
Вы хотите выполнить стандартные текстовые операции (срезание символов, по-
иск, замену) над строками байтов.

Байтовые строки поддерживают большую часть тех же встроенных операций, что
и текстовые строки. Например:
"""

data = b'Hello World'
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

"""Такие операции можно проделать и над байтовыми массивами:"""

data = bytearray(b'Hello World')
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

"""
Вы можете просто применить к байтовым строкам поиск совпадений с помощью
регулярных выражений, но сами шаблоны должны быть определены как
байты. Например:
"""
data = b'FOO:BAR,SPAM'
import re
# re.split('[:,]', data)            # TypeError: cannot use a string pattern on a bytes-like object
print(re.split(b'[:,]', data))

"""
Практически все доступные для текстовых строк операции будут работать и на
байтовых строках. Однако есть несколько заметных отличий, о которых нужно
знать. Во-первых, при индексировании байтовых строк мы получаем целые чис-
ла, а не символы. Например:
"""
a = 'Hello World'       # Тестовая строка
print(a[0], a[1])

b = b'Hello World'       # Байтовая строка
print(b[0])
print(b[1])
"""
Эта разница в семантике может влиять на программы, которые пытаются об-
работать байтовые данные так же, как и текстовые.
Во-вторых, байтовые строки не предоставляют красивые строковые представ-
ления и не выводятся в симпатичном виде, если сначала не проведено декодиро-
вание в текстовую строку. Например:
"""
s = b'Hello World'
print(s)
print(s.decode('ascii'))

"""Строковые операции форматирования также недоступны для байтовых строк."""
print(b'%10s %10d %10.2f' % (b'ACME', 100, 490.1))
# print(b'{} {} {}'.format(b'ACME', 100, 490.1))                # 'bytes' object has no attribute 'format'

"""
Если вы хотите применить какое-то форматирование к байтовой строке, это
должно быть проделано с помощью обычных текстовых строк и последующего
кодирования. Например:
"""
print('{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii'))

"""
И наконец, вы должны знать, что использование байтовых строк может изме-
нить семантику некоторых операций, особенно тех, что относятся к файловой
системе. Например, если вы предоставляете имя файла закодированным в байто-
вую строку, а не в текстовую, это обычно отключает кодирование и декодирование
имени файла. Например:
"""
# запишем имя файла в UTF-8
with open('jalape\xf1o.txt', 'w') as f:
    f.write('spicy')

# получим содержимое каталога
import os
print(os.listdir('.'))              # текстовая строка, имена декодированы
print(os.listdir(b'.'))             # байтовая строка (имена остались байтами)

"""
Посмотрите, как в последней части этого примера передача имени каталога
в виде байтовой строки вызывает возврат имен файлов в виде недекодированных
байтов. Имя файла, показанное в списке содержимого каталога, содержит «сы-
рую» кодировку UTF-8. См. рецепт 5.15, в нем обсуждается вопрос работы с име-
нами файлов, имеющий отношение к этому случаю.
Некоторые программисты могут склоняться к использованию байтовых строк
в качестве альтернативы текстовым из-за возможного выигрыша в производи-
тельности. Да, операции над байтами могут быть немного более эффективными,
чем работа с текстом (из-за расходов на Unicode), однако такой подход приводит
к грязному и неидиоматическому коду. Вы будете часто сталкиваться с тем, что
байтовые строки не очень хорошо сочетаются с другими частями Python, и закон-
чите тем, что будете вручную выполнять всевозможные операции кодирования-
декодирования, чтобы все работало. Так что если вы работаете с текстом, исполь-
зуйте обычные текстовые строки, а не байтовые.
"""

