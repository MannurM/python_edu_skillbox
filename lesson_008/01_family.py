# -*- coding: utf-8 -*-

from random import randint

from termcolor import cprint


# Часть первая
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


class House:

    def __init__(self):
        self.food = 50
        self.dirt = 0
        self.money = 100
        self.cat_food = 50
        self.cat = None
        self.fur_coat_count = 0
        self.money_count = 0
        self.food_eat_count = 0
        # self.mort_count = 0
        # self.mort_count_grief = 0

    def act(self):
        self.dirt += 5

    def __str__(self):
        return 'В доме еды осталось {}, кошачей еды осталось {}, денег осталось {}, уровень грязи {}'.format(
            self.food, self.cat_food, self.money, self.dirt)

    def results(self):
        return 'у жены шуб - {} , денег за год заработано - {},{} - еды съедено'.format(
            self.fur_coat_count, self.money_count, self.food_eat_count)


class Family:
    def __init__(self):
        self.name = None
        self.husband = None
        self.wife = None
        self.children = None
        self.fullness = 0
        self.happiness_level = 0
        self.house = None
        self.eat_index = True
        self.life_index = True

    def act(self):
        if not self.happiness_level:
            print('{} умер от горя ...'.format(self.name))
            self.life_index = False
            return self.life_index
        elif not self.fullness:
            print('{} умер...'.format(self.name))
            self.life_index = False
            return self.life_index
        elif self.fullness <= 25:
            self.eat()
            return self.eat_index
        else:
            return True

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.house.food_eat_count += 10  # счетчик съеденной еды
            self.fullness += 10
            self.happiness_level += 5
            self.house.food -= 10
            self.eat_index = False
            return self.eat_index
        else:
            cprint('{} - нет еды'.format(self.name), color='red')
            self.happiness_level -= 10
            self.eat_index = True
            return self.eat_index

    def go_to_the_house(self, husband=None, house=None, wife=None, children=None):
        self.fullness -= 10
        self.happiness_level += 10
        self.house = house
        self.husband = husband
        self.wife = wife
        self.children = children
        cprint('{} въехал в дом'.format(self.name), color='cyan')

    def pet_cat(self):
        self.happiness_level += 5
        cprint('{} гладил кота'.format(self.name), color='cyan')

    def __str__(self):
        return '{} имеет: {} здоровья, {} счастья '.format(
            self.name, self.fullness, self.happiness_level)


class Husband(Family):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.fullness = 50
        self.happiness_level = 80
        self.house = None

    def __str__(self):
        return super().__str__()

    def act(self):
        if not super().act():
            return
        if self.eat_index:
            self.wife.shopping()  # Вообще это немного нарушает установленные правила (1 действие на человека в день)
            # но логика интересная можно пока оставить
            self.eat_index = False
            return
        dice = randint(1, 2)
        if self.house.dirt > 60:
            cprint("{} сказал:{}  - дома грязно!".format(self.name, self.wife.name), color='red')
            self.happiness_level -= 10
            self.wife.clean_house()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.gaming()
        else:
            self.eat()

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10
        self.happiness_level -= 10
        self.house.money_count += 150

    def gaming(self):
        cprint('{} играл  в WoT'.format(self.name), color='yellow')
        self.fullness -= 10
        self.happiness_level += 10


