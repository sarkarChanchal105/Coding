"""
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b


Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
Example 3:

Input: nums = []
Output: []
Example 4:

Input: nums = [-1]
Output: ["-1"]
Example 5:

Input: nums = [0]
Output: ["0"]


Constraints:

0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
All the values of nums are unique.
nums is sorted in ascending order.
Accepted
202,952
Submissions
480,651
Seen this question in a real interview before?

Yes

No

"""


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        ## Handle edge cases
        if len(nums) == 0:  ## if there is no elemenebnt
            return []
        if len(nums) == 1:  ## if there i only one
            return [str(nums[0])]

        if len(nums) == 2:  ## if there are two elements
            diff = abs(nums[0] - nums[1])
            if diff == 0 or diff == 1:
                return [str(nums[0]) + '->' + str(nums[1])]
            else:
                return [str(nums[0]), str(nums[1])]

        ## General cases
        beginRange = nums[0]  ## intialize begin range
        endRange = nums[-1]  ## end of the range

        result = []  ## result array

        ## starting from the 2nd elemenet
        for i in range(1, len(nums)):
            diff = abs(nums[i] - nums[i - 1])  ## calculate the absoltute difference between ith a d i-1 th element

            ## if the absolute difference is o or 1 then continue
            if (diff == 0 or diff == 1) and i < len(nums):
                continue
            ## if the absolute difference is o or 1 then continue and i has reached end of array
            if (diff == 0 or diff == 1) and i == len(nums) - 1:
                if beginRange != endRange:
                    result.append(str(beginRange) + '->' + str(endRange))
                else:
                    result.append(str(beginRange))
                return result

            ## if the absilute difference is greater than 1 then it marks the bgining of new range
            if diff > 1:
                endRange = nums[i - 1]  ## update the end of current range
                if beginRange != endRange:  ## if ebgin and end sre not same
                    result.append(str(beginRange) + '->' + str(endRange))
                else:
                    result.append(str(beginRange))
                beginRange = nums[i]  ## Start of new range
                endRange = nums[-1]  ## End of the new range

        if beginRange == endRange:
            result.append(str(endRange))
            return result

        if len(result) == 0:
            result.append(str(beginRange) + '->' + str(endRange))
            return result

        if beginRange != endRange:
            result.append(str(beginRange) + '->' + str(endRange))
            return result
