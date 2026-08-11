class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        rowZero = False
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    if i == 0:
                        rowZero = True
                    else:
                        matrix[i][0] = 0
                    matrix[0][j] = 0
        print(rowZero)
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                if i == 0 and rowZero:
                    matrix[i][j] = 0
                elif i != 0 and matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0