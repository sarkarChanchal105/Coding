"""
https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

1464. Maximum Product of Two Elements in an Array
Easy

1046

162

Add to List

Share
Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).


Example 1:

Input: nums = [3,4,5,2]
Output: 12
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.
Example 2:

Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
Example 3:

Input: nums = [3,7]
Output: 12


Constraints:

2 <= nums.length <= 500
1 <= nums[i] <= 10^3

"""

from typing import List


## Brute force

# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:

#         result=float(-inf)

#         for i in range(len(nums)):
#             for j in range(len(nums)):

#                 if i==j:
#                     continue

#                 result=max(result, (nums[i]-1)*(nums[j]-1))

#         return result

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        max1 = max(nums[0], nums[1])
        max2 = min(nums[0], nums[1])

        for current in nums[2:]:

            if current > max1:
                max2 = max1
                max1 = current

            else:
                if current > max2:
                    max2 = current

        # print(max1, max2)

        return (max1 - 1) * (max2 - 1)


arr=[3,4,5,2]
arr=[10,2,5,2,10]
object=Solution()

print(object.maxProduct(arr))

