class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s.lower())
        t = sorted(t.lower())

        if s == t:
            return True
        return False


