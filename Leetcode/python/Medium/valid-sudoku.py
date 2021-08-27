import numpy as np


class Solution:
    def isValidSudoku(self, board) -> bool:

        ## Check rows

        # print("Checking rows")
        for i in range(len(board[0])):
            temp = board[i]
            if not self.checkValidity(temp):
                return False

        # print("Checking Columns")
        for j in range(len(board[0])):
            temp = []
            for k in range(len(board)):
                temp.append(board[k][j])
            if not self.checkValidity(temp):
                return False

        # print("Checking 3x3")
        board = np.array(board)  ## Convert the array to numpy array

        for row in range(0, 9, 3):  ## Since 9x9 matrix.  Sub Matrix 3x3
            for col in range(0, 9, 3):
                startRow = row  ## starting row
                endRow = row + 3  ## end row
                startCol = col  ## starting column
                endCol = col + 3  ## End column
                grid = board[startRow:endRow, startCol:endCol]  ## get the grid with 3x3 sub matric
                # print("Grid", grid)
                temp = []

                ## Get all elements of the sub matrix (3x3)
                for i in range(3):
                    for j in range(3):
                        temp.append(grid[i][j])
                if not self.checkValidity(temp):  ## check for the validity
                    return False

        return True

    def checkValidity(self, array):

        # print("array=", array)
        hashTable = {}
        for a in array:
            if a != ".":
                if a in hashTable:
                    print("a =", a)
                    return False
                else:
                    hashTable[a] = 1
        return True