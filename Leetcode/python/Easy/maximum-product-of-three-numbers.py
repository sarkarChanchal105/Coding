"""
https://leetcode.com/problems/maximum-product-of-three-numbers/
"""


class Solution:
    def maximumProduct(self, nums):

        min1 = nums[0]  ## minimum value
        min2 = nums[0]  ## Second min value

        max1 = nums[0]  ## maximum vaue
        max2 = nums[0]  ## Second Max value
        max3 = nums[0]  ## third maximum

        # Calculate max first
        n=len(nums)
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                nums[i+1],nums[i]=nums[i],nums[i+1]
        max1=nums[n-1] ## the last element is the max
        n=n-1 ## No need to consider last element in the next calcu.atom
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                nums[i+1],nums[i]=nums[i],nums[i+1]
        max2=nums[n-1]
        n=n-1
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                nums[i+1],nums[i]=nums[i],nums[i+1]
        max3=nums[n-1]

        n=len(nums)

        for i in range(n-2,-1,-1):
            if nums[i]>nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]

        min1=nums[0]

        for i in range(n-2,0,-1):
            if nums[i]>nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]

        min2=nums[1]

        #print(min1, min2)

        return max(max1*max2*max3,min1*min2*max1)


object=Solution()

nums=[1,2,3,4]
result=object.maximumProduct(nums)
print(result)
