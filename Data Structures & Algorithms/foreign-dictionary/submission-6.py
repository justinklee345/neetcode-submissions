class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c : set() for word in words for c in word}

        for i in range(len(words) - 1):
            first = words[i]
            second = words[i + 1]
            minLen = min(len(first), len(second))

            if len(first) > len(second) and first[:minLen] == second[:minLen]:
                return ""
            
            for i in range(minLen):
                if first[i] != second[i]:
                    adj[first[i]].add(second[i])
                    break
        
        print(adj)
        res = []
        visited = {}
        def dfs(c):
            print(c, visited, res)
            if c in visited:
                return visited[c]
            
            visited[c] = True

            for nei in adj[c]:
                if dfs(nei):
                    return True
                
            visited[c] = False
            res.append(c)
        
        for charac in adj.keys():
            if dfs(charac):
                print(charac)
                return ""
            

        return "".join(res[::-1])