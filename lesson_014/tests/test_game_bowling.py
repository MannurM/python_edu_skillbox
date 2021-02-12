

from python_base.lesson_014.bowling import Game
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
