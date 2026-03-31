class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        alphabet = [0 for i in range(26)]
        alphabet2 = [0 for i in range(26)]

        for charac in s:
            alphabet[ord(charac) - ord('a')] += 1

        for charac in t:
            alphabet[ord(charac) - ord('a')] -= 1
            
        if alphabet == alphabet2:
            return True
        return False



