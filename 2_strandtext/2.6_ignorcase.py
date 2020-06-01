"""
Вам необходимо найти и, возможно, заменить текст, не обращая внимания на ре-
гистр букв.
"""
import re

text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python', text, flags=re.IGNORECASE))
print(re.sub('python', 'snake', text, flags=re.IGNORECASE))

"""
Последний пример демонстрирует ограничение способа: текст замены не будет
совпадать по регистру с заменяемым текстом. Если вам нужно исправить такое
поведение, используйте функцию поддержки:
"""

def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace


# пример использования этой функции
print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))

"""
В случаях простого применения re.INGNORECASE достаточно для поиска совпа-
дений без учета регистра. Однако обратите внимание, что этого может оказаться
недостаточно для некоторых случаев работы с Unicode, использующих выравни-
вание регистров (case folding).
"""

