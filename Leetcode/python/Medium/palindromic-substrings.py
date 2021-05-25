"""
https://leetcode.com/problems/palindromic-substrings/

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".


Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


Note:

"""
""""

The idea is similiar to the problem longest palindromic substring. 

"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        Total = len(s)  ## Since each character is palindrom itself. Hence initialize with the lenght of the string

        ## for each character  calculate the number of palindroms
        for i in range(1,len(s)):
            odd = self.getNumberOfPalindroms(s, i - 1, i + 1) ## if the palindrom has odd number of character. Ex. aba. i will point to b. check whether i-1 and i+1 are matching or not.
            even = self.getNumberOfPalindroms(s, i - 1, i) ## if the palindrom is even. Ex. aa.  i points to the right most amd i-1 points to left a.
            Total += odd + even ## add the total number of palindroms

        return Total

    def getNumberOfPalindroms(self, s, startIdx, endIdx):
        count = 0
        while startIdx >= 0 and endIdx < len(s):
            if s[startIdx] != s[endIdx]:
                break
            count += 1
            startIdx-=1
            endIdx+=1
        return count


object=Solution()

s='aaa'


s="fdsklf"
print(object.countSubstrings(s))

