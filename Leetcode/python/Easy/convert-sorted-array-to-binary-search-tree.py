"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        left = 0;
        right = len(nums) - 1  ## get the left and right . inilize eith 0 and len(nums)- respetively

        return self.helperFuction(left, right, nums)  ## use the helper function. Conceptually binary search

    def helperFuction(self, left, right, nums):
        if left > right:  ## if left is greater than right that there is no element avilable in the sub tree
            return None

        mid = (left + right) // 2  ## calculate the mid position

        root = TreeNode(nums[mid])  ## the middelement is the root
        root.left = self.helperFuction(left, mid - 1, nums)  ## recursively build the left sub tree
        root.right = self.helperFuction(mid + 1, right, nums)  ## recusrsively build the right sub tree

        return root  ## return root


"""
Complexity Analysis

Time complexity: \mathcal{O}(N)O(N) since we visit each node exactly once.

Space complexity: \mathcal{O}(N)O(N). \mathcal{O}(N)O(N) to keep the output, and \mathcal{O}(\log N)O(logN) for the recursion stack.

"""