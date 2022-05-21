
"""
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.



Example 1:


Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4


Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.

https://leetcode.com/problems/island-perimeter/



"""



class Solution:
    def islandPerimeter(self, grid) -> int:

        rows =len(grid) ## Get the total number of rows
        cols =len(grid[0]) ## get the total number of columns

        peremeter =0

        ## For cell in the grid
        for row in range(rows):
            for col in range(cols):

                if grid[row][col] ==1:   ## check if the current cell is land
                    peremeter+=4 ## add four sides in the permiter calculation

                    if row >0 and grid[row -1][col ]==1: ## check if the cell just above is also land
                        peremeter -=2 ## if Yes, then reduce by 2

                    if col >0 and grid[row][col -1 ]==1: ## check if the cell left to the current cell is also land
                        peremeter -=2 ## if Yes, reduce by 2

        return peremeter



object=Solution()


grid=[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]


print(object.islandPerimeter(grid))
