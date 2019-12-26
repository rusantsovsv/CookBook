"""
Вы хотите записать данные в файл, но только в том случае, если его еще нет в фай-
ловой системе.

Эта задача легко решается с помощью использования малоизвестного режима x
работы open() (вместо обычного режима w):
"""

with open(r'files\somefile', 'wt') as f:
    f.write('Hello\n')

#with open(r'files\somefile', 'xt') as f:           File exists: 'files\\somefile'
    #f.write('Hello\n')

"""Если файл в бинарном режиме, используйте режим xb вместо xt."""

"""
Этот рецепт демонстрирует удивительно элегантное решение проблемы, иногда
возникающей при записи в файлы (например, случайной перезаписи существую-
щего файла). Альтернативное решение – предварительная проверка:
"""

import os
if not os.path.exists(r'files\somefile'):
    with open(r'files\somefile', 'wt') as f:
        f.write('Hello\n')
else:
    print('File already exists!')


