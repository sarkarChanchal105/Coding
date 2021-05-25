"""
https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

A string is a valid parentheses string (denoted VPS) if it meets one of the following:

It is an empty string "", or a single character not equal to "(" or ")",
It can be written as AB (A concatenated with B), where A and B are VPS's, or
It can be written as (A), where A is a VPS.
We can similarly define the nesting depth depth(S) of any VPS S as follows:

depth("") = 0
depth(C) = 0, where C is a string with a single character not equal to "(" or ")".
depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's.
depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.

Given a VPS represented as string s, return the nesting depth of s.



Example 1:

Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation: Digit 8 is inside of 3 nested parentheses in the string.
Example 2:

Input: s = "(1)+((2))+(((3)))"
Output: 3
Example 3:

Input: s = "1+(2*3)/(2-1)"
Output: 1
Example 4:

Input: s = "1"
Output: 0


Constraints:

1 <= s.length <= 100
s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
It is guaranteed that parentheses expression s is a VPS.

"""

"""
The idea is to calcultate the different between the following

1. Number of left brackets before the present character
2. Number of right bracker before the presetn character

"""

class Solution:
    def maxDepth(self, s: str) -> int:
        last_char = ''
        number_of_left_bracekts_before = 0 ## Number of left brackets before presetn characet
        number_of_right_bracekts_before = 0 ## Number of right brackets before the present character
        max_depth = 0 ## Initalize max depth to zero

        ## For each character in string S
        for chr in s:
            if chr == '(':  ## if this is a left bracket then
                number_of_left_bracekts_before += 1 ## inceement by 1
            elif chr == ')': ## of this is a right bracket then
                number_of_right_bracekts_before += 1 ## Increment by 1
                if last_char == '(': ## Special case such as '()'
                    max_depth = 1+max(number_of_left_bracekts_before - number_of_right_bracekts_before, max_depth)
            else:
                ## if this neither left nor right braket then
                max_depth = max(number_of_left_bracekts_before - number_of_right_bracekts_before, max_depth)
            last_char = chr ## keep track of the last character
        return max_depth ## result



object=Solution()
s="(1+(2*3)+((8)/4))+1"
#s="()"
print(object.maxDepth(s))





