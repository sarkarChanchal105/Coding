"""
https://leetcode.com/problems/top-k-frequent-words/solution/

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.

"""
import heapq, collections


class Solution:
    # def topKFrequent(self, words, k):
    #     hash_table = {}
    #
    #     for word in words:
    #         if word in hash_table:
    #             hash_table[word] += 1
    #         else:
    #             hash_table[word] = 1
    #
    #     sorted_words = sorted(hash_table.items(), key=lambda item: (-item[1], item[0]))
    #
    #     print(sorted_words)
    #
    #     result = []
    #
    #     for i in range(k):
    #         result.append(sorted_words[i][0])
    #     return result
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]


words=["i", "love", "leetcode", "i", "love", "coding"]
k=2

object=Solution()

print(object.topKFrequent(words,k))