class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(i, j):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS:
                return 0
            
            if grid[i][j] == 0:
                return 0
            
            if visited[i][j] == 1:
                return 0
            
            visited[i][j] = 1
            res = 1 + dfs(i, j + 1) + dfs(i, j - 1) + dfs(i + 1, j) + dfs(i - 1, j)
            return res
            
        res = float('-inf')
        for i in range(ROWS):
            for j in range(COLS):
                res = max(res, dfs(i,j))
        
        return res