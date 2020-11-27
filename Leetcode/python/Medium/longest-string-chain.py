"""

https://leetcode.com/problems/longest-string-chain/

Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.



Example 1:

Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".


Note:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of English lowercase letters.



"""


class Solution:
    def longestStrChain(self, words) :

        words=sorted(words,key=len) ## sort the word based on lenmght
        #print(words)
        dict={}  ## Create an empyt dictionary

        ## at first each word will have chain of length 1
        for word in words:
            dict[word]=1

        ## for each word, remove one element at a time and
        ## if the elemebt exists in the dictionary then compare which lenght is max
        for word in words:
            for i in range(len(word)):
                substr=word[0:i]+word[i+1:] ## remove one character at a time
                if substr in dict.keys(): ## if the substring already exists  in the dictionary
                    dict[word]=max(dict[word],dict[substr]+1) ## check which chain is max
        return(max(dict.values())) ## retrun the max chain value


object=Solution()
words=["a","b","ba","bca","bda","bdca"]
print(object.longestStrChain(words))













