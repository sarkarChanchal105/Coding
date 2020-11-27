"""
https://leetcode.com/problems/number-of-islands/submissions/

"""


class Solution:
    def numIslands(self, grid):

        number_of_islands = 0

        if not grid:
            return 0

        rows = len(grid)
        columns = len(grid[0])
        isVisited = [[False for x in range(columns)] for y in range(rows)]

        for i in range(rows):
            for j in range(columns):
                if isVisited[i][j] is False and grid[i][j] == '1':
                    self.depth_first_search(i, j, grid, isVisited, rows, columns)
                    number_of_islands += 1
        return number_of_islands

    def depth_first_search(self, row, col, grid, isVisited, rows, columns):

        isVisited[row][col] = True
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        for k in range(len(dx)):
            next_row = row + dx[k]
            next_col = col + dy[k]
            if self.isSafe(next_row, next_col, rows, columns):
                if isVisited[next_row][next_col] is False and grid[next_row][next_col] == '1':
                     self.depth_first_search(next_row, next_col, grid, isVisited, rows, columns)

    def isSafe(self, row, col, rows, columns):
        return 0 <= row < rows and 0 <= col < columns



array=[
        ["1","1","1"],
        ["0","1","0"],
        ["0","1","0"]
    ]

object=Solution()

result=object.numIslands(array)

print("Result :",result)
