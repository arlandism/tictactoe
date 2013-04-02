# Testing class for Tic Tac Toe
import tictactoe
import unittest

class BoardTesting(unittest.TestCase):
    """Testing class for Tic Tac Toe Board implementation"""

    def test_board_attributes_and_methods(self):
        """Testing the game board's attributes and simple methods"""
        s = tictactoe.Game()
        empty_dict = {1:None, 2:None, 3:None, 4:None, 5:None, 6:None,
                      7:None, 8:None, 9:None}
        self.assertEqual(s.board, empty_dict)
        expected_layout = ["","","","","","","","",""]
        actual_layout = s.generate_layout()
        self.assertEqual(expected_layout, actual_layout)

    def test_critical_methods_at_begining(self):
        """Tests for more crucial methods of the Game class
           Assumes beginning of game i.e. no moves have been made."""
        
        test_game = tictactoe.Game()
        self.assertEqual(test_game.generate_moves(), range(1,10))
        self.assertEqual(test_game.winner(), None)
        self.assertEqual(test_game.game_over(), False)

    def test_critical_methods(self):
        """More thorough tests for crucial methods of Game class."""
        
        test_game = tictactoe.Game()
        test_game.board[1] = 'x'
        test_game.board[2] = 'x'
        test_game.board[3] = 'x'
        self.assertEqual(test_game.winner(),'x')
        self.assertEqual(test_game.game_over(),True)
        
        test_game.board[1] = 'o'
        test_game.board[2] = 'o'
        test_game.board[3] = 'o'
        self.assertEqual(test_game.game_over(),True)
        self.assertEqual(test_game.winner(), 'o')
        
        for i in range(4,10):
            test_game.board[i] = 'v'
        self.assertEqual(test_game.game_over(), True)
        test_game.board = {1:'x', 2:'o', 3:'x', 4:'x',
                           5:'o',6:'o',7:'o',8:'x',9:'x'}
        self.assertEqual(test_game.game_over(), True)
        self.assertEqual(test_game.winner(), None)
        empty_board = tictactoe.Game().board
        for j in range(1,10):
            test_game.reset(j)
        self.assertEqual(test_game.board, empty_board)

    def test_player_methods(self):
        """Tests for the Player class methods"""
        player = tictactoe.Player('x')
        game = tictactoe.Game()
        player.move(1,game)
        self.assertEqual(game.board[1],'x')
        
    def test_ai(self):
        """Tests for the AI class"""
        computer = tictactoe.AI('o')
        game = tictactoe.Game()
        computer.minimax(1,game,'o')
        print computer.get_moves(game)
        # TODO

if __name__ == "__main__":
    unittest.main(exit=False)
