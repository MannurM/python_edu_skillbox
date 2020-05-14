# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd
sd.resolution = (600, 600)
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
start_point_x = 50
start_point_y = 50
end_point_x = 350
end_point_y = 450

for color in rainbow_colors:
    start_point = sd.get_point(start_point_x, start_point_y)
    end_point = sd.get_point(end_point_x, end_point_y)

    color = color

    width = 4

    sd.line(start_point=start_point, end_point=end_point, color=color, width=width)

    start_point_x += 5
    end_point_x += 5
# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
x = 300
y = -50
for color in rainbow_colors:
    point = sd.get_point(x, y)
    radius = 600
    width = 9
    sd.circle(center_position=point, radius=radius, color=color, width=width)
    y -= 10
sd.pause()
