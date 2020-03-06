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

from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        dict=defaultdict(int)
        dict[0]=1
        count=sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            if (sum-k) in dict.keys():
                count+=dict[sum-k]

