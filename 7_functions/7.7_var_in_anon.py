"""
Вы определили анонимную функцию, используя lambda, но вы также хотите за-
хватить значения некоторых переменных во время определения.

Рассмотрим поведение следующей программы:
"""

x = 10

a = lambda y: x + y
x = 20

b = lambda y: x + y

"""
А теперь задайте себе вопрос: какими будут значения a(10) и b(10)? Если вы
думаете, что 20 и 30, то ошибаетесь:
"""

print(a(10))
print(b(10))

"""
Проблема в том, что значение x, используемое в lambda-выражении, является
свободной переменной, которая связывается во время выполнения, а не во время
определения. Так что значение x в lambda-выражениях будет таким, каким ему
случится быть во время выполнения. Например:
"""

x = 15
print(a(10))

x = 3

print(a(10))

"""
Если же вы хотите, чтобы анонимная функция захватывала значение во время
определения и сохраняла его, используйте значение по умолчанию:
"""

x = 10

a = lambda y, x=x: y + y

x = 20

b = lambda y, x=x: x + y

print(a(10), b(10))

"""
Проблема, которую мы рассматриваем в этом рецепте, возникает, когда случается
перемудрить с lambda-функциями. Например, вы можете ожидать, что при соз-
дании списка lambda-выражений с использованием генератора списка или цик-
ла lambda-функции запомнят итерационные переменные во время определения.
Например:
"""

funcs = [lambda x: x+n for n in range(5)]
for f in funcs:
    print(f(0))

"""
Обратите внимание, что все функции считают, что n имеет последнее значение,
полученное в ходе итераций. Теперь сравните со следующим:
"""

funcs = [lambda x, n=n: x + n for n in range(5)]
for f in funcs:
    print(f(0))

"""
Как вы видите, теперь функции захватывают значения n во время определения.
"""