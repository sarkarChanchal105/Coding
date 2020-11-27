"""
https://leetcode.com/problems/friend-circles/


There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:

Input:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
The 2nd student himself is in a friend circle. So return 2.


Example 2:

Input:
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.



Constraints:

1 <= N <= 200
M[i][i] == 1
M[i][j] == M[j][i]

"""

class Solution:
    def findCircleNum(self, M) :

        number_of_nodes=len(M)  ## Get the numbe of nodes
        visted=[0]*number_of_nodes ## Create an array of size number of nodes
        circle=0 ## Initalize the number of circles as zero
        ## For each node execute the deprth first search
        for i in range(number_of_nodes):
            if visted[i]==0: ## if the node already not visited
                visted[i]=1 ## Set vited
                self.depth_first_search(i,visted,number_of_nodes,M) ## call DFS
                circle+=1

        return circle


    def depth_first_search(self,starting_vertex, visted,number_of_nodes, M):
        for x in range(number_of_nodes):
            if x!=starting_vertex and visted[x]==0 and M[x][starting_vertex]==1:
                visted[x]=1
                self.depth_first_search(x, visted,number_of_nodes,M)


M=[
    [1,1,0],
    [1,1,0],
    [0,0,1]
]



object=Solution()

result=object.findCircleNum(M)

print(result)





