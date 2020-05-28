from time import sleep
from turtle import width

import simple_draw as sd

sd.resolution = [1200, 600]
background_color = (0, 8, 98)

radius = 200
radius_clean = radius + 1

color_clean = background_color

for _ in range(10):
    color = sd.random_color()
    point = sd.random_point()

    for x in range(radius - 1):

        if x <= 1:
            width = 1
        else:
            width = 2

        sd.circle(center_position=point, radius=radius - x, color=color, width=width)
        #sleep(.005)
        sd.circle(center_position=point, radius=radius_clean, color=color_clean, width=width)
        radius_clean -= 1

    new_radius = 1
    radius_clean = 1
    color = sd.invert_color(color)

    for x in range(radius):

        if x <= 1:
            width = 1
        else:
            width = 2

        sd.circle(center_position=point, radius=new_radius + x, color=color, width=width)
        #sleep(.005)
        sd.circle(center_position=point, radius=radius_clean, color=color_clean, width=width)
        radius_clean += 1

    sd.circle(center_position=point, radius=new_radius + x, color=color, width=width)

    color = sd.random_color()

    for x in range(radius):
        if x <= 1:
            width = 1
        else:
            width = 2

        sd.circle(center_position=point, radius=new_radius + x, color=color, width=width)
            # sleep(.005)
        sd.circle(center_position=point, radius=radius_clean, color=color_clean, width=width)
        radius_clean += 1

    sd.circle(center_position=point, radius=new_radius + x, color=color, width=width)




sd.pause()
