import copy

class AI: 

    def __init__(self, level=1, player=2):
        self.level = level 
        self.player = player 
        self.opponent = 1 if player == 2 else 2
        
    
    def eval(self, main_board):  
        eval, move = self.minimax(main_board, False)

        print(f"\nPlayer{self.player} choose {move} with evaluation: {eval}\n")
        return move

    def minimax(self, board, maximizing): 
        #terminal case 
        case = board.final_state() 

        if case == self.opponent : 
            print("Terminal State with evaluation 1")
            return 1, None
        elif case == self.player: 
            print("Terminal State with evaluation -1")
            return -1, None
        elif board.is_full(): 
            print("Terminal State with evaluation 0")
            return 0, None
        
        if maximizing: 
            max_eval = -10 
            best_move = None 
            empty_sqrs = board.get_empty_sqrs() 

            for (row, col) in empty_sqrs: 
                print(f"Player{self.opponent} may consider the move ({row}, {col})")
                temp_board = copy.deepcopy(board)
                temp_board.mark_sqr(row, col, self.opponent)
                eval = self.minimax(temp_board, False)[0]
                

                if eval > max_eval: 
                    max_eval = eval 
                    best_move = (row, col)
            
            return max_eval, best_move
        else: 
            min_eval = 10 
            best_move = None 
            empty_sqrs = board.get_empty_sqrs() 

            for (row, col) in empty_sqrs: 
                print(f"Player{self.player} (AI) is considering the move ({row},{col})")
                temp_board = copy.deepcopy(board)
                temp_board.mark_sqr(row, col, self.player)
                eval = self.minimax(temp_board, True)[0]
                
                if eval < min_eval: 
                    min_eval = eval 
                    best_move = (row, col)
            
            return min_eval, best_move
