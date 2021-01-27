# Правила такие.
#
# Всего 10 кеглей. Игра состоит из 10 фреймов. В одном фрейме до 2х бросков, цель - сбить все кегли.
# Результаты фрейма записываются символами:
#   «Х» – «strike», все 10 кеглей сбиты первым броском
#   «<число>/», например «4/» - «spare», в первый бросок сбиты 4 кегли, во второй – остальные
#   «<число><число>», например, «34» – в первый бросок сбито 3, во второй – 4 кегли.
#   вместо <число> может стоять прочерк «-», например «-4» - ни одной кегли не было сбито за первый бросок
# Результат игры – строка с записью результатов фреймов. Символов-разделителей между фреймами нет.
# Например, для игры из 4 фреймов запись результатов может выглядеть так:
#   «Х4/34-4»
# Предлагается упрощенный способ подсчета количества очков:
#   «Х» – strike всегда 20 очков
#   «4/» - spare всегда 15 очков
#   «34» – сумма 3+4=7
#   «-4» - сумма 0+4=4
# То есть для игры «Х4/34-4» сумма очков равна 20+15+7+4=46

# 20 15 7 4
# фрейм всегда строка
#  Х  -  один бросок  = 20. Состояние 1
#  4/6, 8/2, 9/1 - два броска сбиты все кегли  =  15. Состояние 2
#  34 -  сумма по итогам двух бросков по кеглям.  Состояние 3
#  -4 -  сумма по итогам  двух бросков по кеглям, но первый бросок мимо. Состояние 4,  чем отличается от 3??
#  условие задачи - игра всегда из десяти фреймов
# счетчик всегда в каком - то из состояний
# также состояние ошибки  -  когда переданные данные не могут буть разделены на фреймы и посчитаны очки.
# виды ошибок свои - лишние данные в строке, неправильные данные - > 9, не 10 бросков во фрейме

# пробный вариант
# def get_score(game_result):
#     game_result = game_result
#     result_len = len(game_result)
#     result_count = 0
#     step_ = 0
#     while step_ <= result_len - 1:  # for step_ in range(result_len):
#         print(f' счетчик {result_count}')
#         try:
#             print(f'шаг{step_}, значение {game_result[step_]},')
#             if step_ == len(game_result) - 1:
#                 print('Конец записи')
#                 break
#
#             elif game_result[step_] == 'X':
#                 result_count += 20
#                 step_ += 1
#                 continue
#
#             elif game_result[step_] == '/':
#                 step_ += 1
#                 continue
#
#             elif game_result[step_] == '-':
#                 if game_result[step_ + 1].istep_digit():
#                     if int(game_result[step_ + 1]) >= 1 or int(game_result[step_ + 1]) <= 9:
#                         result_count += int(game_result[step_ + 1])
#                         step_ += 2
#                         continue
#                     else:
#                         raise Exception('Вне диапазона')
#                 else:
#                     step_ += 1
#                     raise Exception('Некоректные данные')
#
#             elif not game_result[step_].istep_digit():
#                 step_ += 1
#                 raise Exception('Некоректные данные')
#             elif game_result[step_].istep_digit() and game_result[step_ + 1] == '/':
#                 if int(game_result[step_]) < 1 or int(game_result[step_]) > 9:
#                     raise Exception('Вне диапазона')
#                 else:
#                     result_count += 15
#                     step_ += 1
#                     continue
#
#             elif game_result[step_].isdigit() and game_result[step_ + 1].isdigit():
#                 if game_result[step_ - 1].isdigit():
#                     result_count += int(game_result[step_]) + int(game_result[step_ + 1])
#                     step_ += 2
#                 else:
#                     step_ += 1
#                     raise Exception('Это не работает!')
#
#         except Exception as exc:
#             print(exc)
#         # проверить на количество бросков 10.
#     return result_count


# res = get_score(game_result='X2/-353XX9/-7-523')  # 20 + 15 + 3 + 8 + 20 + 20 + 15 + 7 + 5 + 5    118
# print(f'Итого очков - {res}')
# res = get_score(game_result='X22/-353XX99/.-7--523')  # лишние данные 2 9 . -
# print(f'Итого очков - {res}')

