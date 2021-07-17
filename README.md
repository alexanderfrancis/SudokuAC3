# **SudokuAC3**

This Sudoku solver uses the AC3 constraint-checking algorithm to begin trying to solve a given puzzle. If AC3 is not able to completely solve the puzzle by itself, the program will invoke a backtracking algorithm to finish the remaining steps.


### Acceptable Puzzle Formats

The program will accept Sudoku puzzles that are in the form of a *.txt* file. The file must consist of a 9x9 representation of the puzzle you wish to solve, where each row in the text file corresponds to a row in the puzzle and no spaces in-between characters or lines. Here is an example:

![Text File Example](https://i.imgur.com/zNpe8Yw.png)

### How to Run

The program is simple to execute, simply change the line in the Sudoku class definition where the file is open and replace the string literal of the target to any valid text puzzle file that you would like to compute results for. Once you have the puzzle replaced, run the main method in your preferred IDE or command-line.

```python
f = open('sudoku7.txt', 'r')             #replace sudoku7.txt
```

### Example Output

Here is an instance of the program solving the seventh puzzle included in the repository using the command-line:

![Runtime Example](https://i.imgur.com/LKrxmb6.png)
