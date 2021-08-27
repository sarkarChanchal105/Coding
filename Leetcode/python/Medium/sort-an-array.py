class Solution:
    def sortArray(self, nums):

        return self.mergeSort(nums)

    def mergeSort(self, nums):

        if len(nums) <= 1:
            return nums

        mid = int(len(nums) / 2)
        left_array = nums[:mid]
        right_array = nums[mid:]

        left_array = self.mergeSort(left_array)
        right_array = self.mergeSort(right_array)

        block = []

        l = r = 0

        while l < len(left_array) and r < len(right_array):

            if left_array[l] < right_array[r]:

                block.append(left_array[l])
                l += 1

            else:

                block.append(right_array[r])
                r += 1

        if l < len(left_array):
            block += left_array[l:]

        if r < len(right_array):
            block += right_array[r:]

        return block


object=Solution()

nums = [5,2,3,1]

result=object.mergeSort(nums)

print(result)

