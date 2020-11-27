"""

https://leetcode.com/problems/longest-continuous-increasing-subsequence/

Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.

A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].



Example 1:

Input: nums = [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
4.
Example 2:

Input: nums = [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly
increasing.


Constraints:

0 <= nums.length <= 104
-109 <= nums[i] <= 109

"""


class Solution:
    def findLengthOfLCIS(self, nums):

        n = len(nums)
        if n == 0:
            return n

        maxLen = 1 ## DEFAULT VALUE OF THE MAXLEN
        start = 0 ## BEGINING OF NEW INCREASING SUBSEQUENCE

        for i in range(len(nums)):
            if i and nums[i-1] >= nums[i]:  ## IF THE CONTINOUS SUBSEQUENCE IS INCREASING
                start = i ## KEEP ON INCREASING THE VARIABLE start
            maxLen = max(maxLen,i-start+1 )
        print(nums)
        print(maxLen)
        return maxLen

#nums = [1, 3, 5, 4, 7]

nums=[1,3,5,7]

#nums=[2,2,2,2,2]
object = Solution()
object.findLengthOfLCIS(nums)

#
# class Solution:
#     def findLengthOfLCIS(self, nums):
#         pass
