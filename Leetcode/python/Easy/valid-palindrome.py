"""
https://leetcode.com/problems/valid-palindrome/

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false


Constraints:

s consists only of printable ASCII characters.


"""


class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = ''.join(filter(str.isalnum, s)).lower()
        n = len(s)

        ## Approach 1

        for i in range(int(n / 2)):
            if s[i] != s[n - i - 1]:
                return False
        return True

        ## Approach 2

#         left,right=0,n-1
#         while left < right:
#             if s[left]!=s[right]:
#                 return False
#             left+=1
#             right-=1
#         return True
