"""
Вы хотите найти текст, используя те же маски, которые обычно применяются
в оболочках Unix (например, *.py, Dat[0-9]*.csv и т. д.).

Модуль fnmatch предоставляет две функции: fnmatch() и fnmatchcase(), которые
можно использовать для такого поиска. Все просто:
"""

from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])

"""
По умолчанию fnmatch() использует те же чувствительные к регистру правила,
что и файловая система текущей операционной системы (то есть правила меня-
ются от системы к системе).

>>> # On OS X (Mac)
>>> fnmatch('foo.txt', '*.TXT')
False
>>> # On Windows
>>> fnmatch('foo.txt', '*.TXT')
True
>>>

Если это различие важно, используйте метод fnmatchcase(). Он ищет именно та-
кие совпадения заглавных и строчных букв, которые вы предоставите:
>>> fnmatchcase('foo.txt', '*.TXT')
False
>>>

Часто упускается из вида возможность использования этих функций на стро-
ках, получаемых при обработке данных, или на строках, не являющихся именами
файлов. Например, у вас есть список адресов:
"""

address = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY'
]

print([addr for addr in address if fnmatchcase(addr, '* ST')])
print([addr for addr in address if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])
