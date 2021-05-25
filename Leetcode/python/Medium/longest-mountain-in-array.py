"""
https://leetcode.com/problems/longest-mountain-in-array/

You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.



Example 1:

Input: arr = [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: arr = [2,2,2]
Output: 0
Explanation: There is no mountain.

"""


class Solution:
    def longestMountain(self, arr: List[int]) -> int:

        """
        The idea is to find the peak with minimum lenght . for element i to be peak, a[i] > a[i+1] and a[i]>a[i-1]

        if ith the element is the peak, then, traverse on both sides until the elements are strictly dereasing.


        """
        n = len(arr)  ## get the lenght of the array
        globalLongestPeak = 0

        if n < 3:  ## Edge case if the number of elements is less than 3
            return globalLongestPeak

        for i in range(1, n - 1):
            ## check of current number is peak with minimum conditions
            isPeak = arr[i] > arr[i - 1] and arr[i] > arr[i + 1]

            if isPeak:  ## if current element is a peak with minimum number of elements
                leftIdx = i - 2
                while leftIdx >= 0 and arr[leftIdx] < arr[
                    leftIdx + 1]:  ## Travese to the left until elements are strictly drecreasing
                    leftIdx -= 1

                rightIdx = i + 2
                while rightIdx <= n - 1 and arr[rightIdx] < arr[
                    rightIdx - 1]:  ## Travese to the right unti emenets are strictly decreasing
                    rightIdx += 1

                currentLongestPeak = rightIdx - leftIdx - 1  ## calculate the lenght of the current peak

                globalLongestPeak = max(globalLongestPeak, currentLongestPeak)  ## Find the maximum so far

                i = rightIdx  ## since peak  spans untile rightIdx, hence there is no other peak until rightIdx.  Hence we are safe to begin our search
                ## from rightIdx

        return globalLongestPeak


