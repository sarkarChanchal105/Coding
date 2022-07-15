"""
https://leetcode.com/problems/longest-uncommon-subsequence-ii/solution/

Given an array of strings strs, return the length of the longest uncommon subsequence between them. If the longest uncommon subsequence does not exist, return -1.

An uncommon subsequence between an array of strings is a string that is a subsequence of one string but not the others.

A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.

For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get "abc". Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).


Example 1:

Input: strs = ["aba","cdc","eae"]
Output: 3
Example 2:

Input: strs = ["aaa","aaa","aa"]
Output: -1


Constraints:

2 <= strs.length <= 50
1 <= strs[i].length <= 10
strs[i] consists of lowercase English letters.

"""

from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:

        n = len(strs)

        ans = -1
        i = j = 0
        for i in range(n):
            valid= True
            for j in range(n):
                if i == j:
                    continue
                if self.is_subseq(strs[i], strs[j]):
                    valid=False
                    break

            if valid:
                ans = max(ans, len(strs[i]))

        return ans

    def is_subseq(self, s1, s2) -> bool:  ## checks if S1 is a subsequence of S2

        i = j = 0

        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:  ## check if the charasters match
                i += 1  ## increment i
            j += 1  ## always increment

        return i == len(s1)  ## return true only if we have exhausted all characters in string S1

object=Solution()

arr=["a","b","c","d","e","f","a","b","c","d","e","f"]


print(object.findLUSlength(arr))

