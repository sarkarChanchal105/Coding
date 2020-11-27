"""
https://leetcode.com/problems/increasing-triplet-subsequence/

iven an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true
Example 2:

Input: [5,4,3,2,1]
Output: false

"""


class Solution:
    def increasingTriplet(self, nums):

        first=float("inf")  ## Initlaize with infiture value
        second=float("inf")

        ## for a n element in the array, if less than equal to first then make that first
        ## if less than second the make that second
        ## else we have found a triplet
        for a in nums:
            if a<=first:
                first=a
            elif a<=second:
                second=a
            else:
                return True
        return False