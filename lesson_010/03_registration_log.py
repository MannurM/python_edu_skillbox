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
                try:
                    if not line:
                        # print('ошибка - Нет данных в строке', line)
                        raise IndexError('ошибка -  Нет данных в строке')
                    if len != 3:
                        line = line.split()
                        name = line[0]
                        email = line[1]
                        age = line[2]
                    else:
                        # print('ошибка - Неполные данные', 'line', line)
                        raise ValueError('ошибка - Неполные данные')

                    if not name.isalpha():
                        # print('ошибка - В имени пользователя не только буквы!', name, line)
                        raise NotNameError('ошибка - В имени пользователя не только буквы!')

                    if chr(64) is email:
                        if not chr(46) in email:
                            # print('ошибка - Поле email не содержит "@" и  "." ', email, line)
                            raise NotEmailError('ошибка - Поле email не содержит "@" и  "." ')

                    if not age.isdigit():
                        # print('ошибка - Возраст не является числом', age, line)
                        raise ValueError('ошибка - Возраст не является числом')
                    if 99 > int(age) > 10:
                        # print(age, '-age')
                        self.registrations_good.append(line)
                    else:
                        raise ValueError('ошибка - Возраст выходит за пределы диапазона')

                except (IndexError, ValueError, NotNameError, NotEmailError):
                    self.registrations_bad.append(line)

            # print(len(self.registrations_bad), 'self.registrations_bad')
            # print(len(self.registrations_good), 'self.registrations_good')

    def create_result_files(self, file_result_bad, file_result_good):
        self.file_result_bad = file_result_bad
        self.file_result_good = file_result_good
        self.file_bad = open(self.file_result_bad, mode='w')
        self.file_good = open(self.file_result_good, mode='w')

        for index in self.registrations_bad:
            value_line = str(index) + '\n'
            self.file_bad.write(value_line)
        self.file_bad.close()

        for index in self.registrations_good:
            value_line = str(index) + '\n'
            self.file_good.write(value_line)
        self.file_good.close()

    def run_programm(self, file_name, file_result_bad, file_result_good):
        self.read(file_name)
        self.create_result_files(file_result_bad, file_result_good)


cleaner = Cleaner()
cleaner.run_programm(file_name='registrations.txt',
                     file_result_bad='registrations_bad.log', file_result_good='registrations_good.log')

# cleaner.read(file_name='registrations.txt')
# cleaner.create_result_files(file_result_bad='registrations_bad.log', file_result_good='registrations_good.log')
