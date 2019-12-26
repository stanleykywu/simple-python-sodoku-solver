# Simple Python Sudoku Solver
Using backtracking to solve and create Sudoku puzzles 

- Use backtracking recursion to be able to solve a sudoku board
- Generate random sudoku board
  - Create random permutations of first 9 counting numbers (1, 2, ... 8, 9)
    - Place them in the three diagonal boxes of empty sudoku board (these only have box validity and not row/column)
    - Fill in the rest recursively (backtrack solving)
  - Randomize the positions of all 81 boxes
    - For every position, remove and check to see if still only one unique solution
    - Remove if only one solution, keep if more than one
  
