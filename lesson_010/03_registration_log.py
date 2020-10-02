# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.


class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


class Cleaner:

    def __init__(self):
        self.file_name = None
        self.registrations_bad = []
        self.registrations_good = []
        self.file_result_bad = None
        self.file_result_good = None
        self.file_bad = None
        self.file_good = None

    def read(self, file_name):
        self.file_name = file_name
        with open(self.file_name, mode='r', encoding='utf-8') as file:
            for line in file:
                line = line[:-1]
                valid_data = line
                # print(line)
                try:
                    if not valid_data:
                        # print('ошибка - Нет данных в строке', valid_data)
                        raise IndexError('ошибка -  Нет данных в строке')
                    line = line.split()
                    name = line[0]
                    email = line[1]
                    age = line[2]
                    if not len(age):  # TODO Вот здесь не находит ошибку - что-то не так?
                        # TODO хочу проверить на наличие символов в переменной

                        print('ошибка - Неполные данные', 'valid_data', valid_data)
                        raise ValueError('ошибка - Неполные данные')

                    for symbol in name:
                        if symbol.isalpha():
                            continue
                        else:
                            # print('ошибка - В имени пользователя не только буквы!', name, valid_data)
                            raise NotNameError('ошибка - В имени пользователя не только буквы!')

                    if not chr(64) or not chr(46) in email:
                        # print('ошибка - Поле email не содержит "@" и  "." ', email, valid_data)
                        raise NotEmailError('ошибка - Поле email не содержит "@" и  "." ')
                    if not age.isdigit():
                        # print('ошибка - Возраст не является числом', age, valid_data)
                        raise ValueError('ошибка - Возраст не является числом')
                    if 99 > int(age) > 10:
                        # print(age, '-age')
                        self.registrations_good.append(valid_data)
                    else:
                        raise ValueError('ошибка - Возраст выходит за пределы диапазона')

                except IndexError:
                    self.registrations_bad.append(valid_data)

                except ValueError:
                    self.registrations_bad.append(valid_data)

                except NotNameError:
                    self.registrations_bad.append(valid_data)

                except NotEmailError:
                    self.registrations_bad.append(valid_data)

            print(len(self.registrations_bad), 'self.registrations_bad')
            print(len(self.registrations_good), 'self.registrations_good')

    def create_result_files(self, file_result_bad, file_result_good):
        self.file_result_bad = file_result_bad
        self.file_result_good = file_result_good
        self.file_bad = open(self.file_result_bad, mode='w')
        self.file_good = open(self.file_result_good, mode='w')

        for index in self.registrations_bad:
            value_line = index + '\n'
            self.file_bad.write(value_line)
        self.file_bad.close()

        for index in self.registrations_good:
            value_line = index + '\n'
            self.file_good.write(value_line)
        self.file_good.close()


cleaner = Cleaner()
cleaner.read(file_name='registrations.txt')
cleaner.create_result_files(file_result_bad='registrations_bad.log', file_result_good='registrations_good.log')
