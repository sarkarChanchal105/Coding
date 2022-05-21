"""
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.



Example 1:

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.


Constraints:

1 <= arr1.length, arr2.length, arr3.length <= 1000
1 <= arr1[i], arr2[i], arr3[i] <= 2000


"""

class Solution:
    def arraysIntersection(self, arr1, arr2, arr3):
        dict = {}
        for a in arr1+arr2+arr3:

            if a in dict:
                dict[a]+=1
            else:
                dict[a]= 1

        result = []
        for k, v in dict.items():
            if v > 2:
                result.append(k)
        return result




arr1=[1,2,3,4,5]
arr2=[1,2,5,7,9]
arr3=[1,3,4,5,8]


object=Solution()
print(object.arraysIntersection(arr1,arr2,arr3))


##  Three pointer Approach O(N)/O(1)

class Solution:
    def arraysIntersection(self, arr1, arr2, arr3):

        p1 = p2 = p3 = 0

        n1 = len(arr1)
        n2 = len(arr2)
        n3 = len(arr3)

        result = []

        while p1 < n1 and p2 < n2 and p3 < n3:

            if arr1[p1] == arr2[p2] == arr3[p3]:

                result.append(arr1[p1])

                p1 += 1
                p2 += 1
                p3 += 1

            else:
                if arr1[p1] < arr2[p2]:
                    p1 += 1
                elif arr2[p2] < arr3[p3]:
                    p2 += 1
                else:
                    p3 += 1

        return result
