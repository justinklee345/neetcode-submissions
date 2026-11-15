class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        vocab = set(s[0])
        maxSize = 1

        l = 0
        for r in range(1, len(s)):
            if s[r] in vocab:
                maxSize = max(maxSize, len(vocab))
                while True:
                    vocab.remove(s[l])
                    l += 1
                    if s[r] not in vocab:
                        break
            vocab.add(s[r])
        return max(maxSize, len(vocab))
            