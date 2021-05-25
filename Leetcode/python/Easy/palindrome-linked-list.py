"""
https://leetcode.com/problems/palindrome-linked-list/
Given the head of a singly linked list, return true if it is a palindrome.



Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false


Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9


Follow up: Could you do it in O(n) time and O(1) space?


"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        if head is None:
            return True

        pointer = head
        n = 0
        while pointer is not None:
            pointer = pointer.next
            n += 1

        # print(n)
        pointer = head
        i = 0

        m = int(n / 2)
        if n % 2 != 0:
            m = m + 1

        while i < m - 1:
            pointer = pointer.next
            i += 1

        # print(pointer, pointer.val)

        new = self.reverseLinkedList(pointer.next)

        pointer.next = new

        pointer = head

        while new is not None:
            if pointer.val != new.val:
                return False

            pointer = pointer.next
            new = new.next

        return True

    def reverseLinkedList(self, head):
        if head is None:
            return
        previous = head
        current = head.next

        while current is not None:
            # print(current.val, previous.val)
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        # print(current, previous.val)

        head.next = None
        head = previous

        return head





