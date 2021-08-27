"""
https://leetcode.com/problems/number-of-closed-islands/

Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.



"""


class Solution:
    def closedIsland(self, grid) -> int:

        rows = len(grid)
        cols = len(grid[0])

        isVisited = [[False for _ in range(cols)] for _ in range(rows)]

        # print(isVisited)

        no_of_islands = 0

        for row in range(rows):
            for col in range(cols):
                if not isVisited[row][col] and grid[row][col]==0:
                    self.depthFirstSearch(grid, isVisited, row, col, rows, cols)
                    no_of_islands += 1
        return no_of_islands

    def depthFirstSearch(self, grid, isVisited, row, col, rows, cols):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, 1, -1]

        isVisited[row][col] = True

        for i in range(len(dx)):
            newRow = row + dx[i]
            newCol = col + dy[i]
            if self.isSafe(newRow, newCol, rows, cols) and isVisited[newRow][newCol] == False and  grid[newRow][newCol]==0:
                return self.depthFirstSearch(grid, isVisited, newRow, newCol, rows, cols)

    def isSafe(self, row, col, rows, cols):

        return 0 < row < rows and 0 < col < cols


object = Solution()

grid = [[1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0]
        ]

print(object.closedIsland(grid))
