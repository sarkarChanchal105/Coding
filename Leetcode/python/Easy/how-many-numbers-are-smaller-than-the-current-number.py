"""

https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.



Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation:
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1).
For nums[3]=2 there exist one smaller number than it (1).
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
Example 2:

Input: nums = [6,5,4,8]
Output: [2,1,0,3]
Example 3:

Input: nums = [7,7,7,7]
Output: [0,0,0,0]


Constraints:

2 <= nums.length <= 500
0 <= nums[i] <= 100
"""


class Solution:
    """
    So the idea is to  sort the array in reverse order and keep on adding the elements in the a dictionay how far each element is from the last element

    """

    def smallerNumbersThanCurrent(self, nums):
        nums1=sorted(nums,reverse=True) ## sort the numbers in reverse order
        out=[]
        dict={}
        n=len(nums1)
        for i in range(n):
            dict[nums1[i]]=n-(i+1)

        #print (dict)

        for a in nums:
            out.append(dict[a])

        return out


# class Solution:
#     def smallerNumbersThanCurrent(self, nums):
#         counts = [0] * 101
#         print(counts)
#         for a in nums:
#             counts[a] += 1
#         print("\n")
#         print(counts)
#         for i in range(1, 101):
#             counts[i] += counts[i - 1]
#             res = [0] * len(nums)
#         print("\n")
#         print(res)
#         for i, a in enumerate(nums):
#             if a > 0:
#                 res[i] = counts[a - 1]
#         return res



nums=[8,1,2,2,3]
object=Solution()

print(object.smallerNumbersThanCurrent(nums)
      )
