"""
https://leetcode.com/problems/sort-characters-by-frequency/

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

"""


class Solution:
    def frequencySort(self, s: str) -> str:

        hash_table = {}  ## initalize a empty hash table

        ## build the frequency hash table
        for chr in s:
            if chr in hash_table.keys():
                hash_table[chr] += 1
            else:
                hash_table[chr] = 1

        ## sort the keys based on the value with descending order
        hash_table = (sorted(hash_table.items(), key=lambda x: x[1], reverse=True))

        result = ''
        ## concatenate the characters in result based on the frequencies
        for key, value in hash_table:
            for i in range(value):
                result += key

        return result

