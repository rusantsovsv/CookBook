"""
Приведенный ниже класс использует модуль heapq для реализации простой оче-
реди с приоритетом.
"""

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        # print(self._queue) # для проверки структуры
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

for i in range(4):
    print(q.pop())

# Первая операция pop() возвращает элемент с наивысшим приоритетом. Также
# заметьте, что два элемента с одинаковым приоритетом (foo и grok) были возвра-
# щены в том же порядке, в каком они были помещены в очередь.
