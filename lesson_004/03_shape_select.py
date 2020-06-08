# -*- coding: utf-8 -*-

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

def color_number():
    color_num = 9

    while not color_num in colors:
        color_num = input('Введите желаемый номер цвета:')

    return color_num


def poly_gon_input():
    poly_gon_in = 2

    while not poly_gon_in in gon_choice.values():
        poly_gon_in = input('Введите желаемое количество углов у фигуры от 3 до 8 включительно:')

        n_digit = poly_gon_in
        if not n_digit.isdigit():
            print('вы ввели не число', poly_gon_in, ',', 'попробуйте еще раз')
            continue

        if int(poly_gon_in) <= 2 or int(poly_gon_in) > 8:
            print('вы ввели некорректный номер', poly_gon_in, ',', 'попробуйте еще раз')
            continue

        else:
            return poly_gon_in


def poly_gon(point, angle=0, length=50, n=3, width=3):
    color_draw = colors[color_num]['sd_name']

    if n < 3:
        print('мало углов')
        return

    i = 0
    angle_n = 360 // n
    point_n = point

    sd.resolution = 1200, 600
    vn = None

    while i < n - 1:
        vn = sd.get_vector(start_point=point_n, angle=angle + angle_n * i, length=length)
        sd.line(start_point=point_n, end_point=vn.end_point, color=color_draw, width=width)

        point_n = vn.end_point
        i += 1

    sd.line(start_point=vn.end_point, end_point=point, color=color_draw, width=width)


color_draw = 0
poly_gon_in = 0
n = 0
i = 3

gon_choice = {
    'треугольник': '3',
    'квадрат': '4',
    'пятиугольник': '5',
    'гайка': '6',
    'семиугольник': '7',
    'восьмиугольник': '8',
}

colors = {
    '0': {'color_name': 'red', 'sd_name': sd.COLOR_RED},
    '1': {'color_name': 'orange', 'sd_name': sd.COLOR_ORANGE},
    '2': {'color_name': 'yellow', 'sd_name': sd.COLOR_YELLOW},
    '3': {'color_name': 'cyan', 'sd_name': sd.COLOR_CYAN},
    '4': {'color_name': 'blue', 'sd_name': sd.COLOR_BLUE},
    '5': {'color_name': 'purple', 'sd_name': sd.COLOR_PURPLE},
    '6': {'color_name': 'green', 'sd_name': sd.COLOR_GREEN},
}

print('Рисуем заставку')
for x in range(150, 900, 300):
    for y in range(100, 600, 300):
        n = i

        poly_gon(point=sd.get_point(x, y), angle=0, length=50, n=n, width=4)

        i += 1

print("Рисуем Вашу фигуру")

color_num = color_number()  # выбор цвета

for user_input, func in gon_choice.items():
    print('выберите фигуру - ', user_input, 'введите - ', gon_choice[user_input])

poly_gon_in = int(poly_gon_input())  # выбираем количество углов

x = 600
y = 200

sd.clear_screen()

poly_gon(point=sd.get_point(x, y), angle=0, length=100, n=poly_gon_in, width=5)

sd.pause()
