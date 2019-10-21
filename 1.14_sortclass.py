"""
Вы хотите отсортировать объекты одного класса, но они не поддерживают опера-
ции сравнения.

Встроенная функция sorted() принимает аргумент key, в котором может быть пере-
дан вызываемый объект, который будет возвращать некоторое значение из объ-
ектов, которое sorted() будет использовать для сравнения этих объектов. Напри-
мер, если у вас в приложении есть последовательность экземпляров класса User
и вы хотите отсортировать их по атрибуту user_id, то вы могли бы предоставить
вызываемый объект, который принимает экземпляр класса User и возвращает
атрибут user_id.
"""


class User:

    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [User(23), User(3), User(99)]

print(sorted(users, key=lambda u: u.user_id))

print(users)

"""Вместо lambda можно применить альтернативный подход с использованием operator.attrgetter():"""

from operator import attrgetter
print(sorted(users, key=attrgetter('user_id')))

"""
Использовать или не использовать lambda или attrgetter() – вопрос личных пред-
почтений. Однако attrgetter() часто оказывается немного быстрее, а также позво-
ляет одновременно извлекать несколько полей. Это аналогично использованию
operator.itemgetter() для словарей (см. рецепт 1.13). Например, если экземпляры
класса User также имеют атрибуты first_name и last_name, вы можете выполнить
вот такую сортировку:

by_name = sorted(users, key=attrgetter('last_name', 'first_name'))

Стоит отметить, что использованный в этом рецепте прием может быть при-
менен к таким функциям, как min() и max().
"""

print(min(users, key=attrgetter('user_id')))
print(max(users, key=attrgetter('user_id')))