import simple_draw as sd


def three(x=800, y=50):
    start_x = x
    start_y = y

    sd.resolution = 900, 700
    root_point = sd.get_point(start_x, start_y)

    sd.start_drawing()

    def draw_branches(start_point, angle=90, length=50, width=1):
        if length < 1:
            return

        brunch = sd.get_vector(start_point=start_point, angle=angle, length=length, width=1)
        brunch.draw(color=sd.COLOR_GREEN)

        random_angle = sd.random_number(10, 90) / 100 * 30
        random_length = sd.random_number(1, 20) / 100 * .5

        next_angle = angle + random_angle
        next_length_1 = length * (.75 - random_length)

        next_point_1 = brunch.end_point

        draw_branches(start_point=next_point_1, angle=next_angle, length=next_length_1, )

        random_angle = sd.random_number(1, 99) / 100 * 30  # увеличил разброс более 40 процентов
        random_length = sd.random_number(1, 20) / 100 * .5

        next_angle = angle - random_angle
        next_length_1 = length * (.75 - random_length)

        draw_branches(start_point=next_point_1, angle=next_angle, length=next_length_1, )

    draw_branches(start_point=root_point, angle=90, length=150)
    sd.finish_drawing()
