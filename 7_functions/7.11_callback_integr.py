"""
Вы пишете код, в котором используются функции обратного вызова, но вас бес-
покоит быстрое размножение маленьких функций и излишняя сложность потока
управления. Вы бы хотели как-то заставить код выглядеть более похожим на нор-
мальную последовательность процедурных шагов.

Функции обратного вызова могут быть встроены в функцию путем использо-
вания генераторов и корутин (сопрограмм). Предположим, у вас есть функция,
которая выполняет какую-то работу и вызывает функцию обратного вызова (см.
рецепт 7.10):
"""

def apply_async(func, args, *, callback):
    # вычисляем результат
    result = func(*args)

    # вызываем функцию обратного вызова
    callback(result)


"""
Теперь взгляните на поддерживающий код, который использует класс Async
и декоратор inlined_async:
"""

from queue import Queue
from functools import wraps


class Async:

    def __init__(self, func, args):
        self.func = func
        self.args = args

def inlined_async(func):
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        result_queue = Queue()
        result_queue.put(None)
        while True:
            result = result_queue.get()
            try:
                a = f.send(result)
                apply_async(a.func, a.args, callback=result_queue.put)
            except StopIteration:
                break
    return wrapper


"""
Эти два фрагмента кода позволят вам встроить в строку шаги функции обрат-
ного вызова, используя инструкции yield. Например:
"""

def add(x, y):
    return x + y

@inlined_async
def test():
    r = yield Async(add, (2, 3))
    print(r)
    r = yield Async(add, ('hello', 'world'))
    print(r)
    for n in range(10):
        r = yield Async(add, (n, n))
        print(r)
    print('Goodbye')

"""
Если вы вызовете test(), то получите такой вывод:
"""
test()

"""
Если исключить специальный декоратор и использование yield, то вы заметите,
что функции обратного вызова нигде не появляются (только «под капотом»).
"""

