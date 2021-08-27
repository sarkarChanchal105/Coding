"""

https://leetcode.com/problems/first-missing-positive/

Given an unsorted integer array nums, find the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.



Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1


Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1



"""

## This one uses extra space for hash set. Need to look into how to optimize the space requirement
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        result=1
        hasshSet=set(nums)
        maxVal=max(nums)
        if maxVal<0:
            return result

        for i in range(1, maxVal+2):
            if i in hasshSet:
                continue
            else:
                return i
