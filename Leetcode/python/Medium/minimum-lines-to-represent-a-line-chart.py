"""
https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/

2280. Minimum Lines to Represent a Line Chart
Medium

185

368

Add to List

Share
You are given a 2D integer array stockPrices where stockPrices[i] = [dayi, pricei] indicates the price of the stock on day dayi is pricei. A line chart is created from the array by plotting the points on an XY plane with the X-axis representing the day and the Y-axis representing the price and connecting adjacent points. One such example is shown below:


Return the minimum number of lines needed to represent the line chart.



Example 1:


Input: stockPrices = [[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]
Output: 3
Explanation:
The diagram above represents the input, with the X-axis representing the day and Y-axis representing the price.
The following 3 lines can be drawn to represent the line chart:
- Line 1 (in red) from (1,7) to (4,4) passing through (1,7), (2,6), (3,5), and (4,4).
- Line 2 (in blue) from (4,4) to (5,4).
- Line 3 (in green) from (5,4) to (8,1) passing through (5,4), (6,3), (7,2), and (8,1).
It can be shown that it is not possible to represent the line chart using less than 3 lines.
Example 2:


Input: stockPrices = [[3,4],[1,2],[7,8],[2,3]]
Output: 1
Explanation:
As shown in the diagram above, the line chart can be represented with a single line.


Constraints:

1 <= stockPrices.length <= 105
stockPrices[i].length == 2
1 <= dayi, pricei <= 109
All dayi are distinct.
"""

from typing import List

import decimal
class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:

        ## Step 1: calculete the lenght of the array
        n = len(stockPrices)
        if n <= 1:
            return 0

        ## Step 2 : sort the array based on X since we have atleast two points
        stockPrices = sorted(stockPrices, key=lambda x: x[0])

        ## Calculate the slope of the first two points
        x0, y0 = stockPrices[0][0], stockPrices[0][1]
        x1, y1 = stockPrices[1][0], stockPrices[1][1]

        prevSlope = (decimal.Decimal(y1 - y0) / decimal.Decimal(x1 - x0))  ## Slope of first two points

        i = 1
        countoflines = 1  ## So far we have one line
        while i < n - 1:

            ## for each i, calculate the slope between xi, yi and xi+1 , yi+1
            x0, y0 = stockPrices[i][0], stockPrices[i][1]
            x1, y1 = stockPrices[i + 1][0], stockPrices[i + 1][1]

            currentSlope = (decimal.Decimal(y1 - y0) / decimal.Decimal(x1 - x0))  ## slope of the current two points

            if currentSlope != prevSlope:  ## of the slopes are not matching then we need new line
                countoflines += 1
            prevSlope = currentSlope  ## current slope becomes the previous slope for the next iteration
            i += 1  ## increment i for considering the next points

        return countoflines


object=Solution()

array=[[1,1],[500000000,499999999],[1000000000,999999998]]


print(object.minimumLines(array))