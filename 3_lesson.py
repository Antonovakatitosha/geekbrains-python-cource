from typing import List


def task_1():

    a = float(input('Enter first number: '))
    b = float(input('Enter second number: '))
    print("{:.2f}".format(dev(a, b)))


def dev(a: float, b: float) -> float:
    if b == 0: return 0
    return a/b


def task_2():

    name = input('Enter your name: ')
    surname = input('Enter your surname: ')
    birth_year = input('Enter your day of birth: ')
    city = input('Enter your city: ')
    email = input('Enter your email: ')
    phone = input('Enter your phone number: ')
    print_user_info(surname=surname, name=name, city=city, birth_year=birth_year, phone=phone, email=email)


def print_user_info(name, surname, birth_year, city, email, phone) -> str:
    print('name: ', name, end=', ')
    print('surname: ', surname, end=', ')
    print('birth_year: ', birth_year, end=', ')
    print('city: ', city, end=', ')
    print('email: ', email, end=', ')
    print('phone: ', phone)


def task_3_my_func(a: float, b: float, c: float) -> float:
    """ return sum of two maximum elements """

    if a < b and a < c: return b + c
    elif b < c: return a + c
    return a + b


def task_4_my_func(x: float, y: int) -> float:
    return 1 if y == 0 else (1/x) * task_4_my_func(x, y + 1)


def task_5():
    global_sum = 0

    print('For exit enter q')
    while True:
        user_str = input('enter a list of numbers: ')
        q_position = user_str.lower().find('q')

        if q_position == 0: break
        if q_position > 0: user_str = user_str[:q_position]

        global_sum += list_sum(user_str.split())
        print('sum of numbers: ', global_sum)
        if q_position > 0: break


def list_sum(user_list: List[str]) -> float:
    sum = 0
    for elem in user_list: sum += float(elem)
    return sum


def task_6():
    user_str = input('Enter string with spaces: ')
    for word in user_str.split():
        print(int_func(word), end=' ')
    print()


def int_func(message: str) -> str:
    return message[0].upper() + message[1:]


task_1()
task_2()
print(task_3_my_func(1, 3, 2))
print(task_4_my_func(2.4, -5))
task_5()
task_6()
