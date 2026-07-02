class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                node = Node()
                curr.children[char] = node
            curr = curr.children[char]
        
        curr.end = True

    def searchBranch(self, node, word):
        curr = node
        for i in range(len(word)):
            if word[i] == ".":
                for child in curr.children:
                    if self.searchBranch(curr.children[child], word[i+1:]):
                        return True
                return False
            if word[i] not in curr.children:
                return False
            curr = curr.children[word[i]]

        return curr.end
        

    def search(self, word: str) -> bool:
        return self.searchBranch(self.root, word)
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)