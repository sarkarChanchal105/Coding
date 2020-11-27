
"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

"""




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return

        results = []

        return self.helperLevelOrderTraversal(root)

    def helperLevelOrderTraversal(self, root):

        if not root:
            return

        q = deque()  ## initlize the queue
        levels = []  ## will store the results

        q.append(root)

        left_to_right = True  ## if true print left to right else Right to left

        while q:
            level = deque()  ## using a quee since we will need to insert at the end or beginning depending on the zig zag fashion
            size = len(q)  # 3 get the soze of the queue

            # print("lveles= {}".format(levels))
            # print("left_to_right= {}".format(left_to_right))
            # print("q= {}".format(q))

            while size != 0:  ## if not zero

                item = q.popleft()  ## pop the element from left
                if left_to_right:  ## if we are going from left to right
                    level.append(item.val)  ## append the value at the end of the queue
                else:
                    level.appendleft(item.val)  ## append the value at the beginning of the queue

                if item.left:  ## is left exsits
                    q.append(item.left)  ## append the object queue
                if item.right:  ## if right exists
                    q.append(item.right)  ## append the object to the quu

                size -= 1

            left_to_right = not left_to_right  ## flip the value
            levels.append(level)  ## append the values to the results array

        return levels




"""
Complexity Analysis

Time Complexity: \mathcal{O}(N)O(N), where NN is the number of nodes in the tree.

We visit each node once and only once.

In addition, the insertion operation on either end of the deque takes a constant time, rather than using the array/list data structure where the inserting at the head could take the \mathcal{O}(K)O(K) time where KK is the length of the list.

Space Complexity: \mathcal{O}(N)O(N) where NN is the number of nodes in the tree.

The main memory consumption of the algorithm is the node_queue that we use for the loop, apart from the array that we use to keep the final output.

As one can see, at any given moment, the node_queue would hold the nodes that are at most across two levels. Therefore, at most, the size of the queue would be no more than 2 \cdot L2⋅L, assuming LL is the maximum number of nodes that might reside on the same level. Since we have a binary tree, the level that contains the most nodes could occur to consist all the leave nodes in a full binary tree, which is roughly L = \frac{N}{2}L= 
2
N
​	
 . As a result, we have the space complexity of 2 \cdot \frac{N}{2} = N2⋅  2N=N in the worst case.


"""