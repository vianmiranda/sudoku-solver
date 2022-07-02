import tkinter as tk
from tkinter import *
from check import check
from solve import solve
import os

window = tk.Tk()
window.title("Sudoku")
window.geometry("750x825")
window.config(background = "#005f60")
window.resizable(width = False, height = False)

frame = tk.Frame(window, bg = "#009AAF")
frame.place(relwidth = 0.96, relheight = 0.96, relx = 0.02, rely = 0.02)

label = tk.Label(frame, text = " Sudoku ", bg = "#009AAF", fg = "#FF9D36", font = "helvetica -36 bold underline").grid(row = 1, column = 1, columnspan = 10, padx = 100)

label = tk.Label(frame, text = "Solve the Sudoku board or have the CPU do it for you!", bg = "#009AAF", fg = "#FFB240", font = "helvetica 11 bold italic").grid(row = 2, column = 1, columnspan = 10, padx = 100)

#Label if sudoku board is not solvable
errorLabel = tk.Label(frame, text = "", bg = "#009AAF", fg = "red", font = "helvetica 12 bold")

#Label if sudoku board is solved
successLabel = tk.Label(frame, text = "", bg = "#009AAF", fg = "#24F224", font = "helvetica 12 bold")

cells = {}

def isInt (n):
    return ((n.isdigit() or n == "") and len(n) < 2)

def grid3x3(row, col, bg, fg):
    for i in range(3):
        for j in range(3):
            entry = tk.Entry(frame, width = 8, bg = bg, fg = fg, font = "helvetica -16 bold", justify = "center", validate = "key", validatecommand = (window.register(isInt), "%P"))
            entry.grid(row = row+i+3, column = col+j+1, padx = 2, pady = 2, ipady = 20)
            cells[(row+i, col+j)] = entry

def grid9x9():
    bg = "#faab36"
    fg = "#008083"
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            grid3x3(i, j, bg, fg)
            if bg == "#faab36":
                bg = "#f78104"
                fg = "#249ea0"
            else:
                bg = "#faab36"
                fg = "#008083"

def fetchVals(chOrSol):
    errorLabel.config(text = "")
    successLabel.config(text = "")
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
    errorLabel.config(text = "")
    successLabel.config(text = "")
    for i in range(9):
        for j in range(9):
            cell = cells[(i, j)]
            cell.delete(0, 'end')

button = tk.Button(frame, command = lambda: fetchVals("checks"), text = "Check", width = 10, height = 2, bg = "#faab36", fg = "#008083", font = "helvetica -14 italic bold")
button.grid(row = 20, column = 1, columnspan = 5, pady = 16)

button = tk.Button(frame, command = lambda: fetchVals("solves"), text = "Solve", width = 10, height = 2, bg = "#f78104", fg = "#249ea0", font = "helvetica -14 italic bold")
button.grid(row = 20, column = 3, columnspan = 5, pady = 16)

button = tk.Button(frame, command = resetVals, text = "Clear", width = 10, height = 2, bg = "#faab36", fg = "#008083", font = "helvetica -14 italic bold")
button.grid(row = 20, column = 5, columnspan = 5, pady = 16)    

grid9x9()

window.mainloop()