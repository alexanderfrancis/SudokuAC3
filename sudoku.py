"""
-------------------------------------------------------
sudoku.py
9x9 Sudoku Puzzle implementation as described in class
-------------------------------------------------------
CP468
Assignment 2
Authors:  Keven Iskander, Carla Castaneda, Nicole Laslavic, Alexander Francis
__updated__ = "2020-11-02"
-------------------------------------------------------
"""
import utilities
# Some Sudoku puzzle examples taken from here:
# https://dingo.sbs.arizona.edu/~sandiway/sudoku/examples.html

class Node:
    domain = [1,2,3,4,5,6,7,8,9]
    value = 0

    def __init__(self, value):
        self.value = value

class Sudoku:

    def __init__(self):
        f = open('sudoku1.txt', 'r')
        lines = f.readlines()
        if len(lines)!=9:
            print('ERROR: Invalid puzzle file')
            self.table = [[0 for i in range(9)] for j in range(9)]
        else:
            self.table = [[0 for i in range(9)] for j in range(9)]
            for i in range(len(lines)):
                for j in range(len(self.table)):
                    #self.table[i][j] = Node(lines[i][j])
                    self.table[i][j] = int(lines[i][j])

        f.close()

    def __eq__(self, sudoku2):
        if self.table == sudoku2.table:
            return True
        return False


    # Code taken from https://stackoverflow.com/questions/37952851/formating-sudoku-grids-python-3
    def print_table(self):
        print("-"*37)
        
        for i, row in enumerate(self.table):
            print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
            if i == 8:
                print("-"*37)
            elif i % 3 == 2:
                print("|" + "---+"*8 + "---|")
            else:
                print("|" + "   +"*8 + "   |")

        # for x in self.table:
        #     for y in x:
        #         print(y.value, end="")

        # print()


    def valid_col(self, col):
        """
        -------------------------------------------------------
        Returns if a column is valid.
        Parameters: self - Matrix
                    col - column index
        Return: Boolean - True if no repeat numbers (1-9) exist
                          in the column
        -------------------------------------------------------
        """
        visited = []
        result = True
        for i in range(9):
            if (not self.table[i][col] in visited):
                if (self.table[i][col] != 0):
                    visited.append(self.table[i][col])
            else:
                return result == False
        return result
            
    def valid_row(self, row):
        """
        -------------------------------------------------------
        Returns if a row is valid.
        Parameters: self - Matrix
                    row - row index
        Return: Boolean - True is no repeat numbers (1-9) exist
                          in the row
        -------------------------------------------------------
        """
        visited = []
        result = True
        for i in range(9):
            if (not self.table[row][i] in visited):
                if (self.table[row][i] != 0):
                    visited.append(self.table[row][i])
            else:
                return result == False
        return result

    def valid_subsquare(self, row, col):
        """
        -------------------------------------------------------
        Returns if a subsquare is valid.
        Parameters: self - Matrix
                    col - column index
                    row - row index
        Return: Boolean - True is no repeat numbers (1-9) exist
                          in the subsquare
        -------------------------------------------------------
        """
        visited = []
        result = True
        r_index = row
        c_index = col

        #Find top left index of subsquare
        r = False
        c = False
        while r == False or c == False:
            if(r == False):
                if(r_index%3 == 0):
                    r = True
                else:
                    r_index -= 1

            if(c == False):
                if(c_index%3 == 0):
                    c = True
                else:
                    c_index -= 1

        for row in range(r_index, r_index+3):
            for col in range(c_index, c_index+3):
                if(not self.table[row][col] in visited):
                    if (self.table[row][col] != 0):
                        visited.append(self.table[row][col])
                else:
                    return result == False
        return result

    def is_valid(self):
        for i in range(9):
            for j in range(9):
                if self.valid_row(i) == False or self.valid_col(j) == False or self.valid_subsquare(i, j) == False:
                    return False

        return True

    def find_empty(self):
        """
        -------------------------------------------------------
        Returns index of next empty box
        Parameters: self - Matrix
        Return: index - (row, column) - tuple that returns next empty square
        -------------------------------------------------------
        """
        for i in range(9):
            for j in range(9):
                if self.table[i][j] == 0:
                    return (i, j)
        return (-1, -1)

    def backtracking(self):
        """
        -------------------------------------------------------
        Returns solved sudoku puzzle using backtracking(recursive)
        Parameters: self - Matrix
        Return: Boolean values
        -------------------------------------------------------
        """
        index = self.find_empty()
        if index == (-1, -1):
            return True
        else:
            row = index[0]
            col = index[1]
        for i in range(1, 10):
            if self.is_valid() == True:
                self.table[row][col] = i
                if self.backtracking() == True:
                    return True
                self.table[row][col] = 0
        return False

def main():
    sud = Sudoku()
    sud.print_table()
    print(sud.is_valid())

if __name__ == "__main__":
    main()