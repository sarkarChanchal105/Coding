"""
https://leetcode.com/problems/jump-game/
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.



Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


"""


## using recustion. Memoization Technique.
## passed 74 test cases out of 75
# class Solution:
#     def canJump(self, nums) -> bool:
#
#         if nums == [0]:
#             return True
#
#         position = 0
#         end_position = len(nums) - 1
#
#         memo = [None] * (end_position + 1)
#         memo[end_position] = True
#
#         return self.canJumpHelper(nums, position, end_position, memo)
#
#     def canJumpHelper(self, nums, position, end_position, memo):
#
#         if memo[position] is not None:
#             return memo[position]
#
#         for i in range(1, nums[position] + 1):
#             current_position = position + i
#             if current_position <= end_position:
#                 if self.canJumpHelper(nums, current_position, end_position, memo):
#                     memo[position] = True
#                     return memo[position]
#
#         memo[position] = False
#         return memo[position]



## Greedy Method
##
""""
Iterating right-to-left, for each position we check if there is a potential jump that reaches a GOOD index (currPosition + nums[currPosition] >= leftmostGoodIndex). If we can reach a GOOD index, then our position is itself GOOD. Also, this new GOOD position will be the new leftmost GOOD index. Iteration continues until the beginning of the array. If first position is a GOOD index then we can reach the last index from the first position.

"""

class Solution:
    def canJump(self, nums) -> bool:
        n=len(nums)
        leftmostGoodIndex=n-1
        for currentPosition in range(n-1,-1,-1):
            if currentPosition+nums[currentPosition]>=leftmostGoodIndex:
                leftmostGoodIndex=currentPosition

        return leftmostGoodIndex==0


object=Solution()

arr=[2,3,1,1,4]
print(object.canJump(arr))