class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        def inb(r, c):
            return 0 <= r < R and 0 <= c < C
        
        q = deque()
        visited = set()
        
        totB = 0
        foundB = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] > 0:
                    totB += 1
                
                if grid[r][c] == 2:
                    foundB += 1
                    q.append((r, c))
                    visited.add((r, c))
        
        minutes = 0
        while q:
            size = len(q)

            for _ in range(size):
                r, c = q.popleft()

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc

                    if (nr,nc) in visited or not inb(nr, nc) or grid[nr][nc] != 1:
                        continue
                    
                    foundB += 1
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    visited.add((nr, nc))

            minutes += 1
            print(grid)
            print(q)
        
        if foundB == totB:
            return max(minutes - 1, 0)
        return -1

