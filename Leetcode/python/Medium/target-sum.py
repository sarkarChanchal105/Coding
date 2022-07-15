"""
https://leetcode.com/problems/target-sum/
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.



Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1


Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000

"""
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        index = 0
        dp = {}
        return self.findTargetSumWaysInner(nums, target, index, dp)

    def findTargetSumWaysInner(self, nums, target, index, dp):
        if index == len(nums):
            if target == 0:
                return 1
        if index >= len(nums):
            return 0

        if target not in dp or index not in dp[target]:
            left = self.findTargetSumWaysInner(nums, target - nums[index], index + 1, dp)
            right = self.findTargetSumWaysInner(nums, target + nums[index], index + 1, dp)

            if target not in dp:
                dp[target] = {}
            dp[target][index] = left + right

        return dp[target][index]


# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         n = len(nums)
#         index = 0

#         return self.findTargetSumWaysInner(nums, target, index, n)


#     def findTargetSumWaysInner(self, nums, target, index, n):

#         if index ==n and target == 0:
#             return 1

#         if index >= n:
#              return 0

#         left=self.findTargetSumWaysInner(nums, target - nums[index], index + 1, n)
#         right=self.findTargetSumWaysInner(nums, target + nums[index], index + 1, n)

#         return left+right


object=Solution()

nums = [1,1,1,1,1]
target = 3

print(object.findTargetSumWays(nums,target))


