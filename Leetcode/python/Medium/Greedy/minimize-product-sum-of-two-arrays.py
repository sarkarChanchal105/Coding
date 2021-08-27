"""
https://leetcode.com/problems/minimize-product-sum-of-two-arrays/

"""


""""
The idea is to create minHeap and maxHeap .Keep om possing the maximum lelement from max heap and then pop minimum ele,e mmnt 

from min heal and multiple them

Time: O(NlongN)
Space=O(N)

"""

import heapq
class Solution(object):
    def minProductSum(self, nums1, nums2):
        r = 0
        maxHeap, minHeap = [], []
        for e in nums1:
            heapq.heappush(minHeap,e)
        for e in nums2:
            heapq.heappush(maxHeap,-e)
        while maxHeap:
            r -= heapq.heappop(maxHeap) * heapq.heappop(minHeap)
        return r


object=Solution()

nums1 = [2,1,4,5,7]
nums2 = [3,2,4,8,6]

print(object.minProductSum(nums1,nums2))





