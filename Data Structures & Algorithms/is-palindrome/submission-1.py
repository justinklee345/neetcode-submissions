class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char.lower()

        l, r = 0, len(cleaned) - 1
        print(cleaned)
        while l <= r:
            if cleaned[l] == cleaned[r]:
                l += 1
                r -= 1
            else:
                return False

        return True