"""
https://leetcode.com/problems/valid-tic-tac-toe-state/submissions/

794. Valid Tic-Tac-Toe State
Medium

429

985

Add to List

Share
Given a Tic-Tac-Toe board as a string array board, return true if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array that consists of characters ' ', 'X', and 'O'. The ' ' character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares ' '.
The first player always places 'X' characters, while the second player always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.


Example 1:


Input: board = ["O  ","   ","   "]
Output: false
Explanation: The first player always plays "X".
Example 2:


Input: board = ["XOX"," X ","   "]
Output: false
Explanation: Players take turns making moves.
Example 3:


Input: board = ["XOX","O O","XOX"]
Output: true


Constraints:

board.length == 3
board[i].length == 3
board[i][j] is either 'X', 'O', or ' '.

"""
from typing import List,Tuple


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:

        ## convert the board into 2D 3X3 matrix , get the count of Xs and Os in the matrix
        matrix, counts_tuple = self.convertboardtomatrix(board)
        cnt_x, cnt_o, cnt_none = counts_tuple

        ## if number x is less than number O then its invalid
        if cnt_x < cnt_o:
            return False

        ## if number of X - number of Os is more than 1 then invalid
        if cnt_x - cnt_o > 1:
            return False

        ## if number of X and Number of Os are equal then if X is a winner then we cant have equal number of zeroes, since the game will end once X is the winner
        if cnt_x == cnt_o:
            ## Check if X is the winner
            winner=self.check_who_iswinner(matrix)
            if winner == {'X'} or winner== {'X', 'O'} or  winner== {'O', 'X'}:
                return False

        ## if number of X - Number of Os =1 then if O is the winner then the game will end before Player X puts another X in the matrix
        if cnt_x - cnt_o == 1:
            winner = self.check_who_iswinner(matrix)
            if winner == {'O'} or winner=={'O','X'}:
                return False

        ## if None of the above conditions satifies then return True
        return True

    """
    This function checks if X or O is the winner by traversing all rows, columns and diagonals
    """

    def check_who_iswinner(self, matrix) -> set:

        winners = set()  ## Let's find out if there are multiple winners

        ## Check if any of the rows have all Xs or Os
        for i in range(len(matrix)):
            set_row = set(matrix[i])
            if len(set_row) == 1:
                if 'X' in set_row or 'O' in set_row:
                    winners.add(list(set_row)[0])
                    # return list(set_row)[0]

        ## Check if any of the columns have all Xs or Os
        for i in range(len(matrix[0])):
            set_columns = set()
            for j in range(len(matrix)):
                set_columns.add(matrix[j][i])
            if len(set_columns) == 1:
                if 'X' in set_columns or 'O' in set_columns:
                    winners.add(list(set_columns)[0])
                    # return list(set_columns)[0]

        ## Check is diagonal-1 (left to right),
        ## have all Xs or Os
        set_diag_1 = set()
        for i in range(len(matrix)):
            set_diag_1.add(matrix[i][i])
        if len(set_diag_1) == 1:
            if 'X' in set_diag_1 or 'O' in set_diag_1:
                winners.add(list(set_diag_1)[0])
                # return list(set_diag_1)[0]

        ## Check is diagonal-2 (right to right),
        ## have all Xs or Os
        set_diag_2 = set()
        row = 0;
        col = len(matrix[0]) - 1
        while col >= 0:
            set_diag_2.add(matrix[row][col])
            col -= 1
            row += 1
        if len(set_diag_2) == 1:
            if 'X' in set_diag_2 or 'O' in set_diag_2:
                winners.add(list(set_diag_2)[0])
                # return list(set_diag_2)[0]
        #print("Winners are: {}".format(winners))
        # return 'Z' ## returns default if any of the above consitions does not satify
        if winners:
            return winners
        return {'z'}

    def convertboardtomatrix(self, board: str):
        matrix = [[None for _ in range(3)] for _ in range(3)]
        cnt_x = cnt_o = cnt_none = 0
        row = 0
        for strng in board:
            col = 0
            for chrr in strng:
                ## Keep count of the Xs, Os since these will help us to determine of the states are valid or not
                if chrr == 'X':
                    cnt_x += 1
                elif chrr == 'O':
                    cnt_o += 1
                else:
                    cnt_none += 1
                matrix[row][col] = chrr  ## fill in the matrix with appropriate characters
                col += 1
            row += 1
        return matrix, (cnt_x, cnt_o, cnt_none)


object=Solution()

#board=["XOX","O O","XOX"]
#board=["XXO","XOX","OXO"]
board=["OOO","   ","XXX"]
#board=["XXX","   ","OOO"]
#board=["XOX","O O","XOX"]
board=["OOO","XXO","XXX"]
print(object.validTicTacToe(board))