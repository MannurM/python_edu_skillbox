
import json
# import datetime
from decimal import *

from lesson_015.write_info import write_info

getcontext().prec = 10
remaining_time = '123456.0987654321'
# если изначально не писать число в виде строки - теряется точность!
field_names = ['current_location', 'current_experience', 'current_date', 'selected_action']


class Game:
    def __init__(self, current_choise, location, skill, time_left, location_index):
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
        self.location_index = location_index
        self.data_loc = {}

        self.state_parametr = {}

    def run_game(self, current_choise, location, skill, time_left, location_index):
        self.location = location
        self.skill = skill
        self.time_left = time_left
        self.current_choise = current_choise
        self.location_index = location_index
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
            'location_index': self.location_index,
        }

        # self.location_from_json, self.mob_from_json = \
        self.open_data(self.state_parametr['location'])
        # self.state_parametr['location_from_json'] = self.location_from_json
        # self.state_parametr['mob_from_json'] = self.mob_from_json

        print('___open_data')
        self.state_location(self.state_parametr)  # начальные параметры
        print('___начальные параметры')
        self.sum_loc = len(self.state_parametr['location_from_json'])
        if self.sum_loc >= 2:
            for x, val in enumerate(self.state_parametr['location_from_json']):
                self.state_parametr['location_from_json'][x] = val[1]
        else:
            self.state_parametr['location_from_json'] = self.state_parametr["location_from_json"][0][1]
        print('!!', self.state_parametr)
        print('___до цикла')
        while self.current_choise != '0':  # цикл выхода из игры по запросу пользователя
            while int(self.time_left) > 0 or self.skill < 280:  # цикл игры
                self.state_parametr['current_choise'] = self.change_act()
                self.state_parametr = self.act_in_location(self.state_parametr)
                print('1___')
                if self.state_parametr['current_choise'] == '2':
                    self.open_data(location=self.state_parametr['location'])
                    self.sum_loc = len(self.state_parametr['location_from_json'])
                    if self.sum_loc >= 2:
                        for x, val in enumerate(self.state_parametr['location_from_json']):
                            self.state_parametr['location_from_json'][x] = val[1]
                    else:
                        self.state_parametr['location_from_json'] = self.state_parametr["location_from_json"][0]
                print('!!', self.state_parametr)
                if self.current_choise == '0':
                    current_move = 3
                    write_info(current_move, self.location, self.skill, self.time_left)
                    break
                self.state_location(self.state_parametr)
                print('2___')
                current_move = self.current_choise
                write_info(current_move, self.location, self.skill, self.time_left)
                print('3___')
                if self.time_left <= 0:
                    current_move = 4
                    write_info(current_move, self.location, self.skill, self.time_left)
                    self.quit_game()
                print('4_____')  # обновление параметров
                self.state_parametr['current_choise'] = '10'
                print('4_____', self.state_parametr['current_choise'])
            if self.current_choise == '0':
                break
        current_move = 5
        write_info(current_move, self.location, self.skill, self.time_left)
        self.quit_game()

        print('___________________________________________')
        print('ИГРА закончилась!!!')
        print('___________________________________________')

    def open_data(self, location):
        print(location, ' change data - location!!!')
        self.data_loc_index = location
        self.mob_from_json = []
        self.location_from_json = []
        print('loc2')
        if self.data_loc_index == 'Location_0_tm0':
            self.data_loc = self.data_loc[self.data_loc_index]
        else:
            # print(self.data_loc_index, self.data_loc)
            self.data_loc = self.data_loc[self.state_parametr['location_index']][self.data_loc_index]
        index_loc = 0
        for index, value in enumerate(self.data_loc):
            # print(index, value, '- index, value')
            if isinstance(value, dict): #  нужен индекс от 1 для тьюплов - не зависящий от количества монстров
                index_loc += 1
                key_data = list(value.keys())
                data_tuple = (index_loc, key_data[0])
                self.location_from_json.append(data_tuple)
            else:
                data_mob = value
                self.mob_from_json.append(data_mob)
        # print(self.location_from_json)
        # print(self.mob_from_json)
        self.state_parametr['mob_from_json'] = self.mob_from_json
        self.state_parametr['location_from_json'] = self.location_from_json
        print('loc3', self.state_parametr['location_from_json'])
        return self.state_parametr

    def state_location(self, state_parametr):
        self.state_parametr = state_parametr
        self.location_index = int(self.state_parametr['location_index'])
        self.you_time = Decimal(remaining_time) - Decimal(self.state_parametr['time_left'])
        print('__________________________________________________________')
        print(f"Вы находитесь в локации {self.state_parametr['location']}, ",
              f"у Вас - {self.state_parametr['skill']} опыта",
              f' и осталось {self.you_time} секунд')
        if self.time_left != '0':
            print(f'прошло уже {self.state_parametr["time_left"]} секунд')
        print(f'Внутри в видите:',
              f' Входы в другие локации {self.state_parametr["location_from_json"]}, ',
              f' Монстров - {len(self.state_parametr["mob_from_json"])}')
        print(f'Выберите действие. Введите соответствующее число: \n'
              f'1.Атаковать монстра(ов) '
              f'2.Перейти в другую локацию '
              f'0.Сдаться и выйти из игры  \n'
              f' Выберите вариант действия? \n'
              f'   Введите число 0, 1 или 2:')

    def change_act(self):
        self.current_choise = input(':')
        while not self.current_choise.isdigit():
            print('Вы ввели  не число!')
            print('Введите число 0, 1 или 2')
            self.current_choise = input(':')
        while 2 < int(self.current_choise) < 0:
            print('Вы ввели неверное число!')
            print('Введите число 0, 1 или 2')
            self.current_choise = input(':')
        else:
            if self.current_choise == '1':
                print(f'Выбранo - атака монстров')
            if self.current_choise == '2':
                print(f'Выбрано -  смена локации')
            if self.current_choise == '0':
                print(f'Выбрано - завершение  игры')
        # print("state", 'current_choise -', self.current_choise, ', Location-', self.location, ', Skill-', self.skill,
        #       ', Time laps-', self.time_left,
        #       ', mob_json-', self.mob_from_json,
        #       ', loc_json-', self.location_from_json)
        return self.current_choise

    def act_in_location(self, state_parametr):
        self.state_parametr = state_parametr
        self.location = self.state_parametr['location']
        self.skill = self.state_parametr['skill']
        self.time_left = self.state_parametr['time_left']
        self.current_choise = self.state_parametr['current_choise']
        self.mob_from_json = self.state_parametr['mob_from_json']
        self.location_from_json = self.state_parametr['location_from_json']
        self.location_index = self.state_parametr['location_index']
        self.state_parametr['location_index'] = 10

        if self.current_choise == '1':
            mob_count = len(self.mob_from_json)
            if mob_count == '' or mob_count == 0:
                print('Монстры уже все уничтожены! Перейдите в другую локация или выходите из игры!')
                return self.state_parametr
            if mob_count > 1:
                while mob_count == 0:
                    print('Выберите монстра для Атаки')
                    number_mob = int(input(f'   Введите номер монстра, 1, 2, 3,  ...еts from {self.mob_from_json}'))
                    # уменьшить количество монстров
                    self.name_mob = self.mob_from_json[number_mob - 1]
                    self.name_mob, self.skill, self.time_left = self.attack_monstr(self.name_mob, self.skill,
                                                                                   self.time_left)
                    self.name_mob = '000'
                    mob_count -= 1
                    self.mob_from_json[number_mob - 1] = '!'
                    self.state_parametr['current_choise'] = self.current_choise
                    self.state_parametr['skill'] += self.skill
                    self.state_parametr['time_left'] += str(Decimal(self.state_parametr['time_left']) +
                                                            Decimal(self.time_left))
                    self.state_parametr['mob_from_json'] = 'destroed!'
                    # !!!
                    print(' Уничтожить еще монстра?')
                    choise_answer = int(input('Любой символ - да, 0 - нет :'))  # проверка ввода!
                    if choise_answer == 0:
                        return self.state_parametr

            else:
                self.name_mob = self.mob_from_json[0]
                self.name_mob, self.skill, self.time_left = \
                    self.attack_monstr(self.name_mob, self.skill, self.time_left)

                self.state_parametr['current_choise'] = self.current_choise
                self.state_parametr['skill'] += self.skill
                self.state_parametr['time_left'] += str(Decimal(self.state_parametr['time_left']) +
                                                        Decimal(self.time_left))
                self.state_parametr['mob_from_json'] = ''
                return self.state_parametr

        if self.current_choise == '2':

            self.location_sum = len(self.location_from_json)
            print('self.location_sum', self.location_sum)
            if self.location_sum > 1:

                print(f'Выберите локацию для перехода от 1 до {self.location_sum}')
                number_location = self.check_choise_location(self.location_sum)
                self.name_location = self.location_from_json[number_location - 1]
                self.location, self.skill, self.time_left, self.location_index = self.go_in_next_location(
                    self.name_location)
            else:
                self.name_location = self.location_from_json[0]
                self.location, self.skill, self.time_left, self.location_index = self.go_in_next_location(
                    self.name_location)
            self.state_parametr['current_choise'] = self.current_choise
            self.state_parametr['skill'] += self.skill
            self.state_parametr['time_left'] = str(Decimal(self.state_parametr['time_left']) + Decimal(self.time_left))
            self.state_parametr['mob_from_json'] = ''
            self.state_parametr['location'] = self.location
            self.state_parametr['location_index'] = self.location_index

            return self.state_parametr

        if self.current_choise == '0':
            return self.state_parametr

    def attack_monstr(self, name_mob, skill, time_left):
        self.skill = skill
        self.time_left = Decimal(time_left)
        self.name_mob = name_mob
        # self.skill_mob = ''
        # self.time_mob = ''
        # self.name_mob_short = ''

        self.name_mob_short, self.skill_mob, self.time_mob = self.name_mob.split('_', 3)
        # print('Разделение на 3', self.name_mob_short, self.skill_mob, self.time_mob)
        self.skill_mob = int(self.skill_mob[3:])
        self.time_mob = Decimal(self.time_mob[2:])
        print('_______________________')
        print(f'Монстр {self.name_mob} атакован! ')
        print(f'Монстр уничтожен! Получено опыта - {self.skill_mob}, потрачено времени - {self.time_mob} ')
        print('_______________________')
        self.time_left += self.time_mob
        self.skill += self.skill_mob
        return self.name_mob, self.skill, self.time_left

    def go_in_next_location(self, location):
        print('go_in_next_location', location)
        self.name_location = location
        self.time_location = ''
        self.location_short = ''
        self.location_digit = ''
        # print('self.name_location',self.name_location)
        self.location_short, self.location_index, self.time_location = self.name_location.split('_', 3)
        self.time_location = self.time_location[2:]
        print('_______________________')
        print(f'Вы перешли в локацию {self.name_location}! ')
        print(f' Получено опыта - {self.skill}, потрачено времени - {self.time_location} ')
        print('_______________________')
        self.time_left += self.time_location
        self.location = self.name_location
        # self.skill += self.skill
        self.location_index = int(self.location_index)
        # Распаковать Location_1_tm1040, изменить текущую локацию, прибавить время
        return self.location, self.skill, self.time_left, self.location_index

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
            self.location_index = 0
            self.run_game(self.current_choise, self.location, self.skill, self.time_left, self.location_index)


def open_json_file():
    with open("rpg.json", "r") as read_file:
        data = json.load(read_file)
    return data


if __name__ == '__main__':
    game = Game(current_choise=0, location=0, skill=0, time_left=0, location_index=0)
    game.run_game(current_choise='10', location='Location_0_tm0', skill=0, time_left='0', location_index=0)

