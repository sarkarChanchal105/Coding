"""
https://leetcode.com/problems/grumpy-bookstore-owner/

Today, the bookstore owner has a store open for customers.length minutes.  Every minute, some number of customers (customers[i]) enter the store, and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy.  If the bookstore owner is grumpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.  When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for X minutes straight, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.



Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes.
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.

"""


class Solution:
    def maxSatisfied(self, customers, grumpy, X):

        print("Before :",customers)
        ##  Get the number of customers when not grumpy
        temp=0
        for i in range(len(customers)):
            if grumpy[i]==0:
                temp+=customers[i]
                customers[i]=0  ## if the customer served then update the number of customers.

        customer_served_without_trick=temp

        print("after :",customers)

         ## Now lets use the trick. Using sliding window technique find the max number of customers
        sliding_sum=0
        window=(0,0)
        for i in range(len(customers)-X+1):
            temp_sliding_sum=sum(customers[i:i+X])
            if sliding_sum < temp_sliding_sum:
                #print(sliding_sum, temp_sliding_sum)
                sliding_sum=temp_sliding_sum
                window=(i,i+X-1)
        customer_served_with_trick=sliding_sum
        print(customer_served_with_trick)
        print(window)

        return customer_served_with_trick + customer_served_without_trick


object=Solution()
customers=[4,10,10]
grumpy=[1,1,0]
X=2

customers=[1,0,1,2,1,1,7,5]
grumpy=[0,1,0,1,0,1,0,1]
X=3


print(object.maxSatisfied(customers,grumpy,X))
