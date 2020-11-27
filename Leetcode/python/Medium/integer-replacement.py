"""
https://leetcode.com/problems/integer-replacement/

Given a positive integer n, you can apply one of the following operations:

If n is even, replace n with n / 2.
If n is odd, replace n with either n + 1 or n - 1.
Return the minimum number of operations needed for n to become 1.



Example 1:

Input: n = 8
Output: 3
Explanation: 8 -> 4 -> 2 -> 1
Example 2:

Input: n = 7
Output: 4
Explanation: 7 -> 8 -> 4 -> 2 -> 1
or 7 -> 6 -> 3 -> 2 -> 1
Example 3:

Input: n = 4
Output: 2


Constraints:

1 <= n <= 231 - 1



"""


# class Solution:
#     def integerReplacement(self, n: int) -> int:

#         if n==1:
#             return 0 ## if n ios already 1 then there is no need to of operation. Hence returen zero

#         if n%2 ==0: ## if n is even, recisively call for n/2
#             return 1+self.integerReplacement(int(n/2))
#         else:
#             ## if n is odd,
#             option1=self.integerReplacement(n+1) # Option 1: add 1
#             option2=self.integerReplacement(n-1) # option 2: add 2

#             return 1+min(option1, option2) ## return the minimum between option 1 and Option 2


class Solution:

    def integerReplacement(self, n) -> int:

        hash_table = {}  ## define DP array

        return self.helperintegerReplacement(n, hash_table)

        # print(hash_table)

    def helperintegerReplacement(self, n, hash_table):

        if n == 1:
            hash_table[n] = 0
            return hash_table[n]  ## if n is already 1 then there is no need to of operation. Hence returen zero

        if n in hash_table:  ## check if the value already exists. If yes, there is no need to recumpute the value
            return hash_table[n]

        if n % 2 == 0:  ## if n is even, recisively call for n/2
            hash_table[n] = 1 + self.helperintegerReplacement(int(n / 2), hash_table)
            return hash_table[n]
        else:
            ## if n is odd,
            option1 = self.helperintegerReplacement(n + 1, hash_table)  # Option 1: add 1
            option2 = self.helperintegerReplacement(n - 1, hash_table)  # option 2: add 2
            hash_table[n] = 1 + min(option1, option2)

            return hash_table[n]  ## return the minimum between option 1 and Option 2
