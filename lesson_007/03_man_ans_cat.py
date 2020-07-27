# -*- coding: utf-8 -*-

import random
from random import randint
# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.
from termcolor import cprint


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py
# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.
# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)
# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня
# Человеку и коту надо вместе прожить 365 дней.


class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.cat = None
        self.cat_list = []

    def __str__(self):
        return 'Я - {}, сытость {}'.format(self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='white')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')
            self.fullness -= 10
            self.shopping()
            self.eat()

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')
            self.work()

    def shopping_food_cat(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за кошачей едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.cat_food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')
            self.work()

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} въехал в дом'.format(self.name), color='cyan')

    def find_cat(self, cat=None):
        self.cat = cat
        self.cat.house = self.house
        self.cat_list.append(self.cat.name_cat)
        self.fullness -= 10
        cprint('{} нашел себе кота - его зовут {}'.format(self.name, self.cat), color='cyan')

    def cleaning(self):
        self.fullness -= 20
        self.house.dirt = 0
        cprint('{} сделал уборку в доме'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness <= 20:  # если сытость '<20', то люди мрут после уборки
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.cat_food <= 30:
            self.shopping_food_cat()
        elif self.house.money < 50:
            self.work()
        elif self.house.dirt > 100:
            self.cleaning()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class Cat:
    def __init__(self, name_cat):
        self.name_cat = name_cat
        self.fullness = 10
        self.house = None

    def __str__(self):
        return '{}'.format(self.name_cat)

    def eat_cat(self):
        if self.house.cat_food >= 10:
            cprint('{} поел'.format(citisen.cat), color='yellow')
            self.fullness += 20
            self.house.cat_food -= 10
        else:
            cprint('{} нет кошачей еды, МЯУУУ!!!'.format(citisen.cat), color='red')
            self.fullness -= 10

    def sleep_cat(self):
        cprint('{} спал весь день'.format(citisen.cat), color='yellow')
        self.fullness -= 10

    def rips_off_Wallpaper(self):
        cprint('{} драл обои целый день'.format(citisen.cat), color='yellow')
        self.fullness -= 10
        self.house.dirt += 5

    def act_cat(self):
        if self.fullness <= 0:
            cprint('{} сдох...'.format(citisen.cat), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat_cat()
        elif dice == 1:
            self.sleep_cat()
        elif dice == 2:
            self.eat_cat()
        else:
            self.rips_off_Wallpaper()


class House:
    def __init__(self):
        self.food = 50
        self.money = 0
        self.dirt = 0
        self.cat_food = 50

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, кошачей еды осталось {}, уровень грязи {}'.format(
            self.food, self.money, self.cat_food, self.dirt)


citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    Man(name='Кенни'),
]
# Список котов
cats = [
    Cat(name_cat='Том'),
    Cat(name_cat='Мурзик'),
    Cat(name_cat='Рыжий'),
    Cat(name_cat='Матроскин'),
    Cat(name_cat='Багира'),
    Cat(name_cat='Гав'),
    Cat(name_cat='Вася'),
    Cat(name_cat='Борис'),
    Cat(name_cat='Феликс'),
]

my_sweet_home = House()
for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)
    # въезд животных
    if citisen.cat is None:
        print('Нужен кот')
        cat_random = random.choice(cats)
        citisen.find_cat(cat=cat_random)

for day in range(1, 366):
    print('================ день {} =================='.format(day))

    for citisen in citizens:
        citisen.act()
        citisen.cat.act_cat()  # действия кота?
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    for citisen in citizens:
        print('Я кот {}, моя сытость {}'.format(citisen.cat, citisen.cat.fullness))
    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
#зачёт!