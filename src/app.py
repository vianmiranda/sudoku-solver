import pyglet, tkinter as tk
from tkinter import *
from check import check
from solve import solve
pyglet.font.add_file("fonts/Prime.ttf")
pyglet.font.add_file("fonts/Aloevera.ttf")

window = tk.Tk()
window.title("Sudoku")
window.geometry("750x850")
window.config(background = "#0C1014")
window.resizable(width = False, height = False)

frame = tk.Frame(window, bg = "#0C1014")
frame.place(relwidth = 0.96, relheight = 0.96, relx = 0.02, rely = 0.02)

label = tk.Label(frame, text = "sudoku", bg = "#0C1014", fg = "#FEE715", font = "Prime -56 bold").grid(row = 1, column = 1, columnspan = 10, padx = 100)

label = tk.Label(frame, text = "Solve the Sudoku board or have the CPU do it for you!", bg = "#0C1014", fg = "#FEE715", font = "Prime 11 bold").grid(row = 2, column = 1, columnspan = 10, padx = 100)

#Label if sudoku board is not solvable
errorLabel = tk.Label(frame, text = "", bg = "#0C1014", fg = "red", font = "Prime 14 bold")

#Label if sudoku board is solved
successLabel = tk.Label(frame, text = "", bg = "#0C1014", fg = "#24F224", font = "Prime 14 bold")

cells = {}

def isInt (n):
    return ((n.isdigit() or n == "") and len(n) < 2)

def grid3x3(row, col, bg, fg):
    for i in range(3):
        for j in range(3):
            entry = tk.Entry(frame, width = 8, bg = bg, fg = fg, font = "Aloevera -16", justify = "center", validate = "key", validatecommand = (window.register(isInt), "%P"))
            entry.grid(row = row+i+3, column = col+j+1, padx = 2, pady = 2, ipady = 20)
            cells[(row+i, col+j)] = entry

def grid9x9():
    bg = "#FEE77D"
    fg = "#0C1014"
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            grid3x3(i, j, bg, fg)
            if bg == "#FEE77D":
                bg = "#FEE715"
                fg = "#101820"
            else:
                bg = "#FEE77D"
                fg = "#0C1014"

def fetchVals(chOrSol):
    errorLabel.grid_remove()
    successLabel.grid_remove()

    board = []

    for i in range(9):
        row = []
        for j in range(9):
            val = cells[(i, j)].get()
            if val == "":
                row.append(0)
            else:
                row.append(int(val))
        board.append(row)

    if chOrSol == "checks":
        checkVals(board)
    elif chOrSol == "solves":
        solveVals(board)
         
def checkVals(grid):
    sum = 0
    solution = True

    for i in range(9):
        if solution == False:
            break
        for j in range(9):
            sum += grid[i][j]
            if check(grid, i, j, grid[i][j]) == False:
                solution = False
                break
                
    if solution and sum == 405:
        successLabel.config(text = "Successfully solved!")
        successLabel.grid(row = 15, column = 1, columnspan = 10, padx = 100)
    elif grid[i][j] == 0 and sum != 405:
        errorLabel.config(text = "Board incomplete!")
        errorLabel.grid(row = 15, column = 1, columnspan = 10, padx = 100)
    else:
        errorLabel.config(text = "Board incorrect! Try again.")
        errorLabel.grid(row = 15, column = 1, columnspan = 10, padx = 100)

def solveVals(grid):
    s = solve(grid)
    
    if s == False:
        errorLabel.config(text = "Board unsolvable! Please fix or create a new board.")
        errorLabel.grid(row = 15, column = 1, columnspan = 10, padx = 100)
    else:
        for i in range(9):
            for j in range(9):
                cells[(i, j)].delete(0, 'end')
                cells[(i, j)].insert(0, s[i][j])
        
        successLabel.config(text = "Successfully solved!")
        successLabel.grid(row = 15, column = 1, columnspan = 10, padx = 100)
    
def resetVals():
    errorLabel.grid_remove()
    successLabel.grid_remove()
    
    for i in range(9):
        for j in range(9):
            cell = cells[(i, j)]
            cell.delete(0, 'end')

button = tk.Button(frame, command = lambda: fetchVals("checks"), text = "CHECK", width = 10, height = 2, bg = "#FEE77D", fg = "#0C1014", font = "Prime -14 bold")
button.grid(row = 20, column = 1, columnspan = 5, pady = 16)

button = tk.Button(frame, command = lambda: fetchVals("solves"), text = "SOLVE", width = 10, height = 2, bg = "#FEE715", fg = "#101820", font = "Prime -14 bold")
button.grid(row = 20, column = 3, columnspan = 5, pady = 16)

button = tk.Button(frame, command = resetVals, text = "CLEAR", width = 10, height = 2, bg = "#FEE77D", fg = "#0C1014", font = "Prime -14 bold")
button.grid(row = 20, column = 5, columnspan = 5, pady = 16)

"""button = tk.Button(frame, command = resetVals, text = "RANDOM", width = 10, height = 2, bg = "#FEE77D", fg = "#0C1014", font = "Prime -14 bold")
button.grid(row = 20, column = 5, columnspan = 5, pady = 16)"""

grid9x9()

window.mainloop()