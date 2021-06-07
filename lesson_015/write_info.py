import csv
import datetime
field_names = ['time_write', 'current_location', 'current_experience', 'current_date', 'selected_action']


def write_info(current_move, state_parametr):
    choise_act = ''
    if current_move == '1':
        choise_act = ' Выбрано - Атаковать монстра'
    if current_move == '2':
        choise_act = ' Выбрано - Перейти в другую локацию'
    if current_move == '0':
        choise_act = ' Выбрано - Сдаться и выйти из игры'
    if current_move == '4':
        choise_act = ' Вы проиграли!!!'
    if current_move == '5':
        choise_act = ' Вы победили!!!'
    time_write = datetime.datetime.now()
    location = state_parametr['location']
    skill = state_parametr['skill']
    time_left = state_parametr['time_left']

    file = 'dungeon.csv'
    write_data = [time_write, location, skill, time_left, choise_act]
    # проверить на существование, проверить на наличие данных
    if file:
        with open(file, 'a', newline='', encoding='cp1251') as file_csv:
            writer = csv.writer(file_csv)
            writer.writerow(write_data)
    else:
        with open(file, 'a', newline='', encoding='cp1251') as file_csv:
            writer = csv.writer(file_csv)
            writer.writerow(field_names)