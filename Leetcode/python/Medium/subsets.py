"""
https://leetcode.com/problems/subsets/


Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]



"""


# class Solution:
#     # def subsets(self, String, current='', index=0):
#     #     if index == len(String):
#     #         print(current)
#     #         return
#     #
#     #     self.subsets(String, current, index + 1)
#     #     self.subsets(String, current+String[index], index + 1)
#
#
#     def subsets1(self, String, current=[[]], index=-1):
#         if index == len(String):
#             print(current)
#             return
#
#         #print(current)
#         self.subsets1(String, current, index + 1)
#         #current+=[[String[index]]]
#         #current[index].append(String[index])
#         current.append([String[index]])
#         self.subsets1(String,current,index + 1)
#
#
# #
# # String='123'
# #
# object=Solution()
# #
# # #object.subsets(String)
#
# String=[1,2,3]
#object.subsets1(String)

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]

        for num in nums:
            t=[curr + [num] for curr in output]
            print(t)
            #output +=
            output+=t

        return output


object=Solution()

nums=[1,2,3]

print(object.subsets(nums))
