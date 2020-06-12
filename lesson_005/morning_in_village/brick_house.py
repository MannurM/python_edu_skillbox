def brick_house(x, y):
    import simple_draw as sd

    sd.resolution = (1200, 600)

    start_point = sd.get_point(x, y)
    end_point = sd.get_point(x + 200, y + 200)
    color = sd.COLOR_DARK_YELLOW
    width = 0

    sd.rectangle(left_bottom=start_point, right_top=end_point, color=color, width=width)
    from morning_in_village.wall import wall
    wall(x, y)

    sd.rectangle(left_bottom=start_point, right_top=end_point, color=sd.COLOR_GREEN, width=1)

    start_point = sd.get_point(x + 50, y + 50)
    end_point = sd.get_point(x + 150, y + 150)
    color = sd.background_color
    width = 0

    sd.rectangle(left_bottom=start_point, right_top=end_point, color=color, width=width)

    from morning_in_village.smiley import smiley
    smiley(x+105, y+105)

    point_list = [sd.get_point(x-10, y + 200), sd.get_point(x + 105, y + 300), sd.get_point(x + 210, y + 200), ]
    sd.polygon(point_list=point_list, color=sd.COLOR_DARK_RED, width=1)
    sd.polygon(point_list=point_list, color=sd.COLOR_DARK_RED, width=0)


