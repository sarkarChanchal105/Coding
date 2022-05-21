


class TrieNode:

    def __init__(self):
        self.children={}
        self.is_end=False
        self.cnt=0  ## For exact match
        self.cnt_start_with=0 ## for count of all words with same prefix



class Trie:

    def __init__(self):
        self.root=TrieNode()


    def insert(self, word: str) -> None:
        currentNode=self.root
        for chr in word:
            if chr in currentNode.children:
                currentNode=currentNode.children[chr]

            else:
                newNode=TrieNode()
                currentNode.children[chr]=newNode
                currentNode=newNode
            currentNode.cnt_start_with+=1
        currentNode.cnt+=1
        currentNode.is_end =True


    def countWordsEqualTo(self, word: str) -> int:

        currentNode=self.root

        for chr in word:
            if chr in currentNode.children:
                currentNode=currentNode.children[chr]
            else:
                return 0

        return currentNode.cnt


    def countWordsStartingWith(self, prefix: str) -> int:

        currentNode=self.root

        for chr in prefix:
            if chr in currentNode.children:
                currentNode=currentNode.children[chr]

            else:
                return 0
        return currentNode.cnt_start_with

    def erase(self, word: str) -> None:

        currentNode=self.root

        for chr in word:
            if chr in currentNode.children:
                currentNode=currentNode.children[chr]
                currentNode.cnt_start_with-=1
        currentNode.cnt-=1






# Your Trie object will be instantiated and called as such:
word='apple'
obj = Trie()
obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)