class Wife(Family):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.fullness = 50
        self.happiness_level = 80
        self.house = None

    def __str__(self):
        return super().__str__()

    def act(self):
        if not super().act():
            return

        if self.eat_index:
            self.shopping()
            self.eat_index = False
            return

        dice = randint(1, 5)
        if self.house.food <= 10:
            self.shopping()
        if self.house.cat_food >= 20:
            print('у кота есть еда! покупать не будем!')
        elif self.house.cat_food <= 10:
            self.shopping_food_cat()
            return
        if self.house.money <= 50:
            print('{}  - мало денег! {} дуй на работу'.format(self.name, self.husband.name))
            self.happiness_level -= 20
            self.fullness -= 5
            self.husband.work()

        if self.house.dirt > 70:
            self.clean_house()
        elif dice == 1:
            self.shopping()
        elif dice == 2:
            self.buy_fur_coat()
        elif dice == 3:
            self.clean_house()
        elif dice == 4:
            self.lying_on_couch()
        else:
            self.eat()

    def shopping(self):

        if self.house.money >= 50:
            cprint('{} сходила в магазин за едой'.format(self.name), color='cyan')
            self.happiness_level += 5
            self.fullness -= 10
            self.house.money -= 50
            self.house.food += 50

        else:
            cprint('{}  - деньги кончились!{} иди на работу! '.format(self.name, self.husband.name), color='red')
            self.happiness_level -= 10
            self.fullness -= 5
            self.husband.happiness_level -= 5
            self.husband.work()

    def buy_fur_coat(self):
        if self.house.money >= 450:
            cprint('{} Купила в магазине шубу!!!'.format(self.name), color='white')
            self.house.money -= 450
            self.happiness_level += 60
            self.fullness -= 10
            self.house.fur_coat_count += 1

        else:
            cprint('{} : - денег на шубу нет!{} иди на работу!'.format(self.name, self.husband.name), color='red')
            self.happiness_level -= 20
            self.fullness -= 5
            self.husband.happiness_level -= 25
            self.husband.work()
            self.fullness -= 10

    def clean_house(self):
        self.fullness -= 10
        self.happiness_level -= 15
        self.house.dirt = 0
        cprint('{} сделала уборку в доме'.format(self.name), color='cyan')

    def lying_on_couch(self):
        self.fullness -= 10
        self.happiness_level -= 5
        cprint('{} лежала на диване'.format(self.name), color='cyan')

    def shopping_food_cat(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за кошачей едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.cat_food += 50
            self.happiness_level += 5
            self.fullness -= 10
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')
            self.happiness_level -= 10
            self.fullness -= 5
            self.husband.happiness_level -= 5
            self.husband.work()


class Cat:

    def __init__(self, name_cat):
        self.name_cat = name_cat
        self.fullness = 10
        self.house = None
        self.wife = None
        self.husband = None

    def __str__(self):
        return '{} имеет: {} здоровье'.format(self.name_cat, self.fullness)

    def act(self):
        if self.fullness <= 0:
            cprint('{} сдох...'.format(self.name_cat), color='red')
            return
        dice = randint(1, 3)
        if self.fullness <= 20:
            self.eat_cat()
        elif dice == 1:
            self.sleep_cat()
        elif dice == 2:
            self.eat_cat()
        else:
            self.rips_off_Wallpaper()

    def eat_cat(self):
        if self.house.cat_food >= 10:
            cprint('{} поел'.format(self.name_cat), color='yellow')
            self.fullness += 20
            self.house.cat_food -= 10
        else:
            cprint('{} нет кошачей еды, МЯУУУ!!!'.format(self.name_cat), color='red')
            self.fullness -= 10

    def sleep_cat(self):
        cprint('{} спал весь день'.format(self.name_cat), color='yellow')
        self.fullness -= 10

    def rips_off_Wallpaper(self):
        cprint('{} драл обои целый день'.format(self.name_cat), color='yellow')
        self.fullness -= 10
        self.house.dirt += 5

    def find_cat(self, house, husband, wife):
        self.house = house
        self.wife = wife
        self.husband = husband
        self.fullness += 10
        cprint('Я кот {}, нашел себе хозяйку {}'.format(self.name_cat, self.wife.name), color='cyan')


class Child(Family):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.fullness = 50
        self.happiness_level = 90
        self.house = None

    def __str__(self):
        return super().__str__()

    def act(self):

        if not super().act():
            return

        if self.eat_index:
            self.wife.shopping()
            self.eat_index = False
            return

        dice = randint(1, 3)
        if dice == 1:
            self.eat()
        elif dice == 2:
            self.shit()
        else:
            self.sleep()

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.house.food_eat_count += 10  # счетчик съеденной еды
            self.fullness += 10
            self.wife.happiness_level += 10
            self.husband.happiness_level += 10
            self.house.food -= 10
            self.eat_index = False
            return self.eat_index
        else:
            cprint('{} - нет еды'.format(self.name), color='red')
            self.eat_index = True
            return self.eat_index

    def sleep(self):
        cprint('{} спал'.format(self.name), color='yellow')
        self.fullness -= 10
        self.wife.happiness_level += 10
        self.husband.happiness_level += 10

    def shit(self):
        cprint('{} покакал'.format(self.name), color='yellow')
        self.fullness -= 10
        self.house.dirt += 5
        self.wife.happiness_level += 10
        self.husband.happiness_level += 10


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
cat = Cat(name_cat='Барсик')
boris = Child(name='Борис')
family = [masha, serge, boris]

cprint('{} встретил {} и они сняли дом'.format(serge.name, masha.name), color='green')

serge.go_to_the_house(house=home, husband=None, wife=masha)
masha.go_to_the_house(house=home, husband=serge, wife=None)
boris.go_to_the_house(house=home, husband=serge, wife=masha, children=None)
cat.find_cat(house=home, husband=serge, wife=masha)
day_stop = False
for day in range(1, 366):
    cprint('================== День {} =================='.format(day), color='white')
    home.act()
    serge.act()
    masha.act()
    boris.act()
    cat.act()

    cprint(serge, color='green')
    cprint(masha, color='green')
    cprint(cat, color='green')
    cprint(boris, color='green')
    cprint(home, color='green')

    for name in family:
        if not name.life_index:
            day_stop = True
            break
    if day_stop:
        break

cprint('+++ИТОГИ+++', color='red')
cprint(home.results(), color='green')

#
# # TODO после реализации первой части - отдать на проверку учителю
#
# ######################################################## Часть вторая
# #
# # После подтверждения учителем первой части надо
# # отщепить ветку develop и в ней начать добавлять котов в модель семьи
# #
# # Кот может:
# #   есть,
# #   спать,
# #   драть обои
# #
# # Люди могут:
# #   гладить кота (растет степень счастья на 5 пунктов)
# #
# # В доме добавляется:
# #   еда для кота (в начале - 30)
# #
# # У кота есть имя и степень сытости (в начале - 30)
# # Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# # Еда для кота покупается за деньги: за 10 денег 10 еды.
# # Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# # Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
# #
# # Если кот дерет обои, то грязи становится больше на 5 пунктов
#
#
# class Cat:
#
#     def __init__(self):
#         pass
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#     def soil(self):
#         pass
#
#
# ######################################################## Часть вторая бис
# #
# # После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
# #
# # Ребенок может:
# #   есть,
# #   спать,
# #
# # отличия от взрослых - кушает максимум 10 единиц еды,
# # степень счастья  - не меняется, всегда ==100 ;)
#
# class Child:
#
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return super().__str__()
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#
# # TODO после реализации второй части - отдать на проверку учителем две ветки
#
#
# ######################################################## Часть третья
# #
# # после подтверждения учителем второй части (обоих веток)
# # влить в мастер все коммиты из ветки develop и разрешить все конфликты
# # отправить на проверку учителем.
#
#
# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')
#
# # Усложненное задание (делать по желанию)
# #
# # Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# # Коты должны выжить вместе с семьей!
# #
# # Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# # Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
# #
# # Дополнительно вносить некий хаос в жизнь семьи
# # - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# # - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# # Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
# #   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
# #
# # в итоге должен получится приблизительно такой код экспериментов
# # for food_incidents in range(6):
# #   for money_incidents in range(6):
# #       life = Simulation(money_incidents, food_incidents)
# #       for salary in range(50, 401, 50):
# #           max_cats = life.experiment(salary)
# #           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
#зачёт!