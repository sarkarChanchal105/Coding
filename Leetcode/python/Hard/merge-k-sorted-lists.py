"""
https://leetcode.com/problems/merge-k-sorted-lists/

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeTwoLists(self, l1, l2):
        prehead = ListNode(-1)
        prev = prehead
        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next

            else:
                prev.next = l2
                l2 = l2.next

            prev = prev.next

        if l1 is not None:
            prev.next = l1
        else:
            prev.next = l2

        return prehead.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        if len(lists) == 0:
            return

        if len(lists) == 1:
            if lists[0]:
                return lists[0]
            else:
                return

        n = len(lists)

        result = self.mergeTwoLists(lists[0], lists[1])

        for j in range(2, n):
            result = self.mergeTwoLists(result, lists[j])

        return result