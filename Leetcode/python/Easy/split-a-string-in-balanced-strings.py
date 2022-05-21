"""
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.



Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
Example 2:

Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
Example 3:

Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".
Example 4:

Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'


"""


class Solution:
    def balancedStringSplit(self, s: str) -> int:

        """
        Loop from left to right maintaining a balance variable when it gets an L increase it by one otherwise decrease it by one.

        Whenever the balance variable reaches zero then we increase the answer by one.

        """

        balanceVar = 0
        result = 0

        for chr in s:
            if chr == 'L':
                balanceVar += 1
            else:
                balanceVar -= 1

            if balanceVar == 0:
                result += 1

        return result
