"""
https://leetcode.com/problems/find-mode-in-binary-search-tree/

Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.


For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2


return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).



"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
The idea is to traverse the tree, store the values of the nodes in a dictionary , calculate the frequencies and then get the mode

"""


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:

        if not root:
            return

        dict_node = {}
        self.traverse_tree(root, dict_node)

        ##print(sorted(dict_node.items(),key=lambda x:x[1], reverse=True))

        max_freq = max(dict_node.values())
        result = []
        for k, v in dict_node.items():
            if v == max_freq:
                result.append(k)

        return result

    def traverse_tree(self, root, dict_node):

        if root is None:
            return

        if root.val in dict_node.keys():
            dict_node[root.val] += 1
        else:
            dict_node[root.val] = 1
        self.traverse_tree(root.left, dict_node)
        self.traverse_tree(root.right, dict_node)

