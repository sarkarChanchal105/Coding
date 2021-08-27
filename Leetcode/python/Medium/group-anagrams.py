"""
https://leetcode.com/problems/group-anagrams/solution/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.


"""


# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#
#         hash_table = {}  ## Create the hash table
#
#         for string in strs:
#             sorted_string = ''.join(sorted(string))  ## get the sorted version of the string
#
#             ## if the sorted string already exsit then append to the existing key
#             ## if not then create a new key
#             if sorted_string in hash_table.keys():
#                 hash_table[sorted_string].append(string)
#             else:
#                 hash_table[sorted_string] = [string]
#
#         return hash_table.values()  ## return the values only



## Better solution  O(NK)  O(NK)
from collections import defaultdict
class Solution:
    def groupAnagrams(self,strs):
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26 ## since all characters are lower case
            for c in s:
                count[ord(c) - ord('a')] += 1 ##
            ans[tuple(count)].append(s)
        print(ans)
        return ans.values()


object=Solution()

strs = ["eat","tea","tan","ate","nat","bat"]

print(object.groupAnagrams(strs))









