"""
https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


https://www.youtube.com/watch?v=3c-p4zWx5yU


"""


## O(nlogn) implementation
# from collections import defaultdict
#
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         dict = defaultdict(int)
#
#         for a in nums:
#             dict[a] += 1
#
#         return (sorted(dict, key=lambda x: dict[x], reverse=True)[:k])




## O(nlogk) implementation
## Step 1 : Build a hashmap with the frequency of the elements
## Step 2:  Build a heap of size k using N elements .
    ## First insert k elemments with time complemexistu O(klogk)
    ## Next, heapPush and heappop N-k elemenets into the heap.
    ## we start popping only when the hapsize become more than K
    ## heappop the lowest from the top and heappush the next element and adjust the position.

from collections import defaultdict

import heapq

class Solution:
    def topKFrequent(self, nums, k: int):
        dict = defaultdict(int)
        for a in nums:
            dict[a] += 1

        return  [ x[0] for x in  heapq.nlargest(k, dict.items(),key= lambda x:x[1]) ]




object=Solution()


nums=[1,1,1,2,2,3]
k=2

print(object.topKFrequent(nums,k))




