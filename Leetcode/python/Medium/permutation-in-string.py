"""
https://leetcode.com/problems/permutation-in-string/

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.



Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False


Constraints:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].


"""


# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         n1 = len(s1)
#         n2 = len(s2)
#         # print(n1,n2)
#         i = 0
#
#         ## curve out the substring of lenghts(s1) eahc time and compare that siubstring in permuation of the S1.
#         while (i + n1 <= n2):
#             sub_s2 = s2[i:i + n1]
#             # print(sub_s2)
#             if self.is_permutation(sub_s2, s1):
#                 return True
#             i += 1
#         return False
#
#     def is_permutation(self, sub_s2, s1):
#         array = [0] * 26  ## assuming that s1 and s2 contains only lower case
#         Total = 0
#         for chr in sub_s2:
#             array[ord(chr) - ord('a')] += 1
#             Total += 1
#
#         for chr in s1:
#             if array[ord(chr) - ord('a')] > 0:
#                 array[ord(chr) - ord('a')] -= 1
#                 Total -= 1
#
#         # print(array, Total)
#         if Total == 0:
#             return True
#         return False


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        s1_array = [0] * 26  ## assuming all characters are within a to z
        s2_array = [0] * 26  ## assuming all characters are within a to z
        ascii_a = ord('a')  ## Get the aschi value of the character 'a'

        ## position zero represents freqncy of character 'a'
        ## Similarly position 1 represent the freqwuency of character 'b'

        for chr in s1:
            t = ord(chr) - ascii_a
            s1_array[t] += 1  ## Get the frequency of characters in S1

        ## Ge the frequency of the characters in S2 only upto leght of S1, starting from
        ## Position zero
        for d in range(n1):
            t = ord(s2[d]) - ascii_a
            s2_array[t] += 1

        i = 0
        while (i + n1 < n2):  ## while the sliding window does not exceed the string S2
            if self.is_permutation(s1_array, s2_array):
                return True
            else:
                s2_array[ord(s2[i + n1]) - ascii_a] += 1  ## add the frequency of the new character
                s2_array[ord(s2[i]) - ascii_a] -= 1  ## remove the frequency of the character by 1 that is no longer in the sliding window
            i += 1
        return self.is_permutation(s1_array, s2_array)

    def is_permutation(self, s1_array, s2_array):
        for i in range(26):
            if s1_array[i] != s2_array[i]:
                return False
        return True


object=Solution()

s1="ab"
s2="eidbaooo"

s1="adc"
s2="dcda"

print(object.checkInclusion(s1,s2))








