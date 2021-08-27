from collections import defaultdict

## Solution 1

#class Solution:
#    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
#         if len(nums1)>len(nums2):
#             return self.intersect(nums2,nums1)
        
#         hashTableNums1=defaultdict(int)
        
#         hashTableNums2=defaultdict(int)
        
#         result=[]
        
#         for num in nums1:  ## Get the frequencies of the numbers (num1)
#             hashTableNums1[num]+=1   ##. O(len(num1))
        
#         ##. ##. O(len(num2))
#         for num in nums2:
#             if num in hashTableNums1:
#                 hashTableNums2[num]+=1 ## keep the frequencies if those numbers in num2 that are also present in num1
                
                
#         ## O(len(num2))
#         for key,value in hashTableNums2.items():
#             hashTableNums2[key]=min(value,hashTableNums1[key])  ## finally keep the minimum of the frequencies
            
#         ## O(len(num2))
#         for key,value in hashTableNums2.items(): 
#             if value>0:
#                 for i in range(value):
#                     result.append(key) ## append the result based on the frequencies
        
#         return result
                

## Solution 2 : Better . Uses less extrac space
    
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        if len(nums1)>len(nums2): ## make a recusive call if len of num1 is greater than len of num2
            return self.intersect(nums2,nums1)
        
        hashTableNums1=defaultdict(int)
        
        for num in nums1:  ## Get the frequencies of the numbers (num1)
            hashTableNums1[num]+=1   ##. O(len(num1))
            
        
        pointer=0
        
        
        for num in nums2:    
            if num in hashTableNums1:
                if hashTableNums1[num]>0:
                    nums1[pointer]=num
                    hashTableNums1[num]-=1
                    pointer+=1
        
        return nums1[:pointer]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        