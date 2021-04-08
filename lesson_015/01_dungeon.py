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
import csv
import sys
import json
import datetime
from decimal import *
getcontext().prec = 10

remaining_time = '123456.0987654321'
# если изначально не писать число в виде строки - теряется точность!
field_names = ['current_location', 'current_experience', 'current_date', 'selected_action']
# Учитывая время и опыт, не забывайте о точности вычислений!


def act_in_location(current_choise, location, skill, time_left):
    if current_choise == 1:
        attack_monstr(skill, time_left)
    if current_choise == 2:
        go_in_next_location(location, skill, time_left)
    if current_choise == 3:
        quit_game()


def attack_monstr(skill, time_left):
    # Распаковать Mob_exp10_tm0, прибавить уровень и время
    pass


def go_in_next_location(location, skill, time_left):
    # Распаковать Location_1_tm1040, изменить текущую локацию, прибавить время
    pass


def quit_game():
    choise_game = input('Хотите сыграть еще 0 -  Нет, любой другой символ - Да :')
    if choise_game.isdigit() and choise_game == 0:
        print('ИГРА закончилась!!!')
        sys.exit()
    else:
        current_choise = 0
        location = 0
        skill = 0
        time_left = 0
        run_game(current_choise, location, skill, time_left)


def open_json_file():
    with open("rpg.json", "r") as read_file:
        data = json.load(read_file)
        # TODO не понимаю как извлечь следующий уровень из rpg.json??
        #  - вкладывать очередной цикл или можно как-то использовать рекурсию??
    if data:
        current_loc_key = list(data.keys())
        location_json = current_loc_key[0]
        print(location_json)
        current_loc_value = list(data.values())[0]
        print(current_loc_value)
        for val in range(len(current_loc_value)):
            if type(current_loc_value[val]) == dict:
                next_data = list(current_loc_value[val].keys())
                next_location = next_data[0]
                print(next_location)
            else:
                print(current_loc_value[val])
            print('')
    # TODO  а может использовать лучше генератор? и работает ли он с json.  и посоветуйте хороший мануал по json,
    #  если возможно. как то поиск гугла выдает однообразную информацию.

    # print(data["Location_0_tm0"][1]["Location_1_tm1040"][2]['Location_3_tm33000'][0]['Location_7_tm33300'][0]
    #       ['Location_10_tm55100'][4]['Location_12_tm0.0987654320'][1])


def state_location(location, skill, time_left):
    # состояние текущей позиции игры(в начале игры или после выполнения локации):
    # - текущая локация
    # - текущее количество опыта
    # - текущие дату и время (для этого используйте библиотеку datetime)
    you_time = float(remaining_time) - time_left
    current_location, next_location, mob_json = open_json_file()  # пока не работает!!!
    location = current_location
    print(f'Вы находитесь в локации {location}, у Вас {skill} опыта и осталось {you_time} секунд')
    if time_left != 0:
        print(f'прошло уже {time_left}')
    list_next_location = next_location
    list_current_mob = mob_json
    print(list_next_location, list_current_mob)
    print(f'Внутри в видите: \n'
          f' Входы в другие локации {list_next_location} \n'
          f' Монстров {list_current_mob}')

    print(f'Выберите действие. Введите соответствующее число: \n'
          f'1.Атаковать монстра '
          f'2.Перейти в другую локацию '
          f'3.Сдаться и выйти из игры '
          f' Выберите вариант действия??? ')
    current_choise = input(':')
    while not current_choise.isdigit() and 3 > int(current_choise) < 1:
        print('Вы ввели неверно!')
        print('Введите число от 1 до 3')
        current_choise = input(':')
    return current_choise, location, skill, time_left


def run_game(current_choise, location, skill, time_left):
    print('ИГРА начинается!!!')
    state_location(location, skill, time_left)
    while time_left > 0 or skill < 280:
        act_in_location(current_choise, location, skill, time_left)
        state_location(location, skill, time_left)
        write_info(current_choise, location, skill, time_left)
        if time_left <= 0:
            current_choise = 4
            write_info(current_choise, location, skill, time_left)
            quit_game()

    current_choise = 5
    write_info(current_choise, location, skill, time_left)
    quit_game()

    # запуск цикла программы, вызов выхода из программы,  вызов записывания результата


def write_info(current_choise, location, skill, time_left):
    choise_act = ''
    if current_choise == 1:
        choise_act = ' Выбрано - Атаковать монстра'
    if current_choise == 2:
        choise_act = ' Выбрано - Перейти в другую локацию'
    if current_choise == 3:
        choise_act = ' Выбрано - Сдаться и выйти из игры'
    if current_choise == 4:
        choise_act = ' Вы проиграли!!!'
    if current_choise == 5:
        choise_act = ' Вы победили!!!'

    file = 'dungeon.csv'
    write_data = [location, skill, time_left, choise_act]
    if not file:
        with open(file, 'a', newline='', encoding='cp-1251') as file_csv:
            writer = csv.writer(file_csv)
            writer.writerow(field_names)

    with open(file, 'a', newline='', encoding='cp-1251') as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow(write_data)

    # 'current_location', 'current_experience', 'current_date'
    # После успешного или неуспешного завершения игры вам необходимо записать
    # всю собранную информацию в csv файл dungeon.csv.


if __name__ == '__main__':
    run_game(current_choise=0, location=0, skill=0, time_left=0)
