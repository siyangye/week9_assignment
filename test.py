import unittest
#import main #this is the wrong line
from main import Game, HumanPlayer #why do I have to import like this?


class TestMain(unittest.TestCase):
    ##wrong line:
    #def test_run(self):
        #board = [
            #['X','X','X'],
            #['O',None,'O'],
            #['O',None,None],
        #
        #self.assertEqual(main.get_winner(board), "X wins!")
        
    ##right lines:
    def test_game_get_winner(self):
        game = Game(HumanPlayer(), HumanPlayer());
        game.board = [
            [game.X_player, None, game.O_player],
            [None, game.X_player, None],
            [None, game.O_player, game.X_player],
        ]
        self.assertEqual(game.get_winner(), game.X_player)

if __name__ == '__main__':
    unittest.main()