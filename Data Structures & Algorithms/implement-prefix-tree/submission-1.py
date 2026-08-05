class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        ptr = self.root
        for charac in word:
            if charac not in ptr.children:
                ptr.children[charac] = TrieNode()
            
            ptr = ptr.children[charac]
        ptr.is_word = True

    def search(self, word: str) -> bool:
        ptr = self.root
        for charac in word:
            if charac not in ptr.children:
                return False
            ptr = ptr.children[charac]
        return ptr.is_word

    def startsWith(self, prefix: str) -> bool:
        print("startswith", prefix)
        ptr = self.root
        for charac in prefix:
            if charac not in ptr.children:
                return False
            ptr = ptr.children[charac]
        return True
        