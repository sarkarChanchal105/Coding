"""
https://leetcode.com/problems/merge-intervals/

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

"""


class Solution:
    def merge(self, intervals) :
        intervals = sorted(intervals, key=lambda x: x[0])
        # print (intervals)

        result = []

        for i in intervals:
            if result and i[0] <= result[-1][1]:
                result[-1][1] = max(i[1], result[-1][1])
                result[-1][0] = min(i[0], result[-1][0])
            else:
                result.append(i)

        return result


object= Solution()
intervals=[[1,3],[2,6],[8,10],[15,18]]
result=object.merge(intervals)

print(result)
