"""
Вы используете регулярные выражения для обработки текста, однако беспокои-
тесь о правильном взаимодействии с символами Unicode.
"""
import re

num = re.compile('\d+')
# ASCII-цифры
print(num.match('123'))

# арабские цифры
print(num.match('\u0661\u0662\u0663'))

"""
Если вам нужно включить специфические символы Unicode в шаблоны, вы мо-
жете использовать обычные последовательности для экранирования символов
Unicode (например, \uFFFF или \\UFFFFFFF). Например, вот регулярное выражение,
которое найдет совпадения со всеми символами на нескольких разных арабских
страницах:
"""

arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')

"""
При выполнении поиска совпадений следует нормализовывать и, по возмож-
ности, чистить текст, приводя его к стандартной форме (см. рецепт 2.9). Также
нужно знать о некоторых специальных случаях. Например, рассмотрим поведе-
ние нечувствительного к регистру поиска совпадений при объединении с приве-
дением к одному регистру:
"""

pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
print(pat.match(s))
print(pat.match(s.upper()))
print(s.upper())

"""
Смешивание Unicode и регулярных выражений – отличный способ взорвать себе
голову. Если вы собираетесь серьезно в это погрузиться, установите стороннюю
библиотеку regex1, в которой есть полная поддержка приведения текстов в Unicode
к одному регистру, а также множество других интересных возможностей, включая
аппроксимирующий поиск совпадений.
"""