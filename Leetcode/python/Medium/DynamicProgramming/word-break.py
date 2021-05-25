"""
https://leetcode.com/problems/word-break/

refernces : https://www.youtube.com/watch?v=1U4jQusbeJc

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.


Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

"""


## recivise solution
# class Solution:
#     def wordBreak(self, s: str, wordDict):
#
#         if len(s)==0: ## base case
#             return True
#
#         ## find the matching prefix from the dictionary ion the string
#         for x in wordDict:
#             prefix=s[0:len(x)]
#
#             ## if there is a match in prexi,
#             ## recusively call for the rest of the string
#             if prefix==x and self.wordBreak(s[len(x):],wordDict):
#                 return True
#         return False ## if no match i found then return False

## recivise solution with Dynamic Programming
class Solution:
    def wordBreak(self, s: str, wordDict):

        memoDict = {}
        return self.wordBreakHelper(s, wordDict, memoDict)

    def wordBreakHelper(self, s, wordDict, memoDict):

        print("S = {} lenght= {} Memo ={}".format(s, len(s), memoDict))
        if s in memoDict:
            return memoDict[s]

        if len(s) == 0:  ## base case
            return True

        ## find the matching prefix from the dictionary ion the string
        for x in wordDict:
            prefix = s[0:len(x)]

            ## if there is a match in prexi,
            ## recusively call for the rest of the string
            if prefix == x:
                memoDict[prefix] = True
                if self.wordBreakHelper(s[len(x):], wordDict, memoDict) == True:
                    memoDict[s] = True
                    return memoDict[s]
        return False  ## if no match i found then return False


# s = "leetcode"
# wordDict = ["leet", "code"]

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
#s = "aaaaaaaaaaaaaaaaaab"

wordDict=["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

wordDict=["aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
#wordDict = ["aaaaaaaaaa"]

object = Solution()

print(object.wordBreak(s, wordDict))
