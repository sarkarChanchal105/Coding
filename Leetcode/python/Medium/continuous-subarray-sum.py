"""
https://leetcode.com/problems/continuous-subarray-sum/solution/

"""


class Solution:
    def checkSubarraySum(self, nums, k):
        dict={}
        sum=0
        dict[0] = -1

        for i in range(len(nums)):
            sum+=nums[i]
            if k!=0:
                sum=sum%k  ## Get the reminder after diving by

            ## if the reminder already exists then there must be
            ## one or more numbers that disvisible by target.
            if sum in dict.keys():
                if (i -dict[sum])>1: ## check if the sub array size is more than 2
                    return True
            else:
                dict[sum]=i  ## keep on adding sum and dicionay position
        return False


object=Solution()
nums=[2,5,33,6,7,25,15]
k=13
nums=[0]
k=0


print(object.checkSubarraySum(nums,k
                        ))

