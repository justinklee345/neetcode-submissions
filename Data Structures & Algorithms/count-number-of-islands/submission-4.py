class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        visited = set()

        def inb(r, c):
            return 0 <= r < R and 0 <= c < C

        cnt = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "0":
                    continue
                
                if (r, c) in visited:
                    continue
                
                cnt += 1
                q = deque([(r, c)])
                visited.add((r, c))
                while q:
                    i, j = q.popleft()

                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = i + dr, j + dc

                        if not inb(nr, nc):
                            continue

                        if grid[nr][nc] == "0":
                            continue

                        if (nr, nc) in visited:
                            continue
                        
                        visited.add((nr, nc))
                        q.append((nr, nc))
        return cnt
                

