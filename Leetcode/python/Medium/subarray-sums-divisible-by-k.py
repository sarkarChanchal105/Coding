"""
https://leetcode.com/problems/subarray-sums-divisible-by-k/

The idea here is to calcualte the prefix sum and keep track of the count of the reminders when the
prefix sums are dvided by k. if we encounter the same reminder between two prefix sume then we can say

the sub array between those two prefix sums is divisible by k

"""



class Solution:
    def subarraysDivByK(self, nums, k) :


        hashTable={0:1} ## Initalize for the edcase when there is at least one value equal to k

        preSum=result=0

        for num in nums:
            preSum+=num  ## Calcualte the prefix sum
            remainder=preSum % k ## then the reminder

            if remainder in hashTable:
                result+=hashTable[remainder] ## if the reminder exists then add the number of previous occurences to the result
                hashTable[remainder]+=1 ## update the number of occurrences of the remainder in hash table
            else:
                hashTable[remainder]=1 ## if the reminder is new in the hash table then just put 1

        return result




object=Solution()
nums = [4,5,0,-2,-3,1]
k = 5

nums = [5]
k = 9


print(object.subarraysDivByK(nums,k))





