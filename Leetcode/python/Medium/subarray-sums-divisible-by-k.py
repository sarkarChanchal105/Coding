"""
https://leetcode.com/problems/subarray-sums-divisible-by-k/

"""



class Solution:
    def subarraysDivByK(self, nums, k) :

        n=len(nums)
        prefixSum=[0]*n
        prefixSum[0]=nums[0]
        hashTable={}
        #print(nums)
        ## Calculate the prefix sum
        for i in range(1,n):
            prefixSum[i]=prefixSum[i-1]+nums[i]

        #print(prefixSum)

        for a in prefixSum:
            reminder=a % k
            if reminder in hashTable:
                hashTable[reminder]+=1
            else:
                hashTable[reminder]=1
        return sum(hashTable.values())+1

object=Solution()
nums = [4,5,0,-2,-3,1]
k = 5

nums = [5]
k = 9


print(object.subarraysDivByK(nums,k))





