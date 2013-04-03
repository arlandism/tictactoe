# Tic Tac Toe
# Arlandis Lawrence

from operator import itemgetter

players = {'x':'o', 'o':'x'}
scores = {'x':-1,'o':1, None:0}

class Game(object):

    WINNING_COMBOS = ([1,2,3], [1,4,7], [1,5,9],
                      [2,5,8], [3,6,9], [3,5,7],
                      [7,8,9], [4,5,6],)
  
    def __init__(self):
        """Initializes empty board"""
        self.board = {1:None, 2:None, 3:None,
                      4:None, 5:None, 6:None,
                      7:None, 8:None, 9:None}

    def generate_layout(self):
        """None -> list of str"""
        layout = [self.board[i] if self.board[i] else "" for i in range(1,10)]
        return layout
    
    def __str__(self):
        return "%2s %2s %2s\n%2s %2s %2s\n%2s %2s %2s" % tuple(self.generate_layout())

    def generate_moves(self):
        """None -> list of int
        Returns list of integers that represent available moves
        on the board."""
        
        return [x for x in self.board if not self.board[x]]

    def winner(self):
        """None -> str/None
        Returns x, o or None if there is no winner"""
        for comb in self.WINNING_COMBOS:
            if self.board[comb[0]] == self.board[comb[1]] == self.board[comb[2]]:
                return self.board[comb[0]]
        return None

    def game_over(self):
        """None -> bool"""
        if not self.winner():
            for val in self.board:
                if self.board[val] == None:
                    return False
        return True

    def reset(self, move):
        """Erases a move"""
        self.board[move] = None

class Player(object):
    
    def __init__(self,token):
        self.token = token

    def move(self, space, game):
        """Assumes space is empty since
        player is only allowed to make
        available moves during game execution."""
        
        game.board[space] = self.token

class AI(object):
    
    def __init__(self,token):
        self.token = token

    def move(self,game):
        """Game -> None
           Makes best move based on current game state."""

        # Only move if the game's not over
        if game.generate_moves():            
            moves = self.get_moves(game)

            #moves is a sorted list with best available move in a tuple at the end
            space = moves[-1][0]
            game.board[space] = self.token
            print "Computer moves to %s" % space

    def minimax(self,space, current_game, token):
        """int, Game, str -> int
           Implementation of the minimax algorithm.
           Try and finally are used to ensure that the game
           will always reset after each iteration."""
        
        try:
            current_game.board[space] = token
            possible_moves = current_game.generate_moves()
            if current_game.game_over():
                return scores[current_game.winner()]
            else:
                values = []
                for move in possible_moves:
                    values.append(self.minimax(move, current_game, players[token]))
                if token == 'o':
                    return min(values)
                else:
                    return max(values)
        finally:
            current_game.reset(space)

    def get_moves(self, game):
        """Game -> list of tup
           Calls minimax algorithm to generate
           a list of moves and their corresponding
           score based on the algorithm. Ranks move list
           according to the algorithmic score and
           returns that move list with tuple containing
           (best_move, best_score) at the end of the list"""
        
        move_list = []
        for move in game.generate_moves():
            move_list.append((move, self.minimax(move, game, 'o')))

        # using itemgetter as key allows 'sorted' function to sort list according to the 
        # item located at the [1] index in each item in list (in this case tuples)
        return sorted(move_list, key=itemgetter(1))
    
if __name__ == "__main__":
    main_game = Game()
    human = Player('x')
    computer = AI('o')
    game_over = False
    while not game_over:
        space = 0
        possible_moves = main_game.generate_moves()
        while space not in possible_moves:
            print "Possible moves are %s\n" % possible_moves
            space = input("Please select a move: ")
        human.move(space, main_game)
        computer.move(main_game)
        print main_game
        game_over = main_game.game_over()
    print "Game Over"
    winner = main_game.winner()
    if winner:
        print "%s wins" % winner
    else:
        print "It's a draw"
