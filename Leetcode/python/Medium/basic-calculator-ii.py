"""
https://leetcode.com/problems/basic-calculator-ii/
Given a string s which represents an expression, evaluate this expression and return its value.
The integer division should truncate toward zero.
Example 1:
Input: s = "3+2*2"
Output: 7
Example 2:
Input: s = " 3/2 "
Output: 1
Example 3:
Input: s = " 3+5 / 2 "
Output: 5
Constraints:
1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
"""


class Solution:
    def calculate(self, s):
        current_number, stack, previous_operator=0,[],'+'

        all_operators={'+','-','/','*'} ## Create a set of operators
        all_numbers=set(str(i) for i in range(10)) ## create a set of positive integers

        ## for each character in the string
        for index in range(len(s)):
            char=s[index]

            if char in all_numbers: ## if the character is a number
                current_number=current_number*10+int(char)  ## keep on formig the complete number untile we encounter an operator

            if char in all_operators or index==len(s)-1: ## if we have encounterteed an operator or reached the end of the string (edge case)
                if previous_operator=='+':
                    stack.append(current_number) ## if the previous operator is + simply append the number to the stack
                if previous_operator=='-':
                    stack.append(-current_number) ## if the previous operator is - simply append the negtive value of the current number
                if previous_operator=='*':  ## if the previous operator is * then evaluate the value. Update the last lement of the stack
                    stack[-1]=stack[-1]*current_number

                if previous_operator=='/':
                    stack[-1]= int(stack[-1]/current_number)

                current_number=0
                previous_operator=char

        return sum(stack)


s= "46"
object=Solution()
print(object.calculate(s))












