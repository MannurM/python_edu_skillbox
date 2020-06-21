import simple_draw as sd


# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# снежинки хранить в глобальных переменных модуля snowfall

def snow_make(N):
    global n_list_x1, n_list_y1, factor_a_list, factor_b_list, step_random_x, step_random_y, length
    for i in range(N):
        x = sd.random_number(- length, 1200)
        n_list_x1.append(x)

        factor_a_random = sd.random_number(3, 9) / 10
        factor_a_list.append(factor_a_random)

        factor_b_random = sd.random_number(1, 10) / 10
        factor_b_list.append(factor_b_random)

        step_x = sd.random_number(-10, 10)
        step_random_x.append(step_x)

        step_y = sd.random_number(5, 25)
        step_random_y.append(step_y)

        y = 750
        n_list_y1.append(y)


def snow_draw_background():
    global n_list_x1, n_list_y1, factor_a_list, factor_b_list
    for i, x in enumerate(n_list_x1):
        factor_a = factor_a_list[i]
        factor_b = factor_b_list[i]
        x = n_list_x1[i]
        y = n_list_y1[i]

        point = sd.get_point(x, y)

        sd.snowflake(center=point, length=length, color=sd.background_color, factor_a=factor_a, factor_b=factor_b)


def snow_shift():
    global n_list_x1, n_list_y1, step_random_x, step_random_y
    for i, x in enumerate(n_list_x1):
        n_list_x1[i] = n_list_x1[i] + step_random_x[i]
        n_list_y1[i] = n_list_y1[i] - step_random_y[i]


def snow_draw_color():
    global n_list_x1, n_list_y1, factor_a_list, factor_b_list
    for i, x in enumerate(n_list_x1):
        factor_a = factor_a_list[i]
        factor_b = factor_b_list[i]
        x = n_list_x1[i]
        y = n_list_y1[i]

        point = sd.get_point(x, y)

        sd.snowflake(center=point, length=length, color=sd.COLOR_WHITE, factor_a=factor_a, factor_b=factor_b)


def snow_create_new(step_drift):
    global n_list_y, n_list_x1, n_list_y1, factor_a_list, factor_b_list, step_random_x, step_random_y, N, length, count, step_count
    # TODO Указывать нужно только те переменные, которые используются внутри этой функции
    for i, x in enumerate(n_list_x1):
        if n_list_y1[i] <= step_drift:
            n_list_y1[i] = 650
            n_list_x1[i] = sd.random_number(-4 * length, 1300)

        if n_list_y1[i] <= 0:
            n_list_y[i] = n_list_y1[i]
    return n_list_y


#  я не понял  смысл задания? ...номера_достигших_низа_экрана() - выдает список номеров снежинок,
# которые вышли за границу экрана
# удалить_снежинки(номера) - удаляет снежинки с номерами из списка...
# или так ---> нужно убрать сугроб, ---> потом сформировать список для удаления,
# снежинок вышедших за пределы экрана ---
# ---> удалить номера снежинок
# но в моей программе если снежинка достигает границы сугроба - она появляется сверху экрана иначе сугроба не будет
# ---> вообщем, я не понял)
# TODO Здесь как раз надо заменить эту простенькую механику обновления.
# TODO Не просто чтобы усложнить, а чтобы получить полный контроль за программой.
# TODO Чтобы можно было настраивать изменения количества снежинок (добавлять/удалять)
# TODO Ну и конечно это практика работы с изменениями данных в процессе работы.
# TODO Тут например популярная ошибка отрабатывается - "удаление снежинок из списка по которому идёт цикл"
def snow_del(snow_del_list):
    # TODO тут тоже нужен global
    # TODO Кроме этого - надо следить за тем, чтобы список индексов был отсортирован по убыванию
    # TODO Чтобы удалять снежинки, начиная с конца
    for i, x in enumerate(snow_del_list):
        if n_list_y1[i] == n_list_y[i]:  # TODO Не очень понимаю идею, зачем второй список создавать?
            del n_list_y1[i]


length = 15
count = 0
step_count = 250

n_list_x1 = []
n_list_y1 = []
n_list_y = []
factor_a_list = []
factor_b_list = []
step_random_x = []
step_random_y = []

# global n_list_x1, n_list_y1, factor_a_list, factor_b_list, step_random_x, step_random_y, N, length, count, step_count
