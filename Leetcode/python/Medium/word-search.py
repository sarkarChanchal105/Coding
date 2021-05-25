"""
https://leetcode.com/problems/word-search/

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.



Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false


Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.


Follow up: Could you use search pruning to make your solution faster with a larger board?

"""

class Solution:

    def exist(self, board, word):
        self.ROWS=len(board)
        self.COLS=len(board[0])
        self.board=board

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.helperBackTracking(row, col, word):
                    return True
        return False

    def helperBackTracking(self, row, col, suffix):

        if len(suffix)==0: ## base case when all characrter have been matched or the inout character is a blank
            return True

        ## Checking boundary conditions/ ALso the current chaacter should match the first character of the suffix otherwise retun Fasle
        if row < 0 or row>=self.ROWS or col <0 or col>=self.COLS or self.board[row][col]!=suffix[0]:
            return False

        result=False
        self.board[row][col]='#' ## update if the character has been visited
        rowColumnOffsets=[(-1,0),(1,0),(0,1),(0,-1)] ## form the down off grids. left, right, up, down

        for rowOffset, colOffset in rowColumnOffsets:
            result=self.helperBackTracking(row+rowOffset,col+colOffset, suffix[1:])

            if result: break
        self.board[row][col]=suffix[0]

        return result









board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

object=Solution()

print(object.exist(board,word))










object=Solution()

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

object.exist(board, word)