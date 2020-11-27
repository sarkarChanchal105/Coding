"""
https://leetcode.com/explore/interview/card/google/59/array-and-strings/3049/

"""

class Solution:
    def threeSum(self, nums):

        ## hadnle edge cases
        if len(nums)>3 and list(set(nums))==[0]:
            return [[0,0,0]]
        if nums==[]:
            return []
        if len(nums)<3:
            return []
        if len(nums)==3:
            if sum(nums)==0:
                return [nums]
            else:
                return []

        #solution_set=[[]]
        solution_set = {} ## this will contain the anser
        for i in range(len(nums) - 3):  ## Since we are looking for three elements
            array = self.twoSum(nums[i + 1:], -nums[i]) ## get the unique list of two elements that sums to negative of nums[i]
            if array!=[[]]:
                for a in array:
                    t=tuple(sorted([nums[i], a[0], a[1]]))  ## Get the results in tuple and sorted
                    solution_set[t]=1 ## use the tuple as the key
        if not solution_set:
            return []
        return [[k[0],k[1],k[2]] for k in solution_set.keys()]

    ## Find the list of pair whose sum is equal to a target value
    def twoSum(self, nums, target):
        """

        Args:
            nums: array input
            target: target value

        Returns:

        """
        dict = {} ## Declare the dictionary that will store the compliments of each number
        array = [[]] ## Empty 2D array to store the pairds

        for i in range(len(nums)):


            if nums[i] in dict.keys():
                if not array[0]:
                    array[0] = [nums[i], nums[dict[nums[i]]]]
                else:
                    array.append([nums[i], nums[dict[nums[i]]]])
            else:
                dict[target - nums[i]] = i
        return array

object = Solution()

array = [-1, 0, 1, 2, -1, -4]



# array=[0,0,0]
# array=[-1,0,1,0]
#
array=[4,4,3,-5,0,0,0,-2,3,-5,-5,0]
print(object.threeSum(array))

#object.twoSum(array, 1)
