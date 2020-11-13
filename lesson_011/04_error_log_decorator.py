# -*- coding: utf-8 -*-

# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'

# TODO в снипетах есть пример хороший
# def time_track(func):
#     def surrogate(*args, **kwargs):
#         started_at = time.time()  TODO структура будет такой же, а внутри surrogate вы выполняете свои действия
#         TODO т.е. try/except блок с запуском функции и записью ошибки в except-е
#         result = func(*args, **kwargs)
#
#         ended_at = time.time()
#         elapsed = round(ended_at - started_at, 4)
#         print(f'Функция работала {elapsed} секунд(ы)')
#         return result
#     return surrogate
def log_errors(func, *args, **kargs):
    file_name = 'function_errors.txt'
    func_in = func(args, **kargs)
    file_log = open(file_name, mode='a+', encoding='utf-8')  # encoding='utf-8'
    line_log = str(func.__name__) + str(func_in) + 'str(Exception.__getattribute__)' + ' текст ошибки' + '\n'
    file_log.write(line_log)
    file_log.close()


# что-то я не то делаю... нужна подсказка

# Проверить работу на следующих функциях
@log_errors
def perky(param):
    return param / 0


@log_errors
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]
for line in lines:
    try:
        check_line(line)
    except Exception as exc:
        print(f'Invalid format:{line}, {exc}')

perky(param=42)

# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла
#
# @log_errors('function_errors.log')
# def func():
#     pass
