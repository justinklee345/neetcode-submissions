class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(current_path, numOpened, numClosed):
            print(current_path)
            if numOpened == numClosed == n:

                res.append("".join(current_path))
                return
            
            if numOpened > n or numClosed > n:
                return
            
            if numOpened < n:
                current_path.append('(')
                backtrack(current_path, numOpened + 1, numClosed)
                current_path.pop()
            
            if numOpened > numClosed:
                current_path.append(')')
                backtrack(current_path, numOpened, numClosed + 1)
                current_path.pop()

        backtrack([], 0, 0)
        return res