# 2 вариант через классы, что-то типа паттернов состояния счетчика очков
class ExtraneousCharacters(Exception):
    pass


class BadData(Exception):
    pass


class TenThrows(Exception):
    pass


# class CounterBowling:
#     """
#     Общий класс боулинг
#     Принимает значения игры в виде строки,
#     Проверяет строку на соответствие и
#     Возвращает количество очков
#     """
#
#     def __init__(self, game_result):
#         self.game_result = game_result
#         self.result_counter = 0
#         self.len_data = 0
#
#     def start_cleaning(self, game_result):  # проверка на лишние и неправильные элементы и 10 бросков
#         self.game_result = game_result
#         try:
#             for date, value in enumerate(self.game_result):
#                 if not value.isdigit() and value != 'X' and value != '/' and value != '-':
#                     raise ExtraneousCharacters('Во фрейме посторонние символы')
#                 elif value == '/' and self.game_result[date + 1] == '/':
#                     raise BadData('Некорректные данные во фрейме!')
#                 elif value == '-' and self.game_result[date + 1] == '-':
#                     raise BadData('Некорректные данные во фрейме!')
#                 elif date == 0 and value == '/':
#                     raise BadData('Некорректные данные во фрейме !')
#                 elif date == len(self.game_result) - 1 and value == '-':
#                     raise BadData('Некорректные данные во фрейме !')
#                 elif value == '-' and self.game_result[date + 1] == '/':
#                     raise BadData('Некорректные данные во фрейме !')
#
#             ten_counter = 0  # проверка на количество страйков
#             self.len_data = len(self.game_result)
#             for data, value in enumerate(self.game_result):
#                 if self.game_result[data] == 'X':
#                     ten_counter += 1
#
#             rest_ten_counter = self.len_data - ten_counter  # проверка на 10 бросков
#             if rest_ten_counter <= 18 or rest_ten_counter >= 2:
#                 if rest_ten_counter % 2 == 0:
#                     if rest_ten_counter / 2 + ten_counter == self.len_data:
#                         print('Бросков 10!')
#             else:
#                 raise TenThrows('Число бросков неверно!')
#             return self.game_result
#         except (ExtraneousCharacters, BadData, TenThrows) as exc:
#             print(f'Входные данные некорректны! Ошибка - тип {type(exc)}, наименование - {exc}')
#
#     def get_store(self, game_result):
#         CounterBowling.start_cleaning(self, game_result=game_result)
#         CounterStraike.requests(self, game_result=game_result)
#         CounterSpare.requests(self, game_result=game_result)
#         CounterOnesum.requests(self, game_result=game_result)
#         CounterNsum.requests(self, game_result=game_result)
#         return self.result_counter
#
#
# class CounterStraike(CounterBowling):  # условие работы счетчика 1 символ в  значении  и равно Х
#     def __init__(self, game_result):
#         super().__init__()
#         self.game_result = game_result
#
#     def requests(self, game_result):
#         self.game_result = game_result
#         for data, value in enumerate(self.game_result):
#             if self.game_result[data] == 'X':
#                 self.result_counter += 20
#                 self.game_result = self.game_result.replace(self.game_result[data], '0', 1)
#         return self.result_counter, self.game_result
#
#
# class CounterSpare(CounterBowling):  # условие работы счетчика 2 символа: 1значание всегда - , второе число от 1 до 9
#     def __init__(self, game_result):
#         super().__init__()
#         self.game_result = self.game_result
#
#     def requests(self, game_result):
#         for data, value in enumerate(self.game_result):
#             if self.game_result[data] == '-' and self.game_result[data + 1].isdigit():
#                 self.result_counter += int(self.game_result[data + 1])
#                 self.game_result = self.game_result.replace(self.game_result[data], '0', 1)
#                 self.game_result = self.game_result.replace(self.game_result[data + 1], '0', 1)
#         return self.result_counter, self.game_result
#
#
# class CounterOnesum(CounterBowling):  # условие счетчика 2 символа:1значение от 1 до 9 2значение всегда /
#     def __init__(self, game_result):
#         super().__init__()
#         self.game_result = game_result
#
#     def requests(self, game_result):
#         for data, value in enumerate(self.game_result):
#             if self.game_result[data] == '/' and self.game_result[data - 1].isdigit():
#                 self.result_counter += 15
#                 self.game_result = self.game_result.replace(self.game_result[data], '0', 1)
#                 self.game_result = self.game_result.replace(self.game_result[data - 1], '0', 1)
#         return self.result_counter, self.game_result
#
#
# class CounterNsum(CounterBowling):  # условие работы счетчика 2 символа - 2 числа
#     def __init__(self, game_result):
#         super().__init__()
#         self.game_result = game_result
#
#     def requests(self, game_result):
#         for data, value in enumerate(self.game_result):
#             if value.isdigit() and self.game_result[data - 1].isdigit():
#                 self.result_counter += int(self.game_result[data]) + int(self.game_result[data - 1])
#                 self.game_result = self.game_result.replace(self.game_result[data], '0', 1)
#                 self.game_result = self.game_result.replace(self.game_result[data - 1], '0', 1)
#         return self.result_counter, self.game_result
#


