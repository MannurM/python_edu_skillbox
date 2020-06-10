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

    while not poly_gon_in in gon_choice:
        poly_gon_in = input('Введите номер фигуры от 3 до 8 включительно:')

        n_digit = poly_gon_in
        if not n_digit.isdigit():
            print('вы ввели не число', poly_gon_in, ',', 'попробуйте еще раз')
            continue

        if int(poly_gon_in) <= 2 or int(poly_gon_in) > 8:
            print('вы ввели некорректный номер', poly_gon_in, ',', 'попробуйте еще раз')
            continue

        else:
            return poly_gon_in


def poly_gon(start_point, start_angle, length=50, n=3, width=3, color=sd.COLOR_RED):
    color_vector_draw = color

    sd.resolution = 1200, 600

    # if n < 3:
    #     print('мало углов')
    #     return

    angle_step = 360 // n
    point_n = start_point
    vn = None

    for angle in range(0, 360 - angle_step, angle_step):
        vn = sd.get_vector(start_point=point_n, angle=start_angle + angle, length=length, width=3)
        vn.draw(color_vector_draw)

        point_n = vn.end_point

    sd.line(start_point=vn.end_point, end_point=start_point, width=3, color=color_vector_draw)

    return
    sd.pause()


color_vector_draw = 0
poly_gon_in = 0
n = 0
i = 3

gon_choice = {
    '3': {'gon_name': 'Треугольник', 'func': poly_gon},
    '4': {'gon_name': 'Квадрат', 'func': poly_gon},
    '5': {'gon_name': 'Пятиугольник', 'func': poly_gon},
    '6': {'gon_name': 'Шестиугольник', 'func': poly_gon},
    '7': {'gon_name': 'Семиугольник', 'func': poly_gon},
    '8': {'gon_name': 'Восьмиугольник', 'func': poly_gon},
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

        poly_gon(start_point=sd.get_point(x, y), start_angle=0, length=50, n=n, width=4, color=sd.COLOR_YELLOW)

        i += 1

print("Рисуем Вашу фигуру")
print('Выберите цвет по номеру')
for number, color_name in colors.items():
    print(number, ':', colors[number]['color_name'])

color_num = color_number()  # выбор цвета
print('Выберите фигуру:')
for user_input, name in gon_choice.items():
    print('    если хотите', gon_choice[user_input]['gon_name'], '- введите цифру -', user_input)

poly_gon_in = poly_gon_input()  # выбираем количество углов

x = 600
y = 200

sd.clear_screen()

func = gon_choice[poly_gon_in]['func']

func(start_point=sd.get_point(x, y), start_angle=0, length=100, n=int(poly_gon_in), width=5,
     color=colors[color_num]['sd_name'])

# poly_gon(start_point=sd.get_point(x, y), start_angle=0, length=100, n=n, width=5, color=colors[color_num]['sd_name'])
print('Готово!')
sd.pause()
