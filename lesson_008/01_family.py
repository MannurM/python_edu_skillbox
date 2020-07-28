# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.

# У меня ошибку выдает  -  а где искать ответ не понятно.
#  Traceback (most recent call last):
#   File "C:/Users/User/PycharmProjects/python_base/lesson_008/01_family.py", line 258, in <module>
#     cprint(serge)
#   File "C:\Users\User\PycharmProjects\edu\venv\lib\site-packages\termcolor.py", line 124, in cprint
#     print((colored(text, color, on_color, attrs)), **kwargs)
#   File "C:\Users\User\PycharmProjects\edu\venv\lib\site-packages\termcolor.py", line 114, in colored
#     text += RESET
# TypeError: unsupported operand type(s) for +=: 'Husband' and 'str'
# TODO Поиск стоит начинать со строки на которую указывает пайтон -- cprint(serge)
# TODO Для ещё одной подсказки стоит попробовать использовать обычный print()
# TODO Тогда выдаётся более понятная ошибка TypeError: __str__ returned non-string (type NoneType)
# TODO метод __str__ который вызывается при попытки печати объекта возвращает нам не строку
# TODO идём смотреть...
class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt = 0
        self.cat_food = 50

    def __str__(self):
        return cprint('В доме еды осталось {}, денег осталось {}, уровень грязи {}'.format(
            self.food, self.money, self.dirt), color='green')
        # уровень счастья - жены, мужа, кота, ребенка -  показать в итогах
        #  кошачей еды осталось {}, self.cat_food,


class Husband:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.happiness_level = 100
        self.house = None
        self.cat = None
        self.wife = None

    def __str__(self):
        # TODO ...И правда. Метод вместо возврата строки пытается сам напечатать её
        # TODO Чтобы это исправить - отсюда надо убрать принт.
        # TODO Этот метод должен возвращать строку.
        # TODO Как и все, ему подобные в вашем коде
        return cprint('{} имеет: {} здоровья, {} счастья '.format(
            self.name, self.fullness, self.happiness_level), color='green')
        # super().__str__()

    def act(self):
        # TODO Попробуйте разделить действия на две части, общую для всех людей и частную для каждого
        # TODO Общие действия надо вынести в общий act
        # TODO Там проверки должны возвращать True/False
        # TODO В наследниках родительский act будет вызываться при помощи super
        # TODO И, если человек жив и не выполнил никаких действий
        #  (из super act() вернулось True), то можно сделать выбор из частных действий
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.money <= 50:
            self.work()
        elif self.house.dirt > 90:
            cprint("{} сказал:{}  - дома грязно!".format(self.name, self.wife.name), color='red')
            self.happiness_level -= 10
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.gaming()
    # TODO Метод eat тоже подходит для общего класса. Чтобы его не писать несколько раз - можно указать его там
    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.happiness_level += 10
            self.house.food -= 10
        else:
            cprint('{} - нет еды'.format(self.name), color='red')
            self.fullness -= 10
            self.happiness_level -= 10
            self.wife.chopping()

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10
        self.happiness_level -= 10

    def gaming(self):
        cprint('{} играл  в WoT'.format(self.name), color='yellow')
        self.fullness -= 10
        self.happiness_level += 10

    def go_to_the_house(self, house, wife=None):
        self.house = house
        self.fullness -= 10
        self.happiness_level += 10
        cprint('{} въехал в дом'.format(self.name), color='cyan')
        self.wife = wife


class Wife:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.happiness_level = 100
        self.child = None
        self.house = None
        self.cat = None
        self.husband = None

    def __str__(self):
        return cprint('{} имеет: {} здоровья, {} счастья'.format(
            self.name, self.fullness, self.happiness_level), color='green')
        # super().__str__()

    def act(self):
        if self.fullness <= 0:
            cprint('{} умерла...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        # elif self.house.cat_food <= 30:
        #     self.shopping_food_cat()
        elif self.house.money <= 50:
            cprint('{}  - нет денег! {} дуй на работу'.format(self.name, self.husband.name), color='red')
            self.happiness_level -= 10
            self.husband.work()
        elif self.house.dirt > 90:
            self.clean_house()
        elif dice == 1:
            self.shopping()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.clean_house()
        else:
            self.buy_fur_coat()

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поела'.format(self.name), color='yellow')
            self.fullness += 10
            self.happiness_level += 10
            self.house.food -= 10
        else:
            cprint('{} -  нет еды'.format(self.name), color='red')
            self.fullness -= 10
            self.happiness_level -= 10
            self.shopping()
            self.eat()

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходила в магазин за едой'.format(self.name), color='yellow')
            self.happiness_level += 10
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{}  - деньги кончились!{} иди на работу! '.format(self.name, self.husband.name), color='red')
            self.happiness_level -= 10
            self.husband.work()

    def buy_fur_coat(self):
        if self.house.money >= 450:
            cprint('{} Купила в магазине шубу!!!'.format(self.name), color='green')
            self.house.money -= 450
            self.happiness_level += 60
        else:
            cprint('{}  - денег на шубу нет!'.format(self.name), color='red')
            self.happiness_level -= 5

    def clean_house(self):
        self.fullness -= 20
        self.happiness_level += 10
        self.house.dirt = 0
        cprint('{} сделала уборку в доме'.format(self.name), color='yellow')

    def go_to_the_house(self, house, husband):
        self.house = house
        self.fullness -= 10
        self.happiness_level += 10
        cprint('{} въехала в дом'.format(self.name), color='cyan')
        self.husband = husband

    # def shopping_food_cat(self):
    #     if self.house.money >= 50:
    #         cprint('{} сходил в магазин за кошачей едой'.format(self.name), color='magenta')
    #         self.house.money -= 50
    #         self.house.cat_food += 50
    #     else:
    #         cprint('{} деньги кончились!'.format(self.name), color='red')
    #         self.work()

    # def make_child(self):
    #     pass

    # def find_cat(self, cat=None):
    #     self.cat = cat
    #     self.cat.house = self.house
    #     # self.cat_list.append(self.cat.name_cat)
    #     self.fullness -= 10
    #     cprint('{} нашел себе кота - его зовут {}'.format(self.name, self.cat), color='cyan')


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')

cprint('{} встретил {} и они сняли дом'.format(serge.name, masha.name), color='red')
masha.go_to_the_house(house=home, husband=serge.name)
serge.go_to_the_house(house=home, wife=masha.name)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='white')
    home.dirt += 5
    serge.act()
    masha.act()
    # cprint(serge, color='green')
    # cprint(masha, color='green')
    # cprint(home, color='green')
    cprint(serge)
    cprint(masha)
    cprint(home)


# TODO после реализации первой части - отдать на проверку учителю

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self):
        pass

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

    def soil(self):
        pass


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child:

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass


# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
murzik = Cat(name='Мурзик')

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
