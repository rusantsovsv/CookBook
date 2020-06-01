"""
Вам нужно манипулировать путями к файлам, чтобы найти имя файла, название
каталога, абсолютный путь и т. д.

Для работы с файловыми путями используйте функции из модуля os.path. Вот
пример, который иллюстрирует несколько ключевых возможностей:
"""

import os
path = r'C:\Users\RusancovS\Desktop\Яндекс Практикум\jupyter_ML\data\train_data_1571975844.csv'

# получение последнего компонента пути
print(os.path.basename(path))

# получение имени каталога
print(os.path.dirname(path))

# соедиение компонентов пути
print(os.path.join('tmp', 'data', os.path.basename(path)))

# раскрытие домашнего каталога
path = r'~\data\train_data_1571975844.csv'
print(os.path.expanduser(path))

# отделение расширения файла
print(os.path.splitext(path))