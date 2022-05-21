"""
https://leetcode.com/problems/zigzag-conversion/

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"


Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000

"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:

        # Step 1: Create a list of lists. There will be numRows number of elements.
        list_of_lists = []
        for i in range(numRows):
            list_of_lists.append([])  ## Append empty list

        ## Step 2: Traverse the sring in ZigZag

        index = 0  ## pointer to the input string s

        while index < len(s):  ## if we have not processed all characters in the string s

            ## Go Down

            for i in range(numRows):
                if index == len(
                    s): break  ## Takes care of the edge case situaltion to prevent the index to go past the string
                list_of_lists[i].append(s[index])
                index += 1

            ## Come back up

            for i in range(numRows - 2, 0, -1):
                if index == len(
                    s): break  ## Takes care of the edge case situaltion to prevent the index to go past the string
                list_of_lists[i].append(s[index])
                index += 1

        # print(list_of_lists)

        result = ''

        for current_list in list_of_lists:
            result += ''.join(current_list)

        return result

