"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

"""


class Solution:
    def findAnagrams(self, s: str, p: str) :
        n1 = len(s)   ## get the lenght of s
        n2 = len(p) ##  Get the lenght of p
        ans = [] ## Initialize ans as empty array
        ## Cover the base/edge cases
        if n1 == 0 or n1 < n2:
            return []
        s_array = [0] * 26  ## since lower case english characters
        p_array = [0] * 26  ## since lower case english characters
        ascii_a = ord('a')  ## get the ascii of character a

        # populate array wit the frequencies
        for chr in p:
            p_array[ord(chr) - ascii_a] += 1
        #print(p_array)
        ## populate the array with frequencies upto the lenght of string p
        for i in range(n2):
            s_array[ord(s[i]) - ascii_a] += 1
        #print(s_array)
        i = 0;
        while (i + n2 < n1): ## While the sliding window does not go out of the string
            if is_anagram(s_array, p_array) :
                ans.append(i)
            s_array[ord(s[i]) - ascii_a] -= 1 ## remove the first element of the sliding
            t=ord(s[i + n2])
            s_array[t - ascii_a] += 1  ## add new element in the sluding window
            i += 1
        if is_anagram(s_array, p_array):
            ans.append(i)
        return ans

def is_anagram(s_array, p_array):
    for i in range(26):
        if s_array[i] != p_array[i]:
            return False
    return True


object=Solution()

s="cbaebabacd"
p="abc"

# s="abab"
# p="ab"


result=object.findAnagrams(s,p)

print(result)




