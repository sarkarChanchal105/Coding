"""

https://leetcode.com/explore/interview/card/google/59/array-and-strings/3047/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start = 0  ## Initialize start and end to the first position
        end = 0  ## Initialize start and end to the first position
        dict = {}  ## dictionary to keey track of the position of the elements

        n = len(s)  ## calculate the length of the string
        ## Handling trivial/edge cases. if lenght is zero then return zero
        if n == 0:
            return 0
        max_length = 1 ## initalize max lenght to zero


        while end < n:  ## if the end has not reached end of the string
            if s[end] in dict.keys(): ## if the character has not repeated before
                if max_length < end - start: ## check if end-start is more than max lenght
                    max_length = end - start
                # if a character is repeated then move start the next character of the firt aoccurence of
                # the repeated character
                start = dict[s[end]] + 1
                end = start ## end should point to start
                dict = {} ## reset the dictionary
            else:
                dict[s[end]] = end ## keep tracking of the position of the elements
                end += 1
        ## calculate the max lenght and return
        if end - start > max_length:
            return end - start

        return max_length


object = Solution()

s = "au"
# s="aab"
# s="abcabcbb"
# s="dvdf"

print(object.lengthOfLongestSubstring(s))
