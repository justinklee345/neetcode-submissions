class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        def inb(r, c):
            return 0 <= r < R and 0 <= c < C

        visited = set()
        maxArea = 0
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0 or (r, c) in visited:
                    continue
                
                q = deque([(r, c)])
                visited.add((r, c))
                localMax = 1
                while q:
                    i, j = q.popleft()

                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = i + dr, j + dc

                        if not inb(nr, nc) or grid[nr][nc] == 0 or (nr, nc) in visited:
                            continue
                        
                        localMax += 1
                        visited.add((nr, nc))
                        q.append((nr, nc))
                maxArea = max(maxArea, localMax)
        return maxArea