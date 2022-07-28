"""
Given a string S, return the number of substrings that have only one distinct letter.

Example 1:

Input: S = "aaaba"
Output: 8
Explanation: The substrings with one distinct letter are "aaa", "aa", "a", "b".
"aaa" occurs 1 time.
"aa" occurs 2 times.
"a" occurs 4 times.
"b" occurs 1 time.
So the answer is 1 + 2 + 4 + 1 = 8.
Example 2:

Input: S = "aaaaaaaaaa"
Output: 55


Constraints:

1 <= S.length <= 1000
S[i] consists of only lowercase English letters.


"""


class Solution:
    def countLetters(self, S: str) -> int:

        if (S =='' or len(S) ==0):
            return 0


        repeatCount=0
        result=0
        prev_char=S[0]

        for i in range(len(S)):
            if prev_char==S[i]:
                repeatCount+=1  ## For the same letter increment the repeatCount and ultimately add to result */
            else:
                repeatCount=1  ## Every time a new letter comes, make repeatCount 1

            result+=repeatCount ## For aaa first add 1, then add 2, then add 3. So 1 + 2 + 3 = 6 total substrings of aaa *
            prev_char =S[i]
        return result

object= Solution()

S="aaaba"

print(object.countLetters(S))

## Efficient Approach

"""
The idea here is to use two pointer approach left and right.

if the character left is equal to the character at right then keep on incrementing right, dont move left.

else, move left to current right and increment right.

We are using the concept of arithmetic progression we counting the number of substrings between left and right.

"""


class Solution:
    def countLetters(self, s: str) -> int:

        left, right, count, TotalCount = 0, 1, 1, 1  ## initilization

        while right < len(s):

            if s[left] == s[right]:
                count += 1  ## increment counter when we are encountering same characters

            else:
                left = right
                count = 1  ## reset counter to 1 since at left we know at least one character is distinct

            right += 1  ## keep on moving right by one
            TotalCount += count  ## Keep on counting the number of the substrings between left and right

        return TotalCount

