"""
https://leetcode.com/explore/interview/card/google/63/sorting-and-searching-4/450/

"""


class Solution:
    def merge(self, intervals):

        n = len(intervals) #3 Ge the lenght of the interval array

        ## Take care of the edge cases
        if n == 1:
            return intervals
        if intervals == []:
           return intervals


        ## Sort the intervals in ascding  order based on the first start time
        intervals = sorted(intervals, key=lambda x: x[0])


        result = [] ## Initialize the result array
        i = 0
        first = intervals[i] ##  First
        second = intervals[i + 1] ## Secomd
        while i < n:
            if first[1] >= second[0]: ## if this is true then the intervals are over lapping
                first = [first[0], max(second[1], first[1])]
                i = i + 1
                if i >= n:## Reached the end of the intervals.
                    result.append(first)
                    break
                second = intervals[i] ## pick the next pair of intervals
            else:
                ## if there is no overlapping we can safely insert first.
                ## check the seconf if that overlaps with the next one
                result.append(first)  ## append the results
                first = second ## assign
                i += 1
                if i == n:
                    result.append(second) ## apend the interval to result
                    break
                else:
                    second = intervals[i]

        return result


object=Solution()
intervals=[[1,3],[2,6],[8,10],[15,18]]
#intervals=[[1,4],[2,3]]
#intervals=[[1,4],[4,5]]
#intervals=[[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
print(object.merge(intervals))