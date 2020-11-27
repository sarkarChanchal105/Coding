"""
https://leetcode.com/problems/binary-tree-level-order-traversal/

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]



"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:  ## Handling the edge cases
            return
        queue = [root]
        levels = []
        while queue:

            level = []  ## initliaze empty array for each level
            size = len(queue)  ## get the size of the queue for this level
            while size != 0:
                item = queue.pop(0)  ## pop the elements of this level
                level.append(item.val)  ## append the value for this level

                ## now append the next level's elements
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)

                size -= 1
            levels.append(
                level)  ## once size becomes zero that means all elements in that level has been processed. So append the level array to levels.
        return levels

    """
    Time Complexity: we are doing total N iterations. 1 per node.
    hence time complexisty is O(N)

    """