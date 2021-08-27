"""

https://leetcode.com/problems/find-median-from-data-stream/solution/

"""


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.sortedArray = []
        self.lenght = len(self.sortedArray)

    def addNum(self, num: int) -> None:

        # self.arr.append(num)
        # self.arr = sorted(self.arr)
        # print("AddNume : array", self.sortedArray)
        self.insertElementInASortedArray(num)
        self.lenght += 1

    def findMedian(self) -> float:

        k = int(self.lenght / 2)

        if self.lenght % 2 == 0:
            return float(self.sortedArray[k - 1] + self.sortedArray[k]) / 2

        else:
            return self.sortedArray[k]

    def binSearchFindPosition(self, target):
        ## Use the binary search technique to find the position of the element to be inserted in the sorted
        start = 0
        end = len(self.sortedArray) - 1
        while start <= end: ## run the loop until start, end cross each other
            mid = (start + end) // 2
            if self.sortedArray[mid] == target:  ## if the element at mid is equal then return mid
                return mid
            else:
                if self.sortedArray[mid] < target: ## if the element at mid is less than target then solution existis between mid+1 and end
                    start = mid + 1
                else:
                    end = mid - 1 ## else solution exits between start and mid -1

        return start ## if target was never found then return start or end+1

    def insertElementInASortedArray(self, target):

        # n=len(self.sortedArray)
        n = self.lenght
        # print("sortedArray:",self.sortedArray)
        # print("n=",n)
        position = self.binSearchFindPosition(target)
        self.sortedArray.append(None)
        i = n
        while i > position:
            self.sortedArray[i] = self.sortedArray[i - 1]
            i -= 1

        self.sortedArray[position] = target
        # print(self.sortedArray)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# array=[1,3,5,6,20,21,22,34,100]
# object=MedianFinder(array)
#
# target=40
# #print(object.binSearchFindPosition(array,target))
# object.insertElementInASortedArray(target)



object=MedianFinder()

object.addNum(1)
object.addNum(2)
print(object.findMedian())
object.addNum(3)
print(object.findMedian())

# object.addNum(1)
# print(object.findMedian())



