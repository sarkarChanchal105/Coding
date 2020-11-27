"""

https://leetcode.com/problems/reverse-string/
"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        high = len(s) - 1;
        low = 0

        while (high > low):
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1