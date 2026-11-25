class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2 ** 31 - 1

        R, C = len(grid), len(grid[0])

        def inb(r, c):
            return 0 <= r < R and 0 <= c < C
        
        q = deque()
        visited = set()

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        steps = 1
        while q:
            size = len(q)

            for _ in range(size):
                r, c = q.popleft()

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc

                    if not inb(nr, nc) or (nr, nc) in visited or grid[nr][nc] == -1:
                        continue
                    
                    grid[nr][nc] = steps
                    q.append((nr, nc))
                    visited.add((nr, nc))
            steps += 1



