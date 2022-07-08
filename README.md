# Sudoku Solver

### GUI Sudoku utilizing the tkinter library. 
- Solves ***any*** sudoku puzzle input using backtracking, as long as it is solvable
- Checks solved sudoku board (automatically for program, button for user if user-solved)
- **50 *unique* sudoku boards** for the user or program to solve
  - 5 modes (easy, medium, hard, expert, master), each consisting of 10 boards

<img src="example.gif" width = "619" height = "719">

## How To Run
1. Install [Python3](https://www.python.org/downloads/)
2. Install the `requirements.txt` file included in the repo: `pip install -r requirements.txt`
3. Go ahead and run: `python src/sudoku.py`

## How It Works
The solver works by using the *backtracking* algorithm. 

**What is backtracking?** Backtracking is when the computer brute-forces its way to the solution; however, rather than the normal technique of brute-forcing where it goes through all possible solutions (and nonsolutions), it cuts down on the possibilities by immediately ending the process upon determining that the current path will not result in a solution (in this case due to an invalid input). It is like a tree - when it fails on a certain branch, it moves on to the next closest possible branch until it reaches a solution branch or exhausts all branches.

## Issues
Since tkinter is single-threaded, when the program freezes (ie. if the user were to input an unsolvable puzzle), other components will not update until the program is no longer in that state. Where this will be most evident is when the stopwatch updates: the stopwatch will remain at its original time. 

Another possible issue is if there were to be an incredibly hard puzzle inputted that would require the `solveSudoku` method to be called over 1,500,000 times, the solver would be unable to solve the puzzle in order to keep the app from crashing. The arbitrary value should still allow for the vast majority of puzzles to be solved; however, if this issue were to be run into, just increase this limit.

## Why This Was Made
This project was inspired by [Tech With Tim](https://www.youtube.com/c/TechWithTim).

The original goal for this project was to just create a gui app for sudoku which checks the solution upon completion for correctness; however, upon stumbling across the backtracking algorithm and how it can be used to solve sudoku puzzles, I decided to learn it and implement it into the program. Once that component was implemented, I decided to tinker around with the tkinter library by creating a dropdown menu that could be used to choose a mode and from that randomly chooses a sudoku board using a 4-dimensional array (first array for mode, second for random board within the mode, and third and fourth being row and column respectively). Lastly, a stopwatch was implemented to keep track of the time it takes to solve the board (see [Issues](https://github.com/vianmiranda/sudoku-solver#issues)) resulting in the final product. 