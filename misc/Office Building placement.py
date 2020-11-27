"""
https://leetcode.com/discuss/interview-question/221639/Off%3C!--googleoff:%20snippet--%3E%3Cdiv%20class=

Given a grid with w as width, h as height. A company wants to develop an office park in the grid where each cell represents a potential building lot. The goal is for the furthest of all lots to be as near as possible to an office building. Given an input n, which is the number of buildings to be placed in the lot, determine the building placement to minimize the distance the most distant empty lot is from the building. Distance is measured in horizontal and vertical directions, i.e. diagonal distance measurement is not considered.

inputs
w: an integer, the width of the grid
h: an integer, the height of the grid
n: an integer, the number of buildings to be placed

For example, w=4, h=4 and n=3. An optimal grid placement sets any lot within two unit distance of the building. The answer for this case is 2.

"0" indicates optimal building placement and in this case the maximal value of all shortest distances to the closest building for each cell is "2".

1 0 1 2
2 1 2 1
1 0 1 0
2 1 2 1
The above represents one optimal solution, there could be more like the above array rotated as an example. The above is an optimal solution because out of the 3 buildings (n=3), one building was placed at index (0,1), second was placed at (2,1) and third was placed at (2,3). The surrounding horizontal and vertical distance is shown as 1 and 2 by adding 1 each time we move horizontally and/or vertically. Note again that diagonal movement is not allowed:

1 ← 0 → 1 → 2
↓
2 ← 1 → 2 ← 1
↑. . ↑
1 ← 0 → 1 ← 0
↓ . . ↓
2 ← 1 → 2 ← 1
Other examples:

Example 1)

w=3, h=3, n=2
Two buildings (zeros) have to be optimally placed. One of the optimal plan for this case is:

01
11
10

0 → 1
↓
1 . . .1
. . . . ↑
1 ← 0


"""


import itertools
from collections import deque
def buildOffice(height, width, n):
    arr = []
    for i in range(height):
        for j in range(width):
            arr.append((i,j,0))
    print(len(arr))

    # for eleme in arr:
    #     print(eleme)

    print(itertools.combinations(arr, n).__sizeof__())

    ans = float("inf")
    for points in itertools.combinations(arr,n):
        print(points)
        q = deque([]); visited = set()
        for m, n, dist in points:
            q.append((m,n,dist))
            visited.add((m,n))
        distAns = 0
        distArr = []
        while q:
            i, j, dist = q.popleft()
            distAns = max(dist, distAns)
            for x, y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if 0<=x<height and 0<=y<width and (x,y) not in visited:
                    q.append((x,y,dist+1))
                    visited.add((x,y))
        ans = min(distAns, ans)

    return ans


print(buildOffice(4,4,3))

