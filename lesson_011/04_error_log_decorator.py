# -*- coding: utf-8 -*-

# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'


def log_errors(func):
    def surrogate(*args, **kwargs):
        try:
            func_in = func(*args, **kwargs)
        except Exception as exc:
            log_file_write(func=func, exc=exc, param_args=args, param_kwargs=kwargs)
            raise exc
        return func_in

    return surrogate


def log_file_write(func, exc, param_args=None, param_kwargs=None):  # file_name
    file_name = 'function_errors.log'
    func_name = str(func.__name__) + "    "
    func_param = str(param_args) + " " + str(param_kwargs) + "    "
    func_exc = str(exc) + "    "
    func_exc_text = str(exc.__doc__) + " "
    func_message = ''.join(func_name + func_param + func_exc + func_exc_text + '\n')
    with open(file_name, mode='a+', encoding='utf-8') as file_log:
        file_log.write(func_message)


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
        print(f'Invalid format: {exc}')

try:
    perky(param=42)
except Exception as exc:
    print(f'Invalid format: {exc}')

# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла
#
# @log_errors('function_errors.log')
# def func():
#     pass
#зачёт!