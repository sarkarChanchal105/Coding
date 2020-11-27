"""
https://leetcode.com/problems/find-k-closest-elements/

Given a sorted array arr, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.



Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]


Constraints:

1 <= k <= arr.length
1 <= arr.length <= 10^4
Absolute value of elements in the array and x will not exceed 104


"""


## Use binary search mechanishm to find the cross over point
def binSearchToFindCrossOverPoint(low, high, arr, x):
    ## Base cases
    if arr[low] > x:  ## if x is smaller than all
        return low
    if arr[high] <= x:  ## if x is greater than all
        return high

    mid = (low + high) // 2 ## ge the mid position
    if x == arr[mid]:
        return mid ## return mid if there is a match
    elif arr[mid] < x:  ## search between mid+1 and high if x is grater than mid position value
        return binSearchToFindCrossOverPoint(mid + 1, high, arr, x)
    else:
        ## search between low and mid -1 if x is less than midle position value
        return binSearchToFindCrossOverPoint(low, mid - 1, arr, x)


class Solution:
    def findClosestElements(self, arr, k: int, x: int):
        low = 0
        high = len(arr) - 1

        ## get the cross over position
        #left = binSearchToFindCrossOverPoint(low, high, arr, x)
        right = binSearchToFindCrossOverPoint(low, high, arr, x) ## set the crossover point as right
        count = 0  ## initilaize count as zero
        result = [] ## result array
        left = right - 1 ## set the left pointed
        if arr[left] == x: ## of there is a match then decrease left by one and append the value
            left -= 1
            count += 1
            result.append(x)

        if arr[right] == x: ## of there is a match then increase right by one and append the value
            right += 1
            count += 1
            result.append(x)


        while count < k: ## while we have not reached the count

            if left < 0 and right <= high: ## if left is already exhainted, but right is still less than quato hihgh, then keep on adding elements from right
                result.append(arr[right])
                right += 1
                count += 1

            ## if left and right are within 0 and high then compare which elment is closer and add that element in the array
            elif right <= high and left >= 0:

                if abs(x - arr[left]) > abs(x - arr[right]):
                    result.append(arr[right])
                    count += 1
                    right += 1
                else:
                    result.append(arr[left])
                    count += 1
                    left -= 1

            ## similary if right has reached the end then keep on adding eelments from the ledt pointer
            elif right > high and left >= 0:
                result.append(arr[left])
                left -= 1
                count += 1
            ## if this happens then we have alrady exhausted everything
            if left < 0 and right > high:
                print("Exhausted all search")
                break
        return sorted(result)


# arr=[1,2,3,4,5]
# k=4
# x=3
#
# arr =[12, 16, 22, 30, 35, 39, 42,
#               45, 48, 50, 53, 55, 56]
#
# k=4
# x=35
#
#
# arr=[1,1,1,10,10,10]
# #arr=[1,10]
# k=1
# x=9
#
arr=[1,3]
k=1
x=2

# arr = [1, 10, 15, 25, 35, 45, 50, 59]
# k = 1
# x = 30

print("inputs  arr={} k={} x={}".format(arr, k, x))
object = Solution()
print(object.findClosestElements(arr, k, x))
