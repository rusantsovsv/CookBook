"""
У вас есть последовательность элементов, и вы хотите узнать, какие элементы
встречаются в ней чаще всего.

Класс collections.Counter разработан как раз для решения подобных задач. В нем
даже есть удобный метод most_common(), который сразу выдаст вам ответ.
"""

words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
         'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
         'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
         'my', 'eyes', "you're", 'under']

from collections import Counter

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)

"""
Если вы хотите увеличить счет вручную, используйте сложение:
"""

morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
for word in morewords:
    word_counts[word] += 1

print(word_counts['eyes'])

# Или можно использовать метод update():
word_counts.update(morewords)
print(word_counts['eyes'])

"""
Малоизвестная возможность экземпляров Counter состоит в том, что они могут
быть легко скомбинированы с использованием разнообразных математических
операций.
"""

a = Counter(words)
b = Counter(morewords)

print(a, b, sep='\n')

c = a + b
print(c)

d = a - b
print(d)
