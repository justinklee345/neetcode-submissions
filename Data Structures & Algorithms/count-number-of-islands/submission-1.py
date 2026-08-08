class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [["0" for j in range(len(grid[i]))] for i in range(len(grid))]

        def dfs(i, j, visited):
            if visited[i][j] == "1":
                return
            
            visited[i][j] = "1"
            
            if i >= 1 and grid[i-1][j] == "1":
                dfs(i - 1, j, visited)
            if i < len(grid) - 1 and grid[i+1][j] == "1":
                dfs(i + 1, j, visited)
            if j >= 1 and grid[i][j-1] == "1":
                dfs(i, j - 1, visited)
            if j < len(grid[i]) - 1 and grid[i][j + 1] == "1":
                dfs(i, j + 1, visited)

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "0":
                    continue
                
                if visited[i][j] == "1":
                    continue
                
                islands += 1
                dfs(i, j, visited)
        return islands
                

        

