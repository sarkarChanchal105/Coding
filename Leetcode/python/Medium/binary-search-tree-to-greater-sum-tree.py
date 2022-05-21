"""
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

1038. Binary Search Tree to Greater Sum Tree
Medium

2005

120

Add to List

Share
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## The idea here is to use reverse In Order Traversal

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.subTotal = 0
        self.bstToGstHelter(root)

        return root

    def bstToGstHelter(self, root):
        if not root:
            return

        self.bstToGstHelter(root.right)
        self.subTotal = root.val + self.subTotal
        root.val = self.subTotal
        self.bstToGstHelter(root.left)
