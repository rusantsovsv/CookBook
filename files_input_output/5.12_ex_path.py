"""
Вам нужно выяснить, существует ли файл или каталог.

Используйте os.path, чтобы проверить, существует ли файл или каталог. Напри-
мер:
"""

import os

print(os.path.exists(r'C:\Users\RusancovS\Desktop\Яндекс Практикум\jupyter_ML\data'))
print(os.path.exists(r'C:\sers\RusancovS\Desktop'))

"""
Вы можете выполнить дополнительные тесты, чтобы проверить тип файла. Эти
проверки возвращают False, если файл не существует:
"""

# это обычный файл?
print(os.path.isfile(r'D:\РСВ_файлы\Python\PyCharm\Cook_book\files_input_output\files\somefile'))

# это каталог?
print(os.path.isdir(r'D:\РСВ_файлы\Python\PyCharm\Cook_book'))

"""
Если вам нужно получить метаданные (например, размер или дату изменения
файла), это тоже можно сделать с помощью модуля os.path:
"""

print(os.path.getsize(r'C:\Users\RusancovS\Desktop\Яндекс Практикум\Полезные ссылки\readme.txt'))
print(os.path.getatime(r'C:\Users\RusancovS\Desktop\Яндекс Практикум\Полезные ссылки\readme.txt'))

import time
print(time.ctime(os.path.getatime(r'C:\Users\RusancovS\Desktop\Яндекс Практикум\Полезные ссылки\readme.txt')))

"""
Проверка файлов с помощью os.path становится очень простой операцией. Един-
ственное, о чем стоит помнить, – так это о разрешениях, особенно при операциях
получения метаданных. Например:
>>> os.path.getsize('/Users/guido/Desktop/foo.txt')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File "/usr/local/lib/python3.3/genericpath.py", line 49, in getsize
return os.stat(filename).st_size
PermissionError: [Errno 13] Permission denied: '/Users/guido/Desktop/foo.txt'
>>>
"""