""""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?


"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        ## If empty then just return
        if head is None:
            return

        ## if there is just one element in the node just returen the head
        if head.next is None:
            return head

        ## Initialize two pointers. First and second
        first = head
        second = head.next

        ## Update the pointers in reverse order
        while (second is not None):
            temp = second.next
            second.next = first
            first = second
            second = temp

        ## At the end of the loop, second will be node and first will point to the last element of the list.
        ## The last element should be the head.

        head.next = None  ## This is needed to avoid the cyclic List node
        head = first  ## the last element is the head after reversal
        return head