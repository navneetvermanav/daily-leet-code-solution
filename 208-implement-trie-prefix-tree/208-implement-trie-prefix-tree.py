class TrieNode:
    def __init__(self):
        self.childrens = {}
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.childrens:
                curr.childrens[i] = TrieNode()
            curr = curr.childrens[i]
        curr.isWord = True

        
    def search(self, word: str) -> bool:
        curr = self.root
        for s in word:
            if s not in curr.childrens:
                return False
            curr = curr.childrens[s]
        return curr.isWord
            
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for s in prefix:
            if s not in curr.childrens:
                return False
            curr = curr.childrens[s]
        return True