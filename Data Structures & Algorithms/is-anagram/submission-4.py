class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        vocab = {}
        for charac in s:
            vocab[charac] = vocab.get(charac, 0) + 1
        
        vocab2 = {}
        for charac in t:
            vocab2[charac] = vocab2.get(charac, 0) + 1
        
        return vocab == vocab2



