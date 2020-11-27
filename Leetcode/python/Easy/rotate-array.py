


class Solution:
    # def rotateq(self, nums, k):
    #     """
    #     Do not return anything, modify nums in-place instead.
    #
    #     """
    #     n=len(nums)
    #
    #     if n<2:
    #         return nums
    #     else:
    #         for j in range(k):
    #             last=nums[-1]
    #             for i in range(n):
    #                 first=nums[i]
    #                 nums[i]=last
    #                 last=first
    #
    #
    #     print(nums)

    def rotate(self,nums,k):
        n=len(nums)
        a=[0]*n
        for i in range(n):
            a[(i+k)%n]=nums[i]
        #print(nums[:])
        nums[:]=a
        #print(nums[:])




nums=[1,2,3,4,5,6,7]
k=3
#print(nums)

object=Solution()
object.rotate(nums,k)



