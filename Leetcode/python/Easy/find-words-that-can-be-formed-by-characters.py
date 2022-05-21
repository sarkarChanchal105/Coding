"""
https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

1160. Find Words That Can Be Formed by Characters
Easy

805

111

Add to List

Share
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.



Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

"""


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        hashTableOfChars = {}

        for chr in chars:

            if chr in hashTableOfChars:
                hashTableOfChars[chr] += 1
            else:
                hashTableOfChars[chr] = 1

        result = 0

        for word in words:

            if self.helperFuction(word, hashTableOfChars):
                result += len(word)

        return result

    def helperFuction(self, word, hashTableOfChars):

        tempHashTable = {}

        for chr in word:
            if chr in tempHashTable:
                tempHashTable[chr] += 1
            else:
                tempHashTable[chr] = 1

        for key, value in tempHashTable.items():

            if key in hashTableOfChars:
                if value > hashTableOfChars[key]:
                    return False
            else:
                return False

        return True



