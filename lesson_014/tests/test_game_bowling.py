

# TODO Пути старайтесь указывать относительно рабочей директории (той, в которой лежит главный запускаемый файл)
# TODO т.к. здесь у нас проект состоит из нескольких "мини"-проектов, то можно выполнить хитрый приём, явно указав
# TODO на рабочую директорию.
# TODO Сделать это можно либо в Run - Edit configurations
# TODO Либо можно просто выделить нужную папку как source root
# TODO для этого надо нажать на неё правой кнопкой - mark directory as - source root
# TODO Либо, если запуск идёт через терминал - нужно в самом терминале отркыть рабочую директорию
# TODO (путь указанный в терминале - используется как рабочая директория)
# TODO Сделать это можно 2 способами
# TODO 1) использовать команду терминала cd (change directory)
# TODO 2) ПКМ на нужной папке в пайчарме - open in terminal
from bowling import Game
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
        game_result = '-1-2-3-4-5-6-7-8-9--'
        self.test_game_run = self.test_game.run_game(game_result=game_result)
        self.assertEqual(self.test_game_run, 45)

    def test_double_number(self):
        game_result = '11122334455443322122'
        self.test_game_run = self.test_game.run_game(game_result=game_result)
        self.assertEqual(self.test_game_run, 54)

    def test_ten_numbers(self):
        game_result = 'XXXXX2/-724--X'
        self.test_game_run = self.test_game.run_game(game_result=game_result)
        self.assertEqual(self.test_game_run, 148)

    def test_(self):
        pass
        # game_result = ''
        # self.test_game_run = self.test_game.run_game(game_result=game_result)
        # self.assertEqual(self.test_game_run, )


if __name__ == '__main__':
    unittest.main()
