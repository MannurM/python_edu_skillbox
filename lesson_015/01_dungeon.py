# -*- coding: utf-8 -*-

# Подземелье было выкопано ящеро-подобными монстрами рядом с аномальной рекой, постоянно выходящей из берегов.
# Из-за этого подземелье регулярно затапливается, монстры выживают, но не герои, рискнувшие спуститься к ним в поисках
# приключений.
# Почуяв безнаказанность, ящеры начали совершать набеги на ближайшие деревни. На защиту всех деревень не хватило
# солдат и вас, как известного в этих краях героя, наняли для их спасения.
#
# Карта подземелья представляет собой json-файл под названием rpg.json. Каждая локация в лабиринте описывается объектом,
# в котором находится единственный ключ с названием, соответствующем формату "Location_<N>_tm<T>",
# где N - это номер локации (целое число), а T (вещественное число) - это время,
# которое необходимо для перехода в эту локацию. Например, если игрок заходит в локацию "Location_8_tm30000",
# то он тратит на это 30000 секунд.
# По данному ключу находится список, который содержит в себе строки с описанием монстров а также другие локации.
# Описание монстра представляет собой строку в формате "Mob_exp<K>_tm<M>", где K (целое число) - это количество опыта,
# которое получает игрок, уничтожив данного монстра, а M (вещественное число) - это время,
# которое потратит игрок для уничтожения данного монстра.
# Например, уничтожив монстра "Boss_exp10_tm20", игрок потратит 20 секунд и получит 10 единиц опыта.
# Гарантируется, что в начале пути будет две локации и один монстр
# (то есть в коренном json-объекте содержится список, содержащий два json-объекта, одного монстра и ничего больше).
#
# На прохождение игры игроку дается 123456.0987654321 секунд.
# Цель игры: за отведенное время найти выход ("Hatch")
#
# По мере прохождения вглубь подземелья, оно начинает затапливаться, поэтому
# в каждую локацию можно попасть только один раз,
# и выйти из нее нельзя (то есть двигаться можно только вперед).
#
# Чтобы открыть люк ("Hatch") и выбраться через него на поверхность, нужно иметь не менее 280 очков опыта.
# Если до открытия люка время заканчивается - герой задыхается и умирает, воскрешаясь перед входом в подземелье,
# готовый к следующей попытке (игра начинается заново).
#
# Гарантируется, что искомый путь только один, и будьте аккуратны в рассчетах!
# При неправильном использовании библиотеки decimal человек, играющий с вашим скриптом рискует никогда не найти путь.
#
# Также, при каждом ходе игрока ваш скрипт должен запоминать следущую информацию:
# - текущую локацию
# - текущее количество опыта
# - текущие дату и время (для этого используйте библиотеку datetime)
# После успешного или неуспешного завершения игры вам необходимо записать
# всю собранную информацию в csv файл dungeon.csv.
# Названия столбцов для csv файла: current_location, current_experience, current_date
#
#
# Пример взаимодействия с игроком:
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло времени: 00:00
#
# Внутри вы видите:
# — Вход в локацию: Location_1_tm1040
# — Вход в локацию: Location_2_tm123456
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали переход в локацию Location_2_tm1234567890
#
# Вы находитесь в Location_2_tm1234567890
# У вас 0 опыта и осталось 0.0987654321 секунд до наводнения
# Прошло времени: 20:00
#
# Внутри вы видите:
# — Монстра Mob_exp10_tm10
# — Вход в локацию: Location_3_tm55500
# — Вход в локацию: Location_4_tm66600
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали сражаться с монстром
#
# Вы находитесь в Location_2_tm0
# У вас 10 опыта и осталось -9.9012345679 секунд до наводнения
#
# Вы не успели открыть люк!!! НАВОДНЕНИЕ!!! Алярм!
#
# У вас темнеет в глазах... прощай, принцесса...
# Но что это?! Вы воскресли у входа в пещеру... Не зря матушка дала вам оберег :)
# Ну, на этот-то раз у вас все получится! Трепещите, монстры!
# Вы осторожно входите в пещеру... (текст умирания/воскрешения можно придумать свой ;)
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло уже 0:00:00
# Внутри вы видите:
#  ...
#  ...
#
# и так далее...
import json
# import datetime
from decimal import *

