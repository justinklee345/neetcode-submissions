class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        vocab = {}

        for c in s:
            vocab[c] = vocab.get(c, 0) + 1
        
        for c in t:
            if c not in vocab or vocab[c] <= 0:
                return False
            vocab[c] -= 1
        
        for key,value in vocab.items():
            if value != 0:
                return False
        return True
