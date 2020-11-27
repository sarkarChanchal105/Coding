"""
https://leetcode.com/problems/longest-increasing-subsequence/

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?



"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)  # get the lenght of the array

        ## Handle the edge case
        if n == 0:
            return n
        ## Initliaze the lis array with default value 1
        lis = [1] * n
        ## Lis[i] : denotes longest increasing subsequence up to index i

        ## Initalize maximum
        max = 1

        for i in range(n):
            ## for each element starting from 0 to n-1 th element
            for j in range(i):
                ## if the i th element is grater than any j<i
                if nums[i] > nums[j] and lis[i] < lis[j] + 1:
                    lis[i] = lis[j] + 1

            if lis[i] > max:
                max = lis[i]
        return max