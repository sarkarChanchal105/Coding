"""
https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [0]
Output: 0
Example 4:

Input: nums = [-1]
Output: -1
Example 5:

Input: nums = [-2147483647]
Output: -2147483647


Constraints:

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1


"""


# class Solution:
#     def maxSubArray(self, nums):
#
#         lenght_dict={}
#
#         """
#         The idea to calkculate if adding a value is inceasing the sum or decreasing the um.
#
#         """
#         n = len(nums)
#         current_max_sum = max_global = nums[0]  ## Set the initial value at oth index
#
#         lenght=1
#
#         for i in range(1, n):
#
#             ## which one is bigger. Current_max_sum+nums[i] or nums[i]
#             ## Meaning should I start a new subarray ay nums[i] or continue the existing one
#
#             if current_max_sum + nums[i]<nums[i]:
#                 lenght_dict[current_max_sum]=lenght
#                 lenght=1
#             else:
#                 lenght +=1
#             current_max_sum = max(nums[i], current_max_sum + nums[i])
#             # print(current_max_sum)
#
#
#             if current_max_sum > max_global:  ## set the maximum so far to global max
#                 max_global = current_max_sum
#
#         return max_global




class Solution:
    def maxSubArray(self, nums):

        lenght_dict={}

        """
        The idea to calkculate if adding a value is inceasing the sum or decreasing the um.

        """
        global_max=sum_so_far=nums[0]

        n=len(nums)

        for i in range(1,n):
            sum_so_far= max(nums[i],nums[i]+sum_so_far)

            global_max=max(global_max,sum_so_far)

        return global_max







object=Solution()

nums=[-2,1,-3,4,-1,2,1,-5,4]

print(object.maxSubArray(nums))


