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
    global n_list_x1, n_list_y1
    # print('n_list_y1', n_list_y1)
    for i, x in enumerate(n_list_x1):
        # print('enumerate', i, x)
        if n_list_y1[i] <= step_drift:
            n_list_y.append(n_list_y1[i])  # TODO Добавлять надо индексы, а не координаты
            # n_list_y1[i] = 650
            # n_list_x1[i] = sd.random_number(-4 * length, 1300)
            # print('n_list_y1_2', n_list_y1)
    # print('1', n_list_y)

    return n_list_y


def snow_del(snow_del_list):
    global n_list_y, n_list_x1, n_list_y1
    # Кроме этого - надо следить за тем, чтобы список индексов был отсортирован по убыванию
    # Чтобы удалять снежинки, начиная с конца
    n_list_y = snow_del_list  # TODO никак не пойму, что это за списки у вас n_list_y
    # TODO Хорошо бы над нэймингом поработать.
    # TODO 1) Чтобы названия списков отражали суть того, что хранят (n_list_x1 -можно заменить на-> snowflakes_x и тд)
    # TODO 2) Желательно не использовать list/dict/tuple в названиях(это не строгое правило, но желательно его
    # TODO придерживаться).
    # print(n_list_y)
    snow_del_list.sort(reverse=True)
    print('Удаление')
    del snow_del_list  # TODO Так вы удаляете список с индексами, а не элемент из другого списка
    # for i, x in enumerate(snow_del_list):# Удаление по  одному  значению
    # TODO Вариант с удалением по одному правильный
    # TODO Только надо удалять значения из всех списков, которые участвуют в рисовании снежинок
    #     del n_list_y[i]
    print('Удалено!!!')


# Здесь как раз надо заменить эту простенькую механику обновления.
# Не просто чтобы усложнить, а чтобы получить полный контроль за программой.
# Чтобы можно было настраивать изменения количества снежинок (добавлять/удалять)
# Ну и конечно это практика работы с изменениями данных в процессе работы.
# Тут например популярная ошибка отрабатывается - "удаление снежинок из списка по которому идёт цикл"
#  я не понял  -  порядок выполнения - можно в snow_create_new все  значения 'y' меньше допустим  нуля -  просто
#  удалить  - соотвественно   все снежинки просто постепенно удалятся -  так  нужно было?
# TODO Да, нужно удалить все снежинки ниже отметки. Но нельзя удалять элементы списка из списка, по которому идёт
# TODO текущий цикл. Удаляя текущий элемент вы сдвигаете список и на следующей итерации будет взят не следующий
# TODO за удаленным элемент, а следующий за ним
# TODO Пример: [a,b,c] - удаляем на первой итерации 'a' - остаётся [b,c] - на следующей итерации пайтон обращается
# TODO к элементу под индексом 1 - а это у нас 'c', в итоге 'b' просто пропускается мимо без обработки.

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
