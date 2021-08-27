"""

https://leetcode.com/problems/pascals-triangle-ii/

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]


"""


class Solution:
    def getRow(self, rowIndex: int):

        if rowIndex==0:
            return [1]

        if rowIndex==1:
            return  [1 ,1]

        result =[[1] ,[1 ,1]]
        numRows =rowIndex -2

        currentRow =1
        while numRows>=0:
            tempArray =[None] *(currentRow+2)
            currentRowArray =result[currentRow]
            tempArray[0] =currentRowArray[0]
            for i in range(1 ,len(currentRowArray )):
                tempArray[i ]=currentRowArray[i -1] +currentRowArray[i]
            tempArray[-1] =currentRowArray[-1]

            result.append(tempArray)
            #print(tempArray)
            numRows-=1
            currentRow+=1
        return result[-1]



object=Solution()

rowIndex=5
print(object.getRow(rowIndex))

