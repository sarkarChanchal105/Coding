"""
https://leetcode.com/problems/squares-of-a-sorted-array/

Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.



Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
"""

# class Solution:
#     def sortedSquares(self, A: List[int]) -> List[int]:

#         return sorted([x**2 for x in A])

class Solution:
    def sortedSquares(self, A):
        result = [None for _ in A]
        left, right = 0, len(A) - 1
        for index in range(len(A)-1, -1, -1):
            if abs(A[left]) > abs(A[right]):
                result[index] = A[left] ** 2
                left += 1
            else:
                result[index] = A[right] ** 2
                right -= 1
        return result


object=Solution()
array=[-4,-1,0,3,10]
print(object.sortedSquares(array))



for i in range(10,1,1):
    print(i)

