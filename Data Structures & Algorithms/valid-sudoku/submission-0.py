class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            checker = [0 for i in range(9)]
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue;
                checker[int(board[i][j]) - 1] += 1

            for val in checker:
                if val > 1:
                    return False
        
        for i in range(9):
            checker = [0 for i in range(9)]
            for j in range(9):
                if board[j][i] == ".":
                    continue;
                checker[int(board[j][i]) - 1] += 1

            for val in checker:
                if val > 1:
                    return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                checker = [0 for i in range(9)]
                for x in range(3):
                    for y in range(3):
                        if board[i+x][j+y] == ".":
                            continue;
                        checker[int(board[i + x][j + y]) - 1] += 1
                
                for val in checker:
                    if val > 1:
                        return False
        return True
