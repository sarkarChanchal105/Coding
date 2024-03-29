"""
https://leetcode.com/problems/maximum-product-subarray/

https://www.youtube.com/watch?v=hJ_Uy2DzE08

152. Maximum Product Subarray
Medium

5434

186

Add to List

Share
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

"""

## O(n2) solution
# class Solution:
#     def maxProduct(self, nums):
#         n=len(nums)
#         result=nums[0]
#         for i in range(n): ## for each i from 0 to n -1
#             temp=1
#             for j in range(i,n): ## each element from ith position to n-1th position
#                 temp=temp*nums[j] ## calculate the product of subarra
#                 result=max(result,temp) ## keep the maximum product
#         return result
#
#
#
# ## O(N) solution



class Solution:
    def maxProduct(self, nums) -> int:
        if len(nums) == 0:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

            max_so_far = temp_max

            result = max(max_so_far, result)

        return result

nums=[2,3,-2,4]
object=Solution()
print(object.maxProduct(nums))



