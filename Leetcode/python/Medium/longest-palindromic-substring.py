""""
Given a string s, return the longest palindromic substring in s.
https://leetcode.com/problems/longest-palindromic-substring/


Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),

"""

"""
## Time COmplexity : O(n^2)  and Space O(n) 
"""



class Solution:
    def longestPalindrome(self, s: str) -> str:
        currentLongest = [0, 1]

        ## Keep the Starting and Ending position of the String.
        ## First letter of the string is a palindron. Hence initualize with [0,1]

        ## So the idea is that palindrom can be even or odd. Hence for each character at position i,
        ## check for the palindrom of even length or odd length

        for i in range(1, len(s)):
            odd = self.getStartEndIdxofLongestPalindrom(s, i - 1,i + 1)  ## check for Palindrom around the ith character. i.e. left and right. ## example aba . Here i is at letter b
            even = self.getStartEndIdxofLongestPalindrom(s, i - 1, i)  ## check for Palindrom around the ith character. aa . Here i is at letter a(right most)

            longestSofar = max(odd, even, key=lambda x: x[1] - x[0]) # now find out which one is the longest even or odd
            currentLongest = max(currentLongest, longestSofar, key=lambda x: x[1] - x[0]) ## calculate the current longest

        return s[currentLongest[0]:currentLongest[1]] ## return the string

    def getStartEndIdxofLongestPalindrom(self, s, startIdx, endIdx):

        ## the idea is to expand leftIdx to left and rightIdx to right until we have matching characters
        while startIdx >= 0 and endIdx < len(s):
            if s[startIdx] != s[endIdx]: ## if this condition matches then we no longer have palindrom
                break
            startIdx -= 1 ## move left pointer to left
            endIdx += 1 ## move right pointer to right

        ## when the loop breaks, left much have gone 1 index left. Hence returning lefrIdx+1.
        return [startIdx + 1, endIdx]



s='chabanchal'
object=Solution()

print(object.longestPalindrome(s))