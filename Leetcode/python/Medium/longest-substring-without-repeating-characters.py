
"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""


class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     hashTable = {}
    #     maxLength = 0
    #
    #     i = 0  ## initiliaze i with 0
    #     for j in range(len(s)):  ## for each character in the string
    #
    #         currChr = s[j]  ## current character
    #
    #         if currChr in hashTable:  ## if current character is repeated
    #             #i = max(hashTable[currChr] + 1, i)  ## update the pointer i
    #             i+=1
    #
    #
    #         maxLength = max(maxLength, j - i + 1)  ## calculate the lemght and keep the max so fat
    #
    #         hashTable[
    #             currChr] = j  ## keep the position of the character which will be used to set the value of i if this character occurs again.
    #
    #     return maxLength

    def lengthOfLongestSubstring(self, s: str) -> int:
        set_substring = set()
        maxLength = 0
        left = right = 0
        max_substring = 0

        while right < len(s):
            print("set_substring: {}".format(set_substring))
            while s[right] in set_substring:
                set_substring.remove(s[left])
                left += 1

            max_substring = max(max_substring, right - left + 1)

            set_substring.add(s[right])

            right += 1

        return max_substring


object=Solution()

s="bbbbb"
s="abba"
s="pwwkew"

print(object.lengthOfLongestSubstring(s))






