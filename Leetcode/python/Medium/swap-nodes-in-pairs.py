""""
https://leetcode.com/problems/swap-nodes-in-pairs/

Given a linked list, swap every two adjacent nodes and return its head.



Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]


Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100

"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        first = head

        ## Handle the edge case if the list as no noded
        if not head:
            return head

        ## keep on swapping the values until valid first, first.nect and first.next.next
        while first and first.next and first.next.next:
            first.val, first.next.val = first.next.val, first.val
            first = first.next.next

        ## if we still have the next node . handling the edge case when there is only one node
        if first.next:
            first.val, first.next.val = first.next.val, first.val

        return head  ## return head