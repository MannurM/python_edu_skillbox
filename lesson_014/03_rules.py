# -*- coding: utf-8 -*-

# Прибежал менеджер и сказал что нужно срочно изменить правила подсчета очков в игре.
# "Выходим на внешний рынок, а там правила игры другие!" - сказал он.
#
# Правила подсчета очков изменяются так:
#
# Если во фрейме страйк, сумма очков за этот фрейм будет равна количеству сбитых кеглей в этом фрейме (10 кеглей)
# плюс количество фактически сбитых кеглей за два следующих броска шара (в одном или двух фреймах,
# в зависимости от того, был ли страйк в следующем броске).
# Например: первый бросок шара после страйка - тоже страйк, то +10 (сбил 10 кеглей)
# и второй бросок шара - сбил 2 кегли (не страйк, не важно как закончится этот фрейм - считаем кегли) - то еще +2.
#
# Если во фрейме сбит спэр, то сумма очков будет равна количеству сбитых кеглей в этом фрейме (10 кеглей)
# плюс количество фактически сбитых кеглей за первый бросок шара в следующем фрейме.
#
# Если фрейм остался открытым, то сумма очков будет равна количеству сбитых кеглей в этом фрейме.
#
# Страйк и спэр в последнем фрейме - по 10 очков.
#
# То есть для игры «Х4/34» сумма очков равна 10+10 + 10+3 + 3+4 = 40,
# а для игры «ХXX347/21» - 10+20 + 10+13 + 10+7 + 3+4 + 10+2 + 3 = 92

# Необходимые изменения сделать во всех модулях. Тесты - дополнить.

# "И да, старые правила должны остаться! для внутреннего рынка..." - уточнил менеджер напоследок.

import argparse

from bowling import BadData, TenThrows

import bowling


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
                try:
                    res = res_one.run_game_eu(game_result=game_result)
                except (BadData, TenThrows) as exc:
                    print(f'Ошибка - {exc}')
                    res = 0
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


if __name__ == '__main__':
    file_input = 'tournament.txt'
    file_output = 'tournament_result_eu.txt'

    parser = create_parser()
    args = parser.parse_args('--file_input tournament.txt --file_output tournament_result_eu.txt'.split())
    open_file_tour(file_input=file_input, file_output=file_output)
