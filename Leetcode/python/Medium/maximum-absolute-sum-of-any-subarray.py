"""

You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:

If x is a negative integer, then abs(x) = -x.
If x is a non-negative integer, then abs(x) = x.


Example 1:

Input: nums = [1,-3,2,3,-4]
Output: 5
Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.
Example 2:

Input: nums = [2,-5,1,-4,3,-2]
Output: 8
Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104

"""

"""
The idea here is to use Kanade's algorithm to find the max and min sub array

"""


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        SubArrayMax = SubArrayMin = 0

        sum_so_far_max = sum_so_far_min = 0

        for i in range(len(nums)):
            ## find the max sum sub array
            sum_so_far_max = max(nums[i], sum_so_far_max + nums[i])
            SubArrayMax = max(SubArrayMax, sum_so_far_max)

            ## find the min sum sub array
            sum_so_far_min = min(nums[i], sum_so_far_min + nums[i])
            SubArrayMin = min(SubArrayMin, sum_so_far_min)

        return max(SubArrayMax, abs(SubArrayMin))