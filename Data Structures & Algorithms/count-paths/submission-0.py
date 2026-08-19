class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # unique[i][j] is the number of ways to reach i, j
        unique = [[0 for j in range(n)] for i in range(m)]

        unique[0][0] = 1
        for i in range(m):
            for j in range(n):
                if j >= 1:
                    unique[i][j] += unique[i][j-1]
                if i >= 1:
                    unique[i][j] += unique[i - 1][j]
        
        print(unique)
        return unique[-1][-1]
