"""
https://leetcode.com/problems/n-ary-tree-level-order-traversal/

Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).



Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]
Example 2:



Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]


Constraints:

The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 10^4]



"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import deque


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        if not root:
            return

        q = deque()  ## initalize a queue
        levels = []  ## will store the results

        q.append(root)

        while q:

            size = len(q)  # get the size of the queue
            level = []  ## store the elements in this level

            while size != 0:  # 3 while we have not processed all elements in a given array
                item = q.popleft()  ## deque the first elelemt in the queue
                level.append(item.val)  ## append the value in the level array
                size -= 1  ## drecrase the size by one since we have append one element from the queue to the level

                ## now enqueue the childrens of the last processed to process the next level
                for children in item.children:
                    q.append(children)
            ## append the level array in levels
            levels.append(level)

        return levels


"""
Complexity Analysis

Time complexity : O(n)O(n), where nn is the number of nodes.

Each node is getting added to the queue, removed from the queue, and added to the result exactly once.

Space complexity : O(n)O(n).

We are using a queue to keep track of nodes we still need to visit the children of. At most, the queue will have 2 layers of the tree on it at any given time. In the worst case, this is all of the nodes. In the best case, it is just 1 node (if we have a tree that is equivalent to a linked list). The average case is difficult to calculate without knowing something of the trees we can expect to see, but in balanced trees, half or more of the nodes are often in the lowest 2 layers. So we should go with the worst case of O(n)O(n), and know that the average case is probably similar.


"""
