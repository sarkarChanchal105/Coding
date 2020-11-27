""""
https://leetcode.com/problems/monotonic-array/

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.



Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
Example 4:

Input: [1,2,4,5]
Output: true
Example 5:

Input: [1,1,1]
Output: true


Note:

1 <= A.length <= 50000
-100000 <= A[i] <= 100000



"""


class Solution:
    def isMonotonic(self, array: List[int]) -> bool:

        """
        The idea is to find the number of increasing elements in the array and the number of decreasing elements in the array
        Monotonic Array:
        1. if all numbers are equal then count_decreasing and count_increasing will be zero
        2. Atleast one of  count_decreasing or count_increasing will be zero
        """

        n = len(array)  ## Get the number of elements in the array

        count_decreasing = count_increasing = 0

        ## Calculate the number of decreasing elements in the array

        for i in range(1, n):
            if array[i - 1] > array[i]:
                count_decreasing += 1
        ## Calculate the number of incrasing  elements in the array
        for i in range(1, n):
            if array[i - 1] < array[i]:
                count_increasing += 1

        if count_increasing * count_decreasing == 0:  ## if at leas one of them is zero
            return True

        return False

