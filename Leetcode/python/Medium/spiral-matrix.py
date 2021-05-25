"""
https://leetcode.com/problems/spiral-matrix/

Given an m x n matrix, return all elements of the matrix in spiral order.



Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

"""


class Solution:
    def spiralOrder(self, matrix):
        result=[]
        startRow=startCol=0
        endRow=len(matrix)-1
        endCol=len(matrix[0])-1

        while startRow<=endRow and startCol<=endCol:

            ## Top Border
            for col in range(startCol,endCol+1):
                #print(matrix[startRow][col], end=' ')
                result.append(matrix[startRow][col])

            ## Right Border
            for row in range(startRow+1, endRow+1):
                #print(matrix[row][endCol], end=' ')
                result.append(matrix[row][endCol])

            ## Bottom Border
            for col in range(endCol-1,startCol-1,-1):
                #print(matrix[endRow][col], end=' ')
                # Edge case when there is a single row in the middle fo the matrix
                if startRow==endRow:
                    break
                result.append(matrix[endRow][col])

            ## Left Border
            for row in range(endRow-1,startRow,-1):
                #print(matrix[row][startCol],end=' ')
                # Edge case when there is a single column in the middle of the matric
                if startCol==endCol:
                    break
                result.append(matrix[row][startCol])



            startRow+=1
            endCol-=1
            startCol+=1
            endRow-=1
        return  result












array=[[1,2,3],[4,5,6],[7,8,9]]
array=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
object=Solution()
print(object.spiralOrder(array))

