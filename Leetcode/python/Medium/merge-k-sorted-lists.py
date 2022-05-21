"""
https://leetcode.com/problems/merge-k-sorted-lists/

ou are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []


Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:

#     def mergeTwoLists(self, l1,l2):
#         prehead=ListNode(-1) ### pointer the result list
#         prev=prehead ## lets initilaize another pointer
#         while l1 and l2: ## if l1 and l3 are not None
#             if l1.val<l2.val: ## if l1.val is less than l2
#                 prev.next=l1  ## the current pointer of the list should point to l1
#                 l1=l1.next  ## lets move the pointer of L1 to next

#             else:
#                 prev.next=l2 ## if l1.val >=l2.next then point the new linked list to l2 memory location
#                 l2=l2.next  ## Move to the next location

#             prev=prev.next

#         if l1 is not None: ## remaining elements are in L1
#             prev.next= l1
#         else:
#             prev.next=l2 ## remaining elements are in L2

#         return prehead.next ## return the next pointer to prehead

#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:

#             ## Handling the edge cases
#             if len(lists)==0:
#                 return
#             if len(lists)==1:
#                 if lists[0]:
#                     return lists[0]
#                 else:
#                     return

#             n=len(lists)

#             ## merge the firsl two lists
#             result=self.mergeTwoLists(lists[0],lists[1])

#             ## iteratively merge rest of the list.
#             for j in range(2,n):
#                 result=self.mergeTwoLists(result,lists[j])

#             return result


"""

The idea is to use heap . Insert all elements into a MinHeap. and then pop the elements one by one and add the elements to a new linked list.

"""

import heapq


class Solution:

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        head = ListNode(None)  ## create a preHead with Value None

        ## build the heap with all elements
        heap = []
        for lsthead in lists:
            node = lsthead
            while node:
                heapq.heappush(heap, node.val)
                node = node.next

        ## create a linkedList by popping the elements from the  Heap
        node = head
        while heap:
            Newnode = ListNode(heapq.heappop(heap))
            node.next = Newnode
            node = node.next

        return head.next






