"""
https://leetcode.com/problems/contiguous-array/

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.

"""

"""
The idea is to keep the prefix sum at each position.

everytime 0 occurs count=count -1  and 1 occurs then count = count +1

example

Initial value of count =0

Inpurt array=[0,1,1,0,1,0]
Count=       [-1,0,1,0,1,0]


"""


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        hashTableOfCounts = {0: -1}  ## Handle the edhe cases
        # hashTableOfCounts={} ## Handle the edhe cases

        count = 0

        maxLength = 0

        ## for each element in the array
        for index, element in enumerate(nums):

            if element == 0:  ## if element is zero then subtract 1
                count -= 1
            else:
                count += 1  ## else add one

            if count in hashTableOfCounts:  ## if the count so far alrady exists then the subrray has equal number of 1s and 0s

                currentPosition = index
                lastOccured = hashTableOfCounts[count]

                maxLength = max(maxLength, currentPosition - lastOccured)

            else:  ## just add the count, index in the hashMap
                hashTableOfCounts[count] = index

        return maxLength




