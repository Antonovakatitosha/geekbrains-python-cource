def task_1():
    l = [1, 5.6, 'a', (1,), [0], {1, 2, 3}, {'a': 'a'}, False, b'text', None]

    for elem in l:
        if isinstance(elem, bool):
            print(elem, 'boolean')
        elif isinstance(elem, type(None)):
            print(elem, 'None')
        elif isinstance(elem, (int, float)):
            print(elem, 'число')
        elif isinstance(elem, (str, bytes)):
            print(elem, 'текст')
        elif isinstance(elem, tuple):
            print(elem, 'кортеж')
        elif isinstance(elem, list):
            print(elem, 'список')
        elif isinstance(elem, set):
            print(elem, 'множество')
        elif isinstance(elem, dict):
            print(elem, 'словарь')


def task_2():
    l = []

    print("Для окончания ввода нажмите q")
    while True:
        elem = input("Введите элемент списка: ")
        if elem == 'q': break

        l.append(elem)

    it = iter(range(len(l)))
    for i1, i2 in zip(it, it):
        l[i1], l[i2] = l[i2], l[i1]

    print(l)


def task_3():
    month = int(input('Введите номер месяца: '))
    if month > 12:
        print('Нет такого месяца')
        return

    seasons_dict = {
        'лето': [6, 7, 8],
        'осень': [9, 10, 11],
        'зима': [12, 1, 2],
        'весна': [3, 4, 5],
    }

    for key, value in seasons_dict.items():
        if month in value:
            print(key)
            break

    seasons_l = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
    print(seasons_l[month - 1])


def task_4():
    message = input("Введите предлоджение: ")
    words = message.split()

    for i, word in enumerate(words):
        print(i, word[:10])


def task_5():
    rating = [7, 5, 3, 3, 2]

    print("Для окончания ввода нажмите q")
    while True:
        elem = input("Введите число: ")
        if elem == 'q': break

        rating.append(int(elem))
        rating.sort(reverse=True)

        print(rating)


def task_6():
    name = 'название'
    price = 'цена'
    amount = 'количество'
    measure = 'ед'

    analytics = {name: [], price: [], amount: [], measure: []}
    products = []
    id_count = 0

    while True:
        if input("Добавить новый товар? да/ нет: ") == 'нет': break

        pr_name = input("Название товара: ")
        pr_price = input("Цена товара: ")
        pr_amount = input("Количество товара: ")
        pr_measure = input("Единицы измерения товара: ")

        new_product = (id_count, {name: name, price: int(pr_price), amount: int(pr_amount), measure: pr_measure})

        products.append(new_product)
        id_count += 1

        if pr_name not in analytics[name]: analytics[name].append(pr_name)
        if pr_price not in analytics[price]: analytics[price].append(pr_price)
        if pr_amount not in analytics[amount]: analytics[amount].append(pr_amount)
        if pr_measure not in analytics[measure]: analytics[measure].append(pr_measure)

    print('Товары', products)
    print('Аналитика', analytics)


task_1()
task_2()
task_3()
task_4()
task_5()
task_6()
