# -*- coding: utf-8 -*-


# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# снежинки хранить в глобальных переменных модуля snowfall
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)
# while True:
#  нарисовать_снежинки_цветом(color=sd.background_color)
#  сдвинуть_снежинки()
#  нарисовать_снежинки_цветом(color)
#  если есть номера_достигших_низа_экрана() то
#       удалить_снежинки(номера)
#       создать_снежинки(count)
# sd.sleep(0.1)
# if sd.user_want_exit():
#     break


import simple_draw as sd
from snowfall import snow_make, snow_draw_background, snow_shift, snow_draw_color, snow_create_new, snow_del

sd.resolution = 1200, 600
N = 50
snow_make(N)

snow_del_count = 0
step_count = 250
step_drift = 15
length = 15

while True:

    sd.start_drawing()

    snow_draw_background()

    snow_shift()

    snow_draw_color()

    snow_del_list = snow_create_new(0)

    # вариант удаления через set
    # snow_del_list = set(snow_create_new(0))
    #
    # if len(snow_del_list) == N:
    #     sd.finish_drawing()
    #     snow_del(snow_del_list)
    #     break
    # print(snow_del_count)

    if snow_del_count > N:
        break
    sd.finish_drawing()

    if len(snow_del_list) >= N:
        snow_del_count += len(snow_del_list)
        snow_del(snow_del_list)

    sd.sleep(0.05)
    if sd.user_want_exit():
        break

sd.pause()
