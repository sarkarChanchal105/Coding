from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size=size
        self.window=[]
        self.queue=deque()
        self.sumof=0
        self.counter=0


#     def next(self, val: int) -> float:

#         self.window.append(val)

#         if len(self.window)>self.size:
#             self.window.pop(0)

#         return float(sum(self.window)/len(self.window))

#     def next(self, val: int) -> float:  ## Peforms better

#         self.window.append(val)
#         self.sumof+=val

#         if len(self.window)>self.size:
#             self.sumof=self.sumof-self.window[0]
#             self.window.pop(0)


#         return float(self.sumof/len(self.window))


    def next(self, val: int) -> float:  ## Peforms even better better O(1) / O(N) N: Window Size
        self.queue.append(val)
        self.counter+=1
        self.sumof+=val

        if self.counter>self.size:
            tail=self.queue.popleft()
            self.counter-=1
            self.sumof-=tail

        return self.sumof / min(self.counter, self.size)



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)