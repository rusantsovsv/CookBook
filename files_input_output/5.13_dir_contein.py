"""
Вы хотите получить список файлов, содержащихся в каталоге файловой системы.

Используйте функцию os.listdir() для получения списка файлов в каталоге:
"""

import os
path_dir = r'D:\РСВ_файлы\Python'
names = os.listdir(path_dir)
print(names)

"""
Вы получите «сырой» список содержимого каталога, включающий все файлы,
подкаталоги, символические ссылки и т. п. Если вам нужно как-то отфильтровать
эти данные, используйте генератор списков вместе с различными функциями
библиотеки
os.path(). Например:
"""

# получить все обычные файлы
names = [name for name in os.listdir(path_dir) if os.path.isfile(os.path.join(path_dir, name))]
print(names)

# получить все каталоги
dirnames = [name for name in os.listdir(path_dir)
            if os.path.isdir(os.path.join(path_dir, name))]

