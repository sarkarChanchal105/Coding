#
# def longestcommonsubstring(inputString, outputString) ->int:
#
#     m=len(inputString)
#     n=len(outputString)
#     return longestcommonsubstringhelper(inputString,outputString,m,n,0)
#
# def longestcommonsubstringhelper(inputString,outputString,m,n,max_sub_string):
#
#     if m==0 or n==0:
#         return max_sub_string
#
#     if inputString[m-1]==outputString[n-1]:
#         max_sub_string=longestcommonsubstringhelper(inputString, outputString,m-1, n-1,max_sub_string+1)
#
#
#     option1=longestcommonsubstringhelper(inputString,outputString,m-1,n,0)
#     option2=longestcommonsubstringhelper(inputString, outputString,m,n-1,0)
#
#     max_sub_string=max(max_sub_string, max(option1,option2))
#
#     return max_sub_string
#
# inputString = "abcdxyz"
# outputString = "xyzabcd"
#
# print(longestcommonsubstring(inputString,outputString))


## Dynamic Programming



def longestcommonsubstring(inputString, outputString) ->int:

    m=len(inputString)
    n=len(outputString)
    dp=[ [-1]*(n+1) for _ in range(m+1)]
    #print(dp)
    return longestcommonsubstringhelper(inputString,outputString,m,n,0,dp)

def longestcommonsubstringhelper(inputString,outputString,m,n,max_sub_string,dp):

    if dp[m][n]!=-1:
        return dp[m][n]

    if m==0 or n==0:
        dp[m][n]=max_sub_string
        return dp[m][n]

    if inputString[m-1]==outputString[n-1]:
        #max_sub_string=longestcommonsubstringhelper(inputString, outputString,m-1, n-1,max_sub_string+1)

        max_sub_string = longestcommonsubstringhelper(inputString, outputString, m - 1, n - 1, max_sub_string + 1,dp)
        dp[m][n]=max_sub_string


    option1=longestcommonsubstringhelper(inputString,outputString,m-1,n,0,dp)
    option2=longestcommonsubstringhelper(inputString, outputString,m,n-1,0,dp)

    max_sub_string=max(max_sub_string, max(option1,option2))

    dp[m][n]=max_sub_string

    return dp[m][n]

inputString = "abc"
outputString = "abx"

print(longestcommonsubstring(inputString,outputString))