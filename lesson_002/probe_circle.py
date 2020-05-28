from random import randint
from time import sleep

import simple_draw as sd
sd.resolution = [1200, 600]

left_bottom = sd.Point(0, 600)
right_top = sd.Point(1200, 0)
color = sd.COLOR_DARK_GREEN
sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=color, width=12)
count = 0
while count < 1000:
    point = sd.random_point()
    radius = randint(1, 20) * 10
    color = sd.random_color()
    sd.circle(center_position=point, radius=radius, color=color, width=int(radius - radius * 0.7))
    sleep(0.3)
    #
    count += 1

    sd.user_want_exit
sd.pause()