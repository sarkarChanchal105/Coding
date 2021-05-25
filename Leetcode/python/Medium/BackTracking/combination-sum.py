"""
https://leetcode.com/problems/combination-sum/

References : https://www.youtube.com/watch?v=yFfv03AE_vA

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.



Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
Example 4:

Input: candidates = [1], target = 1
Output: [[1]]
Example 5:

Input: candidates = [1], target = 2
Output: [[1,1]]

"""


class Solution:
    def combinationSum(self, candidates, target):

        result = [] ## will have the
        temp=[] ## Array to store the temp results
        self.combinationSumHelper(candidates, 0,target,temp, result)
        return result

    def combinationSumHelper(self, candidates,start, target, temp, result): ## Will use back trcking
        """
        Args:
            candidates:
            start: starting position of the element in Candidate array
            target:
            temp:
            result:
        Returns:
        """
        ## base case
        if target<0:
            return
        ## base case
        if target ==0: ## if we have reached the target then append the contents of the temp array in the result array
            result.append(temp[:])

        ## fr each elements in the candidate array make call rescuvtely untile the target is negative
        for i in range(start,len(candidates)):
            temp.append(candidates[i]) ## add the element in the temp array
            self.combinationSumHelper(candidates,i,target-candidates[i], temp,result)
            temp.pop() ## back tracking by removing the last element in the temp array

candidates = [2,3,6,7]
target = 7

object=Solution()

result=object.combinationSum(candidates,target)

print(result)







