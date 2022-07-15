"""
https://leetcode.com/problems/unique-binary-search-trees/


96. Unique Binary Search Trees
Medium

7566

304

Add to List

Share
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.



Example 1:


Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1


"""


## ONLY RECURSION

"""
The idea here is to use Catalan number series https://en.wikipedia.org/wiki/Catalan_number

"""

# class Solution:

#     def numTrees(self, n: int, result=0) -> int:

#         if n<=1:
#             return 1  ## First two numbers are 1

#         result=0 ## for each value of the n, reset the result
#         for i in range(n): ## for each value in in n recsuesive call the function
#             result+=self.numTrees(i,result)*self.numTrees(n-i-1,result)


#         return result


## WITH DP (MEMO) SOLUTION

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [-1] * (n + 1) ## Initalize a DP array with all negatoves
        return self.numTreesInner(n, dp)

    def numTreesInner(self, n, dp):

        if n <= 1: ##if n is 0 or 1 then set the value to 1
            dp[n] = 1
            return dp[n]

        if dp[n] == -1: ## if the number BST is not already calculated for the value of n in the current function call
            dp[n] = 0 ## set the results to zero first
            for i in range(n): # for each value [0,1,2...n] recusively call the function to calculate the number of unique BST
                dp[n] += self.numTreesInner(i, dp) * self.numTreesInner(n - i - 1, dp)

        return dp[n]


object=Solution()

print(object.numTrees(5))


