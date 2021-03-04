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


class ExtraneousCharacters(Exception):
    pass


class BadData(Exception):
    pass


class TenThrows(Exception):
    pass


class GameBowling:
    def __init__(self, game_result, result_counter):
        self.game_result = None
        self.result_counter = None
        self.game_status = None

    def count_hit(self, game_result, result_counter):
        self.game_result = game_result


class Hit1(GameBowling):
    def __init__(self, game_result, result_counter):
        super().__init__(game_result, result_counter)
        self.game_result = game_result
        self.result_counter = result_counter

    def count_hit(self, game_result, result_counter):
        self.game_result = game_result
        current_hit = self.game_result[:1]
        self.result_counter = result_counter
        if current_hit == '0':
            raise BadData('Некорректные данные во фрейме! - 0 во фрейме!')
        if current_hit == 'X':
            self.result_counter += 20
        if current_hit == '-' or current_hit.isdigit():
            self.game_status = Hit2(game_result, self.result_counter)
            self.game_result, self.result_counter = self.game_status.count_hit(game_result, result_counter)
        else:
            if current_hit == '/':
                raise BadData('Некорректные данные во фрейме! - / не может быть первым!')
        self.game_result = self.game_result[1:]
        return self.game_result, self.result_counter


class Hit2(GameBowling):
    def __init__(self, game_result, result_counter):
        super().__init__(game_result, result_counter)
        self.game_result = game_result
        self.result_counter = result_counter

    def count_hit(self, game_result, result_counter):
        self.game_result = game_result
        self.result_counter = result_counter
        current_hit = self.game_result[:1]
        current_hit_next = self.game_result[1:2]
        if current_hit_next == '0':
            raise BadData('Некорректные данные во фрейме! - 0 во фрейме!')
        if current_hit == '-':
            if current_hit_next == '-':
                self.game_result = self.game_result[1:]
                return self.game_result, self.result_counter
            else:
                if current_hit_next.isdigit():
                    self.result_counter += int(current_hit_next)
                    self.game_result = self.game_result[1:]
                    return self.game_result, self.result_counter
                else:
                    raise BadData('Некорректные данные во фрейме! - второй бросок не цифра и ('-')')
        if current_hit.isdigit() and current_hit_next.isdigit():
            sum_digit = int(current_hit) + int(current_hit_next)
            if sum_digit > 9:
                raise BadData('Некорректные данные во фрейме! - сумма 2 бросков больше 9')
            self.result_counter += sum_digit
            self.game_result = self.game_result[1:]
            return self.game_result, self.result_counter
        if current_hit.isdigit() and current_hit_next == '-':
            self.result_counter += int(current_hit)
            self.game_result = self.game_result[1:]
            return self.game_result, self.result_counter
        if current_hit.isdigit() and current_hit_next == '/':
            self.result_counter += 15
            self.game_result = self.game_result[1:]
            return self.game_result, self.result_counter
        else:
            raise BadData('Некорректные данные во фрейме! - ни число, ни пробел, ни слеш!')




class Game:
    def __init__(self, game_result):
        self.game_result = game_result
        self.result_counter = 0
        self.game_status = None
        self.count_frame = 0

    def run_game(self, game_result):
        self.game_result = game_result
        self.game_status = Hit1(game_result, self.result_counter)
        try:
            while self.game_result:
                self.game_result, self.result_counter = self.game_status.count_hit(self.game_result, self.result_counter)
                self.count_frame += 1
            if self.count_frame != 10:
                raise TenThrows(f'{self.count_frame} - неверное  количество попыток во фрейме!')
        except(BadData, TenThrows) as exc:
            print(f'Ошибка - {exc}')
            self.result_counter = 0
        return self.result_counter


