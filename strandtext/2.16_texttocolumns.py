"""
У вас есть длинные строки, которые вы хотите переформатировать таким обра-
зом, чтобы они распределились по заданному пользователем количеству колонок.

Используйте модуль textwrap для переформатирования выводимого текста. Пред-
положим, что у вас есть такая длинная строка:
"""
s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

import textwrap
print(textwrap.fill(s, 70))         # ограничить длину строки 70 символами
print(textwrap.fill(s, 40))         # ограничить длину строки 40 символами
print(textwrap.fill(s, 40, initial_indent=' '))         # ограничить длину строки 40 символами, сделать красную строку
print(textwrap.fill(s, 40, subsequent_indent=' '))      # ограничить длину строки 40 символами, сделать отступ 1 строки

"""
Модуль textwrap – это простой способ очистить текст, особенно если вы хотите,
чтобы вывод соответствовал размерам терминала. К вопросу о размере термина-
ла: вы можете получить его, используя os.get_terminal_size().

У метода fill() есть несколько дополнительных параметров, которые контроли-
руют то, как он обращается с табуляцией, окончаниями предложений и т. д. За
подробностями обратитесь к документации класса textwrap.TextWrapper
"""
