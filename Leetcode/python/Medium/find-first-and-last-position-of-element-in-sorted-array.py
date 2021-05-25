"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

"""

"""
The idea is to use a variation of the Binary search method

"""


class Solution:
    def searchRange(self, nums, target):
        start = 0
        end = len(nums) - 1
        result = [-1, -1]
        result[0] = self.findFirstPosition(nums, start, end, target)
        result[1] = self.findLastPosition(nums, start, end, target)
        return result

    def findFirstPosition(self, nums, start, end, target):
        index = -1
        ## Allow the loop untile start and end meets
        while start <= end:
            midPoint = start + int((end - start) / 2)  ## calculate the mid point

            if nums[
                midPoint] >= target:  ## Trick is using >= as opposed to using > in regular binary search.  Continue the search and keep on decreasing the end when greater than target since we want the earliest position
                end = midPoint - 1
            else:
                start = midPoint + 1  ## if less than equal to target then adjust Start

            if nums[midPoint] == target:  ## check if we have found a target value
                index = midPoint  ## Yes, the update the index

        return index

    def findLastPosition(self, nums, start, end, target):
        index = -1
        while start <= end:
            midPoint = start + int((end - start) / 2)
            if nums[
                midPoint] <= target:  ## Trick is using <= as opposed to using < in regular binary search.  Continue the search and keep on increasing the start when greater than target since we want the latest position
                start = midPoint + 1
            else:
                end = midPoint - 1  ## if less than equal to target then adjust end

            if nums[midPoint] == target:
                index = midPoint

        return index

