import Sudoku_Board as SB
import Sudoku_Player as SP

'''
Sudoku Game Function: Uses the Board and Player
Classes to implement the Sudoku Game
'''

def Game():
    
    # Board and Player Class Calls

    game_board = SB.Board()
    user = SP.Player(game_board)
    
    # Game Home Page

    board_0 = [[' ' for _ in range(9)] for __ in range(9)]
    board_1 = game_board.board
    print(('\033[1m\033[3m      SUDOKU      \033[0m \n').center(50))
    for a in range(9):
      for b in range(9):
        if a not in [0, 1, 3, 4, 6, 7, 9]:
          board_0[a][b] = '.'       
    game_board.display_board(board_0)
    print('\n\033[4m Welcome!! Please Select An Option \033[0m\n\n1. Help\n\n2. New Game')
   
   # Game Logic

    select = input('\n> ')
    if select == '1':
        user.help()
    elif select == '2':
        game_over = False
        game_board.solution_board()         
        board_2 = game_board.puzzle_board(board_1)        
        lives = 10 
        while not game_over:
            game_board.display_board(board_2) 
            row, col, action = user.user_input()
            while board_2[row][col] != ' ': 
                print('\nThis cell already has a value.')       
                row, col, action = user.user_input()
            if action == 's':
                user.show_possible_moves(row, col, board_2)                
            else:                                    
               game_over, lives =  user.enter_value(row, col, board_1, board_2, lives)
               if game_board.is_board_complete(board_2):
                   game_board.display_board(board_1) 
                   print('You Win!!' if not game_over else 'You Lose!!')
                   break               
    else:
        print('Invalid Selection')



if __name__ == '__main__':
    Game()