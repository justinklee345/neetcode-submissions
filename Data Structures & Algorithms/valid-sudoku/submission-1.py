class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValid(sequence):
            seen = [0 for _ in range(9)]

            for item in sequence:
                if item == '.':
                    continue
                
                if seen[int(item) - 1] == 1:
                    return False
                
                seen[int(item) - 1] += 1
            
            return True

        sequences = defaultdict(list)

        for i in range(9):
            for j in range(9):
                value = board[i][j]
                sequences["horizontal " + str(i)].append(value)
                sequences["vertical " + str(j)].append(value)
                sequences["box " + str(i // 3) + "&" + str(j // 3)].append(value)
        
        for sequence in sequences.values():
            if not isValid(sequence):
                return False
        return True

                
