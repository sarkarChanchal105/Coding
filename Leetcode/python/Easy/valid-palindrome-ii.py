"""

https://leetcode.com/problems/valid-palindrome-ii/

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.


"""

"""

Using Two pointer approach.

increment left and decrement right untile we find a mismtach on characters

and then check if deleting at least one of the mismatched character results in a Palindrom.


"""


class Solution:
    def validPalindrome(self, s: str) -> bool:

        n = len(s)
        left, right = 0, n - 1

        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s, left + 1, right, n) or self.isPalindrome(s, left, right - 1, n)

            left += 1
            right -= 1

        return True

    def isPalindrome(self, s, i, j, n):

        #         print(s, i,j)

        #         if i<0 or j>=n:
        #             return False

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

