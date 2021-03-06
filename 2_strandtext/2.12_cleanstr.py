"""
Некий деятель ввел текст «pýtĥöñ» в форму на вашей веб-странице, и вы хотите
как-то почистить эту строку.

Проблема чистки текста применяется к широкому спектру задач с использова-
нием парсинга текста и обработки данных. На самом элементарном уровне вы
можете использовать простые строковые функции (например, str.upper() и str.
lower() для приведения текста к стандартному регистру). Простые замены с ис-
пользованием str.replace() или re.sub() помогут справиться с удалением или из-
менением некоторых специфических последовательностей символов. Вы также
можете нормализовать текст, используя функцию unicodedata.normalize(), как по-
казано в рецепте 2.9.
Однако вы можете захотеть сделать следующий шаг в процессе чистки. Пред-
положим, что вы хотите удалить целые диапазоны символов или диакритические
знаки. Для этого вы можете обратиться к методу str.translate(). Предположим, у вас
есть вот такая замусоренная строка:
"""

s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)

# Первый шаг – удалить пробел. Сделаем небольшую таблицу перевода и задействуем translate():
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None     # Удален
}

a = s.translate(remap)
print(a)

"""
Как вы можете увидеть, символы пробелов, такие как \t и \f , были приведены
к единой форме. Символ возврата каретки \r был удален.
Вы можете продолжить идею и создать намного более крупные таблицы пере-
вода. Например, давайте удалим все комбинирующиеся символы:
"""

import unicodedata
import sys

cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
# print(cmb_chrs)
b = unicodedata.normalize('NFD', a)
print(b)

print(b.translate(cmb_chrs))

"""
В последнем примере с помощью dict.fromkeys() был создан словарь, отобража-
ющий все комбинирующиеся символы Unicode на None.
Первоначальные вводные данные затем были нормализованы в декомпозиро-
ванную форму с использованием unicodedata.normalize(). Далее функция translate()
применяется для удаления диакритических знаков. Похожие приемы могут быть
использованы для удаления символов другого типа (например, управляющих
символов).
Еще один пример – таблица перевода, которая отображает все десятичные циф-
ры Unicode на их эквиваленты в ASCII:
"""

digitmap = {c:ord('0') + unicodedata.digit(chr(c)) for c in range(sys.maxunicode) if unicodedata.category(chr(c)) == 'Nd'}
print(len(digitmap))

# арабские цифры
x = '\u0661\u0662\u0663'
print(x.translate(digitmap))

"""
Еще один прием для чистки текста использует функции кодирования и декоди-
рования ввода-вывода. Идея состоит в выполнении некоторой первичной очистки
текста, а затем пропускании его через encode() и decode() для срезания символов
или изменения. Например:
"""

print(a)
b = unicodedata.normalize('NFD', a)
b = b.encode('ascii', 'ignore').decode('ascii')
print(b)

"""
Здесь процесс нормализации разложил исходный текст на символы вместе с от-
дельными комбинирующимися символами. Последовательное кодирование и де-
кодирование в ASCII просто удаляет все эти символы. Естественно, это сработает
только в том случае, если нашей целью было получение ASCII-представления.

Большой проблемой с чисткой текста может стать производительность. Общее
правило: чем проще обработка, тем быстрее она работает. Для простых замен
метод str.replace() часто оказывается самым быстрым способом – даже если вы-
зывать его несколько раз. Например, чтобы вычистить пробелы, вы можете ис-
пользовать такую программу:
def clean_spaces(s):
s = s.replace('\r', '')
s = s.replace('\t', ' ')
s = s.replace('\f', ' ')
return s
Если вы попробуете это, то обнаружите, что метод немного быстрее использо-
вания translate() или регулярных выражений.
С другой стороны, метод translate() очень быстр, если вам нужно выполнить лю-
бую нетривиальную операцию замены символов на другие символы или удаления
символов.
Производительность – это то, что вам придется изучать в каждом конкретном
приложении. К сожалению, невозможно предложить один прием, который будет
работать лучше всего во всех возможных ситуациях, поэтому пробуйте разные
подходы и измеряйте результаты.
Хотя этот рецепт делает акцент на работе с текстом, похожие приемы могут
быть применены к последовательностям байтов, включая простые замены, пере-
воды и регулярные выражения.
"""

