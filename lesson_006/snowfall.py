import simple_draw as sd


# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# снежинки хранить в глобальных переменных модуля snowfall

def snow_make(N):
    global snowflakes_x, snowflakes_y, factor_a_list, factor_b_list, step_random_x, step_random_y, length
    for i in range(N):
        x = sd.random_number(- length, 1200)
        snowflakes_x.append(x)

        factor_a_random = sd.random_number(3, 9) / 10
        factor_a_list.append(factor_a_random)

        factor_b_random = sd.random_number(1, 10) / 10
        factor_b_list.append(factor_b_random)

        step_x = sd.random_number(-10, 10)
        step_random_x.append(step_x)

        step_y = sd.random_number(5, 25)
        step_random_y.append(step_y)

        y = 750
        snowflakes_y.append(y)


def snow_draw_background():
    global snowflakes_x, snowflakes_y, factor_a_list, factor_b_list
    for i, x in enumerate(snowflakes_x):
        factor_a = factor_a_list[i]
        factor_b = factor_b_list[i]
        x = snowflakes_x[i]
        y = snowflakes_y[i]

        point = sd.get_point(x, y)

        sd.snowflake(center=point, length=length, color=sd.background_color, factor_a=factor_a, factor_b=factor_b)


def snow_shift():
    global snowflakes_x, snowflakes_y, step_random_x, step_random_y
    for i, x in enumerate(snowflakes_x):
        snowflakes_x[i] = snowflakes_x[i] + step_random_x[i]
        snowflakes_y[i] = snowflakes_y[i] - step_random_y[i]


def snow_draw_color():
    global snowflakes_x, snowflakes_y, factor_a_list, factor_b_list
    for i, x in enumerate(snowflakes_x):
        factor_a = factor_a_list[i]
        factor_b = factor_b_list[i]
        x = snowflakes_x[i]
        y = snowflakes_y[i]

        point = sd.get_point(x, y)

        sd.snowflake(center=point, length=length, color=sd.COLOR_WHITE, factor_a=factor_a, factor_b=factor_b)


def snow_create_new(step_drift):
    global snowflakes_x, snowflakes_y, snowflakes_index

    for i, x in enumerate(snowflakes_y):
        if snowflakes_y[i] <= step_drift:
            if i in snowflakes_index:
                # print('index_continue', i, snowflakes_index)
                continue
            else:
                snowflakes_index.append(i)
                # print('index', i, snowflakes_index, snowflakes_x[i], snowflakes_y[i])

    return snowflakes_index


def snow_del(snow_del_list):
    global snowflakes_index, snowflakes_x, snowflakes_y
    # Кроме этого - надо следить за тем, чтобы список индексов был отсортирован по убыванию
    # Чтобы удалять снежинки, начиная с конца

    snowflakes_index.sort(reverse=True)

    # snowflakes_y.sort(reverse=False)
    # print('Удаление')
    # print(snowflakes_index)
    for i, item in enumerate(snowflakes_index):  # Удаление по  одному  значению

        # print('i, x, y', i, snowflakes_x[item], snowflakes_y[item])

        snowflakes_x.pop(item)
        snowflakes_y.pop(item)

    print('Удалено!!!')
    snowflakes_index = []


length = 15
count = 0
step_count = 250

snowflakes_x = []
snowflakes_y = []
snowflakes_index = []
factor_a_list = []
factor_b_list = []
step_random_x = []
step_random_y = []
