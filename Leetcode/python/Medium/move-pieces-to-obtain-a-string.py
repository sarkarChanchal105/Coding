"""
https://leetcode.com/problems/move-pieces-to-obtain-a-string/

You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R', and '_' where:

The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space directly to its left, and a piece 'R' can move to the right only if there is a blank space directly to its right.
The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.
Return true if it is possible to obtain the string target by moving the pieces of the string start any number of times. Otherwise, return false.



Example 1:

Input: start = "_L__R__R_", target = "L______RR"
Output: true
Explanation: We can obtain the string target from start by doing the following moves:
- Move the first piece one step to the left, start becomes equal to "L___R__R_".
- Move the last piece one step to the right, start becomes equal to "L___R___R".
- Move the second piece three steps to the right, start becomes equal to "L______RR".
Since it is possible to get the string target from start, we return true.
Example 2:

Input: start = "R_L_", target = "__LR"
Output: false
Explanation: The 'R' piece in the string start can move one step to the right to obtain "_RL_".
After that, no pieces can move anymore, so it is impossible to obtain the string target from start.
Example 3:

Input: start = "_R", target = "R_"
Output: false
Explanation: The piece in the string start can move only to the right, so it is impossible to obtain the string target from start.

"""


class Solution:
    def canChange(self, start: str, target: str) -> bool:

        i = self.findNextChar(0, start)  ## starting position of the valid chacters in "Start"
        j = self.findNextChar(0, target)  ## starting position of the valid characters in "target"

        if i < 0 and j < 0:
            return True
        if i < 0 or j < 0:
            return False

        ## case when all characters are "_" in both strings

        while True:
            if start[i]!=target[j]: return False ## if they dont match return False
            if start[i]=='R' and i > j: return False ## since we are at 'R", we can only move right. if i >j then there is no way we can get the result. Example. Start : _R  Target=R_  in this case i=1 > j=0
            if start[i] == 'L' and i < j: return False ## since we are at "L", we can only move left. if i<j  then ther eis no way we can get the result. Example Start : L_ Target =_L . in this case i=0 < j=1

            i = self.findNextChar(i+1,start) ## check for the next character ('R' or 'L') in the starting string string
            j = self.findNextChar(j + 1, target) ## check for the next character ('R' or 'L') in the Target string

            if i < 0 and j < 0: ## if both i and j are negative then we have explored all characters
                return True
            if i < 0 or j < 0: ## if this happens then return False.
                return False

    def findNextChar(self, startingPosition, String):

        i = startingPosition
        while i < len(String) and String[i] == '_':
            i += 1
        if i == len(String):
            return -1

        return i


object = Solution()

# start="_L__R__R_"
# target="L______RR"

# start="R_L_"
# target="__LR"

start = "_L__R__R_L"
target = "L______RR_"

start = "__LL"
target = "LL__"
print(object.canChange(start, target))
