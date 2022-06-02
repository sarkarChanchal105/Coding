"""
https://leetcode.com/problems/find-if-path-exists-in-graph/

There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.



Example 1:


Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2
Example 2:


Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.


Constraints:

1 <= n <= 2 * 105
0 <= edges.length <= 2 * 105
edges[i].length == 2
0 <= ui, vi <= n - 1
ui != vi
0 <= source, destination <= n - 1
There are no duplicate edges.
There are no self edges.
"""

from typing import  List

# from collections import defaultdict
# class Solution:
#
#     def validPath(self, n: int, edges: List[List[int]], source: int, destination: int, visited=set()) -> bool:
#
#         if source == destination:
#             return True
#
#         if source in visited:
#             return False
#
#         visited.add(source)
#
#         for edge in edges[source]:
#
#             if self.validPath(n, edges, edge, destination, visited):
#                 return True
#
#         return False


from collections import defaultdict


class Solution:

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        visited = set()
        neighbors = defaultdict(list)

        for n1, n2 in edges:
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)

        return self.validPathHelper(source, destination, visited, neighbors)

    def validPathHelper(self, source, destination, visited, neighbors):

        if source == destination:
            return True

        if source in visited:
            return False

        visited.add(source)

        for neigh in neighbors[source]:

            if self.validPathHelper(neigh, destination, visited, neighbors):
                return True

        return False


#
# n=3
# grapph=[[0,1],[1,2],[2,0]]
# source=0
# destination=2
#
# n=5
# grapph=[[0,4]]
# source=0
# destination=4


n=6
grapph=[[0,1],[0,2],[3,5],[5,4],[4,3]]
source=0
destination=5

n=10
grapph=[[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]]
source=7
destination=5


object=Solution()

print(object.validPath(n,grapph,source,destination))