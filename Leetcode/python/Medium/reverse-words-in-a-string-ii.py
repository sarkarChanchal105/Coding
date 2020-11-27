"""
https://leetcode.com/problems/reverse-words-in-a-string-ii/

Given an input string , reverse the string word by word.

Example:

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Note:

A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.
Follow up: Could you do it in-place without allocating extra space?

"""


class Solution:
    def reverseWords(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ## Revese the string first
        low = 0;
        high = len(s) - 1
        self.reverse(s, low, high)

        ## Revese the individual words
        self.reverse_each_word(s)

    def reverse(self, s, low, high):
        ## Reverse the whole string
        while (low < high):
            s[low], s[high] = s[high], s[low]
            low, high = low + 1, high - 1

    def reverse_each_word(self, s):
        ## Reverse each word
        n = len(s)
        start = end = 0
        while start < n:
            while end < n and s[end] != ' ':
                end += 1
            self.reverse(s, start, end - 1)
            start = end + 1
            end += 1


object=Solution()

s=["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]

object.reverseWords(s)

print(s)