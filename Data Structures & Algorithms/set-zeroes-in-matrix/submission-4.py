class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        for row in matrix:
            row.append(float('inf'))
        matrix.append([float('inf') for _ in range(len(matrix[0]))])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    matrix[i][-1] = 0
                    matrix[-1][j] = 0
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][-1] == 0 or matrix[-1][j] == 0:
                    matrix[i][j] = 0
        
        matrix.pop()
        for row in matrix:
            row.pop()