"""

https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

ou are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it's possible, otherwise, return -1.



Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1
Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
1 <= x <= 109

"""


class Solution:
    def minOperations(self, nums, x: int) -> int:

        if x == 0:
            return 1



        if len(nums)==0:
            return

        option1 = self.minOperations(nums[1:], x - nums[0])
        option2 = self.minOperations(nums[:-1], x - nums[-1])

        if option1 == 1 or option2 == 1:
            return 1
        else:
            return -1


object=Solution()

nums=[1,1,4,2,3]
x=5

print(object.minOperations(nums,x))

