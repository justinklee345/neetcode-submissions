class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        connected = {i: 0 for i in range(n)}

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        def dfs(i):
            if i in visited:
                return
            
            visited.add(i)
            for j in adj[i]:
                dfs(j)
            
        visited = set()
        cnt = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                cnt += 1
        return cnt
