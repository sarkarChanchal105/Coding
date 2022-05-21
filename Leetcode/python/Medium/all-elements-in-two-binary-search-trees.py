"""
https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

1305 All Elements in Two Binary Search Trees
Medium

1168

42

Add to List

Share
Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.



Example 1:


Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
Example 2:

Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]
Example 3:

Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]
Example 4:

Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]
Example 5:


Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]



"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
The idea is to capture the inorder traveral of both of the BST into two arrays and then merge them in one sigle array.

"""


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        result1 = []
        result2 = []

        self.inorder(root1, result1)
        self.inorder(root2, result2)
        return self.mergeTwoSortedArray(result1, result2)

    def mergeTwoSortedArray(self, array1, array2):

        result = []
        m = len(array1)
        n = len(array2)

        i = j = 0

        while i < m and j < n:

            if array1[i] > array2[j]:
                result.append(array2[j])
                j += 1
            else:
                result.append(array1[i])
                i += 1

        # print(i,m,j,n)

        while i < m:
            result.append(array1[i])
            i += 1

        while j < n:
            result.append(array2[j])
            j += 1

        return result

    def inorder(self, root, result):

        if not root:
            return

        if root:
            self.inorder(root.left, result)

            result.append(root.val)

            self.inorder(root.right, result)







