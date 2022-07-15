"""
https://leetcode.com/problems/matrix-diagonal-sum/submissions/

1572. Matrix Diagonal Sum
Easy

1204

22

Add to List

Share
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.



Example 1:


Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8
Example 3:

Input: mat = [[5]]
Output: 5


Constraints:

n == mat.length == mat[i].length
1 <= n <= 100
1 <= mat[i][j] <= 100


"""
from typing import List
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        n = len(mat)
        ## Diagonal 1
        summary = 0
        for i in range(n):
            summary += mat[i][i]


         ## Diagonal 2
        for i in range(n - 1, -1, -1):
            summary += mat[i][n-i-1]

        ## if the number of columns is odd. then we have counted the middle element at the cross section
        ## of both diagonals. Sutract that element from the entire sume
        if n % 2 != 0:
            idx = n // 2
            summary -= mat[idx][idx]

        return summary



object=Solution()
array=[[7,3,1,9],[3,4,6,9],[6,9,6,6],[9,5,8,5]]

print(object.diagonalSum(array))

