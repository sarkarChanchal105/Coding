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

