"""

https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.

Return the number of negative numbers in grid.



Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
Example 3:

Input: grid = [[1,-1],[-1,-1]]
Output: 3
Example 4:

Input: grid = [[-1]]
Output: 1


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100
"""


# class Solution:
#     def countNegatives(self, grid):
#         count_=0
#         for a in grid:
#             for b in a:
#                 if b<0:
#                     count_+=1
#         return count_


# class Solution:
#     def countNegatives(self, grid):
#         count_=0
#         for a in grid:
#             for b in a:
#                 if b<0:
#                     count_+=1
#         return count_


class Solution:
    def countNegatives(self, grid) -> int:
        count_ = 0
        num_row = len(grid)
        num_col = len(grid[0])

        if num_row == 0:
            return 0
        if num_col == 0:
            return 0

        ## Take care of the edge cases
        if num_col == 2 and num_row == 1:
            for a in grid[0]:
                if a < 0:
                    count_ += 1
            return count_

        for i in range(num_row):
            for j in range(num_col):
                if grid[i][j] < 0:  # if we find the a negative number there no need to traverse rest of the
                    # columns in the row.
                    count_ += num_col - j
                    break

        return count_


object= Solution()

grid=[[7,-3]]
#grid=[[3,2],[-3,-3],[-3,-3],[-3,-3]]
print(object.countNegatives(grid))