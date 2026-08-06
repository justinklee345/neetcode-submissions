class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        ptr = self.root
        for charac in word:
            if charac not in ptr.children:
                ptr.children[charac] = TrieNode()
            ptr = ptr.children[charac]
        ptr.is_word = True

    def search(self, word: str) -> bool:
        def dfs(i, ptr):
            if i == len(word):
                return ptr.is_word
            
            charac = word[i]

            if charac == '.':
                for child in ptr.children:
                    if dfs(i + 1, ptr.children[child]):
                        return True
                return False
            
            if charac not in ptr.children:
                return False
            
            return dfs(i + 1, ptr.children[charac])
        return dfs(0, self.root)