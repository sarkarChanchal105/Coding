"""
https://leetcode.com/problems/asteroid-collision/

"""

from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = [] ## Declare the stack
        i=0
        while i<len(asteroids):

            if len(stack) == 0: ## if stack is empty then append the current asteriod regardless of it's sign
                stack.append(asteroids[i])
                 ## stack top is negative and current asteroids is postive then no collision . Append the value
                 ## Or stackstop and current asteroid are of the same sign (+ve,+ve or -ve,-ve), then no collision. Append the value
            elif (stack[-1] < 0 and asteroids[i] < 0) or (stack[-1] > 0 and asteroids[i] > 0) or (stack[-1] < 0 and asteroids[i] > 0):
                stack.append(asteroids[i])

            else: ## Now we have encountered a -ve value asteriod and the stacktop is +ve, lets process the current asteriod
                while len(stack)>0 :
                    # During the processing of the current asteroid, since we may be popping elements, it may so happen that
                    ## stacktop and current asteroid are of same sign again. In that case just break out of the loop. to reprocess the current asteriod
                    if (stack[-1] >0 and asteroids[i] >0) or (stack[-1] <0 and asteroids[i] <0):
                        i-=1
                        break

                    if abs(stack[-1]) < abs(asteroids[i]): ## stack top is +ve and its value is less than absolute value of the current asteroid
                        stack.pop() ## simply pop the element from the stack
                        if len(stack) == 0: ## if stack is empty then there are no more elements to collide with and simply append the current asteroid. and break
                            stack.append(asteroids[i])
                            break

                    elif stack[-1] == abs(asteroids[i]): ## is aboslute values are same
                        stack.pop() ## pop the last element and break
                        break

                    elif stack[-1] > abs(asteroids[i]): ## Stack top is +ve and greater than the current absolute value
                        break

            i+=1

        return stack


object=Solution()

array=[5,10,-5]
print(object.asteroidCollision(array))

array=[-2,-1,1,2]
print(object.asteroidCollision(array))

array=[-2,-2,1,-2]
print(object.asteroidCollision(array))


