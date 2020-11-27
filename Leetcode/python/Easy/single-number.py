"""

https://leetcode.com/problems/single-number/
"""


class Solution:
    def singleNumber(self, nums):
        cache={}
        for a in nums:
            if a in cache.keys():
                cache[a]+=1
            else:
                cache[a]=1

        for k,v in cache.items():
            if v==1:
                return k