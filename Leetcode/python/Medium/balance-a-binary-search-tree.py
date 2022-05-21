""""
https://leetcode.com/problems/balance-a-binary-search-tree/
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.



Example 1:


Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
Example 2:


Input: root = [2,1,3]
Output: [2,1,3]


Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 105
Accepted
62,469
Submissions
79,408
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self._arrayTraversal_ = []
        self.inorderTraverSal(root)
        # print(self._arrayTraversal_)
        return self.formBST_from_SortedArray(self._arrayTraversal_)

    def formBST_from_SortedArray(self, array):

        if not array:
            return None

        mid = len(array) // 2

        root = TreeNode(array[mid])

        root.left = self.formBST_from_SortedArray(array[:mid])

        root.right = self.formBST_from_SortedArray(array[mid + 1:])

        return root

    ## Get the sorted array from in order raversal

    def inorderTraverSal(self, root):

        if root:
            self.inorderTraverSal(root.left)
            self._arrayTraversal_.append(root.val)
            self.inorderTraverSal(root.right)

