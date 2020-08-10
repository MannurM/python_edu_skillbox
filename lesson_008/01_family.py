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
        self.mort_count = 0
        self.mort_count_grief = 0

    def act(self):
        self.dirt += 5

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, уровень грязи {}'.format(
            self.food, self.money, self.dirt)

    def results(self):
        return print(
            'у жены шуб - {} , денег за год заработано - {},{} - еды съедено, умерло - {}, умерло от горя-{}'.format(
                self.fur_coat_count, self.money_count, self.food_eat_count, self.mort_count, self.mort_count_grief))


class Family:

    def __init__(self):
        self.name = None
        self.husband = None
        self.wife = None
        self.child = None
        self.fullness = 0
        self.happiness_level = 0
        self.house = None

    def act(self):

        if not self.happiness_level:
            print('{} умер от горя ...'.format(self.name))
            self.house.mort_count_grief += 1
            return False  # Если человек умер то нужно вернуть False
        elif not self.fullness:
            print('{} умер...'.format(self.name))
            self.house.mort_count += 1
            return False
        elif self.fullness <= 25:
            self.eat()
            return False
        else:
            return True  # если не умер, то True

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.house.food_eat_count += 10
            self.fullness += 10
            self.happiness_level += 5
            self.house.food -= 10
        else:
            cprint('{} - нет еды'.format(self.name), color='red')
            self.fullness -= 10
            self.happiness_level -= 10
            # можно ли здесь вызвать напрямую что-то типа 'self.wife.shopping' - для  покупки еды
            # т.е можно ли из родительского класса вызвать дочерний метод?
            # или запустить return  и в дочернем классе его обработать -  отправить жену за едой?
            # TODO Вызывать тут метод дочернего класса не стоит
            # TODO Но можно дополнить этот метод в дочернем классе
            # TODO т.е. можно тут вернуть False, если нет еды, а там поймать False и обработать (как с act-ом)

    def go_to_the_house(self, husband=None, house=None, wife=None):
        self.fullness -= 10
        self.happiness_level += 10
        self.house = house  # если атрибут используется в этом классе, то и создать его надо в init этого класса
        self.husband = husband
        self.wife = wife
        cprint('{} въехал в дом'.format(self.name), color='cyan')

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
            return  # False

        dice = randint(1, 2)
        if self.house.dirt > 60:
            cprint("{} сказал:{}  - дома грязно!".format(self.name, self.wife), color='red')
            self.happiness_level -= 10

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
            return  # False
        dice = randint(1, 5)
        if self.house.food <= 10:
            self.shopping()
        elif self.house.money <= 50:
            print('{}  - мало денег! {} дуй на работу'.format(self.name, self.husband.name))
            self.happiness_level -= 20
            self.husband.work()
        elif self.house.dirt > 90:
            self.clean_house()
        elif dice == 1:
            self.shopping()
        elif dice == 2:
            self.buy_fur_coat()
        elif dice == 3:
            self.clean_house()
        elif dice == 4:
            self.eat()
        else:
            self.lying_on_couch()

    def shopping(self):

        if self.house.money >= 50:
            cprint('{} сходила в магазин за едой'.format(self.name), color='cyan')
            self.happiness_level += 5
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{}  - деньги кончились!{} иди на работу! '.format(self.name, self.husband.name), color='red')
            self.happiness_level -= 10
            self.husband.happiness_level -= 5
            self.husband.work()

    def buy_fur_coat(self):
        if self.house.money >= 450:
            cprint('{} Купила в магазине шубу!!!'.format(self.name), color='white')
            self.house.money -= 450
            self.happiness_level += 60
            self.house.fur_coat_count += 1

        else:
            cprint('{} : - денег на шубу нет!{} иди на работу!'.format(self.name, self.husband.name), color='red')
            self.happiness_level -= 20
            self.husband.happiness_level -= 5
            self.husband.work()

    def clean_house(self):
        self.fullness -= 15
        self.happiness_level -= 15
        self.house.dirt = 0
        cprint('{} сделала уборку в доме'.format(self.name), color='cyan')

    def lying_on_couch(self):
        self.fullness -= 10
        self.happiness_level -= 5
        cprint('{} лежала на диване'.format(self.name), color='cyan')

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
family_name = Family()  # TODO Этот объект создавать не обязательно

cprint('{} встретил {} и они сняли дом'.format(serge.name, masha.name), color='green')

serge.go_to_the_house(house=home, husband=None, wife=masha)
masha.go_to_the_house(house=home, husband=serge, wife=None)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='white')
    home.act()
    masha.act()
    serge.act()
    # if not serge.act(): # можно ли сюда вернуть False и перебрать весь цикл или просто 'break'
    # TODO Можно людям просто добавить атрибут, который будет равен True пока они живы, а тут проверять
    # TODO Если у кого-то из жителей False вылезет - прервать цикл
    # TODO Только желательно не перебирать всех жителей вручную, а добавить объекты в список
    #     continue
    # elif not masha.act:
    #     continue

    cprint(serge, color='green')
    cprint(masha, color='green')
    cprint(home, color='green')

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
