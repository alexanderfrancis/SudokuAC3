"""
-------------------------------------------------------
sudoku.py
9x9 Sudoku Puzzle implementation as described in class
-------------------------------------------------------
CP468
Assignment 2
Authors:  Keven Iskander, Carla Castaneda, Nicole Laslavic, Alexander Francis
__updated__ = "2020-11-09"
-------------------------------------------------------
"""
import utilities
import time
# Some Sudoku puzzle challenges taken from here:
# https://dingo.sbs.arizona.edu/~sandiway/sudoku/examples.html

class Node:
    domain = [1,2,3,4,5,6,7,8,9]
    value = 0
    def __init__(self, value, domain = domain,row=0,col=0):
        self.value = value
        self.domain = domain
        self.neighbours=[]
        self.row=row
        self.col=col
        return


    def __int__(self):
        return int(self.value)


class Sudoku:
    def __init__(self):
        """
        -------------------------------------------------------
        Populates sodoku puzzle
        Parameters: self - Matrix
        Return: None
        -------------------------------------------------------
        """
        self.lvalues = []
        f = open('sudoku7.txt', 'r')
        lines = f.readlines()
        if len(lines)!=9:
            print('ERROR: Invalid puzzle file')
            self.table = [[Node(0) for i in range(9)] for j in range(9)]
        else:
            self.table = [[0 for i in range(9)] for j in range(9)]
            for i in range(len(self.table)):
                for j in range(len(self.table)):
                    self.lvalues.append(int(lines[i][j]))
                    self.table[i][j] = Node(int(lines[i][j]))
                    self.table[i][j].row=i
                    self.table[i][j].col=j
                    if self.table[i][j].value !=0: 
                        self.table[i][j].domain = [self.table[i][j].value]
            for k in range(len(self.table)):
                for l in range(len(self.table)):
                    if self.table[k][l].value == 0: self.table[k][l].domain = self.update_domain(k,l)
        f.close()
        return


    def print_table(self):
        """
        -------------------------------------------------------
        Prints sodoku puzzle
        Parameters: self - Matrix
        -------------------------------------------------------
        """
        print("-"*31)
        i = 0
        for x in self.table:
            for y in x:
                if i % 9 == 0:
                    print("|", end="")
                if y.value == 0:
                    print(" {} ".format(" "), end="")
                else:    
                    print(" {} ".format(y.value), end="")
                i += 1
                if i % 3 == 0:
                    print('|', end="")
                if i % 9 == 0 and i != 0:
                    print()
                if i % 27 == 0:
                    print("-"*31)
        return


    def print_domain(self, row, col):
        """
        -------------------------------------------------------
        Prints domain of Node at specified index
        Parameters: self - Matrix
                    row - row index
                    col - column index
        Return: None
        -------------------------------------------------------
        """
        print(self.table[row][col].domain)
        return


    def valid_col(self, col):
        """
        -------------------------------------------------------
        Returns if a column is valid.
        Parameters: self - Matrix
                    col - column index
        Return: Boolean - True if no repeat numbers (1-9) exist in the column
                          False if repeat numbers in column
        -------------------------------------------------------
        """
        visited = []
        result = True
        for i in range(9):
            if (not self.table[i][col].value in visited):
                if (self.table[i][col].value != 0):
                    visited.append(self.table[i][col].value)
            else:
                return result == False
        return result
            

    def valid_row(self, row):
        """
        -------------------------------------------------------
        Returns if a row is valid.
        Parameters: self - Matrix
                    row - row index
        Return: Boolean - True if no repeat numbers (1-9) exist in the row
                          False if repeat numbers in row
        -------------------------------------------------------
        """
        visited = []
        result = True
        for i in range(9):
            if (not self.table[row][i].value in visited):
                if (self.table[row][i].value != 0):
                    visited.append(self.table[row][i].value)
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
        Return: Boolean - True if no repeat numbers (1-9) exist in the subsquare
                          False if repeat numbers in subsquare
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
                if(not self.table[row][col].value in visited):
                    if (self.table[row][col].value != 0):
                        visited.append(self.table[row][col].value)
                else:
                    return result == False
        return result


    def is_valid(self):
        """
        -------------------------------------------------------
        Returns if a Sudoku puzzle is valid. Checks each node to see if row, col
        and subsquares are valid.
        Parameters: self - Matrix
                    col - column index
                    row - row index
        Return: Boolean - True if valid
                          False if not valid
        -------------------------------------------------------
        """
        for i in range(9):
            for j in range(9):
                if self.valid_row(i) == False or self.valid_col(j) == False or self.valid_subsquare(i, j) == False:
                    return False
        return True


    def update_domain(self, row, col):
        """
        -------------------------------------------------------
        Returns updated domain for node object where node value does not equal 0.
        Parameters: self - Matrix
                    row - row index
                    col - column index
        Return: List - New domain
        -------------------------------------------------------
        """
        dom = [1,2,3,4,5,6,7,8,9]
        visited = []
        if self.table[row][col].value == 0:
            for i in range(9):
                if not self.table[i][col].value == 0 and not self.table[i][col] in visited:
                    visited.append(self.table[i][col].value)
            for i in range(9):
                if not self.table[row][i].value == 0 and not self.table[row][i] in visited:
                    visited.append(self.table[row][i].value)
            r_index = row
            c_index = col
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
                    if(not self.table[row][col].value in visited):
                        if (self.table[row][col].value != 0):
                            visited.append(self.table[row][col].value)
            new_visited = []
            for i in dom:
                if i not in visited:
                    new_visited.append(i)
            visited = new_visited
            return visited
        return [self.table[row][col].value]


    def backtracking(self):
        """
        -------------------------------------------------------
        Resursively solves sodoku puzzles using backtracking
        Parameters: self - Matrix
        Return: Boolean
        -------------------------------------------------------
        """
        index = self.MRV_heuristic()
        if index == (-1, -1):
            return True
        else:
            row = index[0]
            col = index[1]
        self.table[row][col].domain = self.update_domain(row, col)
        for i in self.table[row][col].domain:
            if self.is_valid() == True:
                self.table[row][col].value = i
                if self.backtracking() == True:
                    return True
                self.table[row][col].value = 0
        return False


    def MRV_heuristic(self):
        """
        -------------------------------------------------------
        Finds the minimum remaining value.
        Parameters: self - Matrix
        Return: index - (row, col) 
        -------------------------------------------------------
        """
        temp_min = [1,2,3,4,5,6,7,8,9]
        index = (-1,-1)
        for i in range(9):
            for j in range(9):
                if len(self.table[i][j].domain) < len(temp_min) and self.table[i][j].value == 0:
                    temp_min = self.table[i][j].domain
                    index = (i,j)
        return index


    def find_neighbours(self,i,j):
        """
        -------------------------------------------------------
        Finds the nodes which constraints of current node called neighbours in this case
        Parameters: self - Sudoku 
                    i- row
                    j-column
        Return: neighbours- list of nodes which are all "neighbours" or constraints of the node in position i,j
        -------------------------------------------------------
        """
        neighbours=[]
        original_i=i
        original_j=j
        for k in range (len(self.table)):
            if (not self.table[i][k] in neighbours and self.table[i][k]!=self.table[original_i][original_j]):
                neighbours.append(self.table[i][k])
        for l in range (len(self.table)):
            if (not self.table[l][j] in neighbours and self.table[l][j]!=self.table[original_i][original_j]):
                neighbours.append(self.table[l][j])
        r = False
        c = False
        while r == False or c == False:
            if(r == False):
                if(i%3 == 0):
                    r = True
                else:
                    i -= 1
            if(c == False):
                if(j%3 == 0):
                    c = True
                else:
                    j -= 1
        for row in range(i, i+3):
            for col in range(j, j+3):
                if(not self.table[row][col] in neighbours and self.table[row][col]!=self.table[original_i][original_j]):
                    neighbours.append(self.table[row][col])
        self.table[original_i][original_j].neighbours=neighbours
        return neighbours


    def constraints(self):
        """
        -------------------------------------------------------
        Gets constraints and arranges in arc pairs
        Parameters: self - Sudoku 
        Return: constraints - list of tuples with a constraint pairs
        -------------------------------------------------------
        """
        constraints=[]
        for i in range (len(self.table)):
            for j in range (len(self.table)):
                neighbours=self.find_neighbours(i,j)
                for k in range (len(neighbours)):
                    constraints.append((self.table[i][j],self.table[i][j].neighbours[k]))
        return constraints


    def AC3(self,constraints):
        """
        -------------------------------------------------------
        Arc consistancy algorithm which makes every variable arc-consistent
        Parameters: self - Sudoku 
                    constraints- constraints in pairs (node,neighbour)
        Return: Boolean - True if no inconsistancies found and False otherwise
        -------------------------------------------------------
        """
        cons_q=utilities.Queue()
        for i in constraints:
            cons_q.insert(i)
        print("length of queue: ",len(cons_q))
        while (cons_q.is_empty()==False):
            arc=cons_q.remove()
            for i in range(len(self.table)):
                for k in range (len(self.table)):
                    if (self.table[i][k].row==arc[0].row and self.table[i][k].col==arc[0].col):
                        node=self.table[i][k]
            revised=self.revise(node,arc[1])
            if (revised[0]):
                if (len(revised[1].domain)==0):
                    return False
                for neighbour in revised[1].neighbours:
                    if (neighbour!=arc[1]):
                        for j in range(len(neighbour.neighbours)):
                            if (neighbour.neighbours[j]==node):
                                neighbour.neighbours[j]=revised[1]
                        cons_q.insert((neighbour,revised[1]))
            print("length of queue: ",len(cons_q))
        return True

        
    def revise(self,x,y):
        """
        -------------------------------------------------------
        Checks if theres a a value in x.domain that does not satisfy
        the constraint between c and y
        Parameters: self - Sudoku 
                    x- node which will be revising domain
                    y- neighbour
        Return: revised - Boolean if domain of x was changed will return true else false
        -------------------------------------------------------
        """
        revised=False
        return_node=x
        for i in x.domain:
            not_satisfied=True
            for j in y.domain:
                if i!=j:
                    not_satisfied=False
            if not_satisfied:
                x.domain.remove(i)
                self.table[x.row][x.col]=x
                revised=True
                return_node=self.table[x.row][x.col]
        return revised, return_node


    def AC3_table(self):
        """
        -------------------------------------------------------
        Populates table by using updated domains per Node
        Parameters: self - Sudoku 
        Return: revised - None
        -------------------------------------------------------
        """
        for i in range(9):
            for j in range(9):
                if (len(self.table[i][j].domain) == 1):
                    value = self.table[i][j].domain[0]
                    self.table[i][j].value = value
        return


def main():
    st = time.time()
    sud = Sudoku()

    print("BEFORE: ")
    sud.print_table()
    print()

    print("AFTER AC3: ")
    constraints=sud.constraints()
    sud.AC3(constraints)
    # print("Is solvable using AC3: ", val)
    sud.AC3_table()
    sud.print_table()
    print()
    flag=True
    for i in range (len(sud.table)):
        for j in range(len(sud.table)):
            if (sud.table[i][j].value==0):
                flag=False
                break

    if(flag==True):
        print("The AC-3 algorithm was able to solve the Sudoku Puzzle")
    else:
        print("The AC-3 algorithm was NOT able to fully solve the Sudoku Puzzle")
        print()
        print("backtracking will solve the Sudoku")
        print()
        print("AFTER BACKTRACKING: ")
        sud.backtracking()
        sud.print_table()

    print("Total Execution Time: %s seconds" % (time.time()-st))

if __name__ == "__main__":
    main()
