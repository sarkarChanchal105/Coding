"""
Find the Increasing subsequence of length three with maximum product
Last Updated: 30-10-2020
Given a sequence of non-negative integers, find the subsequence of length 3 having maximum product with the numbers of the subsequence being in ascending order.
Examples:


Input:
arr[] = {6, 7, 8, 1, 2, 3, 9, 10}
Output:
8 9 10

Input:
arr[] = {1, 5, 10, 8, 9}
Output: 5 8 9



"""



def increasing_subseq_len_three(nums):

    ## lets calculate LSL and LGR for each and every element
    """
    LSL: The largest smaller element on left of given element
    LGR: The largest greater element on right of given element.
    """

    n=len(nums)
    lsl=[-1] * n
    lgr=[-1] * n


    ## calculate LSL

    ## for for any given i, j where j<i, find the largest element which smaller than nums[i]
    for i in range(1,n):
        max_so_far = float('-inf')
        for j in range(i):
            if max_so_far<nums[j] and nums[j]<nums[i]:  ## check if there is any element which more than the max so far and less than element at ith position
                max_so_far=nums[j]
        lsl[i]=max_so_far

    print(lsl)

    print(nums)
    ## calculate LGR

    ## for for any given i, j where j>i and, find the largest element which is greater than nums[i]
    for i in range(n-1,-1,-1):
        max_so_far = float('-inf')
        for j in range(i,n,1):
            if max_so_far < nums[j] and nums[j]>nums[i] : ## Check if there is any element which is more than max so far and greater than the element at the ith position
                max_so_far = nums[j]
        if max_so_far > float('-inf') :
            lgr[i] = max_so_far

    lgr[-1]=-1

    print(lgr)


    max_product=1
    index=0
    for i in range(1,n-1):
        temp=lsl[i]*nums[i]*lgr[i]
        if max_product<temp:
            max_product=temp
            index=i



    print(max_product)

    print("elements {} {} {}".format(lsl[i],nums[i],lgr[i]))








nums=[1, 5, 10, 8, 9]

increasing_subseq_len_three(nums)


