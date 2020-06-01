import math


def drop_first_last(grades):
    first, *middle, last = grades
    return middle


print(drop_first_last((10, 20, 30, 40, 50)))
