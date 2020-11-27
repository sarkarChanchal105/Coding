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

class Solution:
    def validPalindrome(self, s: str) -> bool:

        left, right = 0, len(s)

        number_of_mismatch=0

        while left <right and number_of_mismatch<=1:
            if s[left]!=s[right]:
                number_of_mismatch+=1

        if number_of_mismatch>1:
            return False
        return True


