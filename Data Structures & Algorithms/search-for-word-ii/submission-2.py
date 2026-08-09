class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            ptr = root
            for charac in w:
                if charac not in ptr.children:
                    ptr.children[charac] = TrieNode()
                
                ptr = ptr.children[charac]
            ptr.word = w
            print(ptr, ptr.word, ptr.children)

        rows, cols = len(board), len(board[0])
        res = set()
        visited = set()
        
        def dfs(i, j, node):
            if node.word:
                res.add(node.word)

            if (i < 0 or j < 0 or i > rows - 1 or j > cols - 1
             or (i, j) in visited):
                return
            
            
            charac = board[i][j]
            if charac not in node.children:
                return

            node = node.children[charac]
            visited.add((i, j))

            dfs(i + 1, j, node)
            dfs(i - 1, j, node)
            dfs(i, j - 1, node)
            dfs(i, j + 1, node)

            visited.remove((i, j))

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root)
        
        return list(res)