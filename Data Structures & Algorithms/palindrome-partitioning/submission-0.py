class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(s):
            return s == s[::-1]

        def backtrack(curr, i):
            if i == len(s):
                if isPalindrome(curr[-1]):
                    res.append(curr[:])
                return
            
            # if prev is palindrome, we can start a new one
            if len(curr) >= 1 and isPalindrome(curr[-1]):
                curr.append(s[i])
                backtrack(curr, i + 1)
                curr.pop()
            

            if len(curr) == 0:
                backtrack([s[i]], i + 1)
            else:
                val = curr.pop()
                curr.append(val + s[i])
                backtrack(curr, i + 1)
                curr.pop()
                curr.append(val)
        
        backtrack([], 0)
        print("FINAL", res)
        return res
        
                
            