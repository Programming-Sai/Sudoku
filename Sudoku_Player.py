import random
import Sudoku_Board as SB

'''
Sudoku Player Class: Defines all methods 
related to user input, it's validation
etc.
'''

class Player:
    def __init__(self, board):
        '''
          Initializes The Board class
        '''
        self.board = board


    def user_input(self):
        '''
          Receives User input, validates it and returns it
         
          Parameters:
          
          Returns:
          list: this contains the row, column and the 
          action the user would like to perform 
        '''
        cols = [chr(a) for a in range(97, 97+9)]
        rows = [str(b) for b in range(1, 10)]
        action = ['s', 'e']
        user_input = ''
        while len(user_input) != 3 or user_input[0] not in cols or user_input[1] not in rows or user_input[2] not in action:
           user_input = input('>>> ').lower()
        user_cmds = []
        user_cmds.append(int(user_input[1]) - 1)
        user_cmds.append(int(ord(user_input[0]) - ord('a')))
        user_cmds.append(user_input[2])
        return user_cmds
        

        
                
    def show_possible_moves(self, row, col, board_2):
        '''
          Acquires all possible moves for c cell from the board class
         
          Parameters:
          row(int): the row index
          col(int): the col index
          board(list): the board to possible values for
          
          Returns: None
          
        '''
        print(f'The Possible Values\nFor This Cell Are:\n{self.board.possible_moves(row, col, board_2)}')
                               
                                
                                                                                                
                                
    def enter_value(self, row, col, board_1, board_2, lives):
        '''
          Allows user to populate incomplete board 
         
          Parameters:
          row(int): the row index
          col(int): the col index
          board_1(list): Main board 
          board_2(list): Incomplete board 
          lives(int): number of tries until game over
            
          Returns:
          bool: Based on whether lives is 0 or not
          int: Returns the number of lives left
          
        '''
        safe = False
        user_num = ''
        
        while not safe or user_num not in range(1, 10):           
            while True :
              try:
                user_num = int(input('Enter Sudoku Number '))
                break 
              except ValueError:
                continue   
            safe = self.board.is_valid(row, col, user_num, board_2)             
          
            if not safe:
              board_2[row][col] = user_num
              range_, value = self.board.clashes(row, col, board_2)  
                                       
              print(f'Invalid Moves at {(chr((97+col)-32), row+1)}\nsince {set(a for a in value if a != None)} crashes with these other \ncells {range_}\n' if not safe else '')
              board_2[row][col] = ' '
            else:
              board_2[row][col] = user_num
              if safe and board_1[row][col] != user_num:
                print(f'Sorry {user_num} would clash with another\ncell later on.')
                board_2[row][col] = ' '
            
            
            
            lives -= 1 if not safe or (safe and board_1[row][col] != user_num) else 0 
            print (f'\nYou Have {lives} trys remaining\n' if not safe or (safe and board_1[row][col] != user_num) else '')
            if lives == 0:
                print('You Lose!!')
                return True, None
                       
        print('_______________________________\nThis Move is Ok\n' if board_1[row][col] == user_num else '')   
        return False, lives                                                            
                                                                                       
 
    def help(self):
        '''
          Displays the rules for the game to the user
         
          Parameters:
          
          Returns: None
          
        '''
        with open('Game.txt', 'r') as g:
           print(g.read())    
                                                                                                                                                                                                                                                      
                                                        
                                                                

if __name__ == '__main__':
    board = SB.Board()                                                                  
    v = Player(board)
    
    