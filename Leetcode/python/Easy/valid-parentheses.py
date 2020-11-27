"""
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.


"""


class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) == 0:
            return True

        stack = []
        dict_pairs = {}
        dict_pairs['('] = ')'
        dict_pairs['{'] = '}'
        dict_pairs['['] = ']'

        for chr in s:
            if chr in dict_pairs.keys():
                stack.append(chr)  ## Keep on appending the opening parenthesis
            else:
                if len(stack) == 0:  ## if the stack is already empty that means did ot start with any opening braces
                    return False
                last = stack.pop()  ## if stack is not empty then check whether we are getting matching
                if dict_pairs[last] != chr:
                    return False

        if len(stack) > 0:
            return False
        return True