from lesson_015.write_info import write_info

getcontext().prec = 10
remaining_time = '123456.0987654321'
# если изначально не писать число в виде строки - теряется точность!
field_names = ['current_location', 'current_experience', 'current_date', 'selected_action']


# Учитывая время и опыт, не забывайте о точности вычислений!
# я бы советовал тут использовать классы и по ним сгруппировать функции для удобного взаимодействия

class Game:
    """ струкура класса
            run_game - основной цикл игры
            open_data - считывание данных из json файла
            state_location - фиксация действий на панели
            change_act - выбор номера деймствия в локации,  проверка номера
            act_in_location - действия в локации
            attack_monstr - атака монстров по одному
            go_in_next_location -  переход в другую локацию
            check_choise_location - проверка перехода в другую локацию/ не поключено.
            quit_game - выход из игры, обнуление параметров
            """

    def __init__(self, current_choise, location, skill, time_left):
        self.number_mob = 0
        self.location = location
        self.skill = skill
        self.time_left = Decimal(time_left)
        self.current_choise = current_choise
        self.you_time = 0
        self.mob_from_json = []
        self.name_mob = ''
        self.choise_game = 0
        self.location_from_json = []
        self.location_sum = 0
        self.data_loc = {}
        self.state_parametr = {}

    def run_game(self, current_choise, location, skill, time_left):
        self.location = location
        self.skill = skill
        self.time_left = time_left
        self.current_choise = current_choise
        self.sum_loc = 0

        print('____________________________________________________')
        print('ИГРА начинается!!!')
        print('____________________________________________________')
        if not self.data_loc:
            self.data_loc = open_json_file()
        self.state_parametr = {
            'current_choise': self.current_choise,
            'location': self.location,
            'skill': self.skill,
            'time_left': self.time_left,
            'mob_from_json': '',
            'location_from_json': '',
            'location_index': 0,
        }
        self.state_parametr = self.open_data(self.state_parametr['location'], self.state_parametr['location_index'])
        print('___open_data')
        self.state_location(self.state_parametr)  # начальные параметры
        print('___начальные параметры', self.state_parametr)
        while self.current_choise != '0':  # цикл выхода из игры по запросу пользователя
            while int(self.time_left) > 0 or self.skill < 280:  # цикл игры
                print('___цикл')
                self.state_parametr['current_choise'] = self.change_act(self.state_parametr)
                print('0,5_____')
                self.state_parametr = self.act_in_location(self.state_parametr)
                print('1___', self.state_parametr)

                if self.state_parametr['current_choise'] == '2':
                    self.open_data(self.state_parametr['location'], self.state_parametr['location_index'])
                    # self.sum_loc = len(self.state_parametr['location_from_json'])
                    # if self.sum_loc >= 2:
                    #     for x, val in enumerate(self.state_parametr['location_from_json']):
                    #         self.state_parametr['location_from_json'][x] = val[1]
                    # else:
                    #     self.state_parametr['location_from_json'] = self.state_parametr["location_from_json"][0]
                elif self.state_parametr['current_choise'] == '1':
                    print('проверка уничтожения монстра!!', self.state_parametr['mob_from_json'])
                elif self.state_parametr['current_choise'] == '0':
                    current_move = 3
                    write_info(current_move, self.state_parametr)
                    break
                self.state_location(self.state_parametr)
                print('2___')
                current_move = self.current_choise
                write_info(current_move, self.state_parametr)
                print('3___')
                if self.state_parametr['time_left'] < 0:
                    current_move = 4
                    write_info(current_move, self.state_parametr)
                    self.quit_game()
                    break
                print('4_____')  # обновление параметров

            if self.current_choise == '0':
                break
        current_move = 5
        write_info(current_move, self.state_parametr)
        self.quit_game()

        print('___________________________________________')
        print('ИГРА закончилась!!!')
        print('___________________________________________')

    def open_data(self, location, location_index):
        print('!___location =', self.state_parametr['location'], self.state_parametr['location_index'])
        self.location = location
        self.location_index = int(location_index)
        self.mob_from_json = []
        self.location_from_json = []
        if self.location == 'Location_0_tm0':
            self.state_parametr['location_index'] = 0
            self.data_loc = self.data_loc[self.location]
        else:
            print('____ state_parametr', self.state_parametr)
            print('!_________ self.data_loc \n', self.data_loc)
            self.data_loc = self.data_loc[self.location_index][self.location]
        print('loc2')
        index_loc = 0
        for index, value in enumerate(self.data_loc):
            if isinstance(value, dict):
                index_loc += 1
                key_data = list(value.keys())
                data_tuple = (index_loc, key_data[0])
                self.location_from_json.append(data_tuple)
            else:
                data_mob = value
                self.mob_from_json.append(data_mob)
        self.state_parametr['mob_from_json'] = self.mob_from_json
        sum = len(self.mob_from_json) + len(self.location_from_json)
        self.state_parametr['location_index'] = sum
        self.state_parametr['location_from_json'] = self.location_from_json
        print('loc3', self.state_parametr['location_from_json'])
        return self.state_parametr

    def state_location(self, state_parametr):
        self.state_parametr = state_parametr
        self.you_time = Decimal(remaining_time) - Decimal(self.state_parametr['time_left'])
        print('__________________________________________________________')
        print(f"Вы находитесь в локации {self.state_parametr['location']}, ",
              f"у Вас - {self.state_parametr['skill']} опыта",
              f' и осталось {self.you_time} секунд')
        if self.time_left != '0':
            print(f'прошло уже {self.state_parametr["time_left"]} секунд')

    def change_act(self, state_parametr):
        self.state_parametr = state_parametr
        print(f'Внутри локации {self.state_parametr["location"]} вы видите:',
              f' Входы в другие локации {self.state_parametr["location_from_json"]}, ',
              f' Монстров - {self.state_parametr["mob_from_json"]}')
        print(f'Выберите действие. Введите соответствующее число: \n'
              f'1.Атаковать монстра(ов) \n'
              f'2.Перейти в другую локацию \n'
              f'0.Сдаться и выйти из игры  \n'
              f' Выберите вариант действия? \n'
              f'   Введите число 0, 1 или 2:')
        self.current_choise = input(':')
        while not self.current_choise.isdigit():
            print('Вы ввели  не число!')
            print('Введите число 0, 1 или 2')
            self.current_choise = input(':')
        while (0 > int(self.current_choise)) or (int(self.current_choise) > 2):
            print('Вы ввели неверное число!')
            print('Введите число 0, 1 или 2')
            self.current_choise = input(':')
        else:
            if self.current_choise == '1':
                print(f'Выбранo - атака монстров!')
            if self.current_choise == '2':
                print(f'Выбрано -  смена локации!')
            if self.current_choise == '0':
                print(f'Выбрано - завершение  игры!')
        return self.current_choise

    def act_in_location(self, state_parametr):
        self.state_parametr['time_left'] = Decimal(self.state_parametr['time_left'])
        self.state_parametr = state_parametr
        self.location = self.state_parametr['location']
        self.skill = self.state_parametr['skill']
        self.time_left = self.state_parametr['time_left']
        self.current_choise = self.state_parametr['current_choise']
        self.mob_from_json = self.state_parametr['mob_from_json']
        self.location_from_json = self.state_parametr['location_from_json']

        if self.current_choise == '1':
            mob_count = len(self.mob_from_json)
            if self.mob_from_json == '0' or self.mob_from_json == []:
                print('Монстры уже все уничтожены! Перейдите в другую локация или выходите из игры!')
                return self.state_parametr
            if mob_count > 1:
                while mob_count != 0:
                    print('Выберите монстра для Атаки')
                    for number in range(len(self.mob_from_json)):
                        print(f'Введите номер {number + 1} --- для вызова на бой --- {self.mob_from_json[number]}')
                    number_mob = int(input(':'))
                    while self.mob_from_json[number_mob - 1] == '!':
                        print('монстр уже уничтожен,  выберите другого')
                        number_mob = int(input(':'))

                    self.name_mob = self.mob_from_json[number_mob - 1]
                    self.skill, self.time_left = self.attack_monstr(self.name_mob, self.skill, self.time_left)
                    self.name_mob = ''
                    mob_count -= 1
                    self.mob_from_json[number_mob - 1] = '!'
                    self.state_parametr['skill'] += self.skill
                    self.state_parametr['time_left'] += Decimal(self.time_left)
                    self.state_parametr['mob_from_json'] = '0'
                    if mob_count == 0:
                        break
                    print(' Уничтожить еще монстра?')
                    choise_answer = int(input('Любой символ - да, 0 - нет :'))  # проверка ввода!
                    if choise_answer == 0:
                        return self.state_parametr


            else:
                self.name_mob = self.mob_from_json[0]
                self.skill, self.time_left = self.attack_monstr(self.name_mob, self.skill, self.time_left)
                self.state_parametr['skill'] += self.skill
                self.state_parametr['time_left'] += Decimal(self.time_left)
                self.state_parametr['mob_from_json'] = '0'
            return self.state_parametr

        if self.current_choise == '2':
            self.location_sum = len(self.location_from_json)
            print('self.location_sum', self.location_sum)
            if self.location_sum > 1:
                print(f'Имеются локации {self.location_from_json} \n')
                print(f'Выберите номер локации для перехода от 1 до {self.location_sum}')
                number_location = self.check_choise_location(self.location_sum)
                self.name_location = self.location_from_json[number_location - 1]
                print('self.name_location', self.name_location)
                self.go_in_next_location(self.name_location)
            elif self.location_sum == 1:
                self.name_location = self.location_from_json[0]
                self.go_in_next_location(self.name_location)
            else:
                print('локаций нет ')
            return self.state_parametr
        if self.current_choise == '0':
            return self.state_parametr

    def attack_monstr(self, name_mob, skill, time_left):
        self.skill = skill
        self.time_left = Decimal(time_left)
        self.name_mob = name_mob
        self.name_mob_short, self.skill_mob, self.time_mob = self.name_mob.split('_', 3)
        self.skill_mob = int(self.skill_mob[3:])
        self.time_mob = self.time_mob[2:]
        print('_______________________')
        print(f'Монстр {self.name_mob} атакован! ')
        print(f'Монстр {self.name_mob_short} уничтожен! \n')
        print(f'Получено опыта - {self.skill_mob}, потрачено времени - {self.time_mob} ')
        print('_______________________')
        self.time_left += Decimal(self.time_mob)
        self.skill += self.skill_mob
        return self.skill, self.time_left

    def go_in_next_location(self, location):
        print('go_in_next_location', location)
        self.name_location = location[1]
        self.location_index = location[0]
        self.time_location = ''
        self.location_short = ''
        self.location_digit = ''
        self.location_short, self.location_digit, self.time_location = self.name_location.split('_', 3)
        self.time_location = self.time_location[2:]
        print('_______________________')
        print(f'Вы перешли в локацию {self.name_location}! \n')
        print(f' Потрачено времени - {self.time_location} ')
        print('_______________________')
        self.state_parametr['time_left'] += Decimal(self.time_location)
        self.state_parametr['location'] = self.name_location
        self.state_parametr['location_index'] = self.location_index
        return self.state_parametr

    def check_choise_location(self, location_sum):
        self.location_sum = location_sum
        number_location = input('   Введите номер локации!')
        while not number_location.isdigit():
            print('Вы ввели  не число!')
            print('Введите число 1 или 2')
            number_location = input(':')
        while self.location_sum < int(number_location) < 1:
            print('Вы ввели неверное число!')
            print(f'Введите число от 1 до {self.location_sum}')
            number_location = input(':')
        return int(number_location)

    def quit_game(self):
        self.choise_game = input('Хотите сыграть еще 0 -  Нет, любой другой символ - Да :')
        if self.choise_game != '0':
            self.current_choise = '0'
            self.location = "Location_0_tm0"
            self.skill = 0
            self.time_left = '0'
            self.run_game(self.current_choise, self.location, self.skill, self.time_left)
        else:
            print('выходим из игры')


def open_json_file():
    with open("rpg.json", "r") as read_file:
        data = json.load(read_file)
    return data


if __name__ == '__main__':
    game = Game(current_choise=0, location=0, skill=0, time_left=0)
    game.run_game(current_choise='10', location='Location_0_tm0', skill=0, time_left='0')