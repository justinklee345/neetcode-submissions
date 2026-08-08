class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def search(i, j):
            if (i < 0 or i >= ROWS or j < 0 or j >= COLS
                or grid[i][j] == "0"):
                return
            
            grid[i][j] = "0"

            search(i - 1, j)
            search(i + 1, j)
            search(i, j - 1)
            search(i, j + 1)
        
        islands = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    islands += 1
                    search(i, j)
        return islands

