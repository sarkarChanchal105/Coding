# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        hash_map = {}

        on = head
        position = 0

        while on:
            # print(on.val, on)
            if on in hash_map.keys():
                return on
            else:
                hash_map[on] = position
            position += 1
            on = on.next