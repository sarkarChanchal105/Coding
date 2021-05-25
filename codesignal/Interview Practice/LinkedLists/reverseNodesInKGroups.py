"""
https://app.codesignal.com/interview-practice/task/XP2Wn9pwZW6hvqH67/description

Note: Your solution should have O(n) time complexity, where n is the number of elements in l, and O(1) additional space complexity, since this is what you would be asked to accomplish in an interview.

Given a linked list l, reverse its nodes k at a time and return the modified list. k is a positive integer that is less than or equal to the length of l. If the number of nodes in the linked list is not a multiple of k, then the nodes that are left out at the end should remain as-is.

You may not alter the values in the nodes - only the nodes themselves can be changed.

Example

For l = [1, 2, 3, 4, 5] and k = 2, the output should be
reverseNodesInKGroups(l, k) = [2, 1, 4, 3, 5];
For l = [1, 2, 3, 4, 5] and k = 1, the output should be
reverseNodesInKGroups(l, k) = [1, 2, 3, 4, 5];
For l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] and k = 3, the output should be
reverseNodesInKGroups(l, k) = [3, 2, 1, 6, 5, 4, 9, 8, 7, 10, 11].



"""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

import sys


def reverseNodesInKGroups(l, k):
    if k <= 1:
        return l

    pre_head = ListNode(-999)
    pre_head.next = l

    pointer = 0
    start = l
    end = start

    iteration = 0
    final_head = l
    pointer = 1
    while end is not None and start is not None:
        while pointer < k:
            end = end.next
            pointer += 1
            if end is None:
                break
        if end is None:
            break

        pointer = 0
        result = reverseLinkedList(start, end)

        # print(type(result))
        new_head = result[0]
        new_tail = result[1]
        print(new_head.value, new_head.next.value, new_head.next.next.value)
        if end and end.next:
            start = end.next
        else:
            return final_head
        if iteration == 0:
            final_head = new_head
        pre_head.next = new_head
        pre_head = new_tail
        iteration += 1
    print("Result", final_head, final_head.value)

    print("Traversing the linked list")
    traverseLinkedList(final_head)

    return l


def reverseLinkedList(head, tail):
    new_head = tail
    new_tail = head
    if head is None:
        return head

    if head.next is None:
        return head
    first = head
    second = head.next

    while second != tail and second is not None:
        temp = second.next
        second.next = first
        first = second
        second = temp
    # head.next=None
    # head=new_tail

    return new_head, new_tail


def traverseLinkedList(head):
    while head is not None:
        print(head.value, end=' ')
        head = head.next
    print("\n")