"""
https://leetcode.com/problems/search-a-2d-matrix/

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.


Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
Output: false
Example 3:

Input: matrix = [], target = 0
Output: false


Constraints:

m == matrix.length
n == matrix[i].length
0 <= m, n <= 100
-104 <= matrix[i][j], target <= 104



"""


"""

The idea is to use binary search to check the xistence of a number in matrix

Logically we can imagine n*m matrix as a sorted array (in this case)


"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)  ## Number of rows

        if m == 0:
            return False

        n = len(matrix[0])  ## number of columns

        left = 0;
        right = m * n - 1

        while (left <= right):
            mid_idx = (left + right) // 2
            row = mid_idx // n ##
            col = mid_idx % n

            if matrix[row][col] == target:
                return True
            else:
                if matrix[row][col] > target:
                    right -= 1
                else:
                    left += 1
        return False





