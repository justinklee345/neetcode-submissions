class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = "".join(char.lower() for char in s if char.isalnum())

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                print(l, s[l], r, s[r])
                return False
            l += 1
            r -= 1
        return True
