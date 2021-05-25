"""
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.





"""


class Solution:
    #    def longestCommonPrefix(self, strs: List[str]) -> str:

    #         commonPrefix=''

    #         strs=sorted(strs, key=lambda x:len(x))  ## Sort the string in ascending order lenght

    #         shortestWord=strs[0] ## get the shortest string

    #         for i,chr in enumerate(shortestWord):
    #             for string in strs[1:]:
    #                 if chr==string[i]: ## if the current charter is present in the same position
    #                     continue ## then continue adding the charater to the common prefix
    #                 else:
    #                     return commonPrefix  ## if the pattern breaks then return the result
    #             commonPrefix+=chr

    #         return commonPrefix  ## handle the edge case where all strings are same

    ## Better solution

    def longestCommonPrefix(self, strs) -> str:

        ## Handle the edge cases
        if len(strs) == 0:
            return strs

        if len(strs) == 1:
            return strs[0]

        commonPrefix = strs[0]  ## assume first string the LCP
        strs = strs[1:]  ## consider rest of the elements

        for string in strs:
            while (commonPrefix != ''):
                try:
                    j = string.index(commonPrefix)  ## try to find the first occurence of currenrt common prefix
                    if j == 0:  ## if occures first then break from the loop and move on the next string in the array
                        break
                    else:
                        commonPrefix = commonPrefix[:-1]  ##else, remove the last element of the common Prefic
                except Exception as e:
                    commonPrefix = commonPrefix[
                                   :-1]  ## if there is exception, then remove the last character and try to find the new common ptrfix in the string again. Continue this until commonPrefix becomes null

        return commonPrefix


object=Solution()

array=["flower","flow","flight"]
array=["c","acc","ccc"]
object.longestCommonPrefix(array)