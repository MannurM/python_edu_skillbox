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

    # def can_fall(y):  TODO Этот метод должен оставаться тут
    #     return y <= 0


def get_flakes(N):  # Создание списка снежинок
    flakes = []
    for i in range(N):
        flake_x = sd.random_number(0, 600)
        flake_y = 650
        flake = Snowflake(flake_x, flake_y, length_flake=sd.random_number(5, 15))
        flakes.append(flake)
    return flakes


def append_flakes(count=None):
    for i in count:
        flake_x = sd.random_number(0, 600)
        flake_y = 650
        flake = Snowflake(flake_x, flake_y, length_flake=sd.random_number(5, 15))
        flakes.insert(i, flake)
    return flakes


def can_fall(y):  # TODO эта функция не нужна
    return y <= 0


def get_fallen_flakes(flakes):  # подсчет упавших снежинок
    fallen_flakes = []
    for index, value in enumerate(flakes):
        # if value.y <= 0:  TODO Тут надо было вызывать value.can_fall()
        # TODO Т.к. цикл идёт по списку снежинок, то в value как раз записывается снежинка из flakes

        #     fallen_flakes.append(index) # получить список индексов упавших снежинок
        #     print('подcчитать сколько снежинок уже упало', fallen_flakes)
        if can_fall(value.y):
            fallen_flakes.append(index)
    return fallen_flakes


def remove_flakes(fallen_flakes):
    print('индексы упавших снежинок', fallen_flakes)
    fallen_flakes.reverse()
    for index, value in enumerate(fallen_flakes):
        print('value', value)
        del flakes[value]
        # flakes.pop(value)
    print('Количество снежинок после удаление', len(flakes))


N = 50

fallen_flakes = []
flakes = get_flakes(N)

while True:
    sd.start_drawing()
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes(flakes)  # подчитать сколько снежинок уже упало
    count_fallen_flakes = len(fallen_flakes)
    if count_fallen_flakes > 0:
        remove_flakes(fallen_flakes)  # удалить упавшие снежинки
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
