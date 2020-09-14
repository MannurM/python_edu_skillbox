# -*- coding: utf-8 -*-

import os
import time


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени последней модификации файла
# (время создания файла берется по разному в разых ОС - см https://clck.ru/PBCAX - поэтому берем время модификации).
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником ОС в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит, см .gitignore в папке ДЗ)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

#   os.walk - генерация имен файлов в дереве каталога
#   os.path.dirname - возвращает имя директории
#   os.path.join - соединяет пути с учетом особенностей ОС
#   os.path.normpath - нормализует путь, убирая избыточные разделы
#   os.path.getmtime - время последнего изменения файла
#   time.gmtime - преобразует время
#   os.makedirs - создает директорию,  создавая промежуточные директории
#   shutil.copy2 - копирует содержимое файла + метаданные
# определить тип архива, распаковать архив в память? в папку?
# прочитать директорию с файлами, создать список имен файлов, отсортировать файлы по времени создания
# создать новую директорию - скопировать в неё файлы в отдельные папки за определенный месяц, год


# current_dir = pathlib.Path.cwd()
# home_dir = pathlib.Path.home()
#
# print(current_dir)
# print(home_dir)

class SorteredFiles:

    def __init__(self):
        self.name_old_folder = None
        self.name_new_folder = None
        self.year_time_file = None
        self.mount_time_file = None

    def __str__(self):
        pass

    def reader_files(self, name_old_folder):
        self.name_old_folder = name_old_folder
        for dirpath, dirnames, filenames in os.walk(self.name_old_folder):
            # print(dirpath, dirnames, filenames)
            for file in filenames:
                full_file_path = os.path.join(dirpath, file)
                secs = os.path.getmtime(full_file_path)
                file_time = time.gmtime(secs)
                print(full_file_path)
                print(file_time)
                print('')

    def sorted_time_files(self):
        for dirpath, dirnames, filenames in os.walk(self.name_old_folder):
            for file in filenames:
                full_file_path = os.path.join(dirpath, file)
                # print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
                file_list = os.listdir(dirpath)  # нужно указать все папки для просмотра
                full_list = [os.path.join(dirpath, file) for file in file_list]
                secs = os.path.getmtime(full_file_path)
                file_time = time.gmtime(secs)
                time_sorted_list = sorted(full_list, key=os.path.getmtime)
                # что-то как-то я криво сортирую), "толкните" в правильном направлении!
                # TODO Сортировать в целом не нужно, особенно внутри цикла
                # TODO Общий алгоритм примерно такой:
                # TODO Запускаем цикл по источнику - обращаемся к файлу - смотрим дату - формируем новый путь
                # TODO создаем этот путь (makedirs с параметром exist_ok=True поможет)
                # TODO далее в этот путь переносим этот файл
                # TODO И приступаем к следующему файлу
                print(time_sorted_list, file_time)
        print(time_sorted_list)

    def create_new_folder(self, name_new_folder):
        self.name_new_folder = name_new_folder
        self.year_time_file = os.path.getmtime
        self.mount_time_file = None

    def unpack_archive(self):
        pass


sort_files = SorteredFiles()
sort_files.reader_files(name_old_folder='icons')
sort_files.sorted_time_files()

# sort_files.create_new_folder(name_new_folder='icons_by_year')


# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
