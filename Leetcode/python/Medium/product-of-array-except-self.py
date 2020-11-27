"""
https://leetcode.com/problems/product-of-array-except-self/

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

Accepted
630,538
Submissions
1,037,576

"""


class Solution:

    #     ## O(N) solution but uses extra space
    #     def productExceptSelf(self, nums: List[int]) -> List[int]:

    #         """
    #         The idea is to build to two extra arrays such as left and right
    #         left[i]  = product of all elements left to the index i
    #         right[i] = product of all elements right to the index i

    #         """

    #         n=len(nums)
    #         left=[1]*n  ##Product of all number left of index i
    #         right=[1]*n

    #         for i in range(1,n):
    #             left[i]=left[i-1]*nums[i-1]

    #         for i in range(n-2,-1,-1):
    #             right[i]=right[i+1]*nums[i+1]

    #         result=[]

    #         for i in range(n):
    #             result.append(left[i]*right[i])

    #         return result

    ## O(N) solution but uses extra space
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """
        The idea is not to build to  extra arrays such as left ,right as above. Insted use the answer array

        """

        n = len(nums)
        result = [1] * n

        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]

        print(result)

        ## Instead of keepi track if right array, use a variable right to keep track of the right values.

        right = 1
        for i in range(n - 1, -1, -1):
            result[i] = result[i] * right
            right = right * nums[i]

        return result

