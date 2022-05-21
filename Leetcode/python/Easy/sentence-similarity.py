"""
https://leetcode.com/problems/sentence-similarity/

We can represent a sentence as an array of words, for example, the sentence "I am happy with leetcode" can be represented as arr = ["I","am",happy","with","leetcode"].

Given two sentences sentence1 and sentence2 each represented as a string array and given an array of string pairs similarPairs where similarPairs[i] = [xi, yi] indicates that the two words xi and yi are similar.

Return true if sentence1 and sentence2 are similar, or false if they are not similar.

Two sentences are similar if:

They have the same length (i.e., the same number of words)
sentence1[i] and sentence2[i] are similar.
Notice that a word is always similar to itself, also notice that the similarity relation is not transitive. For example, if the words a and b are similar, and the words b and c are similar, a and c are not necessarily similar.



Example 1:

Input: sentence1 = ["great","acting","skills"], sentence2 = ["fine","drama","talent"], similarPairs = [["great","fine"],["drama","acting"],["skills","talent"]]
Output: true
Explanation: The two sentences have the same length and each word i of sentence1 is also similar to the corresponding word in sentence2.
Example 2:

Input: sentence1 = ["great"], sentence2 = ["great"], similarPairs = []
Output: true
Explanation: A word is similar to itself.
Example 3:

Input: sentence1 = ["great"], sentence2 = ["doubleplus","good"], similarPairs = [["great","doubleplus"]]
Output: false
Explanation: As they don't have the same length, we return false.


Constraints:

1 <= sentence1.length, sentence2.length <= 1000
1 <= sentence1[i].length, sentence2[i].length <= 20
sentence1[i] and sentence2[i] consist of English letters.
0 <= similarPairs.length <= 1000
similarPairs[i].length == 2
1 <= xi.length, yi.length <= 20
xi and yi consist of lower-case and upper-case English letters.
All the pairs (xi, yi) are distinct.


"""


class Solution:
    def areSentencesSimilar(self, sentence1 , sentence2, similarPairs):

        if len(sentence1) != len(sentence2):
            return False
        setSimilarPairs = set()
        for element in similarPairs:
            setSimilarPairs.add((element[0],element[1]))

        for i, word1 in enumerate(sentence1):
            word2=sentence2[i]
            if word1 == word2:
                continue
            elif (word1,word2) in setSimilarPairs or (word2,word1) in setSimilarPairs :
                continue
            else:
                return False

        return True





# sentence1=["an","extraordinary","meal"]
# sentence2=["a","good","dinner"]
# similarPairs=[["great","good"],["extraordinary","good"],["well","good"],["wonderful","good"],["excellent","good"],["fine","good"],
#               ["nice","good"],["any","one"],["some","one"],["unique","one"],["the","one"],["an","one"],["single","one"],["a","one"],["truck","car"],
#               ["wagon","car"],["automobile","car"],["auto","car"],["vehicle","car"],["entertain","have"],["drink","have"],["eat","have"],["take","have"],["fruits","meal"],
#               ["brunch","meal"],["breakfast","meal"],["food","meal"],["dinner","meal"],["super","meal"],["lunch","meal"],["possess","own"],["keep","own"],["have","own"],
#               ["extremely","very"],["actually","very"],["really","very"],["super","very"]]

# sentence1=["great","acting","skills"]
# sentence2=["fine","painting","talent"]
# similarPairs=[["great","fine"],["drama","acting"],["skills","talent"]]
#



sentence1=["an","extraordinary","meal"]
sentence2=["one","good","dinner"]
similarPairs=[["great","good"],["extraordinary","good"],["well","good"],["wonderful","good"],["excellent","good"],["fine","good"],["nice","good"],["any","one"],["some","one"],["unique","one"],["the","one"],
              ["an","one"],["single","one"],["a","one"],["truck","car"],["wagon","car"],["automobile","car"],["auto","car"],["vehicle","car"],["entertain","have"],["drink","have"],["eat","have"],["take","have"],
              ["fruits","meal"],["brunch","meal"],["breakfast","meal"],["food","meal"],["dinner","meal"],["super","meal"],["lunch","meal"],["possess","own"],["keep","own"],["have","own"],["extremely","very"],
              ["actually","very"],["really","very"],["super","very"]]



object=Solution()
print(object.areSentencesSimilar(sentence1,sentence2,similarPairs))








