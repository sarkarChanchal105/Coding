

"""
https://leetcode.com/problems/add-two-numbers/
"""

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None


class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def append(self,data):
        if self.head is None:
            self.head=Node(data)
            self.tail=self.head
        else:
            temp=Node(data)
            self.tail.next=temp
            self.tail=temp

    def printLinkedlist(self):
        node=self.head
        if node is None:
            print("Head is none")
        else:
            while node is not None:
                print(node.data, end=' ')
                node =node.next



class Solution:
    def addTwoNumbers(self, l1, l2):
        l3=linkedList()
        p=l1.head
        q=l2.head
        carry=0
        while p is not None or q is not None:
            x,y=0,0
            if p is not None:
                x=p.data
                p=p.next
            if q is not None:
                y=q.data
                q = q.next
            sum=x+y+carry
            carry=sum//10
            sum=sum%10
            l3.append(sum)
        return l3


## Leetcode Solution
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        l3 = ListNode()  ## Initalize the empty list
        k = l3  ## store the pointer to the empty node
        p = l1  ## first list
        q = l2  ## Second list
        carry = 0  ## By default carry is zero
        while p is not None or q is not None:
            x, y = 0, 0
            if p is not None:
                x = p.val  ## get the value from list l1
                p = p.next
            if q is not None:
                y = q.val  ## get the value from list l2
                q = q.next
            sum = x + y + carry  ## Calculate the sum
            carry = sum // 10  ## Calculate the reuslts after divding sum by 10 (Integer)
            sum = sum % 10  ## Calculate the remainder
            l3.next = ListNode(sum)  ## add the sum to the new list. l3
            l3 = l3.next  ## Move the pointer to the next position

        ## if the carry is greter than..which is actually aleays 1. append a node withg value 1
        if carry > 0:
            l3.next = ListNode(carry)

        ## return pointer to new list.
        return k.next




l1=linkedList()
a=[2,4,3]
for A in a:
    l1.append(A)
#print(l1.head.data)
# print(l1.head.next.data)
# print(l1.head.next.next.data)
# print(l1.tail.data)

b=[5,6,4]
l2=linkedList()
for B in b:
    l2.append(B)


l1.printLinkedlist()
print("\n")
l2.printLinkedlist()

print("\n")
object=Solution()
l3=object.addTwoNumbers(l1,l2)
l3.printLinkedlist()