import simple_draw as sd


def wall(x, y):
    start_x = x
    start_y = y

    sd.resolution = (1200, 600)

    for row, y in enumerate(range(0, 200, 20)):
        x0 = 10 if row % 2 == 0 else 0
        for x in range(x0, 170, 20):
            left_bottom = sd.get_point(start_x + x, start_y + y)
            right_top = sd.get_point(start_x + x + 40, start_y + y + 20)
            sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_GREEN, width=1)

