"""
https://www.geeksforgeeks.org/count-pairs-with-given-sum/

Count pairs with given sum
Last Updated: 04-06-2020
Given an array of integers, and a number ‘sum’, find the number of pairs of integers in the array whose sum is equal to ‘sum’.

Examples:

Input  :  arr[] = {1, 5, 7, -1},
          sum = 6
Output :  2
Pairs with sum 6 are (1, 5) and (7, -1)

Input  :  arr[] = {1, 5, 7, -1, 5},
          sum = 6
Output :  3
Pairs with sum 6 are (1, 5), (7, -1) &
                     (1, 5)

Input  :  arr[] = {1, 1, 1, 1},
          sum = 2
Output :  6
There are 3! pairs with sum 2.

Input  :  arr[] = {10, 12, 10, 15, -1, 7, 6,
                   5, 4, 2, 1, 1, 1},
          sum = 11
Output :  9
Expected time complexity O(n)

"""


def getPairsCount(arr, sum):

    dict={}

    for a in arr:
        if a in dict.keys():
            dict[a]+=1
        else:
            dict[a]=1

    print(dict)
    count=0
    pairs=[]
    distinctPairs={}
    for i in range(len(arr)):
        complement = sum - arr[i]
        if complement in dict.keys():
            count+=1
            pairs.append((arr[i],complement))

            if (complement,arr[i]) not in distinctPairs.keys() and (arr[i],complement) not in distinctPairs.keys():
                distinctPairs[(complement,arr[i])]=1

    print(pairs)
    print(count)
    print(distinctPairs)


arr = [10, 12, 10, 15, -1, 7, 6,5, 4, 2, 1, 1, 1]
sum=11
getPairsCount(arr,sum)

arr = [1, 5, 7, -1, 5]
sum = 6

arr = [1, 6, 6, -1, 5,7]
sum = 12

getPairsCount(arr,sum)
