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

    def __init__(self, value, domain = domain,row=0,col=0):
        self.value = value
        self.domain = domain
        self.neighbours=[]
        self.row=row
        self.col=col

    def __int__(self):
        
        return int(self.value)

class Sudoku:

    def __init__(self):
        f = open('sudoku2.txt', 'r')
        lines = f.readlines()
        if len(lines)!=9:
            print('ERROR: Invalid puzzle file')
            self.table = [[Node(0) for i in range(9)] for j in range(9)]
        else:
            self.table = [[0 for i in range(9)] for j in range(9)]
            for i in range(len(self.table)):
                for j in range(len(self.table)):
                    self.table[i][j] = Node(int(lines[i][j]))
                    self.table[i][j].row=i
                    self.table[i][j].col=j
                    if self.table[i][j].value !=0: 
                        self.table[i][j].domain = [self.table[i][j].value]


            for k in range(len(self.table)):
                for l in range(len(self.table)):
                    if self.table[k][l].value == 0: self.table[k][l].domain = self.update_domain(k,l)

        f.close()

    def __eq__(self, sudoku2):
        if self.table == sudoku2.table:
            return True
        return False


    # Code taken from https://stackoverflow.com/questions/37952851/formating-sudoku-grids-python-3
    def print_table(self):
        print("-"*37)
        
        for i, row in enumerate(self.table):
            print(("|" + " {}   {}   {} |"*3).format(*[x.value if x.value != 0 else " " for x in row]))
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

    def print_domain(self, row, col):
        print(self.table[row][col].domain)


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
        Return: Boolean - True is no repeat numbers (1-9) exist
                          in the row
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
                if(not self.table[row][col].value in visited):
                    if (self.table[row][col].value != 0):
                        visited.append(self.table[row][col].value)
                else:
                    return result == False
        return result

    def is_valid(self):
        for i in range(9):
            for j in range(9):
                if self.valid_row(i) == False or self.valid_col(j) == False or self.valid_subsquare(i, j) == False:
                    return False

        return True


    def update_domain(self, row, col):
        """
        -------------------------------------------------------
        Returns updated domain for node object where value != 0.
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
            
            new_visited = []
            for i in dom:
                if i not in visited:
                    new_visited.append(i)

            # print(new_visited)

            visited = new_visited
            # print(visited
            
            return visited
        return [self.table[row][col].value]



    def backtracking(self):
        """
        -------------------------------------------------------
        Returns solved sudoku puzzle using backtracking(recursive)
        Parameters: self - Matrix
        Return: Boolean values
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
                if(not self.table[row][col] in neighbours and self.table[row][col]!=self.table[original_i][original_j]  ):

                    neighbours.append(self.table[row][col])

        self.table[original_i][original_j].neighbours=neighbours

        return neighbours

    def constraints(self):

        constraints=[]

        for i in range (len(self.table)):
            for j in range (len(self.table)):

                neighbours=self.find_neighbours(i,j)

                for k in range (len(neighbours)):

                    constraints.append((self.table[i][j],self.table[i][j].neighbours[k]))


                    # if (i==0 and j==1):
                    #     #print("i",i," ","j",j)
                    #     print((self.table[i][j].value,self.table[i][j].neighbours[k].value))

        return constraints

    def AC3(self,constraints):
        cons_q=utilities.Queue()

 

        for i in constraints:
            cons_q.insert(i)
            # print(i[0].value)
        
        while (cons_q.is_empty()==False):
            arc=cons_q.remove()
            # print(arc)

            revised=self.revise(arc[0],arc[1])
            #print("revised value", revised)
            if (revised[0]):
                


                if (len(revised[1].domain)==0):
                    return False


                for neighbour in revised[1].neighbours:
                    if (neighbour!=arc[1]):
                        for j in range(len(neighbour.neighbours)):
                            if (neighbour.neighbours[j]==arc[0]):
                                neighbour.neighbours[j]=revised[1]
                                #print("domain neigh before",arc[0].domain)
                                #print("domain neigh after",revised[1].domain)
                                
                        cons_q.insert((neighbour,revised[1]))

        return True

        

    def revise(self,x,y):

        #rint("X-domain",x.domain)
        #print("y-domain",y.domain)
        revised=False
        return_node=x
        
        for i in x.domain:
            invalid=True
            for j in y.domain:
                if i!=j:
                    invalid=False
            if invalid:
                #print("--------------")
                #print("before removing",x.domain)
                #print("removing",i)
                x.domain.remove(i)
                #print("new domain",x.domain)
                self.table[x.row][x.col]=x
                #print("new node domain",self.table[x.row][x.col].domain)
                revised=True
                return_node=self.table[x.row][x.col]
  

        return revised, return_node

    def AC3_table(self):
        for i in range(9):
            for j in range(9):
                if (len(self.table[i][j].domain) == 1):
                    value = self.table[i][j].domain[0]
                    self.table[i][j].value = value
        return



def main():
    sud = Sudoku()

    print("BEFORE: ")
    sud.print_table()
    print()
    
    print("AFTER AC3: ")
    constraints=sud.constraints()
    sud.AC3(constraints)

    # for row in range(len(sud.table)):
    #     for col in range(len(sud.table)):
    #         sud.print_domain(row,col)

    sud.AC3_table()
    sud.print_table()
    print()

    print("AFTER BACKTRACKING: ")
    sud.backtracking()
    sud.print_table()

 
if __name__ == "__main__":
    main()