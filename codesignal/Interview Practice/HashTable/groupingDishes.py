"""
https://app.codesignal.com/interview-practice/task/xrFgR63cw7Nch4vXo/description

You are given a list dishes, where each element consists of a list of strings beginning with the name of the dish, followed by all the ingredients used in preparing it. You want to group the dishes by ingredients, so that for each ingredient you'll be able to find all the dishes that contain it (if there are at least 2 such dishes).

Return an array where each element is a list beginning with the ingredient name, followed by the names of all the dishes that contain this ingredient. The dishes inside each list should be sorted lexicographically, and the result array should be sorted lexicographically by the names of the ingredients.

Example

For
  dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
            ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
            ["Quesadilla", "Chicken", "Cheese", "Sauce"],
            ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]
the output should be
  groupingDishes(dishes) = [["Cheese", "Quesadilla", "Sandwich"],
                            ["Salad", "Salad", "Sandwich"],
                            ["Sauce", "Pizza", "Quesadilla", "Salad"],
                            ["Tomato", "Pizza", "Salad", "Sandwich"]]
For
  dishes = [["Pasta", "Tomato Sauce", "Onions", "Garlic"],
            ["Chicken Curry", "Chicken", "Curry Sauce"],
            ["Fried Rice", "Rice", "Onions", "Nuts"],
            ["Salad", "Spinach", "Nuts"],
            ["Sandwich", "Cheese", "Bread"],
            ["Quesadilla", "Chicken", "Cheese"]]
the output should be
  groupingDishes(dishes) = [["Cheese", "Quesadilla", "Sandwich"],
                            ["Chicken", "Chicken Curry", "Quesadilla"],
                            ["Nuts", "Fried Rice", "Salad"],
                            ["Onions", "Fried Rice", "Pasta"]]




"""

from collections import defaultdict


def groupingDishes(dishes):
    hashTable = defaultdict(list)

    for element in dishes:
        dish = element[0]
        ingredients = element[1:]
        for ingredient in ingredients:
            hashTable[ingredient].append(dish)

    # print(hashTable)

    for k, v in hashTable.items():
        #print("key = {} Value = {}".format(k, v))
        hashTable[k]=sorted(hashTable[k])

    for k, v in hashTable.items():
        print("key = {} Value = {}".format(k, v))
        #hashTable[k]=sorted(hashTable[k])

    result=[]

    for key in sorted(hashTable.keys()):
        if len(hashTable[key])>=2:
            temp=[]
            temp.append(key)
            for value in hashTable[key]:
                temp.append(value)
            result.append(temp)

    return (result)





dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
            ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
            ["Quesadilla", "Chicken", "Cheese", "Sauce"],
            ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]


groupingDishes(dishes)
