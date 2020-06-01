"""
Вы создаете собственные объекты, которые хотите сделать итерируемыми, и ище-
те простой способ реализовать протокол итератора.

На текущий момент простейший способ реализации итерируемости в объекте – это
использование генератора. В рецепте 4.2 был представлен класс Node, представ-
ляющий древовидные структуры. Возможно, вы захотите реализовать итератор,
который будет обходить узлы поиском в глубину. Вот как можно это сделать:
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

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


# пример
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)

"""
В этой программе метод depth_first() может просто прочесть и описать. Сначала
он выдает себя, а затем итерируется по каждому потомку, выдавая элементы, про-
изводимые методом depth_first() потомка (используя yield from).
"""

"""
Протокол итератора Python требует __iter__(), чтобы вернуть специальный объект
итератора, в котором реализована операция __next__(), а исключение StopIteration
используется для подачи сигнала о завершении. Однако создание таких объектов
часто может стать запутанным делом. Например, следующая программа демон-
стрирует альтернативную реализацию метода depth_first(), использующую ассо-
циированный класс итератора:
"""


class Node:

    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, other_node):
        self._children.append(other_node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        return DepthFirstIterator(self)


class DepthFirstIterator:
    """
    Depth-first traversal
    """

    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        # возвращает себя, если только что запущен, создает итератор для потомков
        if self._children_iter is None:
            self._children_iter = iter(self._node)
            return self._node

        # если обрабатывает потомка - возвращает его следующий элемент
        elif self._child_iter:
            try:
                nextchild = next(self._child_iter)
                return nextchild
            except StopIteration:
                self._child_iter = None
                return next(self)

        # переходим к следующему потомку и начинаем итерировать по нему
        else:
            self._child_iter = next(self._children_iter).depth_first()
            return next(self)


"""
Класс DepthFirstIterator работает так же, как и версия на основе генератора,
но он беспорядочен и некрасив, поскольку итератор вынужден хранить много
сложной информации о состоянии итерационного процесса. Откровенно говоря,
никому не нравится писать такой мозговыносящий код. Реализуйте итератор на
базе генератора и успокойтесь на этом.
"""
