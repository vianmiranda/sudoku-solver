from check import check

count = 0

def solveSudoku(sudoku, row, col):
    global count
    count += 1

    #arbitrary number to keep track of recursion so app doesn't crash
    if count > 1000000: 
        print("over 9000!")
        return False
    elif row == 8 and col == 9:
        return True
    elif col == 9:
        row += 1
        col = 0
    
    if sudoku[row][col] > 0:
        return solveSudoku(sudoku, row, col+1)

    for n in range (1, 10):
        if check(sudoku, row, col, n):
            sudoku[row][col] = n
            if solveSudoku(sudoku, row, col+1):
                return True
        sudoku[row][col] = 0

    return False

def solve(sudoku):
    global count
    if solveSudoku(sudoku, 0, 0):
        count = 0
        return sudoku
    else: 
        count = 0
        return False