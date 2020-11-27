"""
https://leetcode.com/problems/first-unique-character-in-a-string/submissions/

Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.


Note: You may assume the string contains only lowercase English letters.

"""


class Solution:
    def firstUniqChar(self, s: str) -> int:

        dict = {}

        for a in s:
            if a in dict.keys():
                dict[a] += 1
            else:
                dict[a] = 1

        print(dict)

        for i, b in enumerate(s):
            # print(b,i)
            if b in dict.keys():
                if dict[b] == 1:
                    # print("here")
                    return i
        return -1
