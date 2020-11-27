"""
https://leetcode.com/problems/subarray-sum-equals-k/solution/

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

"""

class Solution:
    def subarraySum(self, nums, k) -> int:
        count = 0
        accumulative = {0:1}
        curSum = 0
        for index, num in enumerate(nums):
            curSum += num
            if curSum - k in accumulative:
                count += accumulative[curSum - k]
            accumulative[curSum] = accumulative[curSum] + 1 if curSum in accumulative else 1
        return count

object=Solution()

nums=[3,4,7,2,-3,1,4,2]

k=7
print(object.subarraySum(nums,k))

