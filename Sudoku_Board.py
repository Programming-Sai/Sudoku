import random 
import copy

'''
Sudoku Board Class: Defines all methods 
related to board generation, cell value 
validation etc.
'''


class Board:
    def __init__(self):
        '''
          Initializes The empty Board as a 2D list and it's Sudoku numbers.
        '''
        self.board = [[' ' for a in range(9)] for b in range(9)]
        self.numbers = [b for b in range(1, 10)]
        
        
        
    @staticmethod
    def is_duplicate_in_list(list):
        '''
          Checks if there are duplicates in the board 
         
          Parameters:
          list(list): the list to search 
          
          Returns:
          bool: Based on whether there is a duplicate or not
          int: Returns the duplicate number
          
        '''
        list_set = set()
        for element in list:
            if element != ' ':
                if element in list_set:
                    return False, element 
            list_set.add(element)
        return True, None 
            
                          
                                                      
    @staticmethod
    def find(board, list, target):
        '''
          Searches through the board to find an element 
          
          Parameters:
          list(list): the list to search 
          board(list): the main board to compare with
          target(int): the element to search for 
          
          Returns:
          list: Returns a list or tupled indices of where the target can be found 
          
        '''  
        return [(i, j) for i, j in list if board[i][j] == target and board[i][j] != ' ']
   
   
   
    def get_row(self, row, col):
        '''
          Gets the entire row based on the cell in the board 
         
          Parameters:
          row(int): the row index
          col(int): the col index
          
          Returns:
          list: Returns a list or tupled indices of the row 
          
        '''
        main_row = [(row, col)]
        for a in range(1, 9):
            col_1 = col + a
            col_2 = col - a
            main_row.append((row, col_1)) if col_1 < 9 else '' 
            main_row.append((row, col_2)) if col_2 > -1 else ''     
        return main_row
        
       
                  
    def get_col(self, row, col):
        '''
          Gets the entire column based on the cell in the board 
         
          Parameters:
          row(int): the row index
          col(int): the col index
          
          Returns:
          list: Returns a list or tupled indices of the column 
          
        '''
        main_col = [(row, col)]
        for a in range(1, 9):
            row_1 = row + a
            row_2 = row - a
            main_col.append((row_1, col)) if row_1 < 9 else '' 
            main_col.append((row_2, col)) if row_2 > -1 else ''  
        return main_col
        
                        
        
    def get_block(self, row, col): 
        '''
          Gets the entire block/subgrid based on the cell in the board 
         
          Parameters:
          row(int): the row index
          col(int): the col index
          
          Returns:
          list: Returns a list or tupled indices of the block/subgrid 
          
        '''       
        block_centers = [1, 4, 7]
        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]              
        def blocks(r, c):
            block_cells = []
            for offset in offsets:
                block_cells.append(((r + offset[0]), (c + offset[1])))
            return (block_cells)            
        block =[]
        for a in block_centers:
            for b in block_centers:                
                block.append(blocks(a, b))       
        for cell_range in block:
            if (row, col) in cell_range:
                return cell_range
       
       
       
    def is_valid(self, row, col, num, board = None):
        '''
          Validates the value in the cell, 
          making sure it follows all the rules of sudoku
         
          Parameters:
          row(int): the row index
          col(int): the col index
          num(int): the Sudoku number in a cell 
          board(list): the board to be checked 
          
          Returns:
          bool: Returns true/false based on whether cell value is valid or not
          
        '''
        if board == None:
            board = self.board
        else:
            board = board
        if num in board[row]:
            return False 
        if num in [board[a][col] for a in range(9)]:
            return False
        block_range = self.get_block(row, col)
        if num in [board[i][j] for i, j in block_range]:
            return False    
        return True



    def clashes(self, row, col, board):
        '''
          Checks for clashes  and where they occur 
         
          Parameters:
          row(int): the row index
          col(int): the col index
          board(list): the board to check 
          
          Returns:
          tuple: Returns a tuple that contains
          a list of indices of the clashes and 
          a set that contains the 
          values causing the clashes
          
        '''
        rows = self.get_row(row, col)
        cols = self.get_col(row, col)
        blocks = self.get_block(row, col)
        
        at = set()
        row_safe, at_1 = self.is_duplicate_in_list([board[r][c] for r, c in rows])
        col_safe, at_2 = self.is_duplicate_in_list([board[r][c] for r, c in cols])
        block_safe, at_3 = self.is_duplicate_in_list([board[r][c] for r, c in  blocks])
        if not row_safe or not col_safe or not block_safe:
           foul_cells = list(set(self.find(board, rows, at_1) + self.find(board, cols, at_2) + self.find(board, blocks, at_3)))
           foul_cells.remove((row, col))
           at.add(at_1)
           at.add(at_2)
           at.add(at_3)
      
           foul_cells = [((chr((97+b)-32)), (a+1)) for a, b in foul_cells]
           return (foul_cells, at)
        return [], at
          
              
    
    def solution_board(self):  
        '''
          Generate the completed Sudoku Board  
         
          Parameters:
          
          
          Returns:
          bool: Returns a True/False based on
          whether it found a solvable board or not 
          
        '''      
        for row in range(9):                     
            for col in range(9):
                if self.board[row][col] == ' ':
                     random.shuffle(self.numbers)
                     for num in self.numbers:       
                        if self.is_valid(row, col, num):
                            self.board[row][col] = num
                            if self.solution_board():
                                return True
                            self.board[row][col] = ' '
                     return False
        return True 
                              
                                                                                                                                                                  
                                                                                                                                                                                                                                                                                                                                                                                                                                          
    def puzzle_board(self, board):
        '''
          Generate a second board 
          (copy of main board) that 
          is an incomplete version of the 
          completed one
         
          Parameters:
          board(list): the board the be copied 
          
          Returns:
          list: Returns incomplete board
          
        '''
        board = copy.deepcopy(board)   
        i = 0  
        used = set()
        row = 0
        col = 0
        while i < 60 or (row, col) not in used:
            row, col = (random.randint(0, 8), random.randint(0, 8))
            board[row][col] = ' '  
            used.add((row, col)) 
            i += 1 
        return board 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    def is_board_complete(self, board):
        '''
          Checks if the incomplete board is completed
         
          Parameters:
          board(list): the incomplete board 
          
          Returns:
          bool: Returns true/false based on whether board is completed or not
          
        '''
        return True if self.board == board else False

        
                        
    def possible_moves(self, row, col, board):
        '''
          Obtains all possible values for a given cell
         
          Parameters:
          row(int): the row index
          col(int): the col index
          board(list): the board being worked with
          
          Returns:
          list: Returns a list of potential values
          
        '''
        possible = []                    
        for num in self.numbers:           
                if self.is_valid(row, col, num, board):
                  possible.append(num)              
        return possible 
        
        
                        
    def display_board(self, board_1):
            '''
              Displays the board to the user 
             
              Parameters:
              board_1(list): the board to display 
              
              Returns: None
              
            '''  
            board = board_1.copy()
            for a in range(9):
              for b in range(9):
               board[a][b] = str(board[a][b])        
            k = 0
            m = 0
            d = ['|' for s in range(9)]
            e = [' ' for t in range(9)]
            cols = [chr(b) for b in range(65, (65 + 9))]
            print('    ', end = '')
            for c in cols:
                m += 1
                print((" " if m in [4, 7] else "") + ('\033[3m ' + c + ' \033[0m'), end="") 
            print('\n   .' + ('  _ _ _ _ _ _  _  _ _ _ _  __') + '.')    
            for x in board:
              k += 1
              c = [str(z) for z in x]
              d = ['|' for s in range(len(x))]
              e = [' ' for t in range(len(x))]
              d[-1] = d[-1] + '_'  if k % 3 == 0 else d[-1]                  
              print(('\033[3m' + str(k) + '\033[0m')  , ' |', '  '.join(c[:3]) , '|', '  '.join(c[3:6]), '|', '  '.join(c[6:]) , '|')   
              print(' ' , ' |' , ('_ _' if k % 3 == 0 else ' ').join('    ') ,  ('_' if x == board[-1] or x == board[-4] or x == board[-7] else '|') ,  ('_ _' if k % 3 == 0 else '       | ').join('   '), '__|' if k % 3 == 0 else '  ')
            for a in range(9):
              for b in range(9):
               board[a][b] = ' ' if board[a][b] == ' ' or board[a][b] == '.' else int(board[a][b])
                
    
                          
                          
                                 
                                    
                
if __name__ == '__main__':                                                                                                
    board = Board()
    