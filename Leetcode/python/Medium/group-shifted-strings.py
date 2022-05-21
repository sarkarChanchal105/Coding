"""
https://leetcode.com/problems/group-shifted-strings/

We can shift a string by shifting each of its letters to its successive letter.

For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.



Example 1:

Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
Example 2:

Input: strings = ["a"]
Output: [["a"]]


Constraints:

1 <= strings.length <= 200
1 <= strings[i].length <= 50
strings[i] consists of lowercase English letters.


"""

from collections import defaultdict
class Solution:
    def groupStrings(self, strings) :

        result=[] ## where fineal result will be stored

        ## group same lenght of strings in the same gr
        hashTable=defaultdict(list)
        for word in strings:
            hashTable[len(word)].append(word)

        #print(hashTable)

        hashTableGroups=defaultdict(list) ## this dictiona will store the shifting groups

        for key,value in hashTable.items():

            ## Edge cases. if leght is one or only string then
            if key==1 or len(value)==1:
                result.append(value)

            else:
                processedWord = set() ## keep the processed words in one set
                ## for each word in a give group
                for i in range(len(value)):
                    Word=value[i] ## get the word
                    if Word not in processedWord: ## if the word ias not been processed already
                        hashTableGroups[Word]=[Word] ## add word in the dictionary
                        ## for each word in the group
                        for j in range(len(value)):
                            #print("Value",value,j,key)
                            currentWord=value[j]
                            if i==j: ## if the same word
                                continue
                            else:  ## else check whether the two words are in the same shofting group
                                if self.check_shift(Word,currentWord): ## if yes
                                    hashTableGroups[Word].append(currentWord) ## add the word in the group
                                    processedWord.add(currentWord) ## add in the processed
        #print(hashTableGroups)

        for key,value in hashTableGroups.items():
            result.append(value)

        return result

    def check_shift(self,word1,word2):

        if len(word1)!=len(word2):
            return False
        previousDiff=diff=None
        for ch1,ch2 in zip(word1,word2):
            if ord(ch1)>ord(ch2):
                diff=26-(ord(ch1)-ord(ch2))
            else:
                diff = ord(ch2) - ord(ch1)

            if previousDiff==None:
                previousDiff=diff

            if previousDiff!=diff:
                return False

        return True



object=Solution()

strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]

strings=["fpbnsbrkbcyzdmmmoisaa","cpjtwqcdwbldwwrryuclcngw","a","fnuqwejouqzrif","js","qcpr","zghmdiaqmfelr","iedda","l","dgwlvcyubde","lpt","qzq","zkddvitlk","xbogegswmad","mkndeyrh","llofdjckor","lebzshcb","firomjjlidqpsdeqyn","dclpiqbypjpfafukqmjnjg","lbpabjpcmkyivbtgdwhzlxa","wmalmuanxvjtgmerohskwil","yxgkdlwtkekavapflheieb","oraxvssurmzybmnzhw","ohecvkfe","kknecibjnq","wuxnoibr","gkxpnpbfvjm","lwpphufxw","sbs","txb","ilbqahdzgij","i","zvuur","yfglchzpledkq","eqdf","nw","aiplrzejplumda","d","huoybvhibgqibbwwdzhqhslb","rbnzendwnoklpyyyauemm"]

print(object.groupStrings(strings))
#print(object.check_shift('az','ba'))