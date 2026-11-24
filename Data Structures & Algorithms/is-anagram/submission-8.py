class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        vocab1, vocab2 = {}, {}

        for charac in s:
            vocab1[charac] = vocab1.get(charac, 0) + 1
        for charac in t:
            vocab2[charac] = vocab2.get(charac, 0) + 1
        if vocab1 == vocab2:
            return True
        return False
