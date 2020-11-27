""""
https://leetcode.com/problems/third-maximum-number/
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.



"""



class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)  ## Build the set with numers in the list

        maximum = max(nums)  ## get the maximum number

        if len(nums) < 3:  ## if lenght of set is less than 3 then retunr maximim
            return maximum

        ## continue to find the third maximum (distinct) by removing first and second maximum
        nums.remove(maximum)
        second_max = max(nums)
        nums.remove(second_max)
        return max(nums)

