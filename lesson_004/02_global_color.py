# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


color_draw = 0
color_num = 0
# TODO В этом случае удобнее создать словарь следующей структуры
# TODO словарь = {'0': {'color_name': 'red', 'sd_name': sd.COLOR_RED},...}
# TODO Таким образом для каждого цвета у нас будет свой словарь. И у каждого словаря будут одинаковые ключи
# TODO 'color_name' и 'sd_name'
# TODO Тогда можно будет легко проверить ввод (user_input in словарь)
# TODO А если среди ключей есть выбор пользователя - по этому ключу мы получим нужный вложенный словарь
# TODO А там все ключи одинаковые, можем получить как название цвета, так и sd_цвет
colors = {
    0: sd.COLOR_RED,
    1: sd.COLOR_ORANGE,
    2: sd.COLOR_YELLOW,
    3: sd.COLOR_GREEN,
    4: sd.COLOR_CYAN,
    5: sd.COLOR_BLUE,
    6: sd.COLOR_PURPLE,
}


# TODO Подобный тип кода(создание функций - def), который создает какой-то инструмент для дальнейшего использования
# TODO Но сам по себе ничего не делает - надо располагать в начале, а "исполняемый" код
# TODO В частности вызов функций и создание точек - после этого "подготовительного" кода)
def n_gon(point, angle=0, length=50, n=3, width=3):
    color_draw = colors.get(int(color_num))

    sd.resolution = 1200, 600

    if n < 3:
        print('мало углов')
        return
    i = 0
    angle_n = 180 - (n - 2) * 180 / n
    point_n = point

    while i < n - 1:
        vn = sd.get_vector(start_point=point_n, angle=angle + angle_n * i, length=length)
        sd.line(start_point=point_n, end_point=vn.end_point, color=color_draw, width=width)

        point_n = vn.end_point
        i += 1

    sd.line(start_point=vn.end_point, end_point=point, color=color_draw, width=width)

    sd.pause()


def color_number():
    color_num = input('Введите желаемый номер цвета:')

    color_digit = color_num

    if not color_digit.isdigit():
        print('вы ввели не число, попробуйте еще раз')
        color_num = 0
        color_number()

    if 0 < int(color_num) > 6:
        print('вы ввели некорректный номер, попробуйте еще раз')
        color_number()

    else:
        return color_num


print('Возможные цвета:')
print('0: red')
print('1: orange')
print('2: yellow')
print('3: green')
print('4: cyan')
print('5: blue')
print('6: purple')

color_num = color_number()

point = sd.get_point(600, 250)

n_gon(point, angle=0, length=50, n=12, width=4)
# работает до n = 25, при длине вектора length < 50 дальше накапливается ошибка в углах поворота вектора
