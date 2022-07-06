from check import check

count = 0

# solves using backtracking (yay..)
def solveSudoku(sudoku, row, col):
    global count
    count += 1

    if count > 1500000: # arbitrary number to keep track of recursion so app doesn't crash
        print("over 9000!")
        return False
    elif row == 8 and col == 9: # if row/col counter passes last box, can end recursion
        return True
    elif col == 9: # if col counter gets through entire row, move to next row
        row += 1
        col = 0

    if sudoku[row][col] > 0: # skips prefilled inputs
        return solveSudoku(sudoku, row, col+1)    

    for n in range (1, 10):
        if check(sudoku, row, col, n): # checks if value works 
            sudoku[row][col] = n
            if solveSudoku(sudoku, row, col+1):
                return True
        sudoku[row][col] = 0 # resets value if previous condition is not met

    return False

# returns solved board if it worked
def solve(sudoku): 
    global count
    count = 0
    if solveSudoku(sudoku, 0, 0):
        return sudoku
    else: 
        return False