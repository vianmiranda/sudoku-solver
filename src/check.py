def check(sudoku, row, col, num):
    # check rows
    for i in range (9): 
        if sudoku[i][col] == num and i != row:
            return False

    # check cols
    for j in range (9): 
        if sudoku[row][j] == num and j != col:
            return False

    # check 3x3s
    gridRow = (row // 3) * 3 # gives multiples of 3 only from 0-6
    gridCol = (col // 3) * 3 # and finds current 3x3 grid
    for i in range (gridRow, gridRow + 3): 
        for j in range (gridCol, gridCol + 3):
            if sudoku[i][j] == num and (i != row and j != col):
                return False

    return True