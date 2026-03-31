class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        newStr = ""
        
        for charac in s:
            if charac in alphanum:
                newStr += charac
        s = newStr.lower()
        print(s)

        i = 0
        j = len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                print(i, j)
                return False
            i += 1
            j -= 1
        return True
