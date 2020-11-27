"""

https://leetcode.com/problems/longest-palindromic-subsequence/

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".


Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".


Constraints:

1 <= s.length <= 1000
s consists only of lowercase English letters.


"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        n = len(s)  ## get the lenght of the string

        matrix = [[-1 for _ in range(n)] for _ in range(n)]  ## for the DP array matrix

        left = 0  ## left pointer is zerp
        right = n - 1  ## right pointer to the last elemt of the string

        return self.lps(s, left, right, matrix)  ## call the helper function

    def lps(self, s, left, right, matrix):

        if matrix[left][right] != -1:
            return matrix[left][right]  ## if the value is not -1 then its already computed. No need to calcularte

        if left > right:  ## the pointer cross over each pother then then there is no palindromic sub se between left and right
            matrix[left][right] = 0  ## hence return zero
            return matrix[left][right]

        if left == right:  ## left and right is same, there there only one element.
            matrix[left][right] = 1  ## hence return 1
            return matrix[left][right]

        if s[left] == s[
            right]:  ## the left and right chars match, then  add 2 to the result and recusovely call for left+1 and right -1
            matrix[left][right] = 2 + self.lps(s, left + 1, right - 1, matrix)  ## store the resulr in matrix
            return matrix[left][right]

        else:

            ## if no match the I have two options

            ## consider the string between left+1 and right or left and right-1

            option1 = self.lps(s, left, right - 1, matrix)
            option2 = self.lps(s, left + 1, right, matrix)

            matrix[left][right] = max(option1, option2)  ## store the result into the matrix

            return matrix[left][right]  ## reture the result




