import simple_draw as sd
def rainbow():
    import simple_draw as sd
    sd.resolution = (600, 600)
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

    x = -50
    y = -300
    for color in rainbow_colors:
        point = sd.get_point(x, y)
        radius = 1300
        width = 9
        sd.circle(center_position=point, radius=radius, color=color, width=width)
        y -= 10
        # x += 10
