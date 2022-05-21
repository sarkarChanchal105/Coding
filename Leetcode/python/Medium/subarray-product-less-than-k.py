"""
https://www.youtube.com/watch?v=SxtxCSfSGlo

https://leetcode.com/problems/subarray-product-less-than-k/


Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.



Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Example 2:

Input: nums = [1,2,3], k = 0
Output: 0


"""


class Solution:
    def numSubarrayProductLessThanK(self, nums, k) -> int:

        n = len(nums)
        result = 0

        ## Initialize two pointers
        left = right = 0

        product = 1  ## Initliaze the value of product

        while right < n:  ##
            product *= nums[right]  ## calculate the curent product

            while product >= k and left <= right:  ## if the porudct is more than k then
                product = product / nums[left]  ## Divide the value at left
                left += 1  ## Keep on Dviding until th produc is less than K

            result = result + right - left + 1  ## Calculte the number of sub arrays so far

            right += 1  ## Each step incremenr rght pointer

        return result


object=Solution()

nums=[10,5,2,6]
k=100


print(object.numSubarrayProductLessThanK(nums,k))



