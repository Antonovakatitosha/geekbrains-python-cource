def task_1():
    my_str = "'"
    my_number = 123

    user_str = input('Enter a string: ')
    user_number = int(input('Enter a number: '))

    result = 'Your lucy number: {}, you enter the sting: {bracket}{}{bracket}'
    print(result.format(my_number * user_number, user_str, bracket=my_str))


def task_2():
    seconds = int(input('Enter a seconds: '))

    hours = seconds // (60 * 60)
    seconds %= (60 * 60)

    minutes = seconds // 60
    seconds %= 60

    print('Result: {:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds))


def task_3():
    n = input('Enter n: ')
    print('n + nn + nnn = ', int(n) + int(n + n) + int(n + n + n))


def task_4():
    number = int(input('Enter a number: '))
    max = 0

    while number > 0:
        if number % 10 > max: max = number % 10
        number //= 10

    print('Max number is:', max)


def task_5():
    revenue = int(input('Введите выручку: '))
    costs = int(input('Введите издержки: '))

    if costs > revenue: return print('Убыток')
    print('Рентабильность прибыли', round(revenue / costs, 2))

    staff_amount = int(input('Введите количество сотрудников: '))
    print('Прибыль в расчете на сотрудника', round(revenue / staff_amount, 2))


def task_6():
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    days = 1

    while a < b:
        a *= 1.1
        days += 1

    print(days)


task_1()
task_2()
task_3()
task_4()
task_5()
task_6()
