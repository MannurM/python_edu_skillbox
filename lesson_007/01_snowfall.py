# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку

# x, y = 0, 0
# flake = Snowflake(flake_x=100, flake_y=600, length_flake=sd.random_number(5, 15))
#
# while True:
#     for i in range(flake.step_y):
#         flake.clear_previous_picture()
#         flake.move()
#         print("Снежинка падает на шаге", i)
#         flake.draw()
#         sd.sleep(0.1)
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#
#     if sd.user_want_exit():
#         break
global count_fallen_flakes


class Snowflake:

    def __init__(self, flake_x, flake_y, length_flake):
        self.length = length_flake
        self.y = flake_y
        self.x = flake_x
        self.point = sd.get_point(x=self.x, y=self.y)
        self.color = sd.COLOR_WHITE
        self.factor_a = 0.6
        self.factor_b = 0.35
        self.factor_c = 60
        self.step_y = self.y // self.length + 1

    def clear_previous_picture(self):
        self.color = sd.background_color
        sd.snowflake(center=self.point, length=self.length, color=self.color, factor_a=self.factor_a,
                     factor_b=self.factor_b)

    def move(self):
        self.y -= self.length
        self.point = sd.get_point(x=self.x, y=self.y)

    def draw(self):
        self.color = sd.COLOR_WHITE
        sd.snowflake(center=self.point, length=self.length, color=self.color, factor_a=self.factor_a,
                     factor_b=self.factor_b)

    # def can_fall(self):  TODO Этот метод нужен и его можно за одну строчку выолнить, просто вернув
    #     if self.y > 0:  TODO условие, которое вы используете в if
    #         self.can_fall = True  TODO пример: return a > b
    #         print(self.can_fall)
    #     else:
    #         self.can_fall = False
    #         print('Снежинка упала!')
    #         print(self.can_fall)

    def get_fallen_flakes(self):  # TODO Этот метод должен быть функцией
        # TODO нужно получить на вход список, пройти по нему циклом и проверить есть ли там упавшие снежинки
        # TODO если есть - собрать их индексы в список и вернуть этот список
        if self.y <= 0:
            count_fallen_flakes += 1
        return count_fallen_flakes


def append_flakes(count):
    # TODO тут надо получить список и добавить в него снежинки
    get_flakes(count)


def get_flakes(N):
    flakes = []
    for i in range(N):
        flake_x = sd.random_number(0, 600)
        flake_y = 650
        flake = Snowflake(flake_x, flake_y, length_flake=sd.random_number(5, 15))
        flakes.append(flake)
    return flakes


def get_fallen_flakes():
    global count_fallen_flakes
    if flake.y <= 0:
        count_fallen_flakes += 1
        print('count_fallen_flakes', count_fallen_flakes)
        flake.y = 650
        flake.x = sd.random_number(0, 600)
    return count_fallen_flakes


N = 10
count_fallen_flakes = 0
falen_flakes = 0
flakes = get_flakes(N)
# get_fallen_flakes = 0

while True:
    sd.start_drawing()
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
        fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes > 0:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
