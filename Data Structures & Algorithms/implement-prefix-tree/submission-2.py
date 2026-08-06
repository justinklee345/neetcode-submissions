class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        ptr = self.root
        for char in word:
            if char in ptr.children:
                ptr = ptr.children[char]
            else:
                ptr.children[char] = TrieNode()
                ptr = ptr.children[char]
        ptr.is_word = True

    def search(self, word: str) -> bool:
        ptr = self.root
        for char in word:
            if char not in ptr.children:
                return False
            ptr = ptr.children[char]
        return ptr.is_word

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for char in prefix:
            if char not in ptr.children:
                return False
            ptr = ptr.children[char]
        return True
        
        