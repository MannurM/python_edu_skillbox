# -*- coding: utf-8 -*-

# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта,
# если размеры равны - лист входит в конверт впритирку)
# Не забывайте, что лист бумаги можно перевернуть и попробовать вставить в конверт другой стороной.
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

envelop_x, envelop_y = 10, 7
paper_x, paper_y = 8, 9
# проверить для
paper_x, paper_y = 9, 8
if envelop_x >= paper_x or envelop_x >= paper_y:  # TODO Такие условия не подойдут.
    # TODO Они пропустят любой лист, если одна из его сторон подходит, т.е. лист размером 1, 10000 этот алгоритм
    # TODO пропустит, хотя должен отклонить.
    if envelop_y >= paper_x or envelop_y >= paper_y:
        print('Да')
    else:
        print('Нет')
paper_x, paper_y = 6, 8
if envelop_x >= paper_x or envelop_x >= paper_y:
    if envelop_y >= paper_x or envelop_y >= paper_y:
        print('Да')
    else:
        print('Нет')
paper_x, paper_y = 8, 6
if envelop_x >= paper_x or envelop_x >= paper_y:
    if envelop_y >= paper_x or envelop_y >= paper_y:
        print('Да')
    else:
        print('Нет')
paper_x, paper_y = 3, 4

if envelop_x >= paper_x:
    if envelop_x >= paper_y:
        if envelop_y >= paper_x:
            if envelop_y >= paper_y:
                print('Даaaaa')

else:
    print('Неееет')

paper_x, paper_y = 11, 9
if envelop_x >= paper_x or envelop_x >= paper_y:
    if envelop_y >= paper_x or envelop_y >= paper_y:
        print('Да')
    else:
        print('Нет')
paper_x, paper_y = 9, 11
if envelop_x >= paper_x or envelop_x >= paper_y:
    if envelop_y >= paper_x or envelop_y >= paper_y:
        print('Да')
    else:
        print('Нет')
# (просто раскоментировать нужную строку и проверить свой код)

print("закончились конверты")

# Усложненное задание, решать по желанию.
# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)

# hole_x, hole_y = 8, 9
# brick_x, brick_y, brick_z = 11, 10, 2
# brick_x, brick_y, brick_z = 11, 2, 10
# brick_x, brick_y, brick_z = 10, 11, 2
# brick_x, brick_y, brick_z = 10, 2, 11
# brick_x, brick_y, brick_z = 2, 10, 11
# brick_x, brick_y, brick_z = 2, 11, 10
# brick_x, brick_y, brick_z = 3, 5, 6
# brick_x, brick_y, brick_z = 3, 6, 5
# brick_x, brick_y, brick_z = 6, 3, 5
# brick_x, brick_y, brick_z = 6, 5, 3
# brick_x, brick_y, brick_z = 5, 6, 3
# brick_x, brick_y, brick_z = 5, 3, 6
# brick_x, brick_y, brick_z = 11, 3, 6
# brick_x, brick_y, brick_z = 11, 6, 3
# brick_x, brick_y, brick_z = 6, 11, 3
# brick_x, brick_y, brick_z = 6, 3, 11
# brick_x, brick_y, brick_z = 3, 6, 11
# brick_x, brick_y, brick_z = 3, 11, 6
# (просто раскоментировать нужную строку и проверить свой код)


# Усложненное задание, решать по желанию.
# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)

def brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z):
    hole = 0
    brick_1 = 0
    brick_2 = 0
    brick_3 = 0

    # hole = hole_x + hole_y
    # brick_1 = brick_x + brick_y
    # brick_2 = brick_x + brick_z
    # brick_3 = brick_y + brick_z
    #
    # if hole >= brick_1 and hole >= brick_2 and hole >= brick_3:
    #     print('Да')
    #
    # else:
    #     print('Нет')
    #
    # первоначально было так, потом сказали можно проще - без расчетов, теперь опять считать.
    # Да мне тоже эта лесенка не нравилась.
    # Можно и с минусами!!!
    # result1 = 0
    # result2 = 0
    # result3 = 0
    # result1 = hole - brick_1
    # result2 = hole - brick_2
    # result3 = hole - brick_3
    #
    # if result1 >= 0 and result2 >= 0 and result3 >= 0:
    #     print('Размеры', brick_x, brick_y, brick_z, 'Да')
    # else:
    #     print('Размеры', brick_x, brick_y, brick_z,'Нет')
    # мой вариант годится только для целых чисел


    # Вариант с площадями годится и для дробных значений размеров кирпича
    # а зачем 6 площадей? они же попарно равны
    hole = hole_x * hole_y
    brick_1 = brick_x * brick_y
    brick_2 = brick_x * brick_z
    brick_3 = brick_y * brick_z

    if hole >= brick_1 and hole >= brick_2 and hole >= brick_3:
        print('Да')

    else:
        print('Нет')
print('усложненный блок')

hole_x, hole_y = 8, 9


#тест
brick_x, brick_y, brick_z = 8.1, 8.1, 8.9
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
# не пролезет

brick_x, brick_y, brick_z = 8, 8, 9
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 9, 9, 0
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

# данные
brick_x, brick_y, brick_z = 11, 10, 2
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 11, 2, 10
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 10, 11, 2
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 10, 2, 11
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 2, 10, 11
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 2, 11, 10
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 3, 5, 6
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 3, 6, 5
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 6, 3, 5
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 6, 5, 3
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 5, 6, 3
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 5, 3, 6
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 11, 3, 6
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 11, 6, 3
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 6, 11, 3
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 6, 3, 11
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 3, 6, 11
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)

brick_x, brick_y, brick_z = 3, 11, 6
brick_in_hole(hole_x, hole_y, brick_x, brick_y, brick_z)
