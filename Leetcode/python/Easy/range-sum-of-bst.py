"""
https://leetcode.com/problems/range-sum-of-bst

938. Range Sum of BST
Easy

3005

312

Add to List

Share
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].



Example 1:


Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
Example 2:


Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.


Constraints:

The number of nodes in the tree is in the range [1, 2 * 104].
1 <= Node.val <= 105
1 <= low <= high <= 105
All Node.val are unique.



"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        self._sum_ = 0  ## Initilaize the variable

        self.rangeSumBSThelper(root, low, high)  ## Make a call to the helper fuction

        return self._sum_

    def rangeSumBSThelper(self, root, low, high, summary=0):

        if root:  ## if rooot exists

            if root.val <= high and root.val >= low:  ## check if the value of the current node falls in the bundary
                self._sum_ += root.val  ## if yes then add the value to the boundary

            if root.left:  ## recusively call for the left subtree if exists
                self.rangeSumBSThelper(root.left, low, high, summary)

            if root.right:  ## recursively call for the right subtree if exists
                self.rangeSumBSThelper(root.right, low, high, summary)

