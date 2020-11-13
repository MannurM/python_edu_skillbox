# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


# def get_prime_numbers(n):
#     prime_numbers = []
#     for number in range(2, n + 1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#     return prime_numbers

# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:

    def __init__(self, n):
        self.n = n
        self.i = 0
        self.prime_numbers = []
        self.prime = None

    def __iter__(self):
        self.i = 2
        return self

    def __next__(self):
        for self.i in range(self.i, self.n + 1):
            for self.prime in self.prime_numbers:
                # print(self.i, self.prime)
                if self.i % self.prime == 0:  # Если число делится без остатка, то следующее число, иначе
                    break
            else:
                self.prime_numbers.append(self.i)  # добавить это число
                return self.i

        raise StopIteration()


prime_number_iterator = PrimeNumbers(n=10000)


#
# for number in prime_number_iterator:
#     print('prime number', number)


# можно приступать ко второй части
# после подтверждения части 1 преподователем, можно делать
# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик

def prime_numbers_generator(n, func):
    prime_numbers = []


    for i in range(2, n + 1):
        for prime in prime_numbers:
            if i % prime == 0:
                break
        else:
            prime_numbers.append(i)
            # попробуйте использовать эти переменные
            # Не знаю правда насколько это нужно - собирать такой словарь)
            # Как вариант можно собрать True/False в список
            # а затем использовать all(список_ответов)
            # и если проверка проходит -> делать yield
            # да я в очередной раз стал из заданной задачи придумывать другую - свою))
            # хотел в словаре собирать типа 'досье' на каждое число что-то типа  словарь(ключ - number : значение -
            # - вложенные словари (ключ - функция фильтр1: значение True,...  и так по всем функциям.
            # Затем отдельно  выбираю число и на него выходит досье -
            #  что оно простое, и счастливое, и палиндромное, и ...
            # вобщем, замудрил))
            func_rezult = []
            for func_num in func:
                func_num_rez = func_num(number=i)
                func_rezult.append(func_num_rez)
            # print(i, func_rezult)
            if all(func_rezult):
                yield i

            # просто так указывать функции - не очень хорошо
            # попробуйте передавать их параметром
            # (можно передать список функций)
            # А здесь, чтобы не ограничивать фильтры двумя, подумайте
            # можно ли как-то собрать результаты проверки всех функций (не важно сколько их передали)
            # и проверить все эти результаты перед отправкой числа


def lucky_number(number):
    if number > 10:
        len_number = int(len(str(number)))
        list_number = list(str(number))
        middle_number = int(str(len_number // 2))
        first_sum_num = 0
        last_sum_num = 0

        for num in range(middle_number):
            first_sum_num += int(list_number[num])

        list_number.reverse()
        for num in range(middle_number):
            last_sum_num += int(list_number[num])

        return first_sum_num == last_sum_num


def palindrome_number(number):
    if number > 10:
        len_number = int(len(str(number)))
        list_number = list(str(number))
        middle_number = int(str(len_number // 2))
        return list_number[:middle_number] == list_number[-middle_number:]


def square_number(number):
    return number ** 2 % 2 == 0


func_list = [lucky_number, palindrome_number]  # добавить наименование функций фильтров

for number in prime_numbers_generator(n=10000, func=func_list):
    if number:
        print('Число', number)

# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
#зачёт!