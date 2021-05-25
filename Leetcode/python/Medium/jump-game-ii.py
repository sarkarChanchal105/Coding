"""
https://leetcode.com/problems/jump-game-ii/

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.



Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2

"""

#
# class Solution:
#     def jump(self, nums) -> int:
#         startingPosition = 0
#         endingPosition = len(nums) - 1
#         min_jumps = float("inf")
#         return self.helperJump(nums, startingPosition, endingPosition, min_jumps)
#
#     def helperJump(self, nums, startingPosition, endingPosition, min_jumps):
#
#         #print("startingPosition:{}".format(startingPosition))
#         if endingPosition == startingPosition:
#             return 0
#
#         for i in range(1, nums[startingPosition]+1):
#             currentPosition = i + startingPosition
#             #print("currentPosition:{}".format(currentPosition))
#             if currentPosition <= endingPosition:
#                 #print("min_jumps:{}".format(min_jumps))
#                 min_jumps = min(min_jumps, 1+self.helperJump(nums, currentPosition, endingPosition, min_jumps))
#                 #print("min_jumps:{}".format(min_jumps))
#         return min_jumps


class Solution:
    def jump(self, nums) -> int:
        n = len(nums)
        startingPosition = 0
        endingPosition = len(nums) - 1
        min_jumps = float("inf")
        memo = [[min_jumps] * n] * n

        self.helperJump(nums, startingPosition, endingPosition, min_jumps,memo)
        for i in range(n):
            print(memo[i])


    def helperJump(self, nums, startingPosition, endingPosition, min_jumps,memo):

        # print("startingPosition:{}".format(startingPosition))
        if endingPosition == startingPosition:
            return 0

        for i in range(1, nums[startingPosition] + 1):
            currentPosition = i + startingPosition
            # print("currentPosition:{}".format(currentPosition))
            if currentPosition <= endingPosition:
                # print("min_jumps:{}".format(min_jumps))
                # if memo[currentPosition][endingPosition]==float("inf"):
                #     min_jumps = min(min_jumps,  1+self.helperJump(nums, currentPosition, endingPosition, min_jumps,memo))
                #     memo[currentPosition][endingPosition]=min_jumps
                # else:
                #     min_jumps = min(min_jumps, memo[currentPosition][endingPosition])
                exp=self.helperJump(nums, currentPosition, endingPosition, min_jumps,memo)
                if exp is None:
                    print("Here")
                memo[currentPosition][endingPosition]=min(memo[currentPosition][endingPosition],1+exp)

                # print("min_jumps:{}".format(min_jumps))




object=Solution()

arr=[2,3,1,1,4]
#arr=[2,1,3,2,3,4,5,1,2,8]
#arr=[5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]
print(object.jump(arr))