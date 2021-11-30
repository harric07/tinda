'''
Write a function that will solve a 9x9 Sudoku puzzle.
The function will take one argument consisting 
of the 2D puzzle array, with the value 0 
representing an unknown square.

The Sudokus tested against your function 
will be "easy" (i.e. determinable; there 
will be no need to assume and test possibilities
on unknowns) and can be solved with a brute-force approach.

For Sudoku rules, see the Wikipedia article.

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

sudoku(puzzle)
# Should return
 [[5,3,4,6,7,8,9,1,2],
  [6,7,2,1,9,5,3,4,8],
  [1,9,8,3,4,2,5,6,7],
  [8,5,9,7,6,1,4,2,3],
  [4,2,6,8,5,3,7,9,1],
  [7,1,3,9,2,4,8,5,6],
  [9,6,1,5,3,7,2,8,4],
  [2,8,7,4,1,9,6,3,5],
  [3,4,5,2,8,6,1,7,9]]

'''




def sudoku(puzzle):
    x = Sudoku(puzzle)
    r = x.solve()
    return r



class Sudoku:
    result = []
    board = []

    def __init__(self, board):
        self.board = board

    # check if value x can be put at cell[row][col]
    # return False   if value x has already been used in other cells on current row, or column, or 3x3 box
    # return True    otherwise
    def check(self, row, col, x):
        for i in range(9):
            if self.board[row][i] == x:
                return False
            if self.board[i][col] == x:
                return False
        box_start_row = row - row % 3
        box_start_col = col - col % 3
        for r in range(box_start_row, box_start_row + 3):
            for c in range(box_start_col, box_start_col + 3):
                if self.board[r][c] == x:
                    return False

        return True

    # solve the sudoku and return one result
    def solve(self):
        # init the solve_helper at cell (0, 0)
        if self.solve_helper(0):
            return self.board
        else:
            return None

    # given the sudoku has been filled up to cell k-1, try to solve the sudoku from cell k
    # k is the cell index, counting from left to right and top to bottom.
    #     k is 0, 1, 2, ..., 8     for cell (0,0), (0,1), (0,2), ..., (0,8)
    #     k is 9, 10, 11, ...,     for cell (1,0), (1,1), (1,2), ...
    #     k is 80                  for cell (8,8) (last cell)
    def solve_helper(self, k):
        # if we get pass the last cell, it means we have filled every cells with valid values.
        # return True to notify that we have found a solution
        if (k > 80):
            return True

        r = int(k / 9)
        c = k % 9

        # if this cell has been filled, go on to solve the next cell
        if self.board[r][c] != 0:
            return self.solve_helper(k+1)

        # try to fill each value from 1 to 9 in this cell
        for x in range(1, 10):
            # fill the cell with value x only if x has not appeared on the same row or col or 3x3 box
            if self.check(r, c, x):
                # start backtracking:
                # try x in this cell,
                self.board[r][c] = x
                # then try to solve from the next cell k+1,
                if self.solve_helper(k+1):
                    # solving from k+1 did find one solution (because solve_helper(k+1) returned True)
                    # since we only need 1 solution, we can stop further processing and return here
                    # return True to notify upper recursive solve_helper that we found a solution.
                    return True
                # then clear cell to return the board to the status before x was filled
                self.board[r][c] = 0

        # if we are here, it means we have tried all values in this cell without finding a solution
        # return False to notify upper recursive solve_helper that
        # we didn't find any solution given the current board status
        return False