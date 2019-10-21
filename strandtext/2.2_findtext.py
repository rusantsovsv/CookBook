"""
Вам нужно проверить начало или конец строки на присутствие неких текстовых
шаблонов, таких как расширения файлов, схемы URL и т. д.

Простой способ проверить начало или конец строки – применить метод str.
startswith() или str.endswith().
"""

filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file:'))

url = 'http://www.python.org'
print(url.startswith('http:'))

"""
Если вам нужно проверить несколько вариантов, передайте кортеж с ними
в startswith() или endswith():
"""

import os
filenames = os.listdir('.')
print(filenames)

print([name for name in filenames if name.endswith(('.py'))])

print(any(name.endswith('.py') for name in filenames))

# Другой пример
from urllib.request import urlopen


def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read
    else:
        with open(name) as f:
            return f.read()

"""
Любопытно, что в этом случае на вход нужно подавать именно кортеж. Если так
случилось, что варианты выбора собраны у вас в списке или множестве, сначала
сконвертируйте их с помощью tuple(). Например:
"""
choices = ['http:', 'ftp:']
url = 'http://www.python.org'
# url.startswith(choices)        # TypeError: startswith first arg must be str or a tuple of str, not list
print(url.startswith(tuple(choices)))

"""
Методы startswith() и endswith() предоставляют весьма удобный способ проверки
префиксов и окончаний. Такие же операции можно осуществить с помощью сре-
зов, но это намного менее элегантно. Например:
"""

filename = 'spam.txt'
print(filename[-4:] == '.txt')
url = 'http://www.python.org'
print(url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:')

"""
Вы также можете склониться к использованию регулярных выражений в качестве
альтернативы. Например:
"""
import re
print(re.match('http:|https:|ftp:', url))

"""
Такой подход работает, но часто это будет огнем из пушки по воробьям. Ис-
пользование вышеописанного рецепта проще и работает быстрее.
И последнее: методы startswith() и endswith() отлично работают вместе с дру-
гими операциями, такими как обычные методы свертки данных. Например, это
выражение проверяет каталог на присутствие файлов определенных типов:
"""

import os
if any(name.endswith(('.py', '.h')) for name in os.listdir('.')):
    print('Hello')
