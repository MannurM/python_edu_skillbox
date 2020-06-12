import simple_draw as sd

sd.resolution = (600, 600)


# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smiley(x, y):


    sd.resolution = (600, 600)

    point = sd.get_point(x, y)

    point_eye_1 = sd.get_point(x - 10, y + 3)

    point_eye_2 = sd.get_point(x + 10, y + 3)

    top_1 = sd.get_point(x - 12, y - 6)
    top_2 = sd.get_point(x - 8, y - 8)
    top_3 = sd.get_point(x + 8, y - 8)
    top_4 = sd.get_point(x + 12, y - 6)

    point_list = top_1, top_2, top_3, top_4

    sd.circle(center_position=point, radius=30, color=sd.COLOR_WHITE, width=1)

    sd.circle(center_position=point_eye_1, radius=3, color=sd.COLOR_DARK_RED, width=1)

    sd.circle(center_position=point_eye_2, radius=3, color=sd.COLOR_DARK_RED, width=1)

    sd.lines(point_list=point_list, color=sd.COLOR_GREEN, closed=False, width=1)


    # for _ in range(10):
    #     x = sd.randint(30, 570)
    #     y = sd.randint(30, 570)



