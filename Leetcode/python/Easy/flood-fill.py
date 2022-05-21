"""
https://leetcode.com/problems/flood-fill/


An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.

Complexity Analysis

Time Complexity: O(N)O(N), where NN is the number of pixels in the image. We might process every pixel.

Space Complexity: O(N)O(N), the size of the implicit call stack when calling dfs.

"""



#3 The idea here is to use DFS to find the all reachable points, which has exact same colour as of starting node.

class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor):
        startingPoint = (sr, sc) ## for the tuple
        color = image[sr][sc] ## get the color of the starting node
        image[sr][sc] = newColor ## update the color of the starting node

        #3 Edge case
        if color==newColor:
            return image

        ## Call the DFS with the starting node
        self.depthFirstSearch(startingPoint, image, color, newColor)
        return image


    def depthFirstSearch(self, startingPoint, image, color, newColor):

        points = [(1, 0), (0, 1), (-1, 0), (0, -1)] ## right, top, left,down

        ## from the starting point calculate matrix cell in all four directions
        for point in points:
            x = point[0]
            y = point[1]
            newPoint = (startingPoint[0] + x, startingPoint[1] + y)
            X = newPoint[0]
            Y = newPoint[1]
            ## for each new point call DFS
            if self.is_safe(newPoint, image): ## if the new cell is winthin the boundaries of the matrix
                if image[X][Y] == color: ## update the color the new cell if the color of te new cell matches with the color of the starting point
                    image[X][Y] = newColor
                    self.depthFirstSearch(newPoint, image, color, newColor) ## call DFS recusively with the new point

    def is_safe(self, newPoint, image):
        r = len(image)
        c = len(image[0])
        ## if the new cell is within the boundaries
        if 0 <= newPoint[0] < r and c > newPoint[1] >= 0:
            return True
        return False


object = Solution()

# image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
# sr = 1
# sc = 1
# newColor = 2

image=[
    [0,0,0],
    [0,1,1]
]
sr=1
sc=1
newColor=1


print(object.floodFill(image, sr, sc, newColor))
