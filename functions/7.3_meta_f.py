"""
Вы определили функцию, но хотели бы прикрепить дополнительную информацию
к аргументам, чтобы другим людям было легче понять, что делает эта функция.

Аннотации аргументов могут быть полезны, чтобы помочь программистам разо-
браться в том, как нужно применять функцию. Например, рассмотрим такую ан-
нотированную функцию:
"""


def add(x:int, y:int) -> int:
    return x + y


"""
Интерпретатор Python не прикрепляет никакого семантического смысла к ан-
нотациям. Это не проверки типов, они вообще никак не влияют на поведение
Python. Однако они могут помогать другим людям читать исходный код и пони-
мать, что вы имели в виду. А вот сторонние инструменты и фреймворки могут
прикреплять к аннотациям семантический смысл. Также они появляются в до-
кументации:
"""

help(add)

"""
Хотя вы можете прикрепить любой объект к функции в качестве аннотации
(например, числа, строки, экземпляры и т. д.), использование классов или строк
имеет наибольший смысл.

Аннотации функции хранятся в атрибуте функции __annotations__. Например:
"""

print(add.__annotations__)

"""
Хотя можно придумать немало потенциальных применений аннотаций, обыч-
но их используют для документации. Поскольку в Python нет объявлений типов,
часто бывает сложно понять, что нужно передавать в функцию, когда вы просто
читаете исходный код. Аннотации дают дополнительную информацию.
См. продвинутый пример в рецепте 9.20, который показывает, как использо-
вать аннотации для реализации множественной диспетчеризации (т. е. перегру-
женных функций).
"""