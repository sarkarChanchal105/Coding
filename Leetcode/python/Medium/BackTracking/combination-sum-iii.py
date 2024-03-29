"""
https://leetcode.com/problems/combination-sum-iii/

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.



Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations. [1,2,1] is not valid because 1 is used twice.
Example 4:

Input: k = 3, n = 2
Output: []
Explanation: There are no valid combinations.
Example 5:

Input: k = 9, n = 45
Output: [[1,2,3,4,5,6,7,8,9]]
Explanation:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
​​​​​​​There are no other valid combinations.


"""

class Solution:
    def combinationSum3(self, k: int, n: int):

        candiates=[i for i in range(1,10)]
        target=n
        results=[]
        temp=[]
        startIdx=0

        self.combinationSum3Helper(k,candiates,startIdx,temp,target, results )
        return results

    def combinationSum3Helper(self,k,candidates,startIdx,temp,target, results ):

        if target<=0:
            if target==0 and len(temp)==k:
                results.append(temp[:])
            return

        for i in range(startIdx, len(candidates)):

            temp.append(candidates[i])

            self.combinationSum3Helper(k,candidates,i+1,temp,target-candidates[i],results)

            temp.pop()



object=Solution()

k = 3
n = 7

print(object.combinationSum3(k,n))















