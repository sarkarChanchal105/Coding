class Solution:
    def numberOfSteps(self, num: int, number_of_steps=0) -> int:

        if num == 0:
            return number_of_steps
        else:
            if num % 2 == 0:
                num = num / 2
                number_of_steps += 1
                print(num,number_of_steps)
                return self.numberOfSteps(num, number_of_steps)
            else:
                if num % 2 != 0:
                    num = (num - 1)
                    number_of_steps += 1
                    print(num, number_of_steps)
                    return self.numberOfSteps(num, number_of_steps)


object= Solution()

print(object.numberOfSteps(14))
print(object.numberOfSteps(8))
