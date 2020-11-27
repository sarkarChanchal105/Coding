"""
https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?



"""


class SparseVector:
    def __init__(self, nums: List[int]):
        self.tupple = []

        ## Creating pari of tupples index amd value where value non zero
        for i in range(len(nums)):
            if nums[i] != 0:
                self.tupple.append((i, nums[i]))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVectorq') -> int:
        ans = 0
        ## multiplye value if an onely if the ondexes match
        for tup1 in self.tupple:
            for tup2 in vec.tupple:
                if tup1[0] == tup2[0]:
                    ans += tup1[1] * tup2[1]

        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)