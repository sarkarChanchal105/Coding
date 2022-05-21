# class Solution:

#     ## Using linear Search O(N)
#     def peakIndexInMountainArray(self, arr: List[int]) -> int:

#         i=0

#         for i in range(len(arr)-1):
#             if arr[i]< arr[i+1]:
#                 continue
#             else:
#                 break

#         return i


class Solution:

    ## Using Binary Search O(Log N)
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        lo = 0;
        hi = len(arr) - 1

        while lo < hi:

            mid = lo + ((hi - lo) // 2)

            if arr[mid] < arr[mid + 1]:
                lo = mid + 1
            else:
                hi = mid

        return lo


arr = [24,69,100,99,79,78,67,36,26,19]
object=Solution()

object.peakIndexInMountainArray(arr)