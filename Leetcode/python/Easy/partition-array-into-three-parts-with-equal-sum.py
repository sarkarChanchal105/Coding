"""
https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/



Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])



Example 1:

Input: A = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
Example 2:

Input: A = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
Example 3:

Input: A = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4


Constraints:

3 <= A.length <= 50000
-10^4 <= A[i] <= 10^4
"""


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:

        ## Firche check whether the sum of all elements are disvisble by 3. i.e. reminder should be zero.
        summary = sum(A)
        if summary % 3 != 0:
            return False

        ## if the array can be partitioned in three parts with eual sum, then each partition will have 1/3 of total sum
        targetSumInEachPartition = summary // 3

        ## The idea is to determine if the sum of all elements in current partition is ewaua to target sum then move on the next partition

        sumOfCurrentPartition = 0
        countOfPartitions = 0
        for i in range(len(A)):
            sumOfCurrentPartition += A[i]  ## calculate the sum of current partition
            if sumOfCurrentPartition == targetSumInEachPartition:  ## check whether it matched
                sumOfCurrentPartition = 0  ## update of the sum of current parition to zero to begin a new partiton
                countOfPartitions += 1  ## add the number of partitions

        # print(countOfPartitions)

        if countOfPartitions >= 3:
            return True
        return False
