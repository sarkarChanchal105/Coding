"""
https://app.codesignal.com/tournaments/X5u5pCHmoGtYqAc3E/D

Given a sorted integer array that does not contain any duplicates, return a summary of the number ranges it contains.

Example

For nums = [-1, 0, 1, 2, 6, 7, 9], the output should be
composeRanges(nums) = ["-1->2", "6->7", "9"].

"""


def composeRanges(nums):


    ## Handle edge cases
    if len(nums) == 0: ## if there is no elemenebnt
        return []
    if len(nums) == 1: ## if there i only one
        return [str(nums[0])]

    if len(nums) == 2: ## if there are two elements
        diff = abs(nums[0] - nums[1])
        if diff == 0 or diff == 1:
            return [str(nums[0]) + '->' + str(nums[1])]
        else:
            return [str(nums[0]), str(nums[1])]

    ## General cases
    beginRange = nums[0] ## intialize begin range
    endRange = nums[-1] ## end of the range

    result = [] ## result array

    ## starting from the 2nd elemenet
    for i in range(1, len(nums)):
        diff = abs(nums[i] - nums[i - 1]) ## calculate the absoltute difference between ith a d i-1 th element

        ## if the absolute difference is o or 1 then continue
        if (diff == 0 or diff == 1) and i < len(nums):
            continue
        ## if the absolute difference is o or 1 then continue and i has reached end of array
        if (diff == 0 or diff == 1) and i == len(nums) - 1:
            if beginRange != endRange:
                result.append(str(beginRange) + '->' + str(endRange))
            else:
                result.append(str(beginRange))
            return result

        ## if the absilute difference is greater than 1 then it marks the bgining of new range
        if diff > 1:
            endRange = nums[i - 1]## update the end of current range
            if beginRange != endRange: ## if ebgin and end sre not same
                result.append(str(beginRange) + '->' + str(endRange))
            else:
                result.append(str(beginRange))
            beginRange = nums[i] ## Start of new range
            endRange = nums[-1] ## End of the new range

    if beginRange == endRange:
        result.append(str(endRange))
        return result

    if len(result)==0:
        result.append(str(beginRange) + '->' + str(endRange))
        return result

    if beginRange != endRange:
        result.append(str(beginRange) + '->' + str(endRange))
        return result


nums=[-1, 0, 1, 2, 6, 7, 9]
#nums=[0, 1, 2]
#nums=[0,2,3,4,6,8,9]
print(composeRanges(nums))