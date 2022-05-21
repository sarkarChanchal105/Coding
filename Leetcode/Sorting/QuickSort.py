



def quickSort(arr):

    if len(arr)<=1:
        return arr

    pivot=arr[0]

    left=[x for x in arr if x<pivot]
    middle=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]

    return quickSort(left)+middle+quickSort(right)


arr=[-9,11,90,100,101,900,-90,9000]

arr=[890,11]

print(quickSort(arr))