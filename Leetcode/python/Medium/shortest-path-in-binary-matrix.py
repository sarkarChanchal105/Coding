"""
https://leetcode.com/problems/shortest-path-in-binary-matrix/

1091. Shortest Path in Binary Matrix
Medium

1680

90

Add to List

Share
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.



Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1


Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1


N : Number of cells.
Time Complexity : O(N),
Space: O(N) : Most number of elements that can be enqued

"""

from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:

        ##  Get the boundaries of the grid
        maxRow = len(grid) - 1
        maxCol = len(grid[0]) - 1

        ## Trivial Situation
        if grid[0][0] != 0 or grid[maxRow][maxCol] != 0:
            return -1

        ## from a given point I can move to 8 directions
        possibleDirection = [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]

        ## Define a queue. Will BFS to find the shortest Path
        q = deque()
        Starting = (0, 0) ## start from 0,0 as the problem states

        q.append(Starting) ## append the starting node in the queue
        grid[0][0] = 1 ## set the value to 1


        while q: # while the queue is not empty

            currentCell = q.popleft() ## pop one element

            currentCellRow = currentCell[0] # get the row and colum of the current cell
            currentCellCol = currentCell[1]

            distance = grid[currentCellRow][currentCellCol] ## get the distance upto the current cell

            ## check if we have already reached the end , just return the distance
            if (currentCellRow, currentCellCol) == (maxRow, maxCol):
                return distance

            ## Elese from current point move to all possible 8 directions
            for possible in possibleDirection:
                newPossibleRow = currentCellRow + possible[0]
                newPossibleCol = currentCellCol + possible[1]
                tupple = (newPossibleRow, newPossibleCol)

                if self.isaValidCell(grid, tupple): ## if its a valid cell then
                    grid[newPossibleRow][newPossibleCol] = distance + 1 ## update the sitance in the cell
                    q.append(tupple) ## add the current cell in the queue for further processing

        return -1

    def isaValidCell(self, grid, tupple):

        maxRow = len(grid) - 1
        maxCol = len(grid[0]) - 1

        newRow = tupple[0]
        newCol = tupple[1]

        # valueAtNewCell=grid[newRow][newCol]

        if newRow >= 0 and newRow <= maxRow and newCol >= 0 and newCol <= maxCol: ## if the current cell is not outside the boundary of the grid

            if grid[newRow][newCol] == 0: ## check if the value at the current cell is zero.
                return True
        return False


object=Solution()
grid = [
        [1,0,0],
        [1,1,0],
        [1,1,0]
        ]

grid=[
        [0,1],
        [1,0]
]

print(object.shortestPathBinaryMatrix(grid))









