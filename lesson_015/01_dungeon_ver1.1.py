
import json
# import datetime
from decimal import *
from lesson_015.write_info import write_info

getcontext().prec = 13
remaining_time = '123456.0987654321'
# если изначально не писать число в виде строки - теряется точность!
field_names = ['current_location', 'current_experience', 'current_date', 'selected_action']


class Game:
    """ струкура класса
        run_game - основной цикл игры
        open_data - считывание данных из json файла
        state_location - фиксация действий на панели
        change_act - выбор номера деймствия в локации,  проверка номера
        act_in_location - действия в локации
        attack_monstr - атака монстров по одному
        go_in_next_location -  переход в другую локацию
        check_choise_location - проверка перехода в другую локацию
        """
    def __init__(self, current_choise, location, skill, time_left):
        self.location_index = 0
        self.number_mob = 0
        self.location = location
        self.skill = skill
        self.time_left = Decimal(time_left)
        self.current_choise = current_choise
        self.you_time = 0
        self.mob_from_json = []
        self.name_location = []
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
        self.data_loc = {}
        print('self.data_loc', self.data_loc)
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
        self.state_parametr = self.open_data(self.data_loc, self.state_parametr['location'],
                                             self.state_parametr['location_index'])
        self.state_location(self.state_parametr)  # начальные параметры

        while self.current_choise != '0':  # цикл выхода из игры по запросу пользователя
            while int(self.time_left) > 0 or self.skill < 280:  # цикл игры
                self.state_parametr['current_choise'] = self.change_act(self.state_parametr)
                self.state_parametr = self.act_in_location(self.state_parametr)
                self.state_parametr = self.condition_analysis(self.state_parametr)
                current_move = self.state_parametr['current_choise']
                if current_move == '4' or current_move == '5':
                    write_info(current_move, self.state_parametr)
                    self.state_parametr['current_choise'] = '0'
                    break   # return
                else:
                    self.state_location(self.state_parametr)
                    write_info(current_move, self.state_parametr)
            if self.state_parametr['current_choise'] == '0':
                break
        print('___________________________________________')
        print('ИГРА закончилась!!!')
        print('___________________________________________')

    def open_data(self, data_loc,  location, location_index):
        self.data_loc = data_loc
        self.location = location
        self.location_index = location_index
        self.mob_from_json = []
        self.location_from_json = []
        if self.location == 'Location_0_tm0':
            self.state_parametr['location_index'] = 0
            self.data_loc = self.data_loc[self.location]
        else:
            self.data_loc = self.data_loc[self.location_index][self.location]
        index_loc = 0
        for key, value in enumerate(self.data_loc):
            if isinstance(value, dict):
                index_loc += 1
                key_data = list(value.keys())
                data_tuple = (index_loc, key_data[0])
                self.location_from_json.append(data_tuple)
            else:
                data_mob = value
                self.mob_from_json.append(data_mob)
        self.state_parametr['mob_from_json'] = self.mob_from_json
        self.state_parametr['sum_mob'] = len(self.state_parametr['mob_from_json'])
        self.state_parametr['location_from_json'] = self.location_from_json
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
                    choise_answer = input('Любой символ - да, 0 - нет :')  # проверка ввода!
                    if int(choise_answer) == 0:
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
            if self.location_sum > 1:
                print(f'Имеются локации {self.location_from_json} \n')
                print(f'Выберите номер локации для перехода от 1 до {self.location_sum}')
                number_location = self.check_choise_location(self.location_sum)
                self.name_location = self.location_from_json[number_location - 1]
                self.state_parametr['location_index'] = number_location + self.state_parametr['sum_mob'] - 1
                self.go_in_next_location(self.name_location)
            elif self.location_sum == 1:
                self.name_location = self.location_from_json[0]
                self.state_parametr['location_index'] = self.state_parametr['sum_mob']
                self.go_in_next_location(self.name_location)
            else:
                print('локаций нет !')
                self.state_parametr['location'] = 'dead_end'

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
        self.time_left = Decimal(self.time_mob)
        self.skill = self.skill_mob
        return self.skill, self.time_left

    def go_in_next_location(self, location):
        self.name_location = location[1]
        self.time_location = ''
        self.location_short = ''
        self.location_digit = ''
        if self.name_location == 'Hatch_tm159.098765432':
            self.location_short,  self.time_location = self.name_location.split('_', 2)
        else:
            self.location_short, self.location_digit, self.time_location = self.name_location.split('_', 3)
        self.time_location = self.time_location[2:]
        print('_______________________')
        print(f'Вы перешли в локацию {self.name_location}! \n')
        print(f' Потрачено времени - {self.time_location} ')
        print('_______________________')
        self.state_parametr['time_left'] += Decimal(self.time_location)
        self.state_parametr['location'] = self.name_location
        return self.state_parametr

    def check_choise_location(self, location_sum):
        self.location_sum = location_sum
        number_location = input('   Введите номер локации!')
        while not number_location.isdigit():
            print('Вы ввели  не число!')
            print('Введите число 1 или 2')
            number_location = input(':')
        number_location = int(number_location)
        while number_location > self.location_sum or number_location < 1:
            print('Вы ввели неверное число!')
            print(f'Введите число от 1 до {self.location_sum}')
            number_location = input(':')
            number_location = int(number_location)
        return number_location

    def condition_analysis(self, state_parametr):
        self.state_parametr = state_parametr
        if self.state_parametr['time_left'] < 0:
            print('____________________________')
            print(f'Вы погибли в {self.state_parametr["location"]}, Вам не хватило времени!')
            print('____________________________')
        if self.state_parametr['current_choise'] == '2':
            self.open_data(self.data_loc, self.state_parametr['location'],
                           self.state_parametr['location_index'])
            if not self.state_parametr['location_from_json'] \
                    and not self.state_parametr['location'] == 'Hatch_tm159.098765432':
                print('____________________________')
                print(f'Это тупик - {self.state_parametr["location"]}, вы погибли от голода!')
                print('____________________________')
                self.state_parametr['current_choise'] = '4'
                return self.state_parametr
            if self.state_parametr['location'] == 'Hatch_tm159.098765432':
                print('____________________________')
                print('Игра закончилась, вы  победили!!!')
                print('____________________________')
                self.state_parametr['current_choise'] = '5'
        elif self.state_parametr['current_choise'] == '1':
            print(f'Монстров - {self.state_parametr["mob_from_json"]} ')
        elif self.state_parametr['current_choise'] == '0':
            print(f'ВЫходим!')
        return self.state_parametr


def open_json_file():
    with open("rpg.json", "r") as read_file:
        data = json.load(read_file)
    return data


if __name__ == '__main__':
    game = Game(current_choise=0, location=0, skill=0, time_left=0)
    print('Хотите сыграть в игру?')
    choise_game = input('Нажмите 0 -  Нет, любой другой символ - Да :')
    while choise_game != '0':
        game.run_game(current_choise='10', location='Location_0_tm0', skill=0, time_left='0')
        print('Хотите еще разок сыграть?')
        choise_game = input('Нажмите 0 -  Нет, любой другой символ - Да :')
    else:
        print('_______________________')
        print('Нет, тогда до свидания!')
