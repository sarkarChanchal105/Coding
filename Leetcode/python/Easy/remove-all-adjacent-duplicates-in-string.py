"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.



Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
Example 2:

Input: s = "azxxzy"
Output: "ay"


Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.

"""

"""
The idea here is to use a Stack. Push an element if current character does not match with the last element


"""


class Solution:
    def removeDuplicates(self, s: str) -> str:

        stack = []

        for chr in s:

            if stack:

                if stack[-1] == chr:
                    stack.pop()

                else:
                    stack.append(chr)


            else:
                stack.append(chr)

        return ''.join(stack)

