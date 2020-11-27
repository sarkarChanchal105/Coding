"""
https://leetcode.com/problems/binary-tree-inorder-traversal/

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def helper(self, node, result):
        if node is None:
            return
        if node.left:
            self.helper(node.left, result)

        result.append(node.val)

        if node.right:
            self.helper(node.right, result)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.helper(root, result)
        return result