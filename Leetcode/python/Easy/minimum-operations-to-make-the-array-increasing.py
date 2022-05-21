"""
https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/

You are given an integer array nums (0-indexed). In one operation, you can choose an element of the array and increment it by 1.

For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].
Return the minimum number of operations needed to make nums strictly increasing.

An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1. An array of length 1 is trivially strictly increasing.



Example 1:

Input: nums = [1,1,1]
Output: 3
Explanation: You can do the following operations:
1) Increment nums[2], so nums becomes [1,1,2].
2) Increment nums[1], so nums becomes [1,2,2].
3) Increment nums[2], so nums becomes [1,2,3].
Example 2:

Input: nums = [1,5,2,4,1]
Output: 14
Example 3:

Input: nums = [8]
Output: 0


Constraints:

1 <= nums.length <= 5000
1 <= nums[i] <= 104

"""


class Solution:
    def minOperations(self, nums) -> int:

        #print(nums)

        number_of_operations=0

        for i in range(1,len(nums)): # starting from the second element

            if nums[i-1]>=nums[i]: ## check if the previous element is greater or qual to current element
                diff=nums[i-1]-nums[i]+1 ## calculate the minimum number of operations to make the current number one more than the previous nu,ber
                number_of_operations+=diff
                nums[i]=nums[i]+diff ## update the current number so that the array becomes increasing strictly
        #print(number_of_operations)
        return number_of_operations

nums = [1, 5, 2, 4, 1]
object=Solution()
print(object.minOperations(nums))







