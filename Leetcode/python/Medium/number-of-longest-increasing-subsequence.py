"""
https://leetcode.com/problems/number-of-longest-increasing-subsequence/

Given an integer array nums, return the number of longest increasing subsequences.



Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.



Constraints:

0 <= nums.length <= 2000
-106 <= nums[i] <= 106



"""


class Solution:
    def findNumberOfLIS(self, nums):

        n = len(nums)

        if n == 0:
            return n

        lis = [1] * n
        count = [1] * n

        maxlen = 1

        for i in range(n):  ## for each element from index 0 to n-1
            for j in range(i):  ## for eack elemenbt from index 0 to i-1
                if nums[i] > nums[j]:  ## if sequenc is increasing . i.e for any given j<i, i have nums[i] > nums[j]
                    if lis[i] < lis[j] + 1:  ## if adding the jth element in the seuence incease the LIS
                        lis[i] = lis[j] + 1
                        count[i] = count[j]
                    elif lis[i] == lis[j] + 1:  ## if adding the jth elemnt keeps the lis[i] same then it mean occurence of new subsequence
                        count[i] = count[i] + count[j]

        print(lis)
        print(count)

        maxlen = max(lis)

        result = 0
        for i in range(n):
            if lis[i] == maxlen:
                result += count[i]

        return result


object=Solution()

nums = [1,3,5,4,7]

nums = [80,90,100, 70,71,72, 60,61,62]

#nums = [1,3,5,4,7,8]

#nums = [10,11,8,9,2,6]

#nums = [2,2,2,2,2]
#nums=[1,2,4,3,5,4,7,2]

print(object.findNumberOfLIS(nums))