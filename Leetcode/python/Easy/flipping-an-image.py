"""
https://leetcode.com/problems/flipping-an-image/

832. Flipping an Image
Easy

2200

206

Add to List

Share
Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.

For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

For example, inverting [0,1,1] results in [1,0,0].


Example 1:

Input: image = [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
Example 2:

Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]


Constraints:

n == image.length
n == image[i].length
1 <= n <= 20
images[i][j] is either 0 or 1.


"""


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        for i in range(len(image)):
            self.reverseArrayInplace(image[i], len(image[i]))
        return image

    def reverseArrayInplace(self, array, n) -> None:
        left = 0;
        right = n - 1

        while left < right:
            array[left], array[right] = array[right], array[left]
            for idx in [left, right]:
                # if array[idx]==0:
                #     array[idx]=1
                # else:
                #     array[idx]=0
                array[idx] ^= 1
            left += 1
            right -= 1

        if left == right:
            # if array[left]==0:
            #     array[left]=1
            # else:
            #     array[left]=0
            array[left] ^= 1