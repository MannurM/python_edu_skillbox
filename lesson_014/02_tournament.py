# -*- coding: utf-8 -*-

# Прибежал менеджер и сказал что нужно срочно просчитать протокол турнира по боулингу в файле tournament.txt
#
# Пример записи из лога турнира
#   ### Tour 1
#   Алексей	35612/----2/8-6/3/4/
#   Татьяна	62334/6/4/44X361/X
#   Давид	--8/--8/4/8/-224----
#   Павел	----15623113-95/7/26
#   Роман	7/428/--4-533/34811/
#   winner is .........
#
# Нужно сформировать выходной файл tournament_result.txt c записями вида
#   ### Tour 1
#   Алексей	35612/----2/8-6/3/4/    98
#   Татьяна	62334/6/4/44X361/X      131
#   Давид	--8/--8/4/8/-224----    68
#   Павел	----15623113-95/7/26    69
#   Роман	7/428/--4-533/34811/    94
#   winner is Татьяна

# Код обаботки файла расположить отдельном модуле, модуль bowling использовать для получения количества очков
# одного участника. Если захочется изменить содержимое модуля bowling - тесты должны помочь.
#
# Из текущего файла сделать консольный скрипт для формирования файла с результатами турнира.
# Параметры скрипта: --input <файл протокола турнира> и --output <файл результатов турнира>

import argparse
from datetime import datetime

import bowling

from collections import Counter
import os


def create_parser():
    parser = argparse.ArgumentParser(description='bowling_file')
    parser.add_argument('--file_input', type=str, required=True, help='file_data_bowling')
    parser.add_argument('--file_output', type=str, required=True, help='file_data_bowling')
    return parser


def open_file_tour(file_input, file_output):
    file_name = file_input
    file_output = file_output
    list_tour = []
    with open(file_name, mode='r', encoding='utf8') as file:
        for line in file:
            if line == '\n':
                continue
            line = line[:-1]
            if line[:3] == '###':
                tour_name = int(line[9:12])
                write_result_tour(file_output=file_output, tour_name=tour_name)
                continue
            if line[:9] != 'winner is':
                line_list_1 = line.split(sep='\t', maxsplit=1)
                name_gamer = line_list_1[0]
                game_result = line_list_1[1]
                res_one = bowling.Game(game_result=None)
                res = res_one.run_game(game_result=game_result)
                res_str = str(res)
                list_tour.append((res, name_gamer))
                write_result_tour(file_output=file_output, name_gamer=name_gamer, game_result=game_result, res=res_str)
            else:
                list_tour.sort(reverse=True)
                res_winner = str(list_tour[0][0])
                name_winner = list_tour[0][1]
                list_tour = []
                if res_winner == '0':
                    name_winner = 'Not win!'
                    write_result_tour(file_output=file_output, name_winner=name_winner, res_winner=res_winner)
                else:
                    write_result_tour(file_output=file_output, name_winner=name_winner, res_winner=res_winner)



            # if tour_name == tour_name:
            #     res_one = bowling.Game(game_result=None)
            #     res = res_one.run_game(game_result=game_result)
            #     res_str = str(res)
            #     list_tour.append((res, name_gamer))
            #     write_result_tour(file_output=file_output, name_gamer=name_gamer, game_result=game_result, res=res_str)
            # else:
            #     list_tour.sort(reverse=True)
            #     res_winner = list_tour[0][0]
            #     name_winner = list_tour[0][1]
            #     write_result_tour(file_output=file_output, name_winner=name_winner)
            #     write_result_tour(file_output=file_output, tour_name=tour_name)
            #     tour_name_old += 1
            #     # print(f'{tour_name_old} ТУР')
            #     res_winner=res_winner
            #     res_one = bowling.Game(game_result=None)
            #     res = res_one.run_game(game_result=game_result)
            #     res_str = str(res)
            #     list_tour.append((res, name_gamer))
            #     write_result_tour(file_output=file_output, name_gamer=name_gamer, game_result=game_result, res=res_str)


def write_result_tour(tour_name=None, name_gamer=None, game_result=None, res=None, name_winner=None,
                      file_output=None, res_winner=None):
    file_name = file_output
    with open(file_name, mode='a', encoding='utf8') as file:
        if tour_name:
            file.write('### Tour ' + str(tour_name) + '\n')
        if name_gamer:
            file.write(name_gamer + '\t')
        if game_result:
            file.write(game_result + '\t')
        if res:
            file.write(str(res) + '\n')
        if name_winner:
            # file.write('winner is ' + name_winner + ' ' + res_winner + '\n')
            file.write('winner is ' + name_winner + '\n')
            file.write('\n')


def printed_gamer_rating(file_name=None):
    name_gamer_list = []
    name_winner_list = []
    with open(file_name, mode='r', encoding='utf8') as file:
        for line in file:
            if line == '\n':
                continue
            line = line[:-1]
            if line[:3] == '###':
                continue
            if line[:9] == 'winner is':
                winner_name = line[10:]
                name_winner_list.append(winner_name)
                continue
            line_list_1 = line.split(sep='\t', maxsplit=2)
            name_gamer = line_list_1[0]
            name_gamer_list.append(name_gamer)

    dict_count_game = Counter(name_gamer_list)
    dict_count_winner = Counter(name_winner_list)
    dict_count_game['Not win!'] = 0
    # print(dict_count_game)
    print('+------------+-----------------+-------------+')
    print('|  Игрок     |  сыграно матчей | всего побед |')
    print('+------------+-----------------+-------------+')
    for name, value in dict_count_game.items():
        name_winner = name
        if name_winner in dict_count_winner.keys():
            value_win = dict_count_winner[name_winner]
        else:
            value_win = '000'

        len_name_symbol = len(name)
        len_bs = ' ' * (8 - int(len_name_symbol))
        len_count_symbol = len(str(value))
        len_bs_value = ' ' * (8 - int(len_count_symbol))
        len_win_symbol = len(str(value_win))
        len_bs_win = ' ' * (5 - int(len_win_symbol))
        print('| ', name, len_bs,  '|      ', value, len_bs_value, '|     ', value_win, len_bs_win, '|')
        print('+------------+-----------------+-------------+')


if __name__ == '__main__':
    file_input = 'tournament.txt'
    file_output = 'tournament_result.txt'

    parser = create_parser()
    args = parser.parse_args('--file_input tournament.txt --file_output tournament_result.txt'.split())
    open_file_tour(file_input=file_input, file_output=file_output)
    printed_gamer_rating(file_name=file_output)

# Ошибка в расчётах
# ### Tour 2
# Татьяна	42X--3/4/2-8271171/	113  здесь есть фрейм 82 - он должен вызывать ошибку (т.к. 8+2 больше 9)
# Роман	811/X--3/XX171/43	129
# Ринат	-263X815/5/27-----6	85
# Алексей	--8-X3/4/1/-12651X	108
# Павел	3-6/5/9/5---1/--5-52	80
# winner is Роман

# Усложненное задание (делать по желанию)
#
# После обработки протокола турнира вывести на консоль рейтинг игроков в виде таблицы:
#
# +----------+------------------+--------------+
# | Игрок    |  сыграно матчей  |  всего побед |
# +----------+------------------+--------------+
# | Татьяна  |        99        |      23      |
# ...
# | Алексей  |        20        |       5      |
# +----------+------------------+--------------+
