
""""
https://leetcode.com/problems/house-robber/
"""
#
# class Solution:
#     def rob(self, nums):
#         rob1,rob2=0,0
#         #[rob1,rob2,n,n+1,...]
#         for n in nums:
#             temp=max(rob1+n,rob2)
#             rob1=rob2
#             rob2=temp
#         return rob2
#
#
#

#
# list=[1,2,3,1]
# print(object.rob(list))

class Solution:
    def rob(self, nums):
        cache = {}
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        cache[0] = nums[0]
        cache[1] = max(nums[0], nums[1])

        if len(nums) == 2:
            return cache[1]

        i = 0
        for i in range(2, len(nums)):
            cache[i] = max(cache[i - 2] + nums[i], cache[i - 1])
        return cache[i]


object=Solution()
list=[1,2,3,1]
#list=[2,1,1,2]
print(object.rob(list))
