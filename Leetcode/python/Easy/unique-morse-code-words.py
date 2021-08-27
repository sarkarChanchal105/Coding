""""
https://leetcode.com/problems/unique-morse-code-words/

804. Unique Morse Code Words
Easy

1016

908

Add to List

Share
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

'a' maps to ".-",
'b' maps to "-...",
'c' maps to "-.-.", and so on.
For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.

For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
Return the number of different transformations among all words we have.



Example 1:

Input: words = ["gin","zen","gig","msg"]
Output: 2
Explanation: The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
There are 2 different transformations: "--...-." and "--...--.".
Example 2:

Input: words = ["a"]
Output: 1

"""


# class Solution:
#     def uniqueMorseRepresentations(self, words: List[str]) -> int:

#         morseArray=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

#         #print(morseArray)

#         #print(ord('a'))
#         start=ord('a')
#         hashTable={}

#         for mrse in morseArray:
#             hashTable[chr(start)]=mrse
#             start+=1

#         #print(hashTable)

#         transformations=set()

#         for word in words:
#             tempMorse=''
#             for char in word:
#                 tempMorse+=hashTable[char]

#             transformations.add(tempMorse)

#         #print(transformations)

#         return len(transformations)

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        MORSE = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
                 "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-",
                 "...-", ".--", "-..-", "-.--", "--.."]

        seen = {"".join(MORSE[ord(c) - ord('a')] for c in word)
                for word in words}

        return len(seen)