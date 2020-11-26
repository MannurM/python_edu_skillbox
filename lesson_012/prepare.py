import os


def file_to_path(folder_name):  # путь до файла
    file_in_folder = os.listdir(folder_name)
    path = os.getcwd() + '/' + folder_name
    for file in file_in_folder:
        file_path = path + '/' + file
        file_path = os.path.normpath(file_path)
        yield file_path
    return


def printed_rezult(dict_value, list_zero):
    volatility_max = []
    for i, v in dict_value.items():
        volatility_max.append(v)
    volatility_min = volatility_max
    #  вывод на консоль
    volatility_max.sort(reverse=True)

    print('Максимальная волатильность:')
    for i in range(3):
        key = get_value(dic=dict_value, value=volatility_max[i])
        print(key, volatility_max[i])

    volatility_min.sort()
    print('Минимальная волатильность:')
    for i in range(3):
        key = get_value(dic=dict_value, value=volatility_min[i])
        print(key, volatility_min[i])

    list_zero.sort()
    print('Нулевая волатильность:')
    print(list_zero)
    return


def get_value(dic, value):
    for key in dic:
        if dic[key] == value:
            return key
