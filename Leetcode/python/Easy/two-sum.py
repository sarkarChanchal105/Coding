"""

https://leetcode.com/problems/two-sum/

"""


class Solution:
    def twoSum(self, nums, target) :
        dict_numbers = {}

        for i in range(len(nums)):
            dict_numbers[nums[i]] = i

        print(dict_numbers)

        for i in range(len(nums)):
            complement=target - nums[i]
            if complement in dict_numbers.keys() and i!=dict_numbers[complement]:
                return [i,dict_numbers[complement]]

nums=[2,7,11,15]
target=9

nums=[3,2,4]
target=6
object= Solution()
result=object.twoSum(nums,target)
print(result)