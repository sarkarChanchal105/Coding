# from collections import  deque
#
# class TrieNode:
#     def __init__(self):
#         #self.children = defaultdict(TrieNode)
#         self.children = {}
#         self.end = False
#
#
# class Trie:
#
#     def __init__(self):
#         self.root=TrieNode()
#
#     def insrtIntoTrie(self, arrayOfElements):
#         currentNode=self.root
#
#         for element in arrayOfElements:
#             if element in currentNode.children:
#                 currentNode = currentNode.children[element]
#             else:
#                 newNode=TrieNode()
#                 currentNode.children[element]=newNode
#                 currentNode=newNode
#
#         currentNode.end=True
#
#
#     def printTrieBottomUp(self,root):
#
#         if root is None:
#             return
#
#         for childKey,ChildValue in root.children.items():
#
#             self.printTrieBottomUp(ChildValue)
#             print(childKey, ChildValue)
#
#
#     def printTrieTopDown(self,root):
#         if root is None:
#             return
#
#         for childKey,ChildValue in root.children.items():
#             print(childKey, ChildValue)
#             self.printTrieTopDown(ChildValue)
#
#
#
#     def printTrieLevelOrder(self,root):
#
#         queue=deque()
#         queue.append(root)
#         while len(queue)>0:
#             currentLevelSize=len(queue)
#             while currentLevelSize>0 and len(queue)>0:
#                 item=queue.pop()
#                 currentLvl = []
#                 if item.children.keys():
#                     currentLvl.append(item.children.keys())
#                     #print(currentLvl)
#                     currentLevelSize-=1
#                     for childKey,childValue in item.children.items():
#                         queue.append(childValue)
#                     print("Children in this level :{}".format(currentLvl))
#
#
#     def searchCocepts(self,conceptArray):
#
#
#
# object=Trie()
#
# array=[['I', 'Love', 'You'],['I','Love','Chicken'],['I', 'Love','South','Indian','Food']]
#
# for ele in array:
#     object.insrtIntoTrie(ele)
#
# # object.printTrieBottomUp(object.root)
# # print('..................................')
# # object.printTrieTopDown(object.root)
# # print('..................................')
#
# object.printTrieLevelOrder(object.root)
#
# cocepts=[['Indian'],['East Indian'],['South Indian']]
#


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:

    def __init__(self):

        self.root = TrieNode()  ## srtart with a blank node

    def insert(self, word: str) -> None:

        currentNode = self.root  ## current Node starts from root

        for chr in word:  ## for each character in the word

            if chr in currentNode.children.keys():  ## if the current charater is children of the current Node
                currentNode = currentNode.children[chr]  ## then get the pointer to that children
            else:
                newNode = TrieNode()  ## if this is new charater, create a new Trie Node
                currentNode.children[chr] = newNode  ## add the new charater with the pointer of the Trie Node
                currentNode = newNode  ## point the current Node the new Node

        currentNode.is_end = True  ## update the is_end to True

    def search(self, word: str) -> bool:  ## Searhc for the whole word

        currentNode = self.root  ## Current Node starts from root

        for letter in word:  ## for each character in the word:

            if letter in currentNode.children:  ## if the letter is a. children of current Node
                currentNode = currentNode.children[letter]  ## get the pointer of that children from distionary lookup
            else:
                return False  ## elase return false.

        return currentNode.is_end  ## if we have reached the end of the word then return True else False

    def startsWith(self, prefix: str) -> bool:
        currentNode = self.root  ## Current Node starts from root

        for letter in prefix:  ## for each character in the word:

            if letter in currentNode.children:  ## if the letter is a. children of current Node
                currentNode = currentNode.children[letter]  ## get the pointer of that children from distionary lookup
            else:
                return False  ## elase return false.

        return True

    # Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)