# Вариант с бросками на основе примера из LMS


class GameBowling:
    def __init__(self, game_result):
        self.game_result = game_result
        self.result_counter = 0
        self.game_status = None

    def count_hit(self, game_result):
        self.game_result = game_result


class Hit1(GameBowling):
    def __init__(self, game_result):
        super().__init__(game_result)
        self.game_result = game_result

    def count_hit(self, game_result):
        self.game_result = game_result
        current_hit = self.game_result[:1]
        if current_hit == 'X':
            self.result_counter += 20
        else:
            if current_hit == '/':
                raise BadData('Некорректные данные во фрейме !')
            current_hit_next = self.game_result[1:2]
            if current_hit == '0' or current_hit_next == '0':
                raise BadData('Некорректные данные во фрейме !')
            print(current_hit, current_hit_next, type(current_hit), type(current_hit_next))
            if current_hit.isdigit():
                if current_hit_next == '/':
                    self.result_counter += 15
                    self.game_result = self.game_result[1:]
            if current_hit == '-':
                self.game_status = Hit2(game_result)  # !!!
            if current_hit.isdigit() and current_hit_next.isdigit():
                if (int(current_hit) + int(current_hit_next)) > 9:
                    raise BadData('Некорректные данные во фрейме !')
                else:
                    self.game_status = Hit2(game_result)
        self.game_result = self.game_result[1:]
        return self.game_result, self.result_counter


class Hit2(GameBowling):
    def __init__(self, game_result):
        super().__init__(game_result)
        self.game_result = game_result

    def count_hit(self, game_result):
        self.game_result = game_result
        current_hit = self.game_result[:1]
        current_hit_next = self.game_result[1:2]
        if current_hit == '-':
            if current_hit_next == '-':
                self.game_result = self.game_result[1:]
            if current_hit_next.isdigit():
                self.result_counter += int(current_hit_next)
                self.game_result = self.game_result[1:]
            else:
                raise BadData('Некорректные данные во фрейме !')
        if current_hit.isdigit():
            self.result_counter += int(current_hit) + int(current_hit_next)
            self.game_result = self.game_result[1:]
        return self.game_result, self.result_counter


class Game:
    def __init__(self, game_result):
        self.game_result = game_result
        self.result_counter = 0
        self.game_status = None
        self.count_frame = 0

    def run_game(self, game_result):
        self.game_result = game_result
        self.game_status = Hit1(game_result)
        while self.game_result:
            self.game_result, self.result_counter = self.game_status.count_hit(self.game_result)
            self.count_frame += 1
        if self.count_frame != 10:
            raise BadData('Некорректные данные во фрейме !')
        return self.result_counter
