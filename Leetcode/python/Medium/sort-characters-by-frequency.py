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


## Solution 1 : O(nlon n)

# class Solution:
#     def frequencySort(self, s: str) -> str:
#
#         hash_table = {}  ## initalize a empty hash table
#
#         ## build the frequency hash table
#         for chr in s:
#             if chr in hash_table.keys():
#                 hash_table[chr] += 1
#             else:
#                 hash_table[chr] = 1
#
#         ## sort the keys based on the value with descending order
#         hash_table = (sorted(hash_table.items(), key=lambda x: x[1], reverse=True))
#
#         result = ''
#         ## concatenate the characters in result based on the frequencies
#         for key, value in hash_table:
#             for i in range(value):
#                 result += key
#
#         return result


## Solution 2 : O(n)


## the idea here is to use bucket sort.

## Step 1 : get the frequency of characters in a hashMap


class Solution:
    def frequencySort(self, s: str) -> str:
        hash_table = {}  ## initalize a empty hash table

        ## build the frequency hash table
        for chr in s:
            if chr in hash_table.keys():
                hash_table[chr] += 1
            else:
                hash_table[chr] = 1

        ## find the maximum frequnecy
        max_freq=max(hash_table.values())

        ## Create the buckets of occurences of characters
        ## the index of the array bucket refers to the frequency of the characters
        buckets=[ [] for x in range(max_freq+1) ]
        for key,value in hash_table.items():
            buckets[value].append(key)

        #print(buckets)
        ## Now build the string
        result_str=''
        for element in range(len(buckets)-1,0,-1):
            #print(buckets[element])
            for chr in buckets[element]:
                result_str+=chr*element
        #print(result_str)
        return result_str
        #print(buckets)



object=Solution()

s="tree"

print(object.frequencySort(s))






























