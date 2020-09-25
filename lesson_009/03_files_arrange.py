# -*- coding: utf-8 -*-

import os
import time
import shutil


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

class SorteredFiles:

    def __init__(self):
        self.name_old_folder = None
        self.name_new_folder = None
        self.year_time_file = None
        self.mount_time_file = None
        self.new_path_file = None

    def __str__(self):
        pass

    def sorted_time_files(self, name_new_folder, name_old_folder):
        self.name_new_folder = name_new_folder
        self.name_old_folder = name_old_folder
        for dirpath, dirnames, filenames in os.walk(self.name_old_folder):
            for file in filenames:
                full_file_path = os.path.join(dirpath, file)
                secs = os.path.getmtime(full_file_path)
                file_time = time.gmtime(secs)

                # смотрим дату
                file_time_year = str(file_time.tm_year)
                file_time_mon = str(file_time.tm_mon)

                # формируем новый путь
                self.new_path_file = self.name_new_folder + '/' + file_time_year + '/' + file_time_mon

                # создаем путь
                os.makedirs(self.new_path_file, exist_ok=True)
                print(self.new_path_file)

                # переносим файл
                file_path = dirpath + '\\' + file
                shutil.copy2(file_path, self.new_path_file, follow_symlinks=False)

    def unpack_archive(self):
        pass


sort_files = SorteredFiles()
sort_files.sorted_time_files(name_old_folder='icons', name_new_folder='icons_by_year')

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
