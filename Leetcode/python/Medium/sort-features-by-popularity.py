"""
https://leetcode.com/problems/sort-features-by-popularity/

You are given a string array features where features[i] is a single word that represents the name of a feature of the latest product you are working on. You have made a survey where users have reported which features they like. You are given a string array responses, where each responses[i] is a string containing space-separated words.

The popularity of a feature is the number of responses[i] that contain the feature. You want to sort the features in non-increasing order by their popularity. If two features have the same popularity, order them by their original index in features. Notice that one response could contain the same feature multiple times; this feature is only counted once in its popularity.

Return the features in sorted order.



Example 1:

Input: features = ["cooler","lock","touch"], responses = ["i like cooler cooler","lock touch cool","locker like touch"]
Output: ["touch","cooler","lock"]
Explanation: appearances("cooler") = 1, appearances("lock") = 1, appearances("touch") = 2. Since "cooler" and "lock" both had 1 appearance, "cooler" comes first because "cooler" came first in the features array.
Example 2:

Input: features = ["a","aa","b","c"], responses = ["a","a aa","a a a a a","b a"]
Output: ["a","aa","b","c"]




"""

from collections import defaultdict

class Solution:
    def sortFeatures(self, features, responses) :

        hashTable = defaultdict(int)

        for i, sentence in enumerate(responses):

            for word in sentence.split():

                if word in hashTable:

                    hashTable[word].add(i)

                else:
                    hashTable[word] = set([i])

        # print(hashTable)

        for key, value in hashTable.items():
            hashTable[key] = len(value)

        # print(hashTable)

        #         newArray=[(i,x) for i,x in enumerate(features)]

        #         print(newArray)

        return sorted(features, key=lambda x: hashTable[x], reverse=True)




object=Solution()


features=["a","aa","b","c"]
responses=["a","a aa","a a a a a","b a"]

print(object.sortFeatures(features,responses))

