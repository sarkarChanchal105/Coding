import queue
from typing import List


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._data = queue.Queue()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self._data.put(x)
        sz = self._data.qsize()
        while sz > 1:
            #print("Before : {}".format(self._data.queue))
            self._data.put(self._data.get())
            #print("After : {}".format(self._data.queue))
            sz -= 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self._data.get()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self._data.queue[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self._data.empty()

#Your MyStack object will be instantiated and called as such:
"""
["MyStack","push","push","push","top"]
[[],[1],[2],[3],[]]
"""
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)

print(obj.top())