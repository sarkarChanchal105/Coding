"""

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

"""


### Brute Force Method


# class Solution:
#     def maxProfit(self, prices) -> int:
#         max_so_far = 0
#         for i in range(len(prices)):
#             price = prices[i]
#             for j in range(len(prices[i:])):
#                 if prices[i:][j] - price > max_so_far:
#                     max_so_far = prices[i:][j] - price
#
#         return max_so_far
#
#
# object=Solution()
# list=[7,1,5,3,6,4]
# print(object.maxProfit(list))

class Solution:
    def maxProfit(self, prices) -> int:
        minPrice=9999999  ## Intilize min price with a big number
        maxPrice=0 ##
        position_min_price=0
        position_max_price=0
        max_so_far=0
        for i,price in enumerate(prices,0):
            ## The minimum price so far and the note the day of the minimum proces
            if price<=minPrice :
                minPrice=price
                position_min_price=i
            else:
                ## calculate the max prices so far and the position and note the day when the max price occurred
                if price >= maxPrice:
                    maxPrice=price
                    position_max_price =i
            ## in order to make profit day of max price should be after the day of the  min price.
            if position_min_price<position_max_price:
                profit=maxPrice-minPrice ## Calculate the profilt
                if profit > max_so_far:
                    max_so_far=profit
                    maxPrice=0 ## Once profit is calculated, discard previouly calculated max price

        return max_so_far


object=Solution()
list=[7,1,5,3,6,4]
list=[2,1,2,1,0,1,2]
list=[3,3,5,0,0,3,1,4]

print(object.maxProfit(list))




