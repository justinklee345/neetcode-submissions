class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        n = len(matrix[0])
        while l <= r:
            print(l, r)
            m = l + ((r - l) // 2)

            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][n - 1] < target:
                l = m + 1
            else:
                l = r = m
            
            if l == r:
                break

        print("Row: ", l, r)

        l2 = 0
        r2 = len(matrix[r]) - 1

        while l2 <= r2:
            print(l2, r2)
            m2 = l2 + ((r2 - l2) // 2)

            if matrix[r][m2] == target:
                return True
            elif matrix[r][m2] < target:
                l2 = m2 + 1
            else:
                r2 = m2 - 1

        return False
