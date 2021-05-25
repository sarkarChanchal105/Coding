"""
https://leetcode.com/problems/reverse-only-letters/

Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.



Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"


Note:

S.length <= 100
33 <= S[i].ASCIIcode <= 122
S doesn't contain \ or "

"""


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:

        """
        The idea is to use two pointer method. left points to 0th and right points to the last element.

        Swap left and right if and only if left and right points to an alphabet.

        after awapping increment left and decrement right untile left less than right

        """

        left = 0
        right = len(S) - 1
        arrayString = [chr for chr in S]

        while left < right:
            while not arrayString[left].isalpha() and left < right:
                left += 1

            while not arrayString[right].isalpha() and right > left:
                right -= 1

            arrayString[left], arrayString[right] = arrayString[right], arrayString[left]

            left += 1
            right -= 1

        return ''.join(arrayString)


object=Solution()

S="ab-cd"
S="7_28]"
k=object.reverseOnlyLetters(S)

print(k)

