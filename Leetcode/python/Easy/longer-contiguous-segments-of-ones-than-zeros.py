"""
https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/

Given a binary string s, return true if the longest contiguous segment of 1s is strictly longer than the longest contiguous segment of 0s in s. Return false otherwise.

For example, in s = "110100010" the longest contiguous segment of 1s has length 2, and the longest contiguous segment of 0s has length 3.
Note that if there are no 0s, then the longest contiguous segment of 0s is considered to have length 0. The same applies if there are no 1s.




"""


# class Solution:
    # def checkZeroOnes(self, s: str) -> bool:
    #     n = len(s)
    #
    #     if n==0: ## Edge case 1: When lenght is zer0
    #         return False
    #     if n==1: ## if there is only one character
    #         if s=='1':
    #             return True
    #         return False
    #     if n==2: ## if the number of characters is two
    #         if s=='11':
    #             return True
    #         return False
    #     if n==3: ## if the number of characters is three
    #         if s=='111' or s=='110':
    #             return True
    #         return False
    #     c_zeroes = [0]
    #     c_ones = [0]
    #     curren_count_one = 0
    #     curren_count_zero = 0
    #
    #     ## for each elements in the array
    #     for i in range(1, n):
    #         if s[i - 1] == s[i]: ## compare with previous element
    #             if s[i - 1] == '1': ## if adjacenets are 1
    #                 curren_count_one += 1 ## add one to the element
    #             else:
    #                 curren_count_zero += 1 ## add one
    #
    #         else:
    #             if curren_count_one > 0:
    #                 curren_count_one += 1
    #                 c_ones.append(curren_count_one)
    #
    #             if curren_count_zero > 0:
    #                 curren_count_zero += 1
    #                 c_zeroes.append(curren_count_zero)
    #
    #             curren_count_one = 0
    #             curren_count_zero = 0
    #
    #     if s[-1] == '0':
    #         curren_count_zero += 1
    #         c_zeroes.append(curren_count_zero)
    #     else:
    #         curren_count_one += 1
    #         c_ones.append(curren_count_one)
    #
    #     return max(c_ones) - max(c_zeroes) > 0

class Solution:
        def checkZeroOnes(self, s: str) -> bool:
            best_one, best_zero, current_one, current_zero = 0, 0, 0, 0

            for i in s:
                if i == "1":
                    current_zero = 0
                    current_one += 1
                else:
                    current_zero += 1
                    current_one = 0

                best_one = max(best_one, current_one)
                best_zero = max(best_zero, current_zero)

            return best_one > best_zero

object = Solution()
s = '1101'
s = '111000'
s='01'
s='101'
print(object.checkZeroOnes(s))
