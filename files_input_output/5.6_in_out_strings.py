"""
Вы хотите скормить текст или бинарную строку программе, которая способна ра-
ботать с файлоподобными объектами.

Используйте классы io.StringIO() и io.BytesIO() для создания файлоподобных объ-
ектов, которые могут работать со строковыми данными. Например:
"""

import io

s = io.StringIO()
s.write('Hello world\n')

print('This is a test', file=s)

# Получить все уже записанные данные
print(s.getvalue())

# обернуть существующую строку файловым интерфейсом
s = io.StringIO('Hello\nWorld\n')

print(s.read(4))
print(s.read())

#Класс io.StringIO должен быть использован только для работы с текстом. Если вы
#работаете с бинарными данными, используйте io.BytesIO. Например:

s = io.BytesIO()
s.write(b'binary data')
print(s.getvalue())
