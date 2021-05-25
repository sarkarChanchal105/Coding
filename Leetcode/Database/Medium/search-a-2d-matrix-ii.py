"""
https://leetcode.com/problems/search-a-2d-matrix-ii/

Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.


Example 1:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
Example 2:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false


Constraints:

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-109 <= matix[i][j] <= 109
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-109 <= target <= 109




"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)  ## Number of rows

        if m == 0:
            return False

        n = len(matrix[0])  ## number of columns

        ## start from the left bottom cell
        row = m - 1
        col = 0

        while col < n and row >= 0:

            if matrix[row][col] == target:
                return True
            else:
                ## if value at row, columne is greater than taret then decrement row
                if matrix[row][col] > target:
                    row -= 1
                else:
                    ## else increase columne
                    col += 1
        return False
