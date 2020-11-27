"""

https://leetcode.com/explore/interview/card/google/59/array-and-strings/339/

"""


class Solution:
    def plusOne(self, digits):
        dict = {} #3 dictionary to keep freqwuency of occurrences
        n = len(digits) ## Length of the digits

        ## Store the frequency of digits
        for a in digits:
            if a in dict.keys():
                dict[a] += 1
            else:
                dict[a] = 1

        ## Speacial case.If all digits are 9
        if 9 in dict.keys() and dict[9] == n:  ##if all are 9s
            result = [0] * (n + 1) ## create an array with n+1 zeroes
            result[0] = 1 ## The first element is 1
            return result

        if digits[-1] < 9:  ## of the last digit is less than 9
            digits[-1] = digits[-1] + 1 ## add one to the last digits
            return digits
        else:
            carry = 1 ## by default carry is 1
            for i in range(n - 1, -1, -1): ## Start from the last element
                sum = digits[i] + carry ## calculate the sum
                #print(sum, digits[i], carry)
                if sum >= 10: ## if sum is greater than zero
                    digits[i] = 0 ## the digit should be zeom with caryy 1
                    carry = 1
                else:
                    digits[i] = sum ## assign the sum, but carry 0. break from the loop
                    break
            return digits



digits=[8,9,9,9]
object=Solution()

result=object.plusOne(digits)

print(result)