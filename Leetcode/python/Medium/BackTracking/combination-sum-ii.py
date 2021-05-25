"""
https://leetcode.com/problems/combination-sum-ii/

Refernece:
https://www.youtube.com/watch?v=IER1ducXujU

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.



Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]


Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

"""


class Solution:
    def combinationSum2(self, candidates, target):
        reults=[]
        temp=[]
        startIdx=0
        candidates=sorted(candidates) ## sort the candidate array tp aavoid duplicates
        self.combinationSum2helper(candidates,startIdx,temp, target,reults)
        return reults



    def combinationSum2helper(self,candidates,startIdx, temp, target, results):

        if target<=0:
            if target==0:
                results.append(temp[:])
            return


        for i in range(startIdx,len(candidates)):
            if startIdx==i or candidates[i]!=candidates[i-1]: # check of the same element appeared in the last iteratio then lets not add it
                temp.append(candidates[i])
                self.combinationSum2helper(candidates,i+1,temp,target-candidates[i],results)
                temp.pop()


object=Solution()


candidates = [10,1,2,7,6,1,5]
target = 8

candidates =[2,5,2,1,2]
target = 5
print(object.combinationSum2(candidates, target))









