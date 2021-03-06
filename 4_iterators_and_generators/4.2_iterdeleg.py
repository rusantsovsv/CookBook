"""
Вы создали нестандартный объект-контейнер, который внутри содержит список,
кортеж или какой-то другой итерируемый объект. Вы хотите заставить ваш новый
контейнер работать с итерациями.

В типичном случае вам нужно определить метод __iter__(), который делегирует
итерацию внутреннему содержимому контейнера. Например:
"""


class Node:

    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)


# пример
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    for ch in root:
        print(ch)

"""
Протокол итераций Python требует, чтобы __iter__() возвращал специальный объ-
ект-итератор, в котором реализован метод __next__(), который и выполняет ите-
рацию. Если вы просто итерируете по содержимому другого контейнера, вам не
стоит беспокоиться о деталях внутреннего механизма процесса. Вам нужно просто
передать запрос на итерацию.
Использование функции iter() здесь позволяет «срезать путь» и написать более
чистый код. iter(s) просто возвращает внутренний итератор, вызывая s.__iter__(), –
примерно так же, как len(s) вызывает s.__len__().
"""
