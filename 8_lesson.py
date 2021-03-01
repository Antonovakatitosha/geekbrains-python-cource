# Task 1
class Date:

    def __init__(self, user_str):
        """ str = day-month-year """
        self.user_str = user_str

    @classmethod
    def to_int(cls, user_str):
        print(*cls.__split_to_int(user_str))

    @staticmethod
    def validate(user_str):
        day, month, year = Date.__split_to_int(user_str)
        if not 0 < day <= 31: return f'Error in day {day}'
        if not 0 < month <= 12: return f'Error in month {month}'
        if not 1950 <= year <= 2030: return f'Error in year {year}'
        return f'Great {day}.{month}.{year}'

    @staticmethod
    def __split_to_int(user_str):
        day = user_str[:user_str.find('-')]
        user_str = user_str[len(day) + 1:]
        month = user_str[:user_str.find('-')]
        year = user_str[len(month) + 1:]

        return int(day), int(month), int(year)


date = Date('11-02-1999')
date.to_int(date.user_str)
print(Date.validate(date.user_str))

date2 = Date('11-20-1930')
print(Date.validate(date.user_str))


# Task 2
class CustomZeroDivError(Exception):
    def __init__(self):
        print('Custom zero division error')


try:
    a = int(input('Enter number '))
    b = int(input('Enter number '))
    if b == 0: raise CustomZeroDivError
    print(f'a / b = {a/b}')
except CustomZeroDivError:
    print('Sorry, try again next time')


# Task 3

class StrInListError(Exception):
    @staticmethod
    def check_list(user_number):
        try:
            int(user_number)
        except:
            raise StrInListError


user_list = []
while True:
    user_number = input('Enter value or "stop" ')
    if user_number.lower() == 'stop': break
    try:
        StrInListError.check_list(user_number)
        user_list.append(int(user_number))
    except StrInListError:
        print('Sorry, not sorry')

print(user_list)


# Task 4, 5, 6
class OfficeEquipment:
    def __init__(self, name, prise, weight):
        self.name = name
        self.prise = prise
        self.weight = weight


class Printer(OfficeEquipment):
    def __init__(self, prise, weight, copy_per_sec):
        self.copy_per_sec = copy_per_sec
        super().__init__('Printer', prise, weight)

    def __str__(self):
        return f'Printer prise: {self.prise:,}; weight: {self.weight}kg; usb_type: {self.copy_per_sec}'


class Scanner(OfficeEquipment):
    def __init__(self, prise, weight, usb_type):
        self.usb_type = usb_type
        super().__init__('Scanner', prise, weight)

    def __str__(self):
        return f'Scanner prise: {self.prise:,}; weight: {self.weight}kg; usb_type: {self.usb_type}'


class Storage:
    def __init__(self):
        self.storage = {}

    def add_to_storage(self, equipment: OfficeEquipment, storage_name: str, quantity: int):
        try:
            self.storage.setdefault(storage_name, []) \
                .append({'equipment': equipment, 'quantity': int(quantity)})
        except ValueError:
            print('Quantity must be int type')

    def chek(self):
        for storage_name, contents in self.storage.items():
            print(f'\nStorage {storage_name}')
            for content in contents:
                print(f'Quantity {content["quantity"]}; Description: {content["equipment"]}')


printer_1 = Printer(2499, 5, 3)
printer_2 = Printer(1900, 4, 1)
scanner_1 = Scanner(4999, 2, '3.0')
scanner_2 = Scanner(33000, 2, '10.0')
scanner_3 = Scanner(1500, 2, '2.0')


storage = Storage()
storage.add_to_storage(printer_1, 'Подсобка', 3)
storage.add_to_storage(scanner_1, 'Подсобка', 10)
storage.add_to_storage(printer_2, 'Бухгалтерия', 2)
storage.add_to_storage(scanner_2, 'Бухгалтерия', 1)
storage.add_to_storage(scanner_2, 'Столовая', 99)
storage.chek()


# Task 7
class ComplexNumber:
    def __init__(self, base: int, imaginary: int):
        self.base = base
        self.imaginary = imaginary

    def __str__(self):
        return f'{self.base} {f"+ {self.imaginary}" if self.imaginary > 0 else f"- {self.imaginary * -1}"}i'

    def __add__(self, other):
        return ComplexNumber(self.base + other.base, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(self.base * other.base, self.imaginary * other.imaginary)


print()
a = ComplexNumber(3, 5)
b = ComplexNumber(4, -2)
print(f'a = {a}', f'b = {b}', sep='\n')
print(f'a + b = {a + b}')
print(f'a * b = {a * b}')
