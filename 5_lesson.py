from functools import reduce
import json


def task_1():
    with open('task_1.txt', 'w') as f:
        while True:
            user_str = input('Your sting: ')
            if user_str == '': break

            f.write(user_str + '\n')


def task_2():
    with open('task_2.txt', 'r') as f:
        for i, line in enumerate(f):
            print('line ', i, ': ', len(line.split()), end='; ')
        print()
        print('Total lines: ', i)


def task_3():
    summ = 0

    with open('task_3.txt', 'r') as f:
        for i, line in enumerate(f):
            surname = line[:line.find(' ')]
            salary = int(line[line.find(' '):].strip())

            summ += salary

            if salary < 20000: print(surname)
        print('Average:', f'{summ / i:.2f}')


def task_4():
    numbers = ['Один', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть', 'Семь', 'Восемь', 'Девять']
    with open('task_4_origin.txt', 'r') as f_origin, open('task_4_result.txt', 'w') as f_result:

        for line in f_origin:
            f_result.write(numbers[int(line[-2]) - 1] + ' ' + line[-2] + '\n')


def task_5():

    with open('task_5.txt', 'w+') as f:
        f.write(' '.join([str(n) for n in range(1, 1000, 3)]))
        f.seek(0)
        print(reduce(lambda a, b: int(a) + int(b), f.read().split(' ')))


def task_6():
    dict = {}
    with open('task_6.txt', 'r') as f:
        for line in f:
            dict[f'{line[:line.find(":")]}'] = \
                sum([get_hours(line, '(л)'), get_hours(line, '(пр)'), get_hours(line, '(лаб)')])
        print(dict)


def get_hours(str, name):
    end = str.find(name)
    if end < 0: return 0
    spaces = [pos for pos in range(len(str)) if str[pos] == ' ' and pos < end]
    return int(str[spaces[-1]: end])


def task_7():
    average_profit, quantity = 0, 0
    firms = []

    with open('task_7.txt', 'r') as f:
        for line in f:
            spaces_pos = [pos for pos in range(len(line)) if line[pos] == ' ']
            profit = int(line[spaces_pos[1] + 1: spaces_pos[2]]) - int(line[spaces_pos[2] + 1:])
            firms.append({line[:spaces_pos[0]]: profit})

            if profit >= 0:
                average_profit += profit
                quantity += 1

    average_profit /= quantity
    firms.append({'average_profit': average_profit})

    with open('task_7_result.py', 'w') as f:
        f.write(json.dumps(firms))


task_1()
task_2()
task_3()
task_4()
task_5()
task_6()
task_7()