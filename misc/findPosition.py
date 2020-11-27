"""

Table: Input File/Table:

Id | Name
L20000|North America

Dimension Table:

Keyfull
|L10000|L15000|L17500|L20000|L30001|L40012|L50011|L60004|0000.1050


Expected Output  -  starting position  of L20000

sample Oracle code  :
INSTR(ch.KEY_FULL, '|L20000')>1
"""

# inputStr = '|L10000|L15000|L17500|L20000|L30001|L40012|L50011|L60004|0000.1050'
# id = 'L20000'
# delim='|'

import sys

def findPosition(inputStr, id, delim):


    array = (inputStr.split(delim))  ## Split the arry based on the delimiter
    # print(array)

    ## Find the the position of the value id in the array
    for i in range(len(array)):
        if array[i] == id:
            break
    ##print(i)
    # print(array[:i])

    ## Construct the string before id with the delimeter
    outputStr = delim.join(array[:i])

    # print(outputStr)

    return (len(outputStr) + 1)


def main():
    inputStr=sys.argv[1]
    id = sys.argv[2]
    delim = sys.argv[3]
    position=findPosition(inputStr,id,delim)
    print(position)

if __name__ == '__main__':
    main()


