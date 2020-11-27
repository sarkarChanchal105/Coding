"""
https://www.geeksforgeeks.org/prefix-sum-array-implementation-applications-competitive-programming/

Prefix Sum Array – Implementation and Applications in Competitive Programming
Last Updated: 04-07-2020
Given an array arr[] of size n, its prefix sum array is another array prefixSum[] of same size such that the value of prefixSum[i] is arr[0] + arr[1] + arr[2] … arr[i].

Examples :

Input  : arr[] = {10, 20, 10, 5, 15}
Output : prefixSum[] = {10, 30, 40, 45, 60}

Explanation : While traversing the array, update
the element by adding it with its previous element.
prefixSum[0] = 10,
prefixSum[1] = prefixSum[0] + arr[1] = 30,
prefixSum[2] = prefixSum[1] + arr[2] = 40 and so on.


"""




def prefixSum(nums):

    if not nums:
        return nums
    n=len(nums)
    result=[0]*n

    result[0]=nums[0]
    for i in range(1,n):
        result[i]=result[i-1]+nums[i]


    return result


nums=[10, 20, 10, 5, 15]

result=prefixSum(nums)
print(nums)
print(result)



