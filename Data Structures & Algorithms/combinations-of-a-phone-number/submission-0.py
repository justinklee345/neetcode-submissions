class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        alpha = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        def backtrack(current_path, i):
            if i == len(digits):
                if current_path != "":
                    res.append(current_path)
                return
            
            for letter in alpha[int(digits[i]) - 2]:
                temp = current_path
                current_path = temp + letter
                backtrack(current_path, i + 1)
                current_path = temp
        
        backtrack("", 0)
        return res

            
