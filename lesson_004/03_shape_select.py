# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

color_draw = 0
color_num = '3'
n_gon_in = 0
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

def n_gon(point, angle=0, length=50, n=3, width=3):
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


def color_number():
    print('Возможные цвета:')
    for number, color_name in colors.items():
        print(number, ':', colors[number]['color_name'])

    color_num = input('Введите желаемый номер цвета:')

    for number, color_name in colors.items():
        if color_num == number:
            color_num = number
            print(color_num)
            return color_num
    else:
        color_number()


def n_gon_input():
    for _ in range(100000):
        n_gon_in = input('Введите желаемое количество углов у фигуры от 3 до 8 включительно:')

        n_digit = n_gon_in
        if not n_digit.isdigit():
            print('вы ввели не число', n_gon_in, ',', 'попробуйте еще раз')
            continue

        if int(n_gon_in) <= 2 or int(n_gon_in) > 8:
            print('вы ввели некорректный номер', n_gon_in, ',', 'попробуйте еще раз')
            continue

        else:
            return n_gon_in


print('Рисуем заставку')
for x in range(150, 900, 300):
    for y in range(100, 600, 300):
        n = i

        n_gon(point=sd.get_point(x, y), angle=0, length=50, n=n, width=4)

        i += 1

print("Рисуем Вашу фигуру")

color_num = color_number()  # выбор цвета

for user_input, func in gon_choice.items():

    print('выберите фигуру - ', user_input, 'введите - ', gon_choice[user_input])

n_gon_in = int(n_gon_input())  # выбираем количество углов

# print('углы', n_gon_in)
# print('цвет', color_num)
x = 600
y = 200

sd.clear_screen()

n_gon(point=sd.get_point(x, y), angle=0, length=100, n=n_gon_in, width=5)

sd.pause()

