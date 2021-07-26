import argparse

from bowling import BadData, TenThrows

import bowling

from collections import Counter


def create_parser():
    parser = argparse.ArgumentParser(description='bowling_file')
    parser.add_argument('--file_input', type=str, required=True, help='file_data_bowling')
    parser.add_argument('--file_output', type=str, required=True, help='file_data_bowling')
    return parser


def open_file_tour(file_input, file_output, choise_rules):
    file_name = file_input
    file_output = file_output
    choise_rules = choise_rules
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
                    if choise_rules == '2':
                        res = res_one.run_game_eu(game_result=game_result)
                    else:
                        res = res_one.run_game(game_result=game_result)
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