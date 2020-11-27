"""
https://leetcode.com/explore/featured/card/google/60/linked-list-5/3064/

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        lenLst = 0
        node = head
        while node is not None:
            lenLst += 1
            node = node.next

        position = lenLst - n

        if position == 0:
            return head.next

        node = head

        for i in range(position - 1):
            node = node.next
        # print("Node.Val=",node.val)
        node_to_del = node.next
        # print("Node to Delete=",node_to_del.val)
        node.next = node_to_del.next

        return head


    def removeNthFromEndSinglePass(self, head: ListNode, n: int) -> ListNode:
        lenLst = 0
        node = head
        while node is not None:
            lenLst += 1
            node = node.next

        position = lenLst - n

        if position == 0:
            return head.next

        node = head

        for i in range(position - 1):
            node = node.next
        # print("Node.Val=",node.val)
        node_to_del = node.next
        # print("Node to Delete=",node_to_del.val)
        node.next = node_to_del.next

        return head
