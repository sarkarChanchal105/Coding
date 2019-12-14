"""
Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's id.

Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  The average score is calculated using integer division.



Example 1:

Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation:
The average of the student with id = 1 is 87.
The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.


Note:

1 <= items.length <= 1000
items[i].length == 2
The IDs of the students is between 1 to 1000
The score of the students is between 1 to 100
For each student, there are at least 5 scores

"""


class Solution:
    def highFive(self, items):
        dict = {}

        for r in items:
            if r[0] not in dict.keys():
                dict[r[0]] = [r[1]]
            else:
                dict[r[0]].append(r[1])

        print(dict)

        for k, v in dict.items():
            dict[k] = sorted(v, reverse=True)

        print(dict)
        result = []
        for k, v in dict.items():
            dict[k] = int(sum(v[0:5]) / 5)
            result.append([k, dict[k]])

        print(result)
        print(dict)

        return result

object=Solution()

list=[[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]

print(object.highFive(list))