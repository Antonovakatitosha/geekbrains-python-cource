import sys
from functools import reduce
from itertools import count, cycle

from typing import List


def task_1(hour_output, hour_rate, prize) -> float:
    return float(hour_output) * float(hour_rate) + float(prize)


def task_2(numbers_list: List[float]) -> List[float]:
    for i, _ in enumerate(numbers_list[1:]):
        if numbers_list[i + 1] > numbers_list[i]:
            yield numbers_list[i + 1]


def task_3():
    return [elem for elem in range(20, 241) if elem % 20 == 0 or elem % 21 == 0]


def task_4(user_list: List[int]) -> List[int]:
    return [elem for elem in user_list if user_list.count(elem) == 1]


def task_5() -> int:
    new_list = [elem for elem in range(100, 1001) if elem % 2 == 0]
    return reduce(lambda x, y: x * y, new_list)


def task_6(start: int, user_list):
    for elem in count(start):
        if elem > 10: break
        print(elem)

    for i, elem in enumerate(cycle(user_list)):
        if i > 15: break
        print(elem, end=' ')
    print()


def task_7():
    for elem in fact(10):
        print(elem)


def fact(n):
    current = 1
    for i in range(1, n+1):
        current *= i
        yield current


# python 4_lesson.py 3 2 5
print(task_1(*sys.argv[1:]))

for elem in task_2([300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]):
    print(elem, end=', ')
print()
print(task_3())
print(task_4([2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]))
print(task_5())
task_6(3, 'test')
task_7()


