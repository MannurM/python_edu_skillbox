# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class Water:
    def __init__(self):
        self.name = 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        if isinstance(other, Terra):
            return Dirt()
        if isinstance(other, Fire):
            return Vapor()

    def __str__(self):
        return 'Вода'


class Fire:
    def __init__(self):
        self.name = 'Огонь'

    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning()
        if isinstance(other, Terra):
            return Lava()
        if isinstance(other, Water):
            return Vapor()

    def __str__(self):
        return 'Огонь'


class Terra:
    def __init__(self):
        self.name = 'Земля'

    def __add__(self, other):
        if isinstance(other, Air):
            return Dust()
        if isinstance(other, Water):
            return Dirt()
        if isinstance(other, Fire):
            return Lava()


    def __str__(self):
        return 'Земля'


class Air:
    def __init__(self):
        self.name = 'Воздух'

    def __add__(self, other):
        if isinstance(other, Terra):
            return Dust()
        if isinstance(other, Water):
            return Storm()
        if isinstance(other, Fire):
            return Lightning()


    def __str__(self):
        return 'Воздух'


class Storm:
    def __init__(self):
        self.name = 'Шторм'

    def __add__(self, other):
        pass

    def __str__(self):
        return 'Шторм'


class Vapor:  # ПАР
    def __init__(self):
        self.name = 'Пар'

    def __add__(self, other):
        pass

    def __str__(self):
        return 'Пар'


class Dirt:  # Грязь
    def __init__(self):
        self.name = 'Грязь'

    def __add__(self, other):
        pass

    def __str__(self):
        return 'Грязь'


class Lightning:  # Молния
    def __init__(self):
        self.name = 'Молния'

    def __add__(self, other):
        pass

    def __str__(self):
        return 'Молния'


class Dust:  # Пыль
    def __init__(self):
        self.name = 'Пыль'

    def __add__(self, other):
        pass

    def __str__(self):
        return 'Пыль'


class Lava:
    def __init__(self):
        self.name = 'Лава'

    def __add__(self, other):
        pass

    def __str__(self):
        return 'Лава'


print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Fire(), '=', Water() + Fire())
print(Water(), '+', Terra(), '=', Water() + Terra())

print(Fire(), '+', Air(), '=', Fire() + Air())
print(Fire(), '+', Terra(), '=', Fire() + Terra())
print(Fire(), '+', Water(), '=', Fire() + Water())

print(Air(), '+', Fire(), '=', Air() + Fire())
print(Air(), '+', Terra(), '=', Air() + Terra())
print(Air(), '+', Water(), '=', Air() + Water())




# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
