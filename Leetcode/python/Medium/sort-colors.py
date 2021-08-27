# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
        
#         """
        
        
#         ## Two pass solution
        
        
#         count_0=count_1=count_2=0
        
#         for a in nums:
#             if a==0:
#                 count_0+=1
#             if a==1:
#                 count_1+=1
                
#             if a==2:
#                 count_2+1
        
#         i=0
#         while i < len(nums):
            
#             if i<count_0:
#                 nums[i]=0
                
#             elif i<count_0+count_1:
#                 nums[i]=1
#             else:
#                 nums[i]=2
                
#             i+=1
        
            
                
        
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        low=mid=0
        high=len(nums)-1
        
        while mid <=high:
            
            if nums[mid]==0:  
                nums[mid],nums[low]=nums[low],nums[mid]
                
                mid+=1 # move to the next element
                low+=1  ## since we have placed a zero in low
                
            elif nums[mid]==1:
                mid+=1 ## dont dow anythiung . Just mpve on to the next element 
                
            
            else:
                if  nums[mid]==2:
                    nums[mid],nums[high]=nums[high],nums[mid]                      
                    high-=1 ## Since we have placed 2 in the high position
                
                
                
                
                
                