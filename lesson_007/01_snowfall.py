# -*- coding: utf-8 -*-

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self):
        self.length = 15
        self.y = 600
        self.point = sd.get_point(x=100, y=self.y)
        self.color = sd.COLOR_WHITE
        self.factor_a = 0.6
        self.factor_b = 0.35
        self.factor_c = 60
        self.step_y = self.y // self.length

    def clear_previous_picture(self):
        self.color = sd.background_color
        sd.snowflake(center=self.point, length=self.length, color=self.color, factor_a=self.factor_a,
                     factor_b=self.factor_b)

    def move(self):
        self.y -= self.length
        self.point = sd.get_point(x=100, y=self.y)

    def draw(self):
        self.color = sd.COLOR_WHITE
        sd.snowflake(center=self.point, length=self.length, color=self.color, factor_a=self.factor_a,
                     factor_b=self.factor_b)

    def can_fall(self):
        pass
    # TODO Только для чего здесь can_fall -  что он должен делать?

x, y = 0, 0
flake = Snowflake()

while True:
    for i in range(flake.step_y):
        flake.clear_previous_picture()
        flake.move()
        print("падаю на шаг", i)
        flake.draw()
        sd.sleep(0.1)
    if not flake.can_fall():
        break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

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

sd.pause()
