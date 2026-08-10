class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(i):
            if i in visited:
                return
            
            visited.add(i)
            for j in adj[i]:
                dfs(j)
        
        visited = set()
        dfs(0)
        if len(visited) < n:
            print("HERE?")
            return False

        def dfs2(i, prev):
            if i in visited:
                return False
            
            visited.add(i)
            res = True
            for j in adj[i]:
                if prev != -1 and prev == j:
                    continue
                res = res and dfs2(j, i)
            visited.remove(i)
            return res

        visited = set()
        print("HERE2")
        return dfs2(0, -1)