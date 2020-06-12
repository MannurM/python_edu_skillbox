def snow():
    N = 20  # количество снежинок 1200/N
    length = 5
    count = 0
    step_drift = length
    step_count = 250

    n_list_x1 = []
    n_list_y1 = []

    factor_a_list = []
    factor_b_list = []
    step_random_x = []
    step_random_y = []

    import simple_draw as sd
    sd.resolution = (1200, 600)

    central_position = sd.get_point(50, 500)
    sd.circle(center_position=central_position, radius=60, color=sd.COLOR_WHITE, width=0)
    central_position = sd.get_point(150, 500)
    sd.circle(center_position=central_position, radius=70, color=sd.COLOR_WHITE, width=0)
    central_position = sd.get_point(250, 500)
    sd.circle(center_position=central_position, radius=60, color=sd.COLOR_WHITE, width=0)
    central_position = sd.get_point(350, 500)
    sd.circle(center_position=central_position, radius=80, color=sd.COLOR_WHITE, width=0)

    for i in range(int(1200 / N)):
        x = sd.random_number(- length, 400)
        n_list_x1.append(x)

        factor_a_random = sd.random_number(3, 9) / 10
        factor_a_list.append(factor_a_random)

        factor_b_random = sd.random_number(1, 10) / 10
        factor_b_list.append(factor_b_random)

        step_x = sd.random_number(-10, 0)
        step_random_x.append(step_x)

        step_y = sd.random_number(5, 25)
        step_random_y.append(step_y)

        y = 500
        n_list_y1.append(y)

    while True:
        count += 1
        sd.start_drawing()

        central_position = sd.get_point(50, 500)
        sd.circle(center_position=central_position, radius=60, color=sd.COLOR_WHITE, width=0)
        central_position = sd.get_point(150, 500)
        sd.circle(center_position=central_position, radius=70, color=sd.COLOR_WHITE, width=0)
        central_position = sd.get_point(250, 500)
        sd.circle(center_position=central_position, radius=60, color=sd.COLOR_WHITE, width=0)
        central_position = sd.get_point(350, 500)
        sd.circle(center_position=central_position, radius=80, color=sd.COLOR_WHITE, width=0)

        for i, x in enumerate(n_list_x1):
            factor_a = factor_a_list[i]
            factor_b = factor_b_list[i]
            x = n_list_x1[i]
            y = n_list_y1[i]

            point = sd.get_point(x, y)

            sd.snowflake(center=point, length=length, color=sd.background_color, factor_a=factor_a, factor_b=factor_b)

            n_list_x1[i] = x = n_list_x1[i] + step_random_x[i]
            n_list_y1[i] = y = n_list_y1[i] - step_random_y[i]

            point = sd.get_point(x, y)

            sd.snowflake(center=point, length=length, color=sd.COLOR_WHITE, factor_a=factor_a, factor_b=factor_b)

            if count == step_count:
                step_drift += length
                step_count += 200

            if y <= step_drift:
                n_list_y1[i] = 500
                n_list_x1[i] = sd.random_number(- length, 400)

        sd.finish_drawing()
        sd.sleep(0.09)

        # if sd.user_want_exit():
        #     break
