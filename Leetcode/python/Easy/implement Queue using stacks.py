"""

https://leetcode.com/problems/implement-queue-using-stacks/solution/
"""


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1=[] ## Actual queue
        self.s2 = [] ## aux stack


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s2.append(x)

        while self.s2:
            self.s1.append(self.s2.pop())



    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # while self.s1:
        #     self.s2.append(self.s1.pop())
        # self.s2.pop()
        # while self.s2:
        #     self.s1.append(self.s2.pop())

        return self.s1.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.s1:
            return self.s1[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.s1)==0:
            return True
        return False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()