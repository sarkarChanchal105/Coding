# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)  ## Create a dummy node with value zero
        dummy.next = head  ## put the dummy node righ in front of head. This become a pre head

        node = head  ## Initliaze variable node. starts from head

        hashTable = {0: dummy}  ## Keey a dictionary of prefix sum and the node object

        currentSum = 0  ## prefixsum =0

        ### Populate the dictionary with the prefix sum
        while node is not None:
            currentSum += node.val  ## calculte prefix sum until the current node
            hashTable[currentSum] = node  ## keep track of the current node
            node = node.next

        node = dummy
        currentSum = 0
        while node is not None:
            # print("..........................................................")
            currentSum += node.val  ## Calculate the prefix sum again
            # print("CurSum: {} Node: {}".format(currentSum, node))
            node.next = hashTable[
                currentSum].next  ## if the current prexis sum exisits already then delete all inbeween nodes between the current node
            # print("CurSum: {} Node: {}".format(currentSum, node))
            ## and the node which computed the the same prefix sum
            node = node.next  ## Move on the next node
            # print("CurSum: {} Node: {}".format(currentSum, node))
            # print("..........................................................")

        return dummy.next

