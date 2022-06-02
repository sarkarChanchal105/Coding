"""
https://leetcode.com/problems/transpose-matrix/

Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.





Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
-109 <= matrix[i][j] <= 109

"""
from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        rows = len(matrix)  ## Get the number of rows
        columns = len(matrix[0])  ## Get the number of columns

        ## if the source matrix is MxN then transposed matrix will be NxM
        transposedMatrix = [[None for _ in range(rows)] for _ in range(columns)]

        columnT = 0  ## Column pointer in the transposed matrix
        for row in matrix:  ## for each row in the original matrix
            currRowT = 0  ## Row pointer in the transposed matrix
            for i, element in enumerate(row):
                transposedMatrix[currRowT][columnT] = row[
                    i]  ##row of original matrix becomes the column of the transposed matrix
                currRowT += 1  ## increment the row
            columnT += 1  ## increment the column pointer
        return transposedMatrix


matrix = [[1,2,3],[4,5,6],[7,8,9]]

object=Solution()

print(object.transpose(matrix))