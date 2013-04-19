# Tic Tac Toe v2
# Arlandis Lawrence

PLAYERS = {'x':'o', 'o':'x'}
SCORES = {'x':-1,'o':1, None:0}

class Game(object):

    WINNING_COMBOS = ([1,2,3], [1,4,7], [1,5,9],
                      [2,5,8], [3,6,9], [3,5,7],
                      [7,8,9], [4,5,6],)
  
    def __init__(self):
        """Initializes empty board"""
        self.board = {}

    def generate_layout(self):
        """None -> list of str"""

        layout = [None] * 9
        for x in self.board.keys():
            layout[x - 1] = self.board[x]
        for y in self.generate_moves() :
            layout[y - 1] = ""
        return layout
    
    def __str__(self):
        return "%2s %2s %2s\n%2s %2s %2s\n%2s %2s %2s" % tuple(self.generate_layout())

    def generate_moves(self):
        """None -> list of int
        Returns list of integers that represent available moves
        on the board."""
        
        return [x for x in range(1,10) if x not in self.board]
    
    def winner(self):
        """None -> str/None
        Returns x, o or None if there is no winner"""
        
        for comb in self.WINNING_COMBOS:
             if (comb[0] in self.board) and (comb[1] in self.board) and (comb[2] in self.board):
                 if self.board[comb[0]] == self.board[comb[1]] == self.board[comb[2]]:
                    return self.board[comb[0]]
        return None

    def game_over(self):
        """None -> bool"""

        if not self.winner():
            return range(1,10) == self.board.keys()
        return True

    def reset(self, move):
        """Erases a move"""

        del self.board[move]

class AI(object):
    
    def __init__(self,token):
        self.token = token

    def move(self,game):
        """Game -> None
           Makes best move based on current game state."""

        # Only move if the game's not over
        if game.generate_moves():            
            moves = self.get_moves(game)
            #moves is a sorted list with best available move in a list at the end
            space = moves[-1][1]
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
                return SCORES[current_game.winner()]
            else:
                values = [self.minimax(move, current_game, PLAYERS[token]) for move in possible_moves]
                if token == self.token:
                    return min(values)
                else:
                    return max(values)
        finally:
            current_game.reset(space)

    def get_moves(self, game):
        """Game -> list of lists
           Calls minimax algorithm to generate
           a list of moves and their corresponding
           score based on the algorithm. Ranks move list
           according to the algorithmic score and
           returns that move list with list containing
           [best_score, best_move] at the end of the list"""
        
        move_list = [[self.minimax(move, game, self.token), move] for move in game.generate_moves()]
        return sorted(move_list)

def capture_input(statement, options, response=0, data_type=int):
    """str, iterable, data type -> data type
       Assumes 0 is outside range of 
       options"""
    while response not in options:
        try:
            response = data_type(raw_input(statement))
        except:
            continue
    return response

def human_move(game, token):
    """Game object -> None"""
    possible_moves = game.generate_moves()
    print "Possible moves are %s" % possible_moves
    game.board[capture_input("Please select a move: ", possible_moves)] = token

def game_play(x):
    main_game = Game()
    human = 'x'
    computer = AI('o')
    game_over = False
    while not game_over:
        if x == 1:
            human_move(main_game, human)
            print main_game
            if main_game.winner() or main_game.game_over():
                break

            computer.move(main_game)
        else:
            computer.move(main_game)
            print main_game
            # Game ends with this move
            if main_game.winner() or main_game.game_over():
                break

            human_move(main_game, human)

        print main_game
        game_over = main_game.game_over()
    winner = main_game.winner()
    
    if winner:
        print "%s wins" % winner
    else:
        print "It's a draw"
        
if __name__ == "__main__":
    print "Welcome to Tic Tac Toe"
    play = True
    while play:
        game_play(capture_input("Would you like to go first or second: [1,2] ", (1,2)))
        play_dict = {"y": True, "n": False}
        key = capture_input("Would you like to play again: (y/n) ", ("y","n"), data_type=str)
        play = play_dict[key]
    
