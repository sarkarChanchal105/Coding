"""
https://app.codesignal.com/interview-practice/task/RvDFbsNC3Xn7pnQfH/description

You're given 2 huge integers represented by linked lists. Each linked list element is a number from 0 to 9999 that represents a number with exactly 4 digits. The represented number might have leading zeros. Your task is to add up these huge integers and return the result in the same format.

Example

For a = [9876, 5432, 1999] and b = [1, 8001], the output should be
addTwoHugeNumbers(a, b) = [9876, 5434, 0].

Explanation: 987654321999 + 18001 = 987654340000.

For a = [123, 4, 5] and b = [100, 100, 100], the output should be
addTwoHugeNumbers(a, b) = [223, 104, 105].

Explanation: 12300040005 + 10001000100 = 22301040105.



"""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

"""
Overall idea is to reverse both the linked list and start adding the values of the nodes and take care of the carry

"""


def addTwoHugeNumbers(a, b):
    result_head = ListNode(
        -1)  ## Initalize the head of the result node with a negative value since we are dealing with only positive values
    last_node = ListNode(-1)  ## lsat_node
    next_node = ListNode(-1)  ## next node

    ## reverse the linkedlists
    a = reverseLinkedlist(a)
    b = reverseLinkedlist(b)

    # traverLinkedList(a)
    # traverLinkedList(b)

    carry = 0  ## initialize carry as zero

    ## travese both the list until we reach None
    while a is not None or b is not None:

        value1 = value2 = 0
        if a is None:  ## Handle the edge case when a becomes None but b is still not None
            value1 = 0
        else:
            value1 = a.value
        if b is None:  ## Handle the edge case when b becomnes None bit a is still not None
            value2 = 0
        else:
            value2 = b.value

        ## calculate the sume from
        sum = value1 + value2 + carry

        carry = 0
        if sum > 9999:  ## if sum is more than 9999 then its more than 4 digits and there is a carry of 1
            carry = 1
            sum = str(sum)[1:]  ## ge the digits by removing the 1
            sum = int(sum)

            # print("Final Value of sum : {}".format(sum))

        ## Now create new nodes as an when sums are evaluated and link the nodes
        if result_head.value == -1:
            result_head = ListNode(sum)
            last_node = result_head
        else:
            next_node = ListNode(sum)
            last_node.next = next_node
            last_node = next_node
        next_node.next = None

        if a:
            a = a.next  ## go to the next node in a
        if b:
            b = b.next  ## go to the next node in b

    if carry > 0:
        last_node.next = ListNode(carry)  ## if there is carry left created a new node and add

    # traverLinkedList(result_head)

    return reverseLinkedlist(result_head)  ## return the reversed linked list


def traverLinkedList(head):
    print("\n")
    while head is not None:
        print(head.value, end=' ')
        head = head.next


def reverseLinkedlist(head):
    if head is None:
        return head
    if head.next is None:
        return head
    first = head
    second = head.next

    while second is not None:
        temp = second.next
        second.next = first
        first = second
        second = temp

    head.next = None
    head = first

    return head
