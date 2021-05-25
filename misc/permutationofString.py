


def permutation(string):

    arr=list(string)
    #print(arr)
    n=len(arr)
    helperPermulation(arr,0,n-1)




def helperPermulation(arr, left, right):

    if left==right:
        print(arr)

    for i in range(left,right+1):
        arr[left],arr[i]=arr[i],arr[left]
        helperPermulation(arr, left+1, right)
        arr[left],arr[i]=arr[i],arr[left]











string='abcd'

permutation(string)




