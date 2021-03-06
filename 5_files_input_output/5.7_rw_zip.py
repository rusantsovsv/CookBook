"""
Вам нужно прочесть или записать данные в файл, сжатый gzip или bz2.

Модули gzip и bz2 делают работу с такими файлами очень легкой. Оба модуля
предоставляют
альтернативную реализацию функции open(). Например, чтобы
прочесть сжатые файлы как текст, сделайте так:
"""

# сжатие с помощью gzip
import gzip
with gzip.open('files/somefile.gz', 'rt') as f:
    text = f.read()

# сжатие файла с помощью bz2
import bz2

with bz2.open('files/somefile.bz2', 'rt') as f:
    text2 = f.read()

"""
Как показано выше, весь ввод и вывод будет использовать текст и проводить
кодирование/декодирование в Unicode. Если же вы хотите работать с бинарными
данными, используйте файловый режим rb или wb.
"""

"""
Чтение и запись сжатых данных по большей части просты. Однако стоит знать,
что выбор правильного файлового режима критически важен. Если вы не обозна-
чите режим явно, то будет выбран режим по умолчанию, то есть бинарный, а это
сломает программы, которые ожидают получить текст. gzip.open() и bz2.open()
принимают те же параметры, что и встроенная функция open(), включая encoding,
errors, newline и т. д.
При записи сжатых данных с помощью необязательного именованного аргу-
мента compresslevel может быть установлен уровень компрессии. Например:
    with gzip.open('somefile.gz', 'wt', compresslevel=5) as f:
        f.write(text)
Уровень по умолчанию – это 9, то есть наивысший. Более низкие уровни увели-
чивают скорость, но снижают степень сжатия данных.
"""

"""
И последнее: малоизвестная особенность gzip.open() и bz2.open() заключается
в том, что они могут работать уровнем выше существующего файла, открытого
в бинарном режиме. Например, такой код работает:
import
    f = open('somefile.gz', 'rb')
    with gzip.open(f, 'rt') as g:
        text = g.read()
Это позволяет модулям gzip и bz2 работать с различными файлоподобными
объектами, такими как сокеты, каналы и файлы в оперативной памяти.
"""