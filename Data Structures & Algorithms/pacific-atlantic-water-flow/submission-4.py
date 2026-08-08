class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac_reachable, atl_reachable = set(), set()

        def dfs(i, j, reachable):
            if (i, j) in reachable:
                return
            
            reachable.add((i, j))

            if i >= 1 and heights[i][j] <= heights[i - 1][j]:
                dfs(i - 1, j, reachable)
            if i < rows - 1 and heights[i][j] <= heights[i + 1][j]:
                dfs(i + 1, j, reachable)
            if j >= 1 and heights[i][j] <= heights[i][j - 1]:
                dfs(i, j - 1, reachable)
            if j < cols - 1 and heights[i][j] <= heights[i][j + 1]:
                dfs(i, j + 1, reachable)
        
        for j in range(cols):
            dfs(0, j, pac_reachable)
            dfs(rows - 1, j, atl_reachable)
        
        for i in range(rows):
            dfs(i, 0, pac_reachable)
            dfs(i, cols - 1, atl_reachable)
        
        print(pac_reachable)
        print(atl_reachable)
        res = pac_reachable.intersection(atl_reachable)
        res = list(res)
        res = [list(val) for val in res]
        
        return res

