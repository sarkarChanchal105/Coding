"""

Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.

"""


class LargerNumKey(str):
    def __lt__(x, y):
        print (x,y)
        return x + y > y + x


class Solution:
    def largestNumber(self, nums):
        k=map(str, nums)
        print("K=",set(k))
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        print(largest_num)
        #return '0' if largest_num[0] == '0' else largest_num

nums=[10,2,23]

object=Solution()
object.largestNumber(nums)




