

# Пути старайтесь указывать относительно рабочей директории (той, в которой лежит главный запускаемый файл)
# т.к. здесь у нас проект состоит из нескольких "мини"-проектов, то можно выполнить хитрый приём, явно указав
# на рабочую директорию.
# Сделать это можно либо в Run - Edit configurations
# Либо можно просто выделить нужную папку как source root
# для этого надо нажать на неё правой кнопкой - mark directory as - source root
# Либо, если запуск идёт через терминал - нужно в самом терминале отркыть рабочую директорию
# (путь указанный в терминале - используется как рабочая директория)
# Сделать это можно 2 способами
# 1) использовать команду терминала cd (change directory)
# 2) ПКМ на нужной папке в пайчарме - open in terminal

from bowling import Game, TenThrows, BadData
import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.test_game = Game(game_result=None)
        self.test_game_run = None

    def test_X(self):
        game_result = 'XXXXXXXXXX'
        self.test_game_run = self.test_game.run_game(game_result=game_result)
        self.assertEqual(self.test_game_run, 200)

    def test_slach(self):
        game_result = '1/2/3/4/5/6/7/8/9/1/'
        self.test_game_run = self.test_game.run_game(game_result=game_result)
        self.assertEqual(self.test_game_run, 150)

    def test_dash(self):
        game_result = '-1-2-3-4-5-6-7-8----'
        self.test_game_run = self.test_game.run_game(game_result=game_result)
        self.assertEqual(self.test_game_run, 36)

    def test_double_number(self):
        game_result = '11122334455443322122'
        self.test_game_run = self.test_game.run_game(game_result=game_result)
        self.assertEqual(self.test_game_run, 54)

    def test_ten_numbers(self):
        game_result = 'XXXXX2/-724--X'
        self.test_game_run = self.test_game.run_game(game_result=game_result)
        self.assertEqual(self.test_game_run, 148)

    def test_more_numbers(self):
        """Лишние броски"""
        game_result = 'XXXXX2/-724--1234'
        with self.assertRaises(TenThrows):
            self.test_game.run_game(game_result=game_result)

    def test_less_numbers(self):
        """Не хватает бросков!"""
        game_result = 'XXXXX2/-724--'
        with self.assertRaises(TenThrows):
            self.test_game.run_game(game_result=game_result)

    def test_bad_slash(self):
        """Неверная запись данных! - двойной слеш!"""
        game_result = 'XXXXX2//-724--X'
        with self.assertRaises(BadData):
            self.test_game.run_game(game_result=game_result)

    def test_bad_zero(self):
        """Неверная запись данных! - нули во фрейме!"""
        game_result = 'X0XXX2/-724--X'
        with self.assertRaises(BadData):
            self.test_game.run_game(game_result=game_result)

    def test_bad_letter(self):
        """Неверная запись данных! - буквы во фрейме!"""
        game_result = 'FOXXX2/-724--X'
        with self.assertRaises(BadData):
            self.test_game.run_game(game_result=game_result)

    def test_bad_summ_number(self):
        """Неверная запись данных! - неправильная запись суммы бросков!"""
        game_result = 'X46XX2/-724--23X'
        with self.assertRaises(BadData):
            self.test_game.run_game(game_result=game_result)

    # internal
    def test_X_eu(self):
        game_result = 'XXXXXXXXXX'
        # 30+30+30+30+30+30+30+30+20+10
        self.test_game_run = self.test_game.run_game_eu(game_result=game_result)
        self.assertEqual(self.test_game_run, 270)

    def test_slach_eu(self):
        game_result = '1/2/3/4/5/6/7/8/9/1/'
        self.test_game_run = self.test_game.run_game_eu(game_result=game_result)
        self.assertEqual(self.test_game_run, 145)

    def test_dash_eu(self):
        game_result = '-1-2-3-4-5-6-7-8----'
        self.test_game_run = self.test_game.run_game_eu(game_result=game_result)
        self.assertEqual(self.test_game_run, 36)

    def test_double_number_eu(self):
        game_result = '11122334455443322122'
        self.test_game_run = self.test_game.run_game_eu(game_result=game_result)
        self.assertEqual(self.test_game_run, 54)

    def test_ten_numbers_eu(self):
        game_result = 'XXXXX2/-724--X'
        # 30 + 30 + 30 + 22 + 20 + 10 + 7 + 6 + 10
        self.test_game_run = self.test_game.run_game_eu(game_result=game_result)
        self.assertEqual(self.test_game_run, 165)

    def test_more_numbers_eu(self):
        """Лишние броски"""
        game_result = 'XXXXX2/-724--1234'
        with self.assertRaises(TenThrows):
            self.test_game.run_game_eu(game_result=game_result)

    def test_less_numbers_eu(self):
        """Не хватает бросков!"""
        game_result = 'XXXXX2/-724--'
        with self.assertRaises(TenThrows):
            self.test_game.run_game_eu(game_result=game_result)

    def test_bad_slash_eu(self):
        """Неверная запись данных! - двойной слеш!"""
        game_result = 'XXXXX2//-724--X'
        with self.assertRaises(BadData):
            self.test_game.run_game_eu(game_result=game_result)

    def test_bad_zero_eu(self):
        """Неверная запись данных! - нули во фрейме!"""
        game_result = 'X0XXX2/-724--X'
        with self.assertRaises(BadData):
            self.test_game.run_game_eu(game_result=game_result)

    def test_bad_letter_eu(self):
        """Неверная запись данных! - буквы во фрейме!"""
        game_result = 'FOXXX2/-724--X'
        with self.assertRaises(BadData):
            self.test_game.run_game_eu(game_result=game_result)

    def test_bad_summ_number_eu(self):
        """Неверная запись данных! - неправильная запись суммы бросков!"""
        game_result = 'X46XX2/-724--23X'
        with self.assertRaises(BadData):
            self.test_game.run_game_eu(game_result=game_result)


    def test_number_eu(self):
        game_result = 'X1/--275/5/X-79-1/'
        # 20 + 10 + 9 + 15+ 20 + 17 +7 +9+ 10
        self.test_game_run = self.test_game.run_game_eu(game_result=game_result)
        self.assertEqual(self.test_game_run, 117)



if __name__ == '__main__':
    unittest.main